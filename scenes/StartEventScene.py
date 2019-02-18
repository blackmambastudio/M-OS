#!/usr/bin/env python

import pygame

from .BaseScene import SceneBase
from .EditScene import EditScene
from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
import mimo

# StartEvent Scene
# PLAY STATUS #1
# should start and print a new mission to accomplish to the player

# next scene will be edit 

class StartEventScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        titlefont = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 44)
        self.title = utils.Text("Start event scene", titlefont)
        self.title.SetPosition(1280/2, 546)
        description = "displays a new event, description\nand all material needed"
        self.description = utils.Text(description, titlefont)
        self.description.SetPosition(1280/2, 50)

        self.AddTrigger(60, self, 'SwitchToScene', EditScene)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                self.SwitchToScene(EditScene)
                

    def Update(self, dt):
        SceneBase.Update(self, dt)
    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
        self.title.RenderWithAlpha(screen)
        self.description.render_multiline(screen)
    

