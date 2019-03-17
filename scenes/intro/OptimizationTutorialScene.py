#!/usr/bin/env python

import pygame
import mimo

from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
from utils import constants

from scenes.BaseScene import SceneBase

# Optimization Scene
# Available actions: back / next - optimization buttons and tunner
# Description: "cinematic explain the player the ludovic experiment"
# Next: material section tutorial


class OptimizationTutorialScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.HWSetup()

        # initialize state
        self.pressed_keys = 0

        # setup the layout for the scene
        self.SetupLayout()

    def HWSetup(self):
        mimo.set_material_buttons_mode([0,0, 1,0, 2,0, 5,0, 6,0, 7,0])
        mimo.set_material_buttons_lock_status([0,1, 1,1, 2,1, 5,1, 6,1, 7,1])

    def SetupLayout(self):
        subtitlefont = pygame.font.Font(constants.VCR_OSD_MONO, constants.FONT_SUBTITLE)

        self.subtitle = utils.Text("", subtitlefont)
        self.subtitle.SetPosition(constants.VIEWPORT_CENTER_X, 610)
        self.subtitle_shadow = utils.Text("", subtitlefont, color=(60,60,60))
        self.subtitle_shadow.SetPosition(constants.VIEWPORT_CENTER_X + 2, 610 + 2)

        self.text0 = "press all the optimization keys"
        self.subtitle.SetText(self.text0)
        self.subtitle_shadow.SetText(self.text0)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                self.OptimizationKeyPressed()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                self.OptimizationKeyPressed()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                self.OptimizationKeyPressed()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                self.OptimizationKeyPressed()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_v:
                self.OptimizationKeyPressed()

    def Update(self, dt):
        SceneBase.Update(self, dt)

    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))

        self.subtitle_shadow.render_multiline(screen)
        self.subtitle.render_multiline(screen)

        graphics.render()

    def OptimizationKeyPressed(self):
        self.pressed_keys += 1

        if self.pressed_keys >= 5:
            self.SwitchToScene("LoadingNews")