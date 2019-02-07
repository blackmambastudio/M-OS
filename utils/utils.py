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
    def __init__(self, path):
        self.image = get_image(path)
        self.opacity = 1.0
        self.position = (200.0, 450.0)
        self.anchor = (0.5, 0.5)

    def SetPosition(self, x, y):
        rect = self.image.get_rect()
        self.position = (x - rect.width*self.anchor[0], y - rect.height*self.anchor[1])

    def RenderWithAlpha(self, screen):
        blit_alpha(screen, self.image, self.position, int(self.opacity))
