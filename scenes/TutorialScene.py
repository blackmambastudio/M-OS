#!/usr/bin/env python

import pygame

from .BaseScene import SceneBase
from .GameScene import GameScene
from utils import utils

class TutorialScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

        self.mimo_blueprint = utils.Sprite('assets/sprites/mimo_blueprint.png', 640, 265)
        self.mimo_blueprint.opacity = 0

        self.printer01 = utils.Sprite('assets/sprites/printer-01.png', 380, 181)
        self.printer02 = utils.Sprite('assets/sprites/printer-02.png', 380, 181)
        self.printer03 = utils.Sprite('assets/sprites/printer-03.png', 380, 181)
        self.printer01.opacity = 0
        self.printer02.opacity = 0
        self.printer03.opacity = 0
        self.printer01.setAnchor(0.5, 1)
        self.printer02.setAnchor(0.5, 1)
        self.printer03.setAnchor(0.5, 1)

        self.sfx_tut_st = utils.get_sound('assets/audio/SFX/SFX_Tut_St.ogg')
        self.sfx_tut_print = utils.get_sound('assets/audio/SFX/SFX_Tut_Print.ogg')


        # second 0
        second = 0
        self.AddTween("easeOutCubic", 2, self.mimo_blueprint, "opacity", 0, 255, second)
        # second 2
        second = 2
        self.AddTrigger(second, self.sfx_tut_st, 'play')

        # second 4
        second = 4
        self.AddTween("easeOutCubic", 0.5, self.mimo_blueprint, "opacity", 255, 64, second)
        self.AddTween("easeOutCubic", 1, self.printer01, "opacity", 0, 255, second)

        # second 5
        second = 5.5
        self.AddTrigger(second, self.sfx_tut_print, 'play')
        self.AddTrigger(second, self.printer01, 'SetOpacity', 0)
        self.AddTrigger(second, self.printer02, 'SetOpacity', 255)
        second = 6
        self.AddTrigger(second, self.printer02, 'SetOpacity', 0)
        self.AddTrigger(second, self.printer03, 'SetOpacity', 255)
        second = 6.5
        self.AddTrigger(second, self.printer03, 'SetOpacity', 0)
        self.AddTrigger(second, self.printer01, 'SetOpacity', 255)
        second = 7
        self.AddTrigger(second, self.printer01, 'SetOpacity', 0)
        self.AddTrigger(second, self.printer02, 'SetOpacity', 255)
        second = 7.5
        self.AddTrigger(second, self.printer02, 'SetOpacity', 0)
        self.AddTrigger(second, self.printer03, 'SetOpacity', 255)
        second = 8
        self.AddTrigger(second, self.printer03, 'SetOpacity', 0)
        self.AddTrigger(second, self.printer01, 'SetOpacity', 255)
        second = 8.5
        self.AddTrigger(second, self.printer01, 'SetOpacity', 0)
        self.AddTrigger(second, self.printer02, 'SetOpacity', 255)
        second = 9
        self.AddTrigger(second, self.printer02, 'SetOpacity', 0)
        self.AddTrigger(second, self.printer03, 'SetOpacity', 255)

        second = 10.5


    
    def ProcessInput(self, events, pressed_keys):
        pass
    
    def Update(self, dt):
        SceneBase.Update(self, dt)
    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
        self.mimo_blueprint.RenderWithAlpha(screen)
        self.printer01.RenderWithAlpha(screen)
        self.printer02.RenderWithAlpha(screen)
        self.printer03.RenderWithAlpha(screen)
