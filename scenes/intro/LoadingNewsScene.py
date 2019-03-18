#!/usr/bin/env python

import pygame
import mimo

from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
from utils import constants

from scenes.BaseScene import SceneBase

# Loading News Scene
# Available actions: back / next
# Description: Shows a message for the player to start editing. Before loading the
#   BeginEventScene, it shows a fake loading news message
# Next: Begin Event Scene

class LoadingNewsScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.HWSetup()

        # initialize state
        self.instruction_msg = "press (w) and (i) to start editing the news"
        self.loading_msg = "facts incoming..."
        self.loading = False
        self.countdown = 3000

        # setup the layout for the scene
        self.SetupLayout()

    def HWSetup(self):
        # TODO: turn on all the lights in MiMo
        pass

    def SetupLayout(self):
        titlefont = pygame.font.Font(constants.VCR_OSD_MONO, constants.FONT_TITLE)

        self.subtitle = utils.Text("", titlefont)
        self.subtitle.SetPosition(constants.VIEWPORT_CENTER_X, constants.VIEWPORT_CENTER_Y)
        self.subtitle_shadow = utils.Text("", titlefont, color=(60,60,60))
        self.subtitle_shadow.SetPosition(constants.VIEWPORT_CENTER_X, constants.VIEWPORT_CENTER_Y)

        self.subtitle.SetText(self.instruction_msg)
        self.subtitle_shadow.SetText(self.instruction_msg)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if not self.loading \
                    and  pygame.key.get_pressed()[pygame.K_w] \
                    and pygame.key.get_pressed()[pygame.K_i]:
                self.loading = True

                # show the "loading facts" message
                self.subtitle.SetText(self.loading_msg)
                self.subtitle_shadow.SetText(self.loading_msg)

    def Update(self, dt):
        SceneBase.Update(self, dt)

        self.countdown -= int(1000 * dt) if self.loading else 0
        if self.countdown < 0:
            self.SwitchToScene("Begin")

    def Render(self, screen):
        screen.fill(constants.PALLETE_BACKGROUND_BLUE)

        self.subtitle_shadow.render_multiline(screen)
        self.subtitle.render_multiline(screen)

        graphics.render()