import os
import pygame
import random

from . import constants

_image_library = {}
_sound_library = {}

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(canonicalized_path).convert_alpha()
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

# music capabilites 
# https://www.pygame.org/docs/ref/music.html?highlight=pygame%20mixer%20sound
def play_music(path, loop=0, delay=0.0, volume=1):
    canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
    pygame.mixer.music.load(canonicalized_path)
    pygame.mixer.music.play(loop, delay)
    pygame.mixer.music.set_volume(volume)

def stop_music():
    pygame.mixer.music.stop()

def fadeout_music(time):
    pygame.mixer.music.fadeout(time)

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)
    return temp

class Tween():
    def __init__(self, func, timeout, obj, prop, start, end, delay, resolution=-1):
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
        self.resolution = resolution

    def Update(self, dt):
        if self.Finished(): return
        if self.delay > 0:
            self.delay -= dt
            return
        
        self.time += dt
        ratio = self.time/self.timeout
        if ratio > 1:
            ratio = 1
        if self.resolution != -1:
            ratio = (int(ratio*self.resolution))/self.resolution
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
        self.rotation = 0
        self.original = self.image
        self.must_update = True
        self.cached_image = self.image
        self.prev_opacity = -1
        self.frame_index = 0
        self.frameDelay = 1
        self.framedt = 0
        self.frameWidth = 0
        self.frameHeight = 0
        self.animationFrames=[]
        #317X374

    def GetRotation(self):
        return self.rotation

    def updateFrame(self, dt):
        self.framedt += dt
        if self.framedt > self.frameDelay:
            self.framedt = 0
            self.frame_index += 1
            if self.frame_index >= len(self.animationFrames):
                self.frame_index = 0

    def RenderFrame(self, screen):
        frame = self.animationFrames[self.frame_index]
        screen.blit(self.image, self.position, (frame*self.frameWidth, 0, self.frameWidth, self.frameHeight))
        

    def SetPosition(self, x, y):
        self.x = x
        self.y = y
        rect = self.image.get_rect()
        self.position = (self.x - rect.width*self.anchor[0], self.y - rect.height*self.anchor[1])

    def GetClipRect(self):
        rect = self.image.get_rect()
        return (self.position[0], self.position[1], rect.width, rect.height)

    def Rotate(self, rotation):
        self.rotation = rotation % 360
        self.image = pygame.transform.rotate(self.original, self.rotation)
        self.SetPosition(self.x, self.y)
        self.must_update = True

    def Scale(self, size):
        rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (int(rect.width*size[0]), int(rect.height*size[1])))
        self.SetPosition(self.x, self.y)
        self.must_update = True

    def Render(self, screen, position=None, area=None):
        if not position:
            position = self.position

    def RenderWithAlpha(self, screen, position=None,area=None):
        if self.must_update or self.prev_opacity != self.opacity :
            self.cached_image = blit_alpha(screen, self.image, self.position, int(self.opacity))
            self.must_update = False
            self.prev_opacity = self.opacity
        else:
            if not position:
                position = self.position
            screen.blit(self.cached_image, position, area)

    def setAnchor(self, x, y):
        self.anchor = (x, y)
        self.SetPosition(self.x, self.y)

    def SetOpacity(self, opacity):
        self.opacity = opacity
        self.must_update = True 


class Text():
    def __init__(self, text, font, x = 0, y = 0, color = constants.PALLETE_DARK_BLUE):
        self.raw_text = text.upper()
        self.color = color
        self.font = font
        self.SetText(text, False)
        self.opacity = 255
        self.anchor = (0.5, 0.5)
        self.SetPosition(x, y)
        self.cached_surface = None

    def SetPosition(self, x, y):
        self.x = x
        self.y = y
        self.position = (self.x - self.text.get_width()*self.anchor[0], self.y - self.text.get_height()*self.anchor[1])

    def render(self, screen):
        screen.blit(self.text, self.position)
        #pass

    def render_cached(self, screen):
        screen.blit(self.cached_surface, self.position)

    # cached function
    def renderWithChromaticDistortion(self, screen):
        if self.cached_surface:
            self.render_cached(screen)
            return
        temp = pygame.Surface((self.text.get_width()+2, self.text.get_height()), pygame.SRCALPHA, 32).convert_alpha()
        temp.blit(self.text_shadow_pink, (0, 0))
        temp.blit(self.text_shadow_blue, (2, 0))
        temp.blit(self.text, (1, 0))
        screen.blit(temp, self.position)
        self.cached_surface = temp
        #pass

    def RenderWithAlpha(self, screen):
        blit_alpha(screen, self.text, self.position, int(self.opacity))
        #pass

    def setAnchor(self, x, y):
        self.anchor = (x, y)
        self.SetPosition(self.x, self.y)

    def SetOpacity(self, opacity):
        self.opacity = opacity

    def SetText(self, text, update_position=True):
        self.cached_surface = None
        self.raw_text = text.upper()
        self.text = self.font.render(self.raw_text, True, self.color)
        self.text_shadow_blue = self.font.render(self.raw_text, True, (0,255,255))
        self.text_shadow_pink = self.font.render(self.raw_text, True, (255,0,255))
        if update_position:
            self.SetPosition(self.x, self.y)

    def DecorateText(self, prefix, suffix):
        self.text = self.font.render(prefix + self.raw_text + suffix, True, self.color)
        self.SetPosition(self.x, self.y)

    def render_multiline(self, screen):
        lines = self.raw_text.splitlines()
        x, y = self.position
        for line in lines:
            word_surface = self.font.render(line, 0, self.color)
            word_width, word_height = word_surface.get_size()
            screen.blit(word_surface, (self.x - word_width*self.anchor[0], y))
            y += word_height

    def SetColor(self, new_color):
        self.color = new_color
        self.cached_surface = None

    # cached function
    def render_multiline_truncated(self, screen, max_width=0, max_height=0):
        if self.cached_surface:
            self.render_cached(screen)
            return
        if max_width == 0:
            max_width = constants.VIEWPORT_WIDTH
        if max_height == 0:
            max_height = constants.VIEWPORT_HEIGHT

        temp = pygame.Surface((max_width, max_height), pygame.SRCALPHA, 32).convert_alpha()
        
        lines = self.raw_text.splitlines()
        x, y = (0, 0)
        space = self.font.size(' ')[0]

        for line in lines:
            words = line.split(" ")
            for word in words:
                word_surface = self.font.render(word, 0, self.color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = 0
                    y += word_height
                temp.blit(word_surface, (x, y))
                x += word_width + space
            x = 0
            y += word_height

        screen.blit(temp, self.position)
        self.cached_surface = temp


def get_image_matrix(path):
    image = get_image(path)
    temp = pygame.Surface((image.get_width(), image.get_height()), pygame.SRCALPHA, 32).convert_alpha()
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

def align_text(text, left, spaces, space_char=' '):
    new_text = text
    new_text = new_text[0:spaces]
    start_index = len(new_text)
    for index in range(start_index, spaces):
        if left:
            new_text += space_char
        else:
            new_text = space_char + new_text

    return new_text


class TextLoader():
    def __init__(self, text_to_load, speed=0.6, load_by_words=False):
        self.current_text = ""
        self.text_to_load = text_to_load
        self.cursor = -1
        self.speed = speed
        self.counter = 0
        self.finished = False
        self.load_by_words = load_by_words

    def update_text(self):
        if self.load_by_words:
            self.cursor = self.text_to_load.find(" ", self.cursor+1)
            if self.cursor == -1:
                self.cursor = len(self.text_to_load) -1
        else:
            self.cursor += 1

        self.current_text = self.text_to_load[:self.cursor]
        self.finished = (self.cursor + 1) == len(self.text_to_load)


    def update(self, dt):
        if self.finished: return False

        self.counter += dt
        if self.counter >= self.speed:
            self.update_text()
            self.counter = 0
            return True

        return False

    def complete(self):
        self.current_text = self.text_to_load
        self.finished = True
