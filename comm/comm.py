#!/usr/bin/env python

import serial

class SerialComm:
    def __init__(self, unavailable_commands):
        self.comm = None
        self.active = False
        self.unavailable_commands = unavailable_commands

    def open(self, port):
        try:
            self.comm = serial.Serial(port, 9600, timeout=0)
            self.active = True
        except:
            print("can't open connection on", port, "port")

    def read(self):
        if not self.active: return
        data = self.comm.read(4)
        while len(data) > 0:
            to_int = [x for x in data]
            data = ser.read(4)

    def write(self, command, payload):
        if not self.active: return
        if command in self.unavailable_commands: return
        data = [0x7E, command, len(payload)] + payload
        comm.write(bytearray(data))

    def activate_buttons(activate):
        message = [int(activate)]
        self.write(0x01, message)

    def activate_tunners(activate):
        message = [int(activate)]
        self.write(0x02, message)

    def set_independent_lights(independent):
        message = [int(independent)]
        self.write(0x03, message)
    
    def clean_matrix():
        self.write(0x04, [0])

    def set_led_brightness(value):
        self.write(0x05, [value%255])

    def set_buttons_backlight(backlight_colors):
        message = [len(backlight_colors)%4] + backlight_colors
        self.write(0x10, message)

    def switch_buttons_backlight(button_lights_on):
        message = [len(button_lights_on)%2] + button_lights_on
        self.write(0x11, message)

    def set_led_light(colors):
        message = [len(colors)%4] + colors
        self.write(0x12, message)

    def display_image(encoded_image):
        self.write(0x13, encoded_image)

    def switch_button_mode(button_modes):
        message = [len(button_modes)%2] + button_modes
        self.write(0x30, message)

    def lock_buttons(button_locks):
        message = [len(button_locks)%2] + button_locks
        self.write(0x31, message)
    
    def switch_buttons(button_status):
        message = [len(button_status)%2] + button_status
        self.write(0x32, message)


material_comm = SerialComm([0x02, 0x04, 0x13])
optimization_comm = SerialComm([])


def init_connections(port_material, port_optimization):
    material_comm.open(port_material)
    optimization_comm.open(port_optimization)

def read_response():
    material_comm.read()
    optimization_comm.read()
    

