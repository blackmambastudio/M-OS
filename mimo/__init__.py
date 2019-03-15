#!/usr/bin/env python3
from emulator import client as emulator
from .comm import comm
import subprocess

LCD = False
PRINTER = False
MATERIAL = False
OPTIMIZATION = False
EMULATOR = False

try:
    from .comm import I2C_LCD
    LCD = True
    lcds_displays = []
    lcd_addresses = [0x27, 0x26, 0x25, 0x24, 0x23, 0x22]
    for address in lcd_addresses:
        lcds_displays.append(I2C_LCD.lcd(address))

except ImportError:
    LCD = False
    print("can't import I2C_LCD")

try:
    from .comm import printer
    PRINTER = True
except ImportError:
    PRINTER = False
    print("can't import thermal printer")


# define all led ids for material and optimization modules
#
#                +   mat leds  +
#                   24-25-26-27         
#                                   ring
#                                  8 - 23
# +----- mat ----+---- opt ----+---- mat -----+
# | button_a  0/q|   matrix    | button_d  4/o|
# | button_b  1/a|   33-96     | button_e  5/k|
# | button_c  2/z| 28d 30f 32g | button_f  6/m|
# |              |   29c 31v   |              |
# | button_no 3/w| button_0-4  | button_ok 7/i|
# +--------------+-------------+--------------+
#
# material leds ids: 0-27
# optimization leds ids: 28-96 // 0 - 68

# buttons ids
# +----- mat ----+---- opt ----+---- mat ----+
# | button_a  0  |             | button_d  7 |
# | button_b  1  |             | button_e  6 |
# | button_c  2  | 08  10  12  | button_f  5 |
# |              |   09  11    |             |
# | button_no 3  | button_0-4  | button_ok 4 |
# +--------------+-------------+-------------+

# use printer 
def printer_interface(logfile):
    command = '/home/pi/M-OS/mimo/printer_server/printer_server.py /home/pi/M-OS/mimo/printer_server/data/{0}.json'.format(logfile)

    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

def termal_print(formatted_message, logfile='agar3s'):
    print("should send:<", formatted_message, "> to thermal printer")
    if EMULATOR:
        emulator.termal_print(formatted_message)
    else:
        # printer.mimo_printer_init()
        printer_interface(logfile)

# use lcd display 
def lcd_display_at(id, message, line=1, pos=0):
    messages = ["",""]
    message = message.upper()
    if len(message)>16:
        messages[0] = message[:16]
        messages[1] = message[16:]
        line = 0

    if EMULATOR:
        if line == 0:
            emulator.lcd_display_at(id, messages[0], 1)
            emulator.lcd_display_at(id, messages[1], 2)
        else:
            emulator.lcd_display_at(id, message, line)

    elif LCD:
        lcd = lcds_displays[id]
        if line == 0:
            lcd.lcd_display_string(messages[0], 1)
            lcd.lcd_display_string(messages[1], 2)
        else:
            lcd.lcd_display_string(message, line)
        

# 0x01 
def set_buttons_enable_status(mat_enable, opt_enable):
    if EMULATOR:
        pass
    else:
        comm.mat.enable_buttons(int(mat_enable))
        comm.opt.enable_buttons(int(opt_enable))

# 0x02
def set_tunners_enable_status(enable):
    if EMULATOR:
        pass
    else:
        comm.opt.enable_tunners(int(enable))


# 0x03
def set_independent_lights(mat_value, opt_value):
    if EMULATOR:
        pass
    else:
        comm.mat.set_independent_lights(int(mat_value))
        comm.opt.set_independent_lights(int(opt_value))

# 0x04 
# see neopixelgraphics

# 0x05 applies brightness to both sections
def set_led_brightness(brightness):
    if EMULATOR:
        emulator.set_led_brightness(brightness)
    else:
        comm.mat.set_led_brightness(brightness)
        comm.opt.set_led_brightness(brightness)

# 0x10
def set_material_buttons_light(values):
    if EMULATOR:
        pass
    else:
        comm.mat.set_buttons_backlight(values)

def set_optimization_buttons_light(values):
    if EMULATOR:
        pass
    else:
        comm.opt.set_buttons_backlight(values)

# 0x11 multiple
def set_material_ligths_on(values):
    if EMULATOR:
        pass
    else:
        comm.mat.switch_buttons_backlight(values)

def set_optimization_ligths_on(values):
    if EMULATOR:
        pass
    else:
        comm.opt.switch_buttons_backlight(values)

# 0x12 multiple 
def set_material_leds_color(values):
    if EMULATOR:
        emulator.set_led_light(values, 0)
    else:
        comm.mat.set_led_light(values)

def set_optimization_leds_color(values):
    if EMULATOR:
        emulator.set_led_light(values, 28)
    else:
        comm.opt.set_led_light(values)

# 0x13 
# see neopixelgraphics
def clean_matrix():
    if EMULATOR:
        emulator.clean_matrix()
    else:
        comm.opt.clean_matrix()

def display_image(image):
    if EMULATOR:
        emulator.display_image(image)
    else:
        comm.opt.display_image(image)

# 0x30 multiple
def set_material_buttons_mode(values):
    if EMULATOR:
        pass
    else:
        comm.mat.switch_button_mode(values)

def set_optimization_buttons_mode(values):
    if EMULATOR:
        pass
    else:
        comm.opt.switch_button_mode(values)

# 0x31 multiple
def set_material_buttons_lock_status(values):
    if EMULATOR:
        pass
    else:
        comm.mat.lock_buttons(values)

def set_optimization_buttons_lock_status(values):
    if EMULATOR:
        pass
    else:
        comm.opt.lock_buttons(values)

# 0x32 multiple
def set_material_buttons_active_status(values):
    if EMULATOR:
        pass
    else:
        comm.mat.switch_buttons(values)

def set_optimization_buttons_active_status(values):
    if EMULATOR:
        pass
    else:
        comm.opt.switch_buttons(values)

def get_tunners_position():
    comm.opt.read_tunner()
    comm.opt.read()
    return comm.opt.tunners

def reset():
    for index in range(0, 6):
        lcd_display_at(index, ' ', 1)
        lcd_display_at(index, ' ', 2)
    set_buttons_enable_status(False, False)
    set_tunners_enable_status(False)
    set_independent_lights(True, True)
    set_led_brightness(50)
    set_material_ligths_on([0,0, 1,0, 2,0, 3,0, 4,0, 5,0, 6,0, 7,0])
    set_optimization_ligths_on([0,0, 1,0, 2,0, 3,0, 4,0])
    mat_leds = []
    for index in range(0, 28):
        mat_leds += [index, 0, 0, 0]
    set_material_leds_color(mat_leds)
    
    opt_leds = []
    for index in range(0, 5):
        opt_leds += [index, 0, 0, 0]
    set_optimization_leds_color(opt_leds)
    clean_matrix()

# should start serial communications if available or use emulator instead...
def init(emulation=False):
    global EMULATOR
    global MATERIAL
    global OPTIMIZATION
    print("mimo starting hardware connection", emulation)
    EMULATOR = emulation
    if EMULATOR:
        emulator.open()
    else:
        comm.init_connections()

    MATERIAL = comm.mat.active
    OPTIMIZATION = comm.opt.active
    #reset()

def update():
    if EMULATOR:
        pass
    else:
        comm.read_response()

def shutdown():
    print("mimo shutdown")
    reset()
    comm.close_connections()
    if EMULATOR:
        emulator.close()
