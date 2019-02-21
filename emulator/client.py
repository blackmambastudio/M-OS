import socket
import sys

sock = None
def open():
    global sock
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 6060)
    sock.settimeout(0.01)
    sock.connect(server_address)


def write(command, payload):
    if not sock:
        print("socket not open")
        return
    # Send data
    data = [0x7E, command, len(payload)] + payload
    print(data)
    sock.send(bytearray(data))


def close():
    write(0x90, [0x01])
    sock.close()


def termal_print(formatted_message):
    message = list(formatted_message.encode())
    write(0x92, message)

# use lcd display 
def lcd_display_at(lcd_id, message, line):
    message = [lcd_id, line]+list(message.encode())
    write(0x91, message)

# 0x01 
def set_buttons_enable_status(mat_enable, opt_enable):
    print("set material buttons enable=", mat_enable, " and optimization buttons enable=", opt_enable)

# 0x02
def set_tunners_enable_status(enable):
    print("set all tunners enable=", enable)

# 0x03
def set_independent_lights(mat_value, opt_value):
    print("should set material lights independent independent=", mat_value, " and optimization lights independent=", opt_value)

# 0x05 applies brightness to both sections
def set_led_brightness(brightness):
    write(0x05, [brightness%256])

# 0x10    
def set_buttons_light(values):
    print("should set button colors for:<", values)

# 0x11 multiple
def set_ligths_on(values):
    print("should turn leds for:<", values) 

def set_led_light(colors, start_index):
    colors = [colors[i]+start_index if i%4==0 else colors[i] for i in range(0, len(colors))]
    message = [len(colors)//4] + colors
    write(0x12, message)

def clean_matrix():
    write(0x04, [0])


def display_image(encoded_image):
    write(0x13, encoded_image)

#0x30
def set_buttons_mode(values):
    print("should set button modes for:<", values)

#0x31
def set_buttons_lock_status(values):
    print("should set button locks for:<", values)

# 0x32 multiple
def set_buttons_active_status(values):
    print("should set button active for:<", values)