#!/usr/bin/env python

import pygame

from scenes.BaseScene import SceneBase
from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
import mimo, random

class DevTestScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        mimo.reset()

        self.logo = utils.Sprite('assets/sprites/logo_MCorp.png', 1280/2, 720/2)
        self.logo.opacity = 0

        self.sfx_mimo_logo = utils.get_sound('assets/audio/SFX/MimoLogo.ogg')
        
        self.AddTween("easeInOutSine", 2, self.logo, "opacity", 0, 255, 1)
        self.AddTrigger(1, self.sfx_mimo_logo, 'play')

        #self.comm.opt.set_led_brightness(50)
        mimo.set_led_brightness(50)
        #self.comm.opt.lock_buttons([3, 0, 4, 0])
        #mimo.set_optimization_leds_color([0, 255, 0, 0])
        #mimo.set_optimization_leds_color([1, 0, 255, 0])
        #mimo.set_optimization_leds_color([2, 0, 0, 255])
        #mimo.set_optimization_leds_color([3, 255, 0, 0])
        #mimo.set_optimization_leds_color([4, 255, 255, 255])
        #mimo.set_independent_lights(False, True)
        mimo.set_independent_lights(True, True)

        #mimo.set_optimization_leds_color([2, 255,0,255])
        #mimo.set_optimization_leds_color([5, 255,0,255])
        #mimo.set_optimization_leds_color([19, 255,0,255])
        #mimo.set_optimization_leds_color([27, 255,0,0])
        #mimo.set_optimization_leds_color([28, 255,255])
        #mimo.set_optimization_leds_color([29, 255,0,255])
        #mimo.set_optimization_leds_color([30, 255,0,255])
        factor = 0.02
        loops = 1
        n_leds = 64+5
        for index in range(0, n_leds*loops):
            self.AddTrigger(4+(1+index)*factor, mimo, 'set_optimization_leds_color', [index%n_leds, int(random.random()*255), int(random.random()*255), int(random.random()*255)])
            self.AddTrigger(4+(1+index+0.9)*factor, mimo, 'set_optimization_leds_color', [index%n_leds, 0, 0, 0])
        #self.comm.opt.activate_buttons(True)
        #mimo.set_buttons_enable_status(False, False)
        #self.comm.opt.activate_tunners(False)
        #mimo.set_tunners_enable_status(False)
        #self.comm.opt.set_independent_lights(False)
        #self.comm.opt.clean_matrix()
        #graphics.clear()
        
        #self.AddTrigger(1, self.comm.mat, 'set_led_light', [0, 125, 125, 0, 1, 255, 255, 0])
        #self.AddTrigger(1, mimo, 'set_material_leds_color', [0, 125, 125, 0, 1, 255, 255, 0])
        #self.AddTrigger(2, self.comm.mat, 'set_led_light', [7, 0, 255, 0])
        #self.AddTrigger(2, mimo, 'set_material_leds_color', [7, 0, 255, 0])
        #self.AddTrigger(3, self.comm.opt, 'set_led_light', [0, 255, 0, 0])
        # debe prender el led del boton de  optimizacion 0
        #self.AddTrigger(3, mimo, 'set_optimization_leds_color', [10, 255, 0, 0])
       
        self.testSprite = AnimatedNeoSprite('assets/tilesprite.png')
        self.testSprite.setFrameRate(8)
        self.testSprite.playing = True
        self.label = TextNeoSprite("people")
#
        self.label.y = 2
#
        font = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 36)
        self.title = utils.Text("Hello Machinaria!", font)
        self.title.opacity = 0
        self.title.SetPosition(400, 200)
        self.AddTween("easeInOutSine", 2, self.title, "opacity", 0, 255, 1)


    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                self.title.SetText("(q) button A pressed")
                pass
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.title.SetText("(a) button B pressed")
                pass
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                self.title.SetText("(z) button C pressed")
                pass
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                self.title.SetText("(w) button NO pressed")
                pass
            if event.type == pygame.KEYDOWN and event.key == pygame.K_o:
                self.title.SetText("(o) button D pressed")
                pass
            if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
                self.title.SetText("(k) button E pressed")
                pass
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                self.title.SetText("(m) button F pressed")
                pass
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                self.title.SetText("(i) button OK pressed")
                pass
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                self.title.SetText("(d) button 0 pressed")
                pass
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                self.title.SetText("(c) button 1 pressed")
                pass
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                self.title.SetText("(f) button 2 pressed")
                pass
            if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
                self.title.SetText("(v) button 3 pressed")
                pass
            if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                self.title.SetText("(g) button 4 pressed")
                pass
    

    def Update(self, dt):
        SceneBase.Update(self, dt)
        self.testSprite.update(dt)
        self.label.x -= 0.1
        if self.label.x < -self.label.width:
            self.label.x = 8

    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
        self.logo.RenderWithAlpha(screen)
        self.testSprite.render()
        #graphics.setColor(0xf0f)
        #self.label.render()
        graphics.render()
        self.title.RenderWithAlpha(screen)
    

