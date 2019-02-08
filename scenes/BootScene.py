#!/usr/bin/env python

import pygame

from .BaseScene import SceneBase
from .TutorialScene import TutorialScene
from utils import utils
from utils import neopixelmatrix as graphics


class BootScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

        self.logo = utils.Sprite('assets/sprites/logo_MCorp.png', 1280/2, 720/2)
        self.logo.opacity = 0

        self.sfx_mimo_logo = utils.get_sound('assets/audio/SFX/MimoLogo.ogg')
        
        self.AddTween("easeInOutSine", 2, self.logo, "opacity", 0, 255, 1)
        self.AddTrigger(1, self.sfx_mimo_logo, 'play')
        #self.AddTrigger(15.5, self, 'SwitchToScene', TutorialScene)

        self.comm.opt.set_led_brightness(20)
        self.comm.opt.activate_buttons(True)
        self.comm.opt.set_independent_lights(False)
        #self.comm.opt.lock_buttons([3, 4])
        self.comm.opt.clean_matrix()
       
        self.posi = [0, 0]
        self.posf = [7, 7]
        self.lockX = True
        self.hue = 0
        self.cont = 0
        self.frequency = 3
        self.ratio = 3
        self.Line = True

        #self.test = utils.get_image_matrix('assets/test.png')
        self.test = utils.get_image_matrix('assets/test.png')
        self.test2 = utils.get_image_matrix('assets/face2.png')
        self.test3 = utils.get_image_matrix('assets/face3.png')
        self.palomita = utils.get_image_matrix('assets/palomita.png')
        self.frame = 0
        self.frames = [self.palomita]


    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                self.frequency += 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                self.Line = not self.Line
            if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                self.frequency -= 1
                if self.frequency < 1:
                    self.frequency = 1
    
    def Update(self, dt):
        SceneBase.Update(self, dt)

        self.cont += 1
        if self.cont%self.frequency == 0:
            self.frame += 1
            if self.frame >= len(self.frames):
                self.frame = 0
        #     self.cont = 0

        #     self.hue += dt*255
        #     if self.hue > 255:
        #         self.hue = 0
        #     color = graphics.wheel(int(self.hue))
        #     graphics.setColorRGB(color)
        #     self.SpinLine()

        #     self.DrawRect()

    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
        self.logo.RenderWithAlpha(screen)


        # if self.Line:
        #     graphics.plotLine(self.posi[0],self.posi[1],self.posf[0],self.posf[1])
        # else:
        #     graphics.drawRect(self.ratio, self.ratio, 8-self.ratio*2, 8-self.ratio*2)
        graphics.drawImage(self.frames[self.frame])
        graphics.render()


    def SpinLine(self):

        if self.lockX:
            self.posi[0] += 1
            self.posf[0] -= 1
            if self.posi[0] == 7:
                self.posi = [0, 7]
                self.posf = [7, 0]
                self.lockX = False
        else:
            self.posi[1] -= 1
            self.posf[1] += 1
            if self.posf[1] == 7:
                self.posi = [0, 0]
                self.posf = [7, 7]
                self.lockX = True
    

    def DrawRect(self):
        self.ratio -= 1
        if self.ratio < 0:
            self.ratio = 3

