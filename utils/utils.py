import os
import pygame

_image_library = {}
_sound_library = {}

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(canonicalized_path)
            _image_library[path] = image
    return image


def get_sound(path):
    global _sound_library
    sound = _sound_library.get(path)
    if sound == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        sound = pygame.mixer.Sound(canonicalized_path)
        _sound_library[path] = sound
    return sound


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)


class Tween():
    def __init__(self, func, timeout, obj, prop, start, end, delay):
        self.tween = func
        self.timeout = timeout
        self.obj = obj
        self.prop = prop
        self.start = start
        self.end = end
        self.interval = end - start
        self.value = 0.0
        self.time = 0.0
        self.delay = delay

    def Update(self, dt):
        if self.Finished(): return
        if self.delay > 0:
            self.delay -= dt
            return
        
        self.time += dt
        ratio = self.time/self.timeout
        if ratio > 1:
            ratio = 1
        self.value = self.tween(ratio)
        setattr(self.obj, self.prop, self.start + self.value*self.interval)

    def Finished(self):
        return self.value == 1


class Sprite():
    def __init__(self, path, x=0, y=0):
        self.image = get_image(path)
        self.opacity = 255
        self.anchor = (0.5, 0.5)
        self.SetPosition(x, y)

    def SetPosition(self, x, y):
        self.x = x
        self.y = y
        rect = self.image.get_rect()
        self.position = (self.x - rect.width*self.anchor[0], self.y - rect.height*self.anchor[1])

    def RenderWithAlpha(self, screen):
        blit_alpha(screen, self.image, self.position, int(self.opacity))

    def setAnchor(self, x, y):
        self.anchor = (x, y)
        self.SetPosition(self.x, self.y)

    def SetOpacity(self, opacity):
        self.opacity = opacity


class Text():
    def __init__(self, text, font, x=0, y=0):
        self.raw_text = text
        self.text = font.render(text, True, (255, 255, 255))
        self.font = font
        self.opacity = 255
        self.anchor = (0.5, 0.5)
        self.SetPosition(x, y)

    def SetPosition(self, x, y):
        self.x = x
        self.y = y
        self.position = (self.x - self.text.get_width()*self.anchor[0], self.y - self.text.get_height()*self.anchor[1])

    def render(self, screen):
        screen.blit(self.text, self.position)

    def RenderWithAlpha(self, screen):
        blit_alpha(screen, self.text, self.position, int(self.opacity))
    
    def setAnchor(self, x, y):
        self.anchor = (x, y)
        self.SetPosition(self.x, self.y)

    def SetOpacity(self, opacity):
        self.opacity = opacity

    def SetText(self, text):
        self.raw_text = text
        self.text = self.font.render(self.raw_text, True, (255, 255, 255))
        self.SetPosition(self.x, self.y)

    def DecorateText(self, prefix, suffix):
        self.text = self.font.render(prefix + self.raw_text + suffix, True, (255, 255, 255))
        self.SetPosition(self.x, self.y)


def get_image_matrix(path):
    image = get_image(path)
    temp = pygame.Surface((image.get_width(), image.get_height())).convert()
    temp.blit(image, (0, 0))
    image_matrix = []
    for j in range(0, image.get_height()):
        image_matrix.append([])
        for i in range(0, image.get_width()):
            color = temp.get_at((i, j))
            image_matrix[j].append(((color.r>>4)<<8) + ((color.g>>4)<<4)+(color.b>>4))
    return image_matrix


def get_frames_for_image(path, width=8, height=8):
    frames = []
    full_image = get_image_matrix(path)

    x_tiles = int(len(full_image[0])/width)
    y_tiles = int(len(full_image)/height)
    for j in range(0, y_tiles):
        for i in range(0, x_tiles):
            frame = []
            for jj in range(0,height):
                frame.append([])
                for ii in range(0,width):
                    frame[jj].append(full_image[j*height+jj][i*width+ii])
            frames.append(frame)
    return frames