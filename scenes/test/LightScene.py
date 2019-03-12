#!/usr/bin/env python

import pygame

from scenes.BaseScene import SceneBase
from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
import mimo, random

class LightScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        mimo.reset()

        mimo.set_led_brightness(120)
        mimo.set_independent_lights(True, True)
        # check ring and bulbs leds
        factor = 0.2
        loops = 50
        n_leds = 28
        leds = list(range(0, 28))
        for index in range(0, n_leds*loops):
            led_i = leds[index%n_leds]
            self.AddTrigger((1.5+index)*factor, mimo, 'set_material_leds_color', [led_i, int(random.random()*255), int(random.random()*255), int(random.random()*255)])
            self.AddTrigger((1.5+index+0.9)*factor, mimo, 'set_material_leds_color', [led_i, 0, 0, 0])


        n_leds = 69
        leds = list(range(0, 69))
        for index in range(0, n_leds*loops):
            led_i = leds[index%n_leds]
            self.AddTrigger((1.5+index)*factor, mimo, 'set_optimization_leds_color', [led_i, int(random.random()*255), int(random.random()*255), int(random.random()*255)])
            self.AddTrigger((1.5+index+0.9)*factor, mimo, 'set_optimization_leds_color', [led_i, 0, 0, 0])




    def Update(self, dt):
        SceneBase.Update(self, dt)
    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
    

