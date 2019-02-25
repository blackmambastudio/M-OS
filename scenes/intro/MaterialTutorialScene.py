#!/usr/bin/env python

import pygame
import mimo

from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames

from scenes.BaseScene import SceneBase
from .OptimizationTutorialScene import OptimizationTutorialScene

# Material tutorial Scene
# Available actions: back / next + material buttons
# Description: ""
# Next: optimization section tutorial


class MaterialTutorialScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.HWSetup()

        subtitlefont = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 32)
        self.subtitle = utils.Text("", subtitlefont)
        self.subtitle.SetPosition(1280/2, 610)

        self.tutorial_part = -1
        self.textLoader = None
        self.LoadNextPart()

        self.text0 = "MiMo analyze and filter material that can evoke emotions on people"
        self.text1 = "Please press the button with the label \"danger on border\""
        self.subtitle.SetText(self.text0)

    def HWSetup(self):
        mimo.set_material_buttons_mode([0,0, 1,0, 2,0, 5,0, 6,0, 7,0])
        mimo.set_material_buttons_lock_status([0,0, 1,0, 2,0, 5,0, 6,0, 7,0])
    

    def LoadNextPart(self):
        pass

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                self.SelectMaterial(0)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.SelectMaterial(1)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                self.SelectMaterial(2)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_o:
                self.SelectMaterial(3)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_k:
                self.SelectMaterial(4)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                self.SelectMaterial(5)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                print("nexT?")
                

    def Update(self, dt):
        SceneBase.Update(self, dt)

    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
        self.subtitle.render_multiline(screen)
        graphics.render()

    def SelectMaterial(self, index):
        print("select material", index)