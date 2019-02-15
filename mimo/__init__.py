#!/usr/bin/env python
from emulator import client as emulator
from .comm import comm

LCD = False
PRINTER = False
MATERIAL = False
OPTIMIZATION = False
EMULATOR = False

try:
    from .comm import I2C_LCD
    LCD = True
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
#                   8-09-10-11         
#                                   ring
#                                  12 - 27
# +----- mat ----+---- opt ----+---- mat ----+
# | button_a  0  |   matrix    | button_d  7 |
# | button_b  1  |   33-96     | button_e  6 |
# | button_c  2  | 28  30  32  | button_f  5 |
# |              |   29  31    |             |
# | button_no 3  | button_0-4  | button_ok 4 |
# +--------------+-------------+-------------+
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
def termal_print(formatted_message):
    print("should send:<", formatted_message, "> to thermal printer")

# use lcd display 
def lcd_display_at(id, message):
    print("should display:<", message, "> on", id, "lcd id")


# 0x01 
def set_buttons_enable_status(mat_enable, opt_enable):
    print("set material buttons enable=", mat_enable, " and optimization buttons enable=", opt_enable)
    if EMULATOR:
        pass
    else:
        comm.mat.enable_buttons(int(mat_enable))
        comm.opt.enable_buttons(int(opt_enable))

# 0x02
def set_tunners_enable_status(enable):
    print("set all tunners enable=", enable)
    if EMULATOR:
        pass
    else:
        comm.opt.enable_tunners(int(enable))


# 0x03
def set_independent_lights(mat_value, opt_value):
    print("should set material lights independent independent=", mat_value, " and optimization lights independent=", opt_value)
    if EMULATOR:
        pass
    else:
        comm.mat.set_independent_lights(int(mat_value))
        comm.opt.set_independent_lights(int(opt_value))

# 0x04 
# see neopixelgraphics

# 0x05 applies brightness to both sections
def set_led_brightness(brightness):
    print("should set the led brightness to:", brightness)
    if EMULATOR:
        emulator.set_led_brightness(brightness)
    else:
        comm.mat.set_led_brightness(brightness)
        comm.opt.set_led_brightness(brightness)

# 0x10
def set_material_buttons_light(values):
    print("should set button colors for:<", values)
    if EMULATOR:
        pass
    else:
        comm.mat.set_buttons_backlight(values)

def set_optimization_buttons_light(values):
    print("should set button colors for:<", values)
    if EMULATOR:
        pass
    else:
        comm.opt.set_buttons_backlight(values)

# 0x11 multiple
def set_material_ligths_on(values):
    print("should turn leds for mat:<", values)
    if EMULATOR:
        pass
    else:
        comm.mat.switch_buttons_backlight(values)

def set_optimization_ligths_on(values):
    print("should turn leds for opt:<", values)
    if EMULATOR:
        pass
    else:
        comm.opt.switch_buttons_backlight(values)

# 0x12 multiple 
def set_material_leds_color(values):
    print("should set colors for:<", values)
    if EMULATOR:
        emulator.set_led_light(values, 0)
    else:
        comm.mat.set_led_light(values)

def set_optimization_leds_color(values):
    print("should set colors for:<", values)
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
    print("should set button modes for:<", values)
    if EMULATOR:
        pass
    else:
        comm.mat.switch_button_mode(values)

def set_optimization_buttons_mode(values):
    print("should set button modes for:<", values)
    if EMULATOR:
        pass
    else:
        comm.opt.switch_button_mode(values)

# 0x31 multiple
def set_material_buttons_lock_status(values):
    print("should set button locks for:<", values)
    if EMULATOR:
        pass
    else:
        comm.mat.lock_buttons(values)

def set_optimization_buttons_lock_status(values):
    print("should set button locks for:<", values)
    if EMULATOR:
        pass
    else:
        comm.opt.lock_buttons(values)

# 0x32 multiple
def set_material_buttons_active_status(values):
    print("should set button active for:<", values)
    if EMULATOR:
        pass
    else:
        comm.mat.switch_buttons(values)

def set_optimization_buttons_active_status(values):
    print("should set button active for:<", values)
    if EMULATOR:
        pass
    else:
        comm.opt.switch_buttons(values)


# should start serial communications if available or use emulator instead...
def init(emulation=False):
    global EMULATOR
    global MATERIAL
    global OPTIMIZATION
    print("mimo starting hardware connection")
    EMULATOR = emulation
    if EMULATOR:
        emulator.open()
    else:
        comm.init_connections('COM5', 'COM15')
    MATERIAL = comm.mat.active
    OPTIMIZATION = comm.opt.active

def update():
    if EMULATOR:
        pass
    else:
        comm.read_response()

def shutdown():
    print("mimo shutdown")
    comm.close_connections()
    if EMULATOR:
        emulator.close()