#!/usr/bin/env python

import pygame

from .BaseScene import SceneBase
from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
import mimo

# Submit Scene
# a summary with the impact of the news will be displayed to the 
# player
# player can submit or cancel the transmission(?) 
# when the player submit the video, the machine will show a Submitting
# process.
# when it will finish go to the results scene

class SubmitScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self, dt):
        SceneBase.Update(self, dt)
    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
    

