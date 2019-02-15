#!/usr/bin/env python

import pygame

from .BaseScene import SceneBase
from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
import mimo

class DevTestScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

        self.logo = utils.Sprite('assets/sprites/logo_MCorp.png', 1280/2, 720/2)
        self.logo.opacity = 0

        self.sfx_mimo_logo = utils.get_sound('assets/audio/SFX/MimoLogo.ogg')
        
        self.AddTween("easeInOutSine", 2, self.logo, "opacity", 0, 255, 1)
        self.AddTrigger(1, self.sfx_mimo_logo, 'play')

        #self.comm.opt.set_led_brightness(50)
        mimo.set_led_brightness(50)
        #self.comm.opt.lock_buttons([3, 0, 4, 0])
        mimo.set_optimization_buttons_lock_status([3, 1, 0, 0, 4, 1])
        mimo.set_optimization_buttons_lock_status([3, 1, 0, 1, 2, 0])
        mimo.set_optimization_buttons_lock_status([3, 1, 0, 0, 4, 1])
        mimo.set_optimization_buttons_light([0, 255, 255, 0])
        self.AddTrigger(8, mimo, 'set_optimization_buttons_lock_status', [0, 1])
        self.AddTrigger(10, mimo, 'set_optimization_buttons_mode', [0, 1])
        self.AddTrigger(12, mimo, 'set_optimization_buttons_lock_status', [0, 0])
        #self.comm.opt.activate_buttons(True)
        mimo.set_buttons_enable_status(True, True)
        #self.comm.opt.activate_tunners(False)
        #mimo.set_tunners_enable_status(False)
        #self.comm.opt.set_independent_lights(False)
        mimo.set_independent_lights(False, False)
        #self.comm.opt.clean_matrix()
        #graphics.clear()
        
        #self.AddTrigger(1, self.comm.mat, 'set_led_light', [0, 125, 125, 0, 1, 255, 255, 0])
        self.AddTrigger(1, mimo, 'set_material_leds_color', [0, 125, 125, 0, 1, 255, 255, 0])
        #self.AddTrigger(2, self.comm.mat, 'set_led_light', [7, 0, 255, 0])
        self.AddTrigger(2, mimo, 'set_material_leds_color', [7, 0, 255, 0])
        #self.AddTrigger(3, self.comm.opt, 'set_led_light', [0, 255, 0, 0])
        # debe prender el led del boton de  optimizacion 0
        self.AddTrigger(3, mimo, 'set_optimization_leds_color', [10, 255, 0, 0])
       
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
        self.label.x -= 0.1
        if self.label.x < -self.label.width:
            self.label.x = 8

    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
        self.logo.RenderWithAlpha(screen)
        #self.testSprite.render()
        graphics.setColor(0xfff)
        self.label.render()
        graphics.render()
        self.title.RenderWithAlpha(screen)
    

