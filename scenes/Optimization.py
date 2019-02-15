#!/usr/bin/env python

import pygame

from .BaseScene import SceneBase
from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
import mimo

# Optimization Scene
# depending on the selected material the player will have
# the opportunity to increase the impact of the transmission
# one of many possible minigames will be loaded and displayed
# to the player

# next screen will depend on player's actions

class OptimizationScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self, dt):
        SceneBase.Update(self, dt)
    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
    

