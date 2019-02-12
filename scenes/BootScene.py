#!/usr/bin/env python

import pygame

from .BaseScene import SceneBase
from .TutorialScene import TutorialScene
from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite


class BootScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

        self.logo = utils.Sprite('assets/sprites/logo_MCorp.png', 1280/2, 720/2)
        self.logo.opacity = 0

        self.sfx_mimo_logo = utils.get_sound('assets/audio/SFX/MimoLogo.ogg')
        
        self.AddTween("easeInOutSine", 2, self.logo, "opacity", 0, 255, 1)
        self.AddTrigger(1, self.sfx_mimo_logo, 'play')
        #self.AddTrigger(15.5, self, 'SwitchToScene', TutorialScene)

        self.comm.opt.set_led_brightness(80)
        self.comm.opt.activate_buttons(True)
        self.comm.opt.set_independent_lights(False)
        #self.comm.opt.lock_buttons([3, 4])
        self.comm.opt.clean_matrix()
       
        self.posi = [0, 0]
        self.posf = [7, 7]
        self.lockX = True
        self.hue = 0
        self.cont = 0
        self.frequency = 5
        self.ratio = 3
        self.Line = True

        #self.test = utils.get_image_matrix('assets/test.png')
        self.test = utils.get_image_matrix('assets/machinaria8x8.png')
        self.test0 = utils.get_image_matrix('assets/face.png')
        self.test2 = utils.get_image_matrix('assets/face2.png')
        self.test3 = utils.get_image_matrix('assets/face3.png')
        self.palomita = utils.get_image_matrix('assets/palomita.png')
        self.testSprite = NeoSprite('assets/FUENTE.png')
        
        self.animated = AnimatedNeoSprite('assets/tilesprite.png')
        self.animated.animation = [0,2,4,6,1,3,5,7,2,2]
        self.animated.playing = True
        

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                self.frequency += 1
                self.animated.setFrameRate(self.animated.framerate+1)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                self.Line = not self.Line
            if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                self.animated.setFrameRate(self.animated.framerate-1)
                self.frequency -= 1
                if self.frequency < 1:
                    self.frequency = 1
    

    def Update(self, dt):
        SceneBase.Update(self, dt)
        self.animated.update(dt)

        self.cont += 1
        if self.cont%self.frequency == 0:
            self.cont = 0
            self.testSprite.x -= 1
            if self.testSprite.x <= -self.testSprite.width:
                self.testSprite.x = 8

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
        #self.testSprite.render()
        self.animated.render()
        #graphics.drawImage(self.frames[seglf.frame])
        #graphics.drawImage(self.test0, x=-1,y=self.frame+5)
        #graphics.drawImage(self.test0, x=0,y=self.frame)
        #graphics.drawImage(self.test0, x=1, y=self.frame+3)
        #graphics.drawImage(self.test0, x=4, y=self.frame-3)
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

