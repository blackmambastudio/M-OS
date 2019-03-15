#!/usr/bin/env python3
import pygame

from .OptimizationScene import OptimizationScene
from utils import utils
from utils import neopixelmatrix as graphics
from random import random
import mimo

class ScanningScene(OptimizationScene):
    def __init__(self):
        OptimizationScene.__init__(self)
        self.line_anim = 0
        mimo.set_led_brightness(250)
        self.line_starting = 8
        self.line_color = 0xf0f

    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self, dt):
        OptimizationScene.Update(self, dt)
        self.line_anim += dt
        if self.line_anim > 0.08:
            self.line_anim = 0
            self.line_starting -= 1
            if self.line_starting < -4:
                self.line_starting = 8


    def Render(self, screen):
        OptimizationScene.Render(self, screen)
        self.draw_color_line(0xfff&self.line_color, self.line_starting)
        self.draw_color_line(0xbbb&self.line_color, self.line_starting+1)
        self.draw_color_line(0x777&self.line_color, self.line_starting+2)
        self.draw_color_line(0x333&self.line_color, self.line_starting+3)
        graphics.render()

    def draw_color_line(self, color, line):
        if line < 0 or line > 7: return
        graphics.setColor(color)
        graphics.plotLine(line, 0, line, 7)
