#!/usr/bin/env python

import pygame

from .BaseScene import SceneBase
from .TitleScene import TitleScene
from utils import utils


class BootScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

        self.logo = utils.Sprite('assets/sprites/logo_MCorp.png')
        self.logo.SetPosition(1280/2, 720/2)
        self.logo.opacity = 0

        self.sfx_mimo_logo = utils.get_sound('assets/audio/SFX/MimoLogo.ogg')
        
        self.AddTween("easeInOutSine", 2, self.logo, "opacity", 0, 255, 1)
        self.AddTrigger(1, self.sfx_mimo_logo, 'play')
        self.AddTrigger(5.5, self, 'SwitchToScene', TitleScene)
        
    
    def ProcessInput(self, events, pressed_keys):
        pass
    
    def Update(self, dt):
        SceneBase.Update(self, dt)

    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
        self.logo.RenderWithAlpha(screen)
        


