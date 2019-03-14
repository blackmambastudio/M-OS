#!/usr/bin/env python

import pygame
import mimo

from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames

from .BaseScene import SceneBase

# Results Scene
#
# last scene, game over

class ResultsScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.AddTrigger(5, self, 'Terminate')
        titlefont = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 44)
        self.title = utils.Text("Results last scene", titlefont)
        self.title.SetPosition(1024/2, 546)

    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self, dt):
        SceneBase.Update(self, dt)
    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
        self.title.RenderWithAlpha(screen)
    

