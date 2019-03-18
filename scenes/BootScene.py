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
            'assets/sprites/logo_MCorp.png',
            constants.VIEWPORT_CENTER_X,
            constants.VIEWPORT_CENTER_Y
        )
        self.logo.SetOpacity(0)

        self.sfx_mimo_logo = utils.get_sound('assets/audio/SFX/MimoLogo.ogg')
        
        self.AddTween("easeInOutSine", 1, self.logo, "opacity", 0, 255, 1)
        self.AddTrigger(1, self.sfx_mimo_logo, 'play')
        self.AddTrigger(18, self, 'SwitchToScene', "Intro")

        mimo.set_led_brightness(50)
        mimo.set_optimization_buttons_lock_status([0, 0, 1, 0, 2, 0])

        font = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 18)
        self.title = utils.Text("M-OS STARTING", font)
        self.title.opacity = 0
        self.title.SetColor(constants.PALLETE_DARK_BLUE)
        self.title.SetPosition(constants.VIEWPORT_CENTER_X, 500)
        self.AddTween("easeInOutSine", 1, self.title, "opacity", 0, 255, 1)
        self.text_updater_counter = 0
        self.text_updater_frequency = 0.06
        self.text_updater_values = ['|', '\\', '-', '/']
        self.text_updater_index = 0
        

        self.AddTween("easeInOutSine", 1, self.title, "opacity", 255, 0, 16.5)
        self.AddTween("easeInOutSine", 1, self.logo, "opacity", 255, 0, 16.5)
        
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
        self.AddTween("easeInOutSine", 1, self, "brightness", 1, 50, 0)
        self.AddTween("easeInOutSine", 1, self, "brightness", 50, 1, 1.5)
        self.AddTween("easeInOutSine", 1, self, "brightness", 1, 50, 3)
        self.AddTween("easeInOutSine", 1, self, "brightness", 50, 1, 4.5)
        self.AddTween("easeInOutSine", 1, self, "brightness", 1, 50, 6)
        self.AddTween("easeInOutSine", 1, self, "brightness", 50, 1, 7.5)
        self.AddTween("easeInOutSine", 1, self, "brightness", 1, 50, 9)
        self.AddTween("easeInOutSine", 1, self, "brightness", 50, 1, 10.5)
        self.AddTween("easeInOutSine", 1, self, "brightness", 1, 50, 12)
        self.AddTween("easeInOutSine", 1, self, "brightness", 50, 1, 13.5)
        self.AddTween("easeInOutSine", 1, self, "brightness", 1, 50, 15)
        self.AddTween("easeInOutSine", 1, self, "brightness", 50, 1, 16.5)
        
        self.AddTrigger(17.5, mimo, 'set_material_leds_color', mat_lights_on)
        self.AddTrigger(17.5, mimo, 'set_optimization_leds_color', opt_lights_on)
        self.AddTrigger(17.5, mimo, 'clean_matrix')



    def scheduleTextLoader(self):
        self.AddTrigger(1.9, self.title, 'SetText', '')
        self.AddTrigger(2, self.title, 'SetText', 'LOADING')
        self.AddTrigger(2.1, self.title, 'SetText', 'LOADING EMOSENSE')
        self.AddTrigger(2.2, self.title, 'SetText', 'LOADING EMOSENSE PREDICTOR')
        self.AddTrigger(2.3, self.title, 'SetText', 'LOADING EMOSENSE PREDICTOR.')
        self.AddTrigger(2.4, self.title, 'SetText', 'LOADING EMOSENSE PREDICTOR..')
        self.AddTrigger(2.5, self.title, 'SetText', 'LOADING EMOSENSE PREDICTOR...')
        self.AddTrigger(4.0, self.title, 'SetText', '')
        self.AddTrigger(4.1, self.title, 'SetText', 'STABLISHING')
        self.AddTrigger(4.2, self.title, 'SetText', 'STABLISHING CONNECTION')
        self.AddTrigger(4.3, self.title, 'SetText', 'STABLISHING CONNECTION WITH')
        self.AddTrigger(4.4, self.title, 'SetText', 'STABLISHING CONNECTION WITH PREDICTOR')
        self.AddTrigger(4.5, self.title, 'SetText', 'STABLISHING CONNECTION WITH PREDICTOR MAINFRAME')
        self.AddTrigger(4.6, self.title, 'SetText', 'STABLISHING CONNECTION WITH PREDICTOR MAINFRAME.')
        self.AddTrigger(4.7, self.title, 'SetText', 'STABLISHING CONNECTION WITH PREDICTOR MAINFRAME..')
        self.AddTrigger(4.8, self.title, 'SetText', 'STABLISHING CONNECTION WITH PREDICTOR MAINFRAME...')
        self.AddTrigger(6, self.title, 'SetText', '')
        self.AddTrigger(6.1, self.title, 'SetText', 'ACTIVATING')
        self.AddTrigger(6.2, self.title, 'SetText', 'ACTIVATING MEDIA')
        self.AddTrigger(6.3, self.title, 'SetText', 'ACTIVATING MEDIA EMOTIONAL')
        self.AddTrigger(6.4, self.title, 'SetText', 'ACTIVATING MEDIA EMOTIONAL ANALYZER')
        self.AddTrigger(6.5, self.title, 'SetText', 'ACTIVATING MEDIA EMOTIONAL ANALYZER.')
        self.AddTrigger(6.6, self.title, 'SetText', 'ACTIVATING MEDIA EMOTIONAL ANALYZER..')
        self.AddTrigger(6.7, self.title, 'SetText', 'ACTIVATING MEDIA EMOTIONAL ANALYZER...')
        self.AddTrigger(8.0, self.title, 'SetText', '')
        self.AddTrigger(8.1, self.title, 'SetText', 'PROCESSING')
        self.AddTrigger(8.2, self.title, 'SetText', 'PROCESSING EMOTIONAL')
        self.AddTrigger(8.3, self.title, 'SetText', 'PROCESSING EMOTIONAL OPTIMIZATION')
        self.AddTrigger(8.4, self.title, 'SetText', 'PROCESSING EMOTIONAL OPTIMIZATION MODULES')
        self.AddTrigger(8.5, self.title, 'SetText', 'PROCESSING EMOTIONAL OPTIMIZATION MODULES.')
        self.AddTrigger(8.6, self.title, 'SetText', 'PROCESSING EMOTIONAL OPTIMIZATION MODULES..')
        self.AddTrigger(8.7, self.title, 'SetText', 'PROCESSING EMOTIONAL OPTIMIZATION MODULES...')
        self.AddTrigger(10, self.title, 'SetText', '')
        self.AddTrigger(10.1, self.title, 'SetText', 'ACCESSING')
        self.AddTrigger(10.2, self.title, 'SetText', 'ACCESSING OPINION')
        self.AddTrigger(10.3, self.title, 'SetText', 'ACCESSING OPINION CENTRAL')
        self.AddTrigger(10.4, self.title, 'SetText', 'ACCESSING OPINION CENTRAL DATAMATRIX')
        self.AddTrigger(10.5, self.title, 'SetText', 'ACCESSING OPINION CENTRAL DATAMATRIX.')
        self.AddTrigger(10.6, self.title, 'SetText', 'ACCESSING OPINION CENTRAL DATAMATRIX..')
        self.AddTrigger(10.7, self.title, 'SetText', 'ACCESSING OPINION CENTRAL DATAMATRIX...')
        self.AddTrigger(12.0, self.title, 'SetText', '')
        self.AddTrigger(12.1, self.title, 'SetText', 'INITIALIZING')
        self.AddTrigger(12.2, self.title, 'SetText', 'INITIALIZING PUCHINTZKY')
        self.AddTrigger(12.3, self.title, 'SetText', 'INITIALIZING PUCHINTZKY ALGORITHM')
        self.AddTrigger(12.4, self.title, 'SetText', 'INITIALIZING PUCHINTZKY ALGORITHM ENGINE')
        self.AddTrigger(12.5, self.title, 'SetText', 'INITIALIZING PUCHINTZKY ALGORITHM ENGINE.')
        self.AddTrigger(12.6, self.title, 'SetText', 'INITIALIZING PUCHINTZKY ALGORITHM ENGINE..')
        self.AddTrigger(12.7, self.title, 'SetText', 'INITIALIZING PUCHINTZKY ALGORITHM ENGINE...')
        self.AddTrigger(14.0, self.title, 'SetText', 'M')
        self.AddTrigger(14.1, self.title, 'SetText', 'M-')
        self.AddTrigger(14.2, self.title, 'SetText', 'M-O')
        self.AddTrigger(14.3, self.title, 'SetText', 'M-OS')
        self.AddTrigger(14.4, self.title, 'SetText', 'M-OS ')
        self.AddTrigger(14.5, self.title, 'SetText', 'M-OS I')
        self.AddTrigger(14.6, self.title, 'SetText', 'M-OS IS')
        self.AddTrigger(14.7, self.title, 'SetText', 'M-OS IS ')
        self.AddTrigger(14.8, self.title, 'SetText', 'M-OS IS R')
        self.AddTrigger(14.9, self.title, 'SetText', 'M-OS IS RE')
        self.AddTrigger(15.0, self.title, 'SetText', 'M-OS IS REA')
        self.AddTrigger(15.1, self.title, 'SetText', 'M-OS IS READ')
        self.AddTrigger(15.2, self.title, 'SetText', 'M-OS IS READY')

