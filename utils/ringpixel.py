
import mimo
import math

ring_led_ids = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 8, 9, 10, 11]
# progress a float between 0 and 1
current_color = [0xff, 0x00, 0x00]
empty = [0,0,0]

cached_progress = -1

def fill_percentage(progress):
    global cached_progress
    # 0 is first one
    # 100 is last one
    message = []
    value = math.ceil(progress*16)
    if cached_progress == value: return
    current_color = wheel(int(progress*64))
    cached_progress = value
    for i in range(0, 16):
        if i < value:
            message += [ring_led_ids[i]]+current_color
        else:
            message += [ring_led_ids[i]]+empty
    mimo.set_material_leds_color(message)


def fill():
    message = []
    for led in ring_led_ids:
        message += [led] + current_color
    mimo.set_material_leds_color(message)

# returns a 
def wheel(pos):
    pos = 255 - pos
    if(pos < 85):
        return [255 - pos * 3, 0, pos * 3]

    if(pos < 170):
        pos -= 85
        return [0, pos * 3, 255 - pos * 3]
  
    pos -= 170;
    return [pos * 3, 255 - pos * 3, 0]
