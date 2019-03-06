#!/usr/bin/env python
import serial
import time
from serial.tools import list_ports

class SerialComm:
    def __init__(self, unavailable_commands):
        self.comm = None
        self.active = False
        self.unavailable_commands = unavailable_commands
        self.emulator_led_index = 0
        self.id = 0
        self.tunners = [0,0]

    def open(self, port):
        try:
            self.comm = serial.Serial(port, 9600, timeout=0.01)
            self.active = True
        except:
            print("can't open connection on", port, "port")

    def read(self):
        if not self.active: return
        
        data = self.comm.read(3)

        while len(data) > 0:
            to_int = [x for x in data]
            data = self.comm.read(to_int[2])
            payload = [x for x in data]
            self.handle_message(to_int[1], payload)
            data = self.comm.read(3)

    def handle_message(self, command, payload):
        print("read command", command, payload)
        if command == 0x91:
            self.id = payload[0]
        if command == 0x41:
            self.tunners[0] = (payload[0]<<8) + payload[1]
            self.tunners[1] = (payload[2]<<8) + payload[3]

    def write(self, command, payload):
        if not self.active: return
        if command in self.unavailable_commands: return
        data = [0x7E, command, len(payload)] + payload
        print("write", data)
        self.comm.write(bytearray(data))
        self.comm.flush()

    def identify(self):
        self.write(0x91, [0])

    def enable_buttons(self, enable):
        self.write(0x01, [enable])

    def enable_tunners(self, enable):
        self.write(0x02, [enable])

    def set_independent_lights(self, independent):
        self.write(0x03, [independent])
    
    def clean_matrix(self):
        self.write(0x04, [0])

    def set_led_brightness(self, value):
        self.write(0x05, [value%256])

    def set_buttons_backlight(self, backlight_colors):
        message = [len(backlight_colors)//4] + backlight_colors
        self.write(0x10, message)

    def switch_buttons_backlight(self, button_lights_on):
        message = [len(button_lights_on)//2] + button_lights_on
        self.write(0x11, message)

    def set_led_light(self, colors):
        message = [len(colors)//4] + colors
        self.write(0x12, message)

    def display_image(self, encoded_image):
        self.write(0x13, encoded_image)

    def switch_button_mode(self, button_modes):
        message = [len(button_modes)//2] + button_modes
        self.write(0x30, message)

    def lock_buttons(self, button_locks):
        message = [len(button_locks)//2] + button_locks
        self.write(0x31, message)
    
    def switch_buttons(self, button_status):
        message = [len(button_status)//2] + button_status
        self.write(0x32, message)

    def read_tunner(self):
        self.write(0x41, [0])

    def close_connection(self):
        if self.active:
            self.comm.close()


mat = SerialComm([0x02, 0x04, 0x13])
opt = SerialComm([])

ARDUINO_DIRS = {
    "MATERIAL": "-",
    "OPTIMIZATION": ""
}


def init_connections():

    res = list_ports.comports()
    for detected in res:
        port = detected.device
        try:
            temp = serial.Serial(port, 9600, timeout=0.5)
            temp.write([0x7e, 0x91, 0x01, 0x00])
            temp.flush()
            data = temp.read(4)
            to_int = [x for x in data]
            if to_int[0] == 0x7E and to_int[1] == 0x91:
                if to_int[3] == 0x99:
                    ARDUINO_DIRS["OPTIMIZATION"] = port
                elif to_int[3] == 0x66:
                    ARDUINO_DIRS["MATERIAL"] = port
            temp.close()
        except:
            print("can't open connection on", port, "port")

    mat.open(ARDUINO_DIRS["MATERIAL"])
    opt.open(ARDUINO_DIRS["OPTIMIZATION"])


def read_response():
    mat.read()
    opt.read()
    
def close_connections():
    mat.close_connection()
    opt.close_connection()
