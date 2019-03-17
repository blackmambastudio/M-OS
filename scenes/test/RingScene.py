#!/usr/bin/env python

import pygame

from scenes.BaseScene import SceneBase
from utils import utils
from utils import ringpixel as ring
import mimo

class RingScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        mimo.reset()
        self.percentage = 0
        mimo.set_led_brightness(120)
        mimo.set_independent_lights(True, True)
        # check ring and bulbs leds
        self.AddTrigger(1, self, 'LoadRing')


    def Update(self, dt):
        SceneBase.Update(self, dt)
    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
        ring.fill_percentage(self.percentage)
    
    def LoadRing(self):
        self.AddTween("easeInSine", 3, self, "percentage", 0, 1.1, 0)
        self.AddTween("linear", 10, self, "percentage", 1, 0, 4)
        self.AddTrigger(13.5, self, 'LoadRing')

