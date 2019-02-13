#!/usr/bin/env python
import pygame
import socket
import sys

pixels = []

class Neopixel():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 12
        self.height = 12
        self.status = True
        self.color = (30,30,30)

    def render(self, screen):
        color = self.color
        pygame.draw.rect(screen, color, pygame.Rect(self.x, self.y, self.width, self.height))

def handlecommand(command, data):
    global pixels
    data = list(data)
    if command == 0x12:
        length = data[0]
        for index in range(0, length):
            i = index*4 + 1
            pixels[data[i]].color = (data[i+1], data[i+2], data[i+3])
            pixels[data[i]].status = True
    if command == 0x13:
        i = 0
        color = (0,0,0)
        set_color = True
        read_once = False

        while i < len(data):
            value = data[i]
            if set_color:
                color = (data[i], data[i+1], data[i+2])
                i += 2
                set_color = False
                read_once = False
            elif value == 0 and read_once:
                set_color = True
            else:
                pixels[value+13].color = color
                read_once = True
            i += 1



def addNeopixelAt(x, y):
    led = Neopixel(x, y)
    led.status = False
    pixels.append(led)
    return led

def run():
    global pixels
    pygame.init()
    screen = pygame.display.set_mode((400, 200))
    clock = pygame.time.Clock()
    running = True

    # material A side
    addNeopixelAt(20, 50)
    addNeopixelAt(20, 80)
    addNeopixelAt(20, 110)
    addNeopixelAt(60, 150)
    # material B side
    addNeopixelAt(240, 150)
    addNeopixelAt(280, 50)
    addNeopixelAt(280, 80)
    addNeopixelAt(280, 110)
    
    # optimization
    addNeopixelAt(130, 100)
    addNeopixelAt(140, 115)
    addNeopixelAt(150, 100)
    addNeopixelAt(160, 115)
    addNeopixelAt(170, 100)
    # matrix
    for index in range(0,64):
        j = index//8
        i = index%8
        led = addNeopixelAt(130+i*6, 35+j*6)
        led.width = 5
        led.height = 5

    #selected material
    addNeopixelAt(115, 5)
    addNeopixelAt(130, 5)
    addNeopixelAt(145, 5)
    addNeopixelAt(160, 5)

        

    # server configuration
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 6060)
    sock.bind(server_address)
    sock.listen(1)
    sock.settimeout(0.1)
    connection = None
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                alt_pressed = True
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_F4 and alt_pressed:
                    running = False

        # stablish connection
        try:
            if not connection:
                connection, client_address = sock.accept()
                print("connection from", client_address)
            else:
                data = connection.recv(3)
                if len(data)>0:
                    command = data[1]
                    data = connection.recv(data[2])
                    handlecommand(command, data)

        except socket.timeout:
            print("timeout")


        # render process
        screen.fill((0,0,0))
        for led in pixels:
            led.render(screen)
        pygame.display.flip()
        clock.tick(60)

    if connection:
        connection.close()





if __name__ == '__main__':
    run()

