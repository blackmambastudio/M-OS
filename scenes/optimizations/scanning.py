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
        self.col_start = 8
        self.row_start = 8
        self.line_color = 0xf0f
        #self.direction = -1 # 1 or -1
        #self.mode = 1 # 0 none, 1 horizontal, 2 vertical
        self.NewScan()

    def ProcessInput(self, events, pressed_keys):
        pass


    def Update(self, dt):
        OptimizationScene.Update(self, dt)
        self.coldown += dt
        if self.coldown > 0.08:
            self.coldown = 0
            self.UpdateLineMov()

    def UpdateLineMov(self):
        if self.mode == 1:
            self.col_start += self.direction
            if self.col_start < -4:
                self.NewScan()
            elif self.col_start > 11:
                self.NewScan()

        elif self.mode == 2:
            self.row_start += self.direction
            if self.row_start < -4:
                self.NewScan()
            elif self.row_start > 11:
                self.NewScan()

    def Render(self, screen):
        OptimizationScene.Render(self, screen)

        self.draw_color_line(0xfff&self.line_color, self.col_start, self.row_start)
        self.draw_color_line(0xbbb&self.line_color, self.col_start, self.row_start-self.direction)
        self.draw_color_line(0x777&self.line_color, self.col_start, self.row_start-self.direction*2)
        self.draw_color_line(0x333&self.line_color, self.col_start, self.row_start-self.direction*3)
        graphics.render()

    def draw_color_line(self, color, col, row):
        if col < 0 or col > 7 or row<0 or row>7: return
        graphics.setColor(color)
        if self.mode == 1:
            graphics.plotLine(col, 0, col, 7)
        elif self.mode == 2:
            graphics.plotLine(0, row, 7, row)

    def NewScan(self):
        #self.mode = int(random()*2) + 1
        #self.direction = -1 if random() <0.5 else 1
        self.mode = 2
        self.direction = -1
        print(self.mode, self.direction)
        if self.mode == 2:
            if self.direction == 1:
                self.row_start = -1
            else:
                self.row_start = 8
            self.col_start = 0
        elif self.mode == 1:
            if self.direction == 1:
                self.col_start = -1
            else:
                self.col_start = 8
            self.row_start = 0
        print(self.col_start, self.row_start)