#!/usr/bin/env python

import serial
from emulator import client as socket

EMULATOR = True

class SerialComm:
    def __init__(self, unavailable_commands):
        self.comm = None
        self.active = False
        self.unavailable_commands = unavailable_commands
        self.emulator_led_index = 0

    def open(self, port):
        try:
            self.comm = serial.Serial(port, 9600, timeout=0)
            self.active = True
        except:
            print("can't open connection on", port, "port")

    def read(self):
        if not self.active: return
        if EMULATOR: return
        data = self.comm.read(4)
        while len(data) > 0:
            to_int = [x for x in data]
            data = self.comm.read(4)

    def write(self, command, payload):
        if not self.active: return
        if command in self.unavailable_commands: return
        data = [0x7E, command, len(payload)] + payload
        if EMULATOR:
            socket.write(bytearray(data))
        else:
            self.comm.write(bytearray(data))
            self.comm.flush()

    def activate_buttons(self, activate):
        message = [int(activate)]
        self.write(0x01, message)

    def activate_tunners(self, activate):
        message = [int(activate)]
        self.write(0x02, message)

    def set_independent_lights(self, independent):
        message = [int(independent)]
        self.write(0x03, message)
    
    def clean_matrix(self):
        self.write(0x04, [0])

    def set_led_brightness(self, value):
        self.write(0x05, [value%256])

    def set_buttons_backlight(self, backlight_colors):
        message = [len(backlight_colors)%4] + backlight_colors
        self.write(0x10, message)

    def switch_buttons_backlight(self, button_lights_on):
        message = [len(button_lights_on)%2] + button_lights_on
        self.write(0x11, message)

    def set_led_light(self, colors):
        if EMULATOR:
            colors = [i+self.emulator_led_index if i%4==0 else i for i in colors]
        message = [int(len(colors)/4)] + colors
        self.write(0x12, message)

    def display_image(self, encoded_image):
        self.write(0x13, encoded_image)

    def switch_button_mode(self, button_modes):
        message = [len(button_modes)%2] + button_modes
        self.write(0x30, message)

    def lock_buttons(self, button_locks):
        message = [len(button_locks)%2] + button_locks
        self.write(0x31, message)
    
    def switch_buttons(self, button_status):
        message = [len(button_status)%2] + button_status
        self.write(0x32, message)

    def close_connection(self):
        if self.active:
            self.comm.close()


mat = SerialComm([0x02, 0x04, 0x13])
opt = SerialComm([])


def init_connections(port_material, port_optimization):
    mat.open(port_material)
    opt.open(port_optimization)

    if EMULATOR:
        mat.active = True
        opt.active = True
        opt.emulator_led_index = 8
        socket.open()

def read_response():
    mat.read()
    opt.read()
    
def close_connections():
    if EMULATOR:
        socket.close()
        mat.active = False
        opt.active = False
    mat.close_connection()
    opt.close_connection()