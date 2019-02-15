#!/usr/bin/env python

import pygame

from .BaseScene import SceneBase
from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
import mimo

# Tutorial Scene
# should explain the player how to use the machine
# follow the previous version, display the modules
# but also should display info to the player to calibrate
# the different inputs

# should expose a module and ask the user to do a specific action
# to continue to the next section
# next section is lobby scene // idle 

class TutorialScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

        mimo.set_led_brightness(50)

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

        titlefont = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 44)
        self.title = utils.Text("", titlefont)
        self.title.SetPosition(1280/2, 546)

        subtitlefont = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 32)
        self.subtitle = utils.Text("", subtitlefont)
        self.subtitle.SetPosition(1280/2, 610)

        # second 0
        second = 0
        self.AddTween("easeOutCubic", 2, self.mimo_blueprint, "opacity", 0, 255, second)
        # second 2
        second = 2
        self.AddTrigger(second, self.sfx_tut_st, 'play')
        self.AddTrigger(second, self.title, 'SetText', '-- M.I.M.O. VERIFICATION PROCESS --')

        # second 4
        second = 4
        self.AddTween("easeOutCubic", 0.5, self.mimo_blueprint, "opacity", 255, 64, second)
        self.AddTween("easeOutCubic", 1, self.printer01, "opacity", 0, 255, second)

        # second 5
        second = 5.5
        self.AddTrigger(second, self.sfx_tut_print, 'play')
        self.AddTrigger(second, self.printer01, 'SetOpacity', 0)
        self.AddTrigger(second, self.printer02, 'SetOpacity', 255)
        self.AddTrigger(second, self.title, 'SetText', 'VERIFYING PRINTER')
        self.AddTrigger(second, self.subtitle, 'SetText', 'READ EACH INCOMING EVENT AND USE THE MATERIAL\nATTACHED TO IT TO TRANSFORM IT INTO THE NEWS')
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
        self.AddTrigger(second, self.title, 'SetText', 'VERIFYING MATERIAL PANEL')
        self.AddTrigger(second, self.subtitle, 'SetText', 'PRESS EACH BUTTON TO SELECT THE MATERIAL\nYOU WANT TO USE TO EVOKE AN EMOTION IN THE CURRENT NEWS')

        self.AddTween('easeOutCubic', 0.5, self.materialL1, "opacity", 0, 255, second)
        self.AddTrigger(10.7, mimo, 'set_material_leds_color', [0, 255, 0, 0])
        second = 11.5
        self.AddTween('easeOutCubic', 0.5, self.materialL2, "opacity", 0, 255, second)
        self.AddTrigger(11.7, mimo, 'set_material_leds_color', [1, 255, 255, 255])
        second = 12.5
        self.AddTween('easeOutCubic', 0.5, self.materialL3, "opacity", 0, 255, second)
        self.AddTrigger(12.7, mimo, 'set_material_leds_color', [2, 0, 255, 0])
        second = 13.5
        self.AddTween('easeOutCubic', 0.5, self.materialR1, "opacity", 0, 255, second)
        self.AddTrigger(13.7, mimo, 'set_material_leds_color', [7, 255, 255, 0])
        second = 14.5
        self.AddTween('easeOutCubic', 0.5, self.materialR2, "opacity", 0, 255, second)
        self.AddTrigger(14.7, mimo, 'set_material_leds_color', [6, 0, 255, 255])
        second = 15.5
        self.AddTween('easeOutCubic', 0.5, self.materialR3, "opacity", 0, 255, second)
        self.AddTrigger(15.7, mimo, 'set_material_leds_color', [5, 255, 0, 255])

        second = 16.5
        self.AddTween('easeOutCubic', 0.5, self.materialL1, "opacity", 255, 0, second)
        self.AddTween('easeOutCubic', 0.5, self.materialL2, "opacity", 255, 0, second)
        self.AddTween('easeOutCubic', 0.5, self.materialL3, "opacity", 255, 0, second)
        self.AddTween('easeOutCubic', 0.5, self.materialR1, "opacity", 255, 0, second)
        self.AddTween('easeOutCubic', 0.5, self.materialR2, "opacity", 255, 0, second)
        self.AddTween('easeOutCubic', 0.5, self.materialR3, "opacity", 255, 0, second)
        self.AddTrigger(17, mimo, 'set_material_leds_color', [0,0,0,0, 1,0,0,0, 2,0,0,0, 7,0,0,0, 6,0,0,0, 5,0,0,0])
        
        second = 18
        self.AddTrigger(second, self.sfx_tut_opt, 'play')
        self.AddTrigger(second, self.title, 'SetText', 'VERIFYING OPTIMIZATION PANEL')
        self.AddTrigger(second, self.subtitle, 'SetText', 'USE THE KNOBS AND BUTTONS TO IMPROVE THE IMPACT\nOF THE EVOKED EMOTION')
        self.AddTween('easeOutCubic', 4, self.opt_knobs, "opacity", 0, 255, second)
        self.AddTween('easeOutCubic', 5, self.opt_buttons, "opacity", 0, 255, second)

        second = 24
        self.AddTrigger(second, self.sfx_tut_end, 'play')
        self.AddTrigger(second, self.title, 'SetText', '-- M.I.M.O. VERIFICATION COMPLETE --')
        self.AddTrigger(second, self.subtitle, 'SetText', 'ALL SYSTEMS WORKING.\nWELCOME!\nYOU CAN START MANUFACTURING THE NEWS.')

        
        #self.torca = AnimatedNeoSprite('assets/Torca_Walk.png', 7, 7)
        #self.torca.playing = True
        #self.torca.setFrameRate(5)


    
    def ProcessInput(self, events, pressed_keys):
        pass
    
    def Update(self, dt):
        SceneBase.Update(self, dt)
        #self.torca.update(dt)
    
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

        self.title.RenderWithAlpha(screen)
        self.subtitle.render_multiline(screen)

        #self.torca.render()
        graphics.render()

