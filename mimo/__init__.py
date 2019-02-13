
from .comm import comm
from .comm import I2C_LCD
from .comm import printer

# use printer 
def print(formatted_message):
    print("should send:<", formatted_message, "> to thermal printer")

# use lcd display 
def lcd_display_at(id, message):
    print("should display:<", message, "> on", id, "lcd id")


# 0x01 
def set_buttons_enable_status(mat_enable, opt_enable):
    print("set material buttons enable=", mat_enable, " and optimization buttons enable=", opt_enable)

# 0x02
def set_tunners_enable_status(enable):
    print("set all tunners enable=", enable)


# 0x03
def set_independent_lights(mat_value, opt_value):
    print("should set material lights independent independent=", mat_value, " and optimization lights independent=", opt_value)

# 0x04 
# see neopixelgraphics

# 0x05 
def set_led_brightness(brightness):
    print("should set the led brightness to:", brightness)

# 0x10
def set_button_light(id, color):
    print("should set button color to: <", color, "> to button:", id)

# 0x10 multiple
def set_buttons_light(values):
    print("should set button colors for:<", values)

# 0x11
def set_ligth_on(id, on):
    print("should turn on=", on, ". led", id)

# 0x11 multiple
def set_ligths_on(values):
    print("should turn leds for:<", values)

# 0x12 
def set_led_color(id, rgb):
    print("should set:<", rgb, "> color on led", id)

# 0x12 multiple 
def set_leds_color(values):
    print("should set colors for:<", values)

# 0x13 
# see neopixelgraphics

# 0x30
def set_button_mode(id, mode):
    print("should set button mode to push=", mode, ". to button:", id)

# 0x30 multiple
def set_buttons_mode(values):
    print("should set button modes for:<", values)

# 0x31 
def set_button_lock_status(id, lock):
    print("should set locked=<", lock, "> to button:", id)

# 0x31 multiple
def set_buttons_lock_status(values):
    print("should set button locks for:<", values)

# 0x32
def set_button_active_status(id, active):
    print("should set active=<", active, "> to button:", id)

# 0x32 multiple
def set_buttons_active_status(values):
    print("should set button active for:<", values)