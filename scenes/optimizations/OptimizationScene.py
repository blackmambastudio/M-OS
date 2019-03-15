#!/usr/bin/env python

import pygame
import mimo
import enum

from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames

from scenes.BaseScene import SceneBase
from scenes.edition.FinishEventScene import FinishEventScene

# Optimization Scene
# PLAY STATUS #3
# depending on the selected material the player will have
# the opportunity to increase the impact of the transmission
# one of many possible minigames will be loaded and displayed
# to the player

# next screen will depend on player's actions

class STATUS(enum.Enum): 
    FINISHING = 1
    PLAYING = 2

class OptimizationScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        titlefont = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 44)
        self.title = utils.Text("Optimization event scene", titlefont)
        self.title.SetPosition(1280/2, 546)

        self.state = STATUS.PLAYING

        # in milliseconds
        self.countdown = 30000
        self.timer = utils.Text("00:00:00", titlefont)
        self.timer.SetPosition(1280/2, 30)


    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                self.SwitchToScene(FinishEventScene)

    # in milliseconds
    def format_time(time):
        to_string = ""
        mins = time//72000
        seconds = (time%72000)//1000
        cents = (time%1000)//10
        if mins < 10:
            to_string += "0"
        to_string += str(mins) + ":"
        if seconds < 10:
            to_string += "0"
        to_string += str(seconds) + ":"
        if cents < 10:
            to_string += "0"
        to_string += str(cents)
        return to_string

    def Update(self, dt):
        SceneBase.Update(self, dt)
        self.countdown -= int(1000*dt)
        self.timer.SetText(OptimizationScene.format_time(self.countdown), False)
        if self.countdown < 0:
            print("time's up!")
            self.FinishOptimization()

    def RenderBackground(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
        self.title.RenderWithAlpha(screen)

    def Render(self, screen):
        self.RenderBackground(screen)
        self.timer.RenderWithAlpha(screen)
    

    # should display the results
    # then shutdown this scene and change it to next one
    def FinishOptimization(self):
        self.state = STATUS.FINISHING
        self.DisplayResults()
        #self.AddTrigger(15, self, 'SwitchToScene', FinishEventScene)

    def IsPlaying(self):
        return self.state == STATUS.PLAYING

    def DisplayResults(self):
        pass