#!/usr/bin/env python

import pygame

from .BaseScene import SceneBase
from .ResultsScene import ResultsScene
from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
import mimo

# Submit Scene
# PLAY STATUS #4
# a summary with the impact of the news will be displayed to the 
# player
# player can submit or cancel the transmission(?) 
# when the player submit the video, the machine will show a Submitting
# process.
# when it will finish go to the results scene

class SubmitScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        titlefont = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 44)
        self.title = utils.Text("Submit scene", titlefont)
        self.title.SetPosition(1280/2, 546)
        self.AddTrigger(60, self, 'SwitchToScene', ResultsScene)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                self.SwitchToScene(ResultsScene)

    def Update(self, dt):
        SceneBase.Update(self, dt)
    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
        self.title.RenderWithAlpha(screen)
    

