#!/usr/bin/env python

import pygame

from scenes.BaseScene import SceneBase
from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
import mimo, random

class VerificationScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        mimo.reset()

        self.logo = utils.Sprite('assets/sprites/logo_MCorp.png', 1280/2, 720/2)
        self.logo.opacity = 0

        self.sfx_mimo_logo = utils.get_sound('assets/audio/SFX/MimoLogo.ogg')
        
        self.AddTween("easeInOutSine", 2, self.logo, "opacity", 0, 255, 1)
        self.AddTrigger(1, self.sfx_mimo_logo, 'play')

        # check ring and bulbs leds
        factor = 0.1
        loops = 50
        n_leds = 20
        leds = list(range(8, 28))
        for index in range(0, n_leds*loops):
            led_i = leds[index%n_leds]
            self.AddTrigger((1.5+index)*factor, mimo, 'set_material_leds_color', [led_i, int(random.random()*255), int(random.random()*255), int(random.random()*255)])
            self.AddTrigger((1.5+index+0.9)*factor, mimo, 'set_material_leds_color', [led_i, 0, 0, 0])

        # check buttons and backlight buttons.
        mimo.set_buttons_enable_status(True, True)
        mimo.set_independent_lights(False, False)
        mimo.set_led_brightness(120)
        mimo.set_material_buttons_lock_status([0,0, 1,0, 2,0, 3,0, 4,0, 5,0, 6,0, 7,0])
        mimo.set_material_buttons_mode([0,0, 1,0, 2,0, 3,0, 4,0, 5,0, 6,0, 7,0])
        mimo.set_optimization_buttons_lock_status([0,0, 1,0, 2,0, 3,0, 4,0])
        mimo.set_optimization_buttons_mode([0,0, 1,0, 2,0, 3,0, 4,0])
        
        # activate knobs
        mimo.set_tunners_enable_status(True)
        
        # create matrix sprite
        self.testSprite = AnimatedNeoSprite('assets/palomita.png')

        self.label = TextNeoSprite("people")
        self.label.y = 2

        font = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 36)
        self.title = utils.Text("Hello Machinaria!", font)
        self.title.opacity = 0
        self.title.SetPosition(400, 200)
        self.AddTween("easeInOutSine", 2, self.title, "opacity", 0, 255, 1)

        # check lcd screens
        for index in range(0, 6):
            mimo.lcd_display_at(index, 'id' + str(index) + '- line 1', 1)
            mimo.lcd_display_at(index, 'id' + str(index) + '- line 2', 2)
        
        # check printer
        #mimo.termal_print({})


    def ProcessInput(self, events, pressed_keys):
        # verify button inputs
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
        graphics.render()
        self.title.RenderWithAlpha(screen)
    

