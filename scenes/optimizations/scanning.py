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
        mimo.set_led_brightness(150)
        mimo.set_tunners_enable_status(True)
        self.index = 8
        self.line_color = 0xf0f
        self.playing = False
        self.direction = 1
        self.mode = 1
        self.speed = 0.02
        

    def ProcessInput(self, events, pressed_keys):
        pass


    def Update(self, dt):
        OptimizationScene.Update(self, dt)
        if not self.playing: return
        
        self.coldown += dt
        if self.coldown > self.speed:
            self.coldown = 0
            self.UpdateLineMov()

    def UpdateLineMov(self):
        self.index += self.direction
        if self.index < -8:
            self.playing = False
        elif self.index > 15:
            self.playing = False

        

    def Render(self, screen):
        OptimizationScene.Render(self, screen)
        if self.playing == False: return
        self.draw_color_line(0xfff&self.line_color, self.index)
        self.draw_color_line(0xddd&self.line_color, self.index-self.direction)
        self.draw_color_line(0xbbb&self.line_color, self.index-self.direction*2)
        self.draw_color_line(0x999&self.line_color, self.index-self.direction*3)
        self.draw_color_line(0x777&self.line_color, self.index-self.direction*4)
        self.draw_color_line(0x555&self.line_color, self.index-self.direction*5)
        self.draw_color_line(0x333&self.line_color, self.index-self.direction*6)
        self.draw_color_line(0x111&self.line_color, self.index-self.direction*7)
        
        graphics.setColor(0)
        graphics.plot(2, 2)
        graphics.plot(3, 2)
        graphics.plot(4, 2)
        graphics.plot(3, 3)
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
        if self.playing or abs(distance)>10: return
        self.speed = 0.02
        self.NewScan(1, distance/abs(distance))

    def SwipeVertical(self, distance):
        if self.playing or abs(distance)>10: return
        self.speed = 0.02
        self.NewScan(2, distance/abs(distance))