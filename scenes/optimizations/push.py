#!/usr/bin/env python3
import pygame

from .OptimizationScene import OptimizationScene
from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite
from random import random
import mimo

class PushScene(OptimizationScene):
    def __init__(self):
        OptimizationScene.__init__(self)
        self.coldown = 0
        mimo.set_led_brightness(150)
        self.pusherDownSprite = NeoSprite('assets/NeoSprites/pusher.png') 
        self.pusherUpSprite = NeoSprite('assets/NeoSprites/pusherUp.png') 
        self.base_color = 0xfff
        self.pusherDownSprite.y = -8
        self.pusherUpSprite.y = 8

        self.colors = [0xf00, 0xff0, 0x0f0, 0x0ff, 0x00f]
        mimo.set_independent_lights(False, True)
        mimo.set_buttons_enable_status(False, True)

        led_lights = []
        index = 0
        for color in self.colors:
            led_lights += [index]
            led_lights += [(color>>8)*0xf, ((color>>4)&0xf)*0xf, (color&0xf)*0xf]
            index += 1
        mimo.set_optimization_leds_color(led_lights)
        self.playing = False

    def ProcessInputOpt(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                self.PushDown()
                self.base_color = self.colors[0]
                print("push down")
                self.playing = True
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                self.PushDown()
                self.base_color = self.colors[2]
                print("push down")
                self.playing = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                self.PushDown()
                self.base_color = self.colors[4]
                print("push down")
                self.playing = True
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                self.PushUp()
                self.base_color = self.colors[1]
                print("push up")
                self.playing = True
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
                self.PushUp()
                self.base_color = self.colors[3]
                print("push up")
                self.playing = True


    def Update(self, dt):
        OptimizationScene.Update(self, dt)
        self.coldown += dt
        if self.coldown >=1:
            self.coldown = 0


    def Render(self, screen):
        OptimizationScene.Render(self, screen)
        #self.pusherSprite.render(0,-2,0x222&self.base_color)
        #self.pusherSprite.render(0,-1,0x666&self.base_color)
        self.pusherDownSprite.render(0,0,0xfff&self.base_color)
        self.pusherUpSprite.render(0,0,0xfff&self.base_color)
        graphics.render()

    def PushDown(self):
        self.AddTween("easeInOutSine", 0.3, self.pusherDownSprite, "y", -8, 0, 0)
        self.AddTween("easeInOutSine", 0.3, self.pusherDownSprite, "y", 0, -8, 0.6)
        self.AddTrigger(1.0, self, "restorePusher")

    def PushUp(self):
        self.AddTween("easeInOutSine", 0.3, self.pusherUpSprite, "y", 8, 0, 0)
        self.AddTween("easeInOutSine", 0.3, self.pusherUpSprite, "y", 0, 8, 0.6)
        self.AddTrigger(1.0, self, "restorePusher")

    def restorePusher(self):
        self.playing = False