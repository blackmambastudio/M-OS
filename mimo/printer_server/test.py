from Adafruit_Thermal import *

printer = Adafruit_Thermal('/dev/serial0', 19200, timeout=5)

printer.feed(4)
printer.println('This is the way the world ends.')
