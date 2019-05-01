#!/usr/bin/env python3
import pygame

from .OptimizationScene import OptimizationScene, STATUS
from utils import utils, constants
from utils import neopixelmatrix as graphics
from random import random, shuffle
import mimo
import pygame

class AimingScene(OptimizationScene):
    def __init__(self):
        self.minigametitle = 'aiming.opt'
        OptimizationScene.__init__(self)

        self.point = {'x': 2, 'y': 2}
        self.debugKnobRight = utils.Text('knobs RIGHT - 0', self.subtitle_font, color=constants.PALETTE_TITLES_DARK_BLUE)
        self.debugKnobRight.SetPosition(constants.VIEWPORT_CENTER_X - 100, 150)
        self.debugKnobLeft = utils.Text('knobs LEFT - 0', self.subtitle_font, color=constants.PALETTE_TITLES_DARK_BLUE)
        self.debugKnobLeft.SetPosition(constants.VIEWPORT_CENTER_X - 100, 200)


    def SetupMimo(self):
        mimo.set_led_brightness(150)
        mimo.set_tunners_enable_status(True)
        mimo.set_independent_lights(False, True)
        

    def ProcessInputOpt(self, events, pressed_keys):
        pass


    def Update(self, dt):
        tunners = mimo.get_tunners_position()
        self.point['x'] = (1020 - tunners[0])//128 # inverse x
        self.point['y'] = tunners[1]//128
        self.debugKnobLeft.SetText('knobs LEFT ' + str(tunners[0]))
        self.debugKnobRight.SetText('knobs RIGHT ' + str(tunners[1]))


    def RenderBody(self, screen):
        self.debugKnobLeft.RenderWithAlpha(screen)
        self.debugKnobRight.RenderWithAlpha(screen)
        graphics.setColor(0xf22)
        graphics.plotLine(self.point['x'], 0, self.point['x'], 7)
        graphics.plotLine(0, self.point['y'], 7, self.point['y'])
        graphics.render()
