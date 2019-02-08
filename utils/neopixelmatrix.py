
from comm.comm import opt

_backbuffer = []
_image = []
_buffer = []
_current_color = 0xf00

def reset():
    global _backbuffer
    global _image
    global _buffer
    _backbuffer = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
    ]
    _image = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
    ]
    _buffer = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
    ]

reset()

def clear():
    if not opt.active: return
    opt.clean_matrix()
    reset()

def renderBuffer(image):
    global _image
    global _backbuffer
    for j in range(0, 8):
        for i in range(0, 8):
            if _image[j][i] != _buffer[j][i]:
                if _buffer[j][i] == 0:
                    _backbuffer[j][i] = -1
                else:
                    _backbuffer[j][i] = _buffer[j][i]
                _image[j][i] = _buffer[j][i]
            else:
                _backbuffer[j][i] = 0

# assuming image = 8x8 pixels
def drawImage(image):
    global _buffer
    _buffer = image

def render():
    global _buffer
    renderBuffer(_buffer)
    _buffer = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]
    ] 
    colors = {}

    for j in range(0, 8):
        for i in range(0, 8):
            color = _backbuffer[j][i]
            if color != 0:
                if color == -1: color = 0
                if color not in colors:
                    colors[color] = []
                colors[color].append(j*8 + i)

    encoded = []
    for color in colors:
        red = (color>>8)
        green = (color >> 4)&0xf
        blue = color&0xf
        print(red, green, blue)
        encoded.append((red<<4) + red)
        encoded.append((green<<4) + green)
        encoded.append((blue<<4) + blue)
        encoded += colors[color] + [0]

    if len(encoded) == 0:
        return
    print(encoded)
    opt.display_image(encoded)


def plot(x, y):
    global _buffer
    _buffer[y][x] = _current_color

def plotLineLow(x0,y0, x1,y1):
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    
    D = 2*dy - dx
    y = y0

    for x in range(x0, x1+1):
        plot(x,y)
        if D > 0:
            y = y + yi
            D = D - 2*dx
    
        D = D + 2*dy
  

def plotLineHigh(x0,y0, x1,y1):
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
  
    D = 2*dx - dy
    x = x0

    for y in range(y0, y1+1):
        plot(x,y)
        if D > 0 :
            x = x + xi
            D = D - 2*dy

        D = D + 2*dx


def plotLine(x0,y0, x1,y1):
    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            plotLineLow(x1, y1, x0, y0)
        else:
            plotLineLow(x0, y0, x1, y1)
    else:
        if y0 > y1:
            plotLineHigh(x1, y1, x0, y0)
        else:
            plotLineHigh(x0, y0, x1, y1)


def drawRect(x, y, width, height):
    for i in range(x,width+x):
        plot(i, y)
        plot(i, y+height-1)
  
    for j in range(y+1, height-1+y):
        plot(x, j)
        plot(x+width-1, j)


def setColor(color):
    global _current_color
    _current_color = color

def setColorRGB(color):
    global _current_color
    _current_color = ((color[0]>>4)<<8) + ((color[1]>>4)<<4) + (color[2]>>4)

def wheel(pos):
    pos = 255 - pos
    if(pos < 85):
        return [255 - pos * 3, 0, pos * 3]

    if(pos < 170):
        pos -= 85
        return [0, pos * 3, 255 - pos * 3]
  
    pos -= 170;
    return [pos * 3, 255 - pos * 3, 0]