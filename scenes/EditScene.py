#!/usr/bin/env python

import pygame

from .BaseScene import SceneBase
from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
import mimo

# Edit Scene
# should load material into the slots, 
# in screen should display info about the news
# when player selects a material, it should be assigned 
# and displayed in screen,
# main screen should also display info about implications of the
# selected material
#
# when player will be ready the next screen should be optimization

class EditScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self, dt):
        SceneBase.Update(self, dt)
    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
    

