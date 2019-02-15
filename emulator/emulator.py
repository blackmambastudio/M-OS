#!/usr/bin/env python
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 5)

import pygame
import socket
import sys
import math

pixels = []
brightness = 50
MAX_BRIGHTNESS = 50
MATRIX_START_ID = 33

class Neopixel():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.status = True
        self.color = (30,30,30)

    def render(self, screen):
        color = (self.color[0]*brightness/MAX_BRIGHTNESS, self.color[1]*brightness/MAX_BRIGHTNESS, self.color[2]*brightness/MAX_BRIGHTNESS)
        pygame.draw.rect(screen, color, pygame.Rect(self.x, self.y, self.width, self.height))


class Text():
    def __init__(self, text, font, x=0, y=0, color=(255, 255, 255)):
        self.color = color
        self.text = font.render(text, True, self.color)
        self.inner_text = text
        self.anchor = (0, 0.5)
        self.SetPosition(x, y)
        self.font = font

    def SetPosition(self, x, y):
        self.x = x
        self.y = y
        self.position = (self.x - self.text.get_width()*self.anchor[0], self.y - self.text.get_height()*self.anchor[1])

    def render(self, screen):
        screen.blit(self.text, self.position)
   
    def setAnchor(self, x, y):
        self.anchor = (x, y)
        self.SetPosition(self.x, self.y)

    def setText(self, text):
        self.inner_text = text
        self.text = self.font.render(text, True, self.color)

    def render_multiline(self, screen):
        words = [word.split(' ') for word in self.inner_text.splitlines()]  # 2D array where each row is a list of words.
        space = self.font.size(' ')[0]  # The width of a space.
        max_width, max_height = screen.get_size()
        x, y = self.position
        for line in words:
            for word in line:
                word_surface = self.font.render(word, 0, self.color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = self.position[0]  # Reset the x.
                    y += word_height  # Start on new row.
                screen.blit(word_surface, (x, y))
                x += word_width + space
            x = self.position[0]  # Reset the x.
            y += word_height  # Start on new row.


class LCD():
    def __init__(self, font, x, y, color):
        self.rows = []
        self.rows.append(Text("0123456789ABCDEF", font, x, y, color))
        self.rows.append(Text("FEDCBA9876543210", font, x, y+20, color))

    def setText(self, row, text):
        self.rows[row].setText(text)

    def render(self, screen):
        self.rows[0].render(screen)
        self.rows[1].render(screen)


def handlecommand(command, data):
    global pixels
    global brightness
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
                pixels[value+MATRIX_START_ID].color = color
                read_once = True
            i += 1
    if command == 0x04:
        for index in range(33,97):
            pixels[index].color = (5, 5, 5)
    if command == 0x05:
        brightness = data[0]


def addNeopixelAt(x, y):
    led = Neopixel(x, y)
    led.status = False
    pixels.append(led)
    return led

def run():
    global pixels
    pygame.init()
    screen = pygame.display.set_mode((640, 400))
    clock = pygame.time.Clock()
    running = True
    font = pygame.font.Font("../assets/fonts/VCR_OSD_MONO_1.001.ttf", 18)
    printer_font = pygame.font.Font("../assets/fonts/VCR_OSD_MONO_1.001.ttf", 14)
    lcd0 = LCD(font, 50, 164, (160,200,190))
    lcd0.setText(0, "> MATERIAL A ---")
    lcd1 = LCD(font, 50, 224, (160,200,190))
    lcd1.setText(0, "> MATERIAL B ---")
    lcd2 = LCD(font, 50, 284, (160,200,190))
    lcd2.setText(0, "> MATERIAL C ---")
    
    lcd3 = LCD(font, 390, 164, (160,200,190))
    lcd3.setText(0, "--- MATERIAL D <")
    lcd4 = LCD(font, 390, 224, (160,200,190))
    lcd4.setText(0, "--- MATERIAL E <")
    lcd5 = LCD(font, 390, 284, (160,200,190))
    lcd5.setText(0, "--- MATERIAL F <")

    printer_text = Text("texto en varias\nlineas...\npara probar que sirva\n... ojala".upper(), printer_font, 40, 40, (255, 255, 198))


    # material A side 0 - 3
    addNeopixelAt(10, 160)
    addNeopixelAt(10, 220)
    addNeopixelAt(10, 280)
    addNeopixelAt(120, 360)
    # material B side 4 - 7
    addNeopixelAt(500, 360)
    addNeopixelAt(590, 280)
    addNeopixelAt(590, 220)
    addNeopixelAt(590, 160)
    
    #selected material 8 - 11
    addNeopixelAt(245, 10)
    addNeopixelAt(285, 10)
    addNeopixelAt(325, 10)
    addNeopixelAt(365, 10)

    # ring 12 - 27
    interval = math.pi/8
    radius = 40
    for index in range(0, 16):
        j = radius*math.cos(interval*index)
        i = radius*math.sin(interval*index)
        led = addNeopixelAt(500+i, 80+j)
        led.width = 10
        led.height = 10
    
    # optimization 28 - 32
    addNeopixelAt(265, 270)
    addNeopixelAt(285, 305)
    addNeopixelAt(305, 270)
    addNeopixelAt(325, 305)
    addNeopixelAt(345, 270)
    
    # matrix 33 - 96
    
    for index in range(0,64):
        j = index//8
        i = index%8
        led = addNeopixelAt(272+i*12, 160+j*12)
        led.width = 10
        led.height = 10
        

    # server configuration
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 6060)
    sock.bind(server_address)
    sock.listen(0)
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
                    if command == 0x90:
                        connection.close()
                        connection = None
                        print("connection dropped!")

        except socket.timeout:
            pass


        # render process
        screen.fill((0,0,0))
        for led in pixels:
            led.render(screen)
        
        lcd0.render(screen)
        lcd1.render(screen)
        lcd2.render(screen)
        lcd3.render(screen)
        lcd4.render(screen)
        lcd5.render(screen)

        printer_text.render_multiline(screen)

        pygame.display.flip()
        clock.tick(60)

    if connection:
        connection.close()


if __name__ == '__main__':
    run()

