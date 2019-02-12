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
        self.frequency = 5
        self.ratio = 3
        self.Line = True

        self.testSprite = NeoSprite('assets/FUENTE.png')
        self.label = TextNeoSprite("to be, or not to be, that is the question: whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune, or to take arms against a sea of troubles and by opposing end them. to die—to sleep, no more; and by a sleep to say we end the heart-ache and the thousand natural shocks that flesh is heir to: 'tis a consummation devoutly to be wish'd. to die, to sleep; to sleep, perchance to dream—ay, there's the rub: for in that sleep of death what dreams may come, when we have shuffled off this mortal coil, must give us pause—there's the respect that makes calamity of so long life. for who would bear the whips and scorns of time, th'oppressor's wrong, the proud man's contumely, the pangs of dispriz'd love, the law's delay, the insolence of office, and the spurns that patient merit of th'unworthy takes, when he himself might his quietus make with a bare bodkin? who would fardels bear, to grunt and sweat under a weary life, but that the dread of something after death, the undiscovere'd country, from whose bourn no traveller returns, puzzles the will, and makes us rather bear those ills we have than fly to others that we know not of? thus conscience does make cowards of us all, and thus the native hue of resolution is sicklied o'er with the pale cast of thought, and enterprises of great pitch and moment with this regard their currents turn awry and lose the name of action.")

        self.label.y = 2
        self.color = [0,0,0]

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                self.frequency += 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                pass
            if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                self.frequency -= 1
                if self.frequency < 1:
                    self.frequency = 1
    

    def Update(self, dt):
        SceneBase.Update(self, dt)

        self.cont += 1
        if self.cont%self.frequency == 0:
            self.cont = 0

            self.label.x -= 1
            if self.label.x <= -self.label.width:
                self.label.x = 7

            self.hue += dt*255
            if self.hue > 255:
                self.hue = 0
            self.color = graphics.wheel(int(self.hue))
            self.SpinLine()
            self.DrawRect()

    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
        self.logo.RenderWithAlpha(screen)


        #self.testSprite.render()
        graphics.setColorRGB(self.color)
        #graphics.plotLine(self.posi[0],self.posi[1],self.posf[0],self.posf[1])
        #graphics.drawRect(self.ratio, self.ratio, 8-self.ratio*2, 8-self.ratio*2)
        #self.animated.render()
        #graphics.setColor(0)
        self.label.render()
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

