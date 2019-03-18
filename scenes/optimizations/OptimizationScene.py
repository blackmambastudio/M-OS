#!/usr/bin/env python

import pygame
import mimo
import enum

from utils import utils
from utils import neopixelmatrix as graphics
from utils import ringpixel as ring
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
from utils import constants

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

        # -- initialize state --------------------------------------------------
        self.state = STATUS.PLAYING
        # in milliseconds
        self.countdown = 20000
        self.current_time = 20000
        self.popup_active = False

        # -- setup layout ------------------------------------------------------
        self.SetupLayout()
        self.SetupPopup()
        #ring.fill()
        #ring.current_color = [0,0,0]

    def SetupLayout(self):
        self.title = utils.Text("Optimization event scene", self.title_font)
        self.title.SetPosition(constants.VIEWPORT_CENTER_X, 546)

        self.timer = utils.Text("00:00:00", self.title_font)
        self.timer.SetPosition(constants.VIEWPORT_CENTER_X, 30)

    def SetupPopup(self):
        self.popup_title = utils.Text("Results", self.title_font, color=[0xff, 0xff, 0xff])
        self.popup_title.SetPosition(constants.VIEWPORT_CENTER_X, 180)
        
        self.popup_description = utils.Text("you are awesome!", self.normal_font, color=[0xff, 0xff, 0xff])
        self.popup_description.SetPosition(constants.VIEWPORT_CENTER_X, 506)


    def ProcessInput(self, events, pressed_keys):
        if not self.IsPlaying():
            for event in events:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                    self.AddTrigger(0.16, self, 'SwitchToScene', "Begin")
                    utils.stop_music()
                    pass
            return
        self.ProcessInputOpt(events, pressed_keys)

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

        if self.IsPlaying():
            self.current_time -= int(1000 * dt)
            if self.current_time < 0:
                self.FinishOptimization()
                self.current_time = 0

            ring.fill_percentage(self.current_time/self.countdown)
            self.timer.SetText(OptimizationScene.format_time(self.current_time), False)

    def RenderBackground(self, screen):
        screen.fill(constants.PALLETE_BACKGROUND_BLUE)
        self.title.RenderWithAlpha(screen)

    def Render(self, screen):
        self.RenderBackground(screen)
        self.timer.RenderWithAlpha(screen)
        
        self.RenderBody(screen)

        if self.popup_active:
            self.RenderPopup(screen)
            return
        self.RenderCortain(screen)
        self.RenderTimeoutAlert(screen)
    
    def RenderBody(screen):
        pass

    # should display the results
    # then shutdown this scene and change it to next one
    def FinishOptimization(self):
        self.state = STATUS.FINISHING
        self.BlinkTimer()
        self.DisplayResults()
        #self.AddTrigger(3.0, self, 'SwitchToScene', FinishEventScene)

    def BlinkTimer(self):
        self.AddTween("easeInOutSine", 0.3, self.timer, "opacity", 255, 0, 0)
        self.AddTween("easeInOutSine", 0.3, self.timer, "opacity", 0, 255, 0.31)
        self.AddTrigger(0.6, self, 'BlinkTimer')

    def IsPlaying(self):
        return self.state == STATUS.PLAYING

    def DisplayResults(self):
        self.popup_active = True
        pass

    def RenderPopup(self, screen):
        pygame.draw.rect(screen, [0x0, 0x0, 0x0], (100, 120, 1080,480))
        self.popup_title.render(screen)
        self.popup_description.render(screen)
