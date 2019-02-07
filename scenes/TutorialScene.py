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

        self.materialL1 = utils.Sprite('assets/sprites/mtlL1.png', 301, 292)
        self.materialL2 = utils.Sprite('assets/sprites/mtlL2.png', 301, 365)
        self.materialL3 = utils.Sprite('assets/sprites/mtlL3.png', 301, 443)
        self.materialR1 = utils.Sprite('assets/sprites/mtlR1.png', 979, 292)
        self.materialR2 = utils.Sprite('assets/sprites/mtlR2.png', 979, 365)
        self.materialR3 = utils.Sprite('assets/sprites/mtlR3.png', 979, 443)
        self.materialL1.opacity = 0
        self.materialL2.opacity = 0
        self.materialL3.opacity = 0
        self.materialR1.opacity = 0
        self.materialR2.opacity = 0
        self.materialR3.opacity = 0

        self.opt_knobs = utils.Sprite('assets/sprites/opt_knobs.png', 640, 325)
        self.opt_buttons = utils.Sprite('assets/sprites/opt_buttons.png', 640, 447)
        self.opt_knobs.opacity = 0
        self.opt_buttons.opacity = 0


        self.sfx_tut_st = utils.get_sound('assets/audio/SFX/SFX_Tut_St.ogg')
        self.sfx_tut_print = utils.get_sound('assets/audio/SFX/SFX_Tut_Print.ogg')
        self.sfx_tut_mat = utils.get_sound('assets/audio/SFX/SFX_Tut_Mat.ogg')
        self.sfx_tut_opt = utils.get_sound('assets/audio/SFX/SFX_Tut_Opt.ogg')
        self.sfx_tut_end = utils.get_sound('assets/audio/SFX/SFX_Tut_End.ogg')


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
        self.AddTrigger(second, self.printer03, 'SetOpacity', 0)
        self.AddTrigger(second, self.sfx_tut_mat, 'play')

        self.AddTween('easeOutCubic', 0.5, self.materialL1, "opacity", 0, 255, second)
        second = 11.5
        self.AddTween('easeOutCubic', 0.5, self.materialL2, "opacity", 0, 255, second)
        second = 12.5
        self.AddTween('easeOutCubic', 0.5, self.materialL3, "opacity", 0, 255, second)
        second = 13.5
        self.AddTween('easeOutCubic', 0.5, self.materialR1, "opacity", 0, 255, second)
        second = 14.5
        self.AddTween('easeOutCubic', 0.5, self.materialR2, "opacity", 0, 255, second)
        second = 15.5
        self.AddTween('easeOutCubic', 0.5, self.materialR3, "opacity", 0, 255, second)

        second = 16.5
        self.AddTween('easeOutCubic', 0.5, self.materialL1, "opacity", 255, 0, second)
        self.AddTween('easeOutCubic', 0.5, self.materialL2, "opacity", 255, 0, second)
        self.AddTween('easeOutCubic', 0.5, self.materialL3, "opacity", 255, 0, second)
        self.AddTween('easeOutCubic', 0.5, self.materialR1, "opacity", 255, 0, second)
        self.AddTween('easeOutCubic', 0.5, self.materialR2, "opacity", 255, 0, second)
        self.AddTween('easeOutCubic', 0.5, self.materialR3, "opacity", 255, 0, second)
        
        second = 18
        self.AddTrigger(second, self.sfx_tut_opt, 'play')
        self.AddTween('easeOutCubic', 4, self.opt_knobs, "opacity", 0, 255, second)
        self.AddTween('easeOutCubic', 5, self.opt_buttons, "opacity", 0, 255, second)

        second = 24
        self.AddTrigger(second, self.sfx_tut_end, 'play')

        



    
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

        self.materialL1.RenderWithAlpha(screen)
        self.materialL2.RenderWithAlpha(screen)
        self.materialL3.RenderWithAlpha(screen)
        self.materialR1.RenderWithAlpha(screen)
        self.materialR2.RenderWithAlpha(screen)
        self.materialR3.RenderWithAlpha(screen)
        
        self.opt_knobs.RenderWithAlpha(screen)
        self.opt_buttons.RenderWithAlpha(screen)

