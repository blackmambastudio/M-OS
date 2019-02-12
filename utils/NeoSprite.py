
from . import neopixelmatrix as Graphics
from . import utils
from .neofont import letters as font

class NeoSprite():
    def __init__(self, path):
        self.image = utils.get_image_matrix(path)
        self.x = 0
        self.y = 0
        self.width = len(self.image[0])
        self.height = len(self.image)

    def render(self):
        Graphics.drawImage(self.image, self.x, self.y)


class AnimatedNeoSprite():
    def __init__(self, path, width=8, height=8):
        self.frames = utils.get_frames_for_image(path, width, height)
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.frame = 0
        self.framerate = 1
        self.time_ratio = 1/self.framerate
        self.time_acc = 0
        self.playing = False
        self.animation = range(0, len(self.frames))
        self.index_animation = 0
    
    def update(self, dt):
        if self.playing:
            self.time_acc += dt
            if self.time_acc > self.time_ratio:
                self.time_acc = 0
                self.index_animation += 1
                if self.index_animation >= len(self.animation):
                    self.index_animation = 0
                self.frame = self.animation[self.index_animation]

    def setFrameRate(self, framerate):
        if framerate == 0: return
        self.framerate = framerate
        self.time_ratio = 1/self.framerate
        self.time_acc = 0


    def render(self):
        Graphics.drawImage(self.frames[self.frame], self.x, self.y)

    def renderFrame(self, frame):
        Graphics.drawImage(self.frames[frame], self.x, self.y)

    def renderFrameAt(self, frame, x, y):
        Graphics.drawImage(self.frames[frame], x, y)


class TextNeoSprite():
    def __init__(self, text):
        self.image = [[],[],[],[],[]]
        for char in text:
            letter = font[char]
            char_spacing = len(letter[0])
            for j in range(0, 5):
                self.image[j] += letter[j] + [0]
        self.x = 0
        self.y = 0
        self.width = len(self.image[0])

    def render(self):
        Graphics.drawMonoPixels(self.image, self.x, self.y)

class SpriteFromFrames():
    def __init__(self, baseSprite, frames):
        self.image = []
        for j in range(0, baseSprite.height):
            self.image.append([])
            for frame in frames:
                self.image[j] += baseSprite.frames[frame][j]

        self.x = 0
        self.y = 0
        self.width = baseSprite.width*len(frames)
        self.height = baseSprite.height

    def render(self):
        Graphics.drawImage(self.image, self.x, self.y)