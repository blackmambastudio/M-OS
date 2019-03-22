#!/usr/bin/env python

import pygame
import mimo

from .BaseScene import SceneBase

from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
from utils import constants

# Boot Scene
# should reset all button and light states,
# clear the led matrix and led ring
# all inputs are locked
# set colors for all leds, turn all leds and increase the brightness
# this boot scene should take some seconds, max 10? 8-6?
# some aditional test display that specific modules are loading.
# after that change to the next scene - tutorial

class BootScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

        self.logo = utils.Sprite(
            constants.SPRITES_INTRO + 'logo_MCorp.png',
            constants.VIEWPORT_CENTER_X,
            constants.VIEWPORT_CENTER_Y
        )
        self.logo.SetOpacity(0)

        self.sfx_mimo_logo = utils.get_sound('assets/audio/SFX/M_OS/UI_Booth.ogg')

        self.AddTrigger(0.1, self.sfx_mimo_logo, 'play')
        self.AddTrigger(9.2, self, 'SwitchToScene', "Begin")

        mimo.set_led_brightness(150)

        font = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 24)
        self.title = utils.Text("M-OS STARTING", font)
        self.title.SetOpacity(0)
        self.title.SetColor(constants.PALLETE_DARK_BLUE)
        self.title.SetPosition(constants.VIEWPORT_CENTER_X, 500)
        self.text_updater_counter = 0
        self.text_updater_frequency = 0.06
        self.text_updater_values = ['|', '\\', '-', '/']
        self.text_updater_index = 0

        resolution = 6
        self.AddTween("easeInOutSine", 1.5, self.title, "opacity", 0, 255, 0)
        self.AddTween("easeInOutSine", 1.5, self.logo, "opacity", 0, 255, 0, resolution)
        self.AddTween("easeInOutSine", 1.5, self.logo, "opacity", 255, 0, 1.5, resolution)
        self.AddTween("easeInOutSine", 1.5, self.logo, "opacity", 0, 255, 3, resolution)
        self.AddTween("easeInOutSine", 1.5, self.logo, "opacity", 255, 0, 4.5, resolution)
        self.AddTween("easeInOutSine", 1.5, self.logo, "opacity", 0, 255, 6, resolution)
        self.AddTween("easeInOutSine", 1.5, self.logo, "opacity", 255, 0, 7.5, resolution)
        self.AddTween("easeInOutSine", 1.5, self.title, "opacity", 255, 0, 7.5, resolution)
        
        self.brightness = 1
        self.cache_brightness = 1
        self.scheduleTextLoader()
        self.whiteSprite = NeoSprite('assets/white.png')
        self.reset_mimo()

    def ProcessInput(self, events, pressed_keys):
        pass
    

    def Update(self, dt):
        SceneBase.Update(self, dt)
        self.text_updater_counter += dt
        if self.text_updater_counter > self.text_updater_frequency:
            if self.cache_brightness != int(self.brightness):
                mimo.set_led_brightness(int(self.brightness))
                self.cache_brightness = self.brightness

            self.text_updater_index += 1
            self.text_updater_counter = 0
            if self.text_updater_index >= len(self.text_updater_values):
                self.text_updater_index = 0
            self.title.DecorateText(self.text_updater_values[self.text_updater_index] + ' ', ' '+self.text_updater_values[-self.text_updater_index])
    
    def Render(self, screen):
        screen.fill(constants.PALLETE_BACKGROUND_BLUE)
        self.logo.RenderWithAlpha(screen)
        self.title.RenderWithAlpha(screen)
        graphics.setColor(0xfff)
        self.whiteSprite.render()
        graphics.render()

    def reset_mimo(self):
        mimo.set_led_brightness(1)
        max_brightness = 150

        mat_all_lights = []
        for index in range(0, 28):
            mat_all_lights += [index, 255, 255, 255]
        mimo.set_material_leds_color(mat_all_lights)
        
        opt_all_lights = []
        for index in range(0, 5):
            opt_all_lights += [index, 255, 255, 255]
        mimo.set_optimization_leds_color(opt_all_lights)
        
        mat_lights_on = []
        for index in range(0, 28):
            mat_lights_on += [index, 0, 0, 0]
        opt_lights_on = []
        for index in range(0, 5):
            opt_lights_on += [index, 0, 0, 0]

        self.brightness = 1
        self.AddTween("easeInOutSine", 1, self, "brightness", 1, max_brightness, 0)
        self.AddTween("easeInOutSine", 1, self, "brightness", max_brightness, 1, 1.5)
        self.AddTween("easeInOutSine", 1, self, "brightness", 1, max_brightness, 3)
        self.AddTween("easeInOutSine", 1, self, "brightness", max_brightness, 1, 4.5)
        self.AddTween("easeInOutSine", 1, self, "brightness", 1, max_brightness, 6)
        self.AddTween("easeInOutSine", 1, self, "brightness", max_brightness, 1, 7.5)
        
        self.AddTrigger(9.1, mimo, 'set_material_leds_color', mat_lights_on)
        self.AddTrigger(9.1, mimo, 'set_optimization_leds_color', opt_lights_on)
        self.AddTrigger(9.1, mimo, 'clean_matrix')


    def scheduleTextLoader(self):
        self.AddTrigger(1.9, self.title, 'SetText', '')
        self.AddTrigger(2, self.title, 'SetText', 'LOADING')
        self.AddTrigger(2.1, self.title, 'SetText', 'LOADING EMOSENSE')
        self.AddTrigger(2.2, self.title, 'SetText', 'LOADING EMOSENSE PREDICTOR')
        self.AddTrigger(2.3, self.title, 'SetText', 'LOADING EMOSENSE PREDICTOR.')
        self.AddTrigger(2.4, self.title, 'SetText', 'LOADING EMOSENSE PREDICTOR..')
        self.AddTrigger(2.5, self.title, 'SetText', 'LOADING EMOSENSE PREDICTOR...')
        self.AddTrigger(3.5, self.title, 'SetText', '')
        self.AddTrigger(3.6, self.title, 'SetText', 'PROCESSING')
        self.AddTrigger(3.7, self.title, 'SetText', 'PROCESSING EMOTIONAL')
        self.AddTrigger(3.8, self.title, 'SetText', 'PROCESSING EMOTIONAL OPTIMIZATION')
        self.AddTrigger(3.9, self.title, 'SetText', 'PROCESSING EMOTIONAL OPTIMIZATION MODULES')
        self.AddTrigger(4.0, self.title, 'SetText', 'PROCESSING EMOTIONAL OPTIMIZATION MODULES.')
        self.AddTrigger(4.1, self.title, 'SetText', 'PROCESSING EMOTIONAL OPTIMIZATION MODULES..')
        self.AddTrigger(4.2, self.title, 'SetText', 'PROCESSING EMOTIONAL OPTIMIZATION MODULES...')
        self.AddTrigger(5.0, self.title, 'SetText', '')
        self.AddTrigger(5.1, self.title, 'SetText', 'INITIALIZING')
        self.AddTrigger(5.2, self.title, 'SetText', 'INITIALIZING PUCHINTZKY')
        self.AddTrigger(5.3, self.title, 'SetText', 'INITIALIZING PUCHINTZKY ALGORITHM')
        self.AddTrigger(5.4, self.title, 'SetText', 'INITIALIZING PUCHINTZKY ALGORITHM ENGINE')
        self.AddTrigger(5.5, self.title, 'SetText', 'INITIALIZING PUCHINTZKY ALGORITHM ENGINE.')
        self.AddTrigger(5.6, self.title, 'SetText', 'INITIALIZING PUCHINTZKY ALGORITHM ENGINE..')
        self.AddTrigger(5.7, self.title, 'SetText', 'INITIALIZING PUCHINTZKY ALGORITHM ENGINE...')
        self.AddTrigger(6.0, self.title, 'SetText', 'M')
        self.AddTrigger(6.1, self.title, 'SetText', 'M-')
        self.AddTrigger(6.2, self.title, 'SetText', 'M-O')
        self.AddTrigger(6.3, self.title, 'SetText', 'M-OS')
        self.AddTrigger(6.4, self.title, 'SetText', 'M-OS ')
        self.AddTrigger(6.5, self.title, 'SetText', 'M-OS I')
        self.AddTrigger(6.6, self.title, 'SetText', 'M-OS IS')
        self.AddTrigger(6.7, self.title, 'SetText', 'M-OS IS ')
        self.AddTrigger(6.8, self.title, 'SetText', 'M-OS IS R')
        self.AddTrigger(6.9, self.title, 'SetText', 'M-OS IS RE')
        self.AddTrigger(7.0, self.title, 'SetText', 'M-OS IS REA')
        self.AddTrigger(7.1, self.title, 'SetText', 'M-OS IS READ')
        self.AddTrigger(7.2, self.title, 'SetText', 'M-OS IS READY')

