#!/usr/bin/env python

import pygame

from .BaseScene import SceneBase
from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
import mimo

# Printing Scene
# should start and print a new mission to accomplish to the player

# next scene will be edit 

class PrintingScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self, dt):
        SceneBase.Update(self, dt)
    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
    

