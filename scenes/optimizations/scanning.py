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
        self.coldown = 0
        mimo.set_led_brightness(250)
        self.index = 8
        self.line_color = 0xf0f
        self.playing = False
        self.direction = 1
        self.mode = 1

    def ProcessInput(self, events, pressed_keys):
        pass


    def Update(self, dt):
        OptimizationScene.Update(self, dt)
        if not self.playing: return
        
        self.coldown += dt
        if self.coldown > 0.06:
            self.coldown = 0
            self.UpdateLineMov()

    def UpdateLineMov(self):
        self.index += self.direction
        if self.index < -4:
            self.playing = False
        elif self.index > 11:
            self.playing = False

        

    def Render(self, screen):
        OptimizationScene.Render(self, screen)
        if self.playing == False: return

        self.draw_color_line(0xfff&self.line_color, self.index)
        self.draw_color_line(0xbbb&self.line_color, self.index-self.direction)
        self.draw_color_line(0x777&self.line_color, self.index-self.direction*2)
        self.draw_color_line(0x333&self.line_color, self.index-self.direction*3)
        graphics.render()

    def draw_color_line(self, color, idx):
        if idx < 0 or idx > 7: return
        graphics.setColor(color)
        if self.mode == 1:
            graphics.plotLine(idx, 0, idx, 7)
        elif self.mode == 2:
            graphics.plotLine(0, idx, 7, idx)

    def NewScan(self, mode, direction):
        self.line_color = [0xf00, 0xff0, 0x0f0, 0x0ff, 0x00f, 0xf0f, 0xfff][int(random()*7)]
        self.mode = mode
        self.direction = int(direction)
        if self.direction == 1:
            self.index = -1
        else:
            self.index = 8
            
        self.playing = True

    def SwipeHorizontal(self, distance):
        if self.playing: return
        self.NewScan(1, distance/abs(distance))

    def SwipeVertical(self, distance):
        if self.playing: return
        self.NewScan(2, distance/abs(distance))