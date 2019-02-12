
from . import neopixelmatrix as Graphics
from . import utils

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
                print(self.index_animation, self.frame)

    def setFrameRate(self, framerate):
        if framerate == 0: return
        self.framerate = framerate
        self.time_ratio = 1/self.framerate
        self.time_acc = 0


    def render(self):
        Graphics.drawImage(self.frames[self.frame], self.x, self.y)
