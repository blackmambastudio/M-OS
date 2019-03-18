#!/usr/bin/env python

import pygame
import mimo

from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
from utils import constants

from scenes.BaseScene import SceneBase

# Material tutorial Scene
# Available actions: back / next + material buttons
# Description: ""
# Next: optimization section tutorial


class MaterialTutorialScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.HWSetup()

        # initialize state
        self.used_mtl = 0

        # setup the layout for the scene
        self.SetupLayout()

    def HWSetup(self):
        mimo.set_material_buttons_mode([0,0, 1,0, 2,0, 5,0, 6,0, 7,0])
        mimo.set_material_buttons_lock_status([0,0, 1,0, 2,0, 5,0, 6,0, 7,0])

    def SetupLayout(self):
        subtitlefont = pygame.font.Font(constants.VCR_OSD_MONO, constants.FONT_SUBTITLE)

        self.subtitle = utils.Text("", subtitlefont)
        self.subtitle.SetPosition(constants.VIEWPORT_CENTER_X, 610)
        self.subtitle_shadow = utils.Text("", subtitlefont, color=(60,60,60))
        self.subtitle_shadow.SetPosition(constants.VIEWPORT_CENTER_X + 2, 610 + 2)

        self.tutorial_part = -1
        self.textLoader = None
        self.LoadNextPart()

        self.text0 = "MiMo analyze and filter material that can evoke emotions on people"
        self.text1 = "Please press the button with the label \"danger on border\""
        self.subtitle.SetText(self.text0)
        self.subtitle_shadow.SetText(self.text0)

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

    def Update(self, dt):
        SceneBase.Update(self, dt)

    
    def Render(self, screen):
        screen.fill(constants.PALLETE_BACKGROUND_BLUE)
        self.subtitle_shadow.render_multiline(screen)
        self.subtitle.render_multiline(screen)
        graphics.render()

    def SelectMaterial(self, index):
        self.used_mtl += 1

        if self.used_mtl >= 4:
            self.SwitchToScene("TutorialOpt")