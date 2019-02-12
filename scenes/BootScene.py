#!/usr/bin/env python

import pygame

from .BaseScene import SceneBase
from .TutorialScene import TutorialScene
from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames

class BootScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

        self.logo = utils.Sprite('assets/sprites/logo_MCorp.png', 1280/2, 720/2)
        self.logo.opacity = 0

        self.sfx_mimo_logo = utils.get_sound('assets/audio/SFX/MimoLogo.ogg')
        
        self.AddTween("easeInOutSine", 2, self.logo, "opacity", 0, 255, 1)
        self.AddTrigger(1, self.sfx_mimo_logo, 'play')
        self.AddTrigger(15.5, self, 'SwitchToScene', TutorialScene)

        self.comm.opt.set_led_brightness(50)
        self.comm.opt.activate_buttons(True)
        self.comm.opt.activate_tunners(False)
        self.comm.opt.set_independent_lights(False)
        self.comm.opt.lock_buttons([3, 4])
        self.comm.opt.clean_matrix()
       
        self.testSprite = NeoSprite('assets/FUENTE.png')
        self.label = TextNeoSprite("the kambucha mushroom people")

        self.label.y = 2

        font = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 36)
        self.title = utils.Text("Hello Machinaria!", font)
        self.title.opacity = 0
        self.title.SetPosition(400, 200)
        self.AddTween("easeInOutSine", 2, self.title, "opacity", 0, 255, 1)


    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                pass
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                pass
            if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                pass
    

    def Update(self, dt):
        SceneBase.Update(self, dt)

    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
        self.logo.RenderWithAlpha(screen)
        #self.testSprite.render()
        graphics.setColor(0xfff)
        self.label.render()
        graphics.render()
        self.title.RenderWithAlpha(screen)
    

