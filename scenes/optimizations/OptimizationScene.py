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
        self.score = 0

        self.SetupMimo()
        
        # -- setup layout ------------------------------------------------------
        self.SetupLayout()
        self.SetupPopup()
        #ring.fill()
        #ring.current_color = [0,0,0]

    def SetupMimo(self):
        mimo.set_led_brightness(200)

    def SetupLayout(self):
        self.frame = utils.Sprite(
            constants.SPRITES_OPTIMIZATION + 'optimization-frame.png',
            constants.VIEWPORT_CENTER_X,
            constants.VIEWPORT_CENTER_Y
        )

        self.title = utils.Text('news optimization - '+self.minigametitle, self.subtitle_font, color=constants.PALLETE_BACKGROUND_BLUE)
        self.title.SetPosition(constants.VIEWPORT_CENTER_X, 40)

        self.timerprogress = 1.0
        self.timerBackground = utils.Sprite(
            constants.SPRITES_OPTIMIZATION+'timer_bar-background.png',
            0,
            77
        )
        self.timerBackground.setAnchor(0,0)
        #self.timer = utils.Text("00:00:00", self.title_font)
        #self.timer.SetPosition(constants.VIEWPORT_CENTER_X, 30)

    def SetupPopup(self):
        self.results_background = utils.Sprite(
            constants.SPRITES_OPTIMIZATION+'optimization_results-popup.png',
            640,
            360
        )
        
        self.popup_description = utils.Text("you are awesome!", self.subtitle_font, color=constants.PALLETE_BACKGROUND_BLUE)
        self.popup_description.SetPosition(constants.VIEWPORT_CENTER_X, 380)

        self.bonus_text = utils.Text("++!", self.subtitle_font, color=constants.PALLETE_BACKGROUND_BLUE)
        self.bonus_text.SetPosition(constants.VIEWPORT_CENTER_X, 420)


        self.right_progress_label = utils.Text("press    to edit the next news", self.subtitle_font, color = constants.PALETTE_TITLES_DARK_BLUE)
        self.right_progress_label.setAnchor(1, 0)
        self.right_progress_label.SetPosition(1200, 660)
        self.right_progress_icon = utils.Sprite("assets/sprites/scenes/common/progress-button-green.png", 745, 642)
        self.right_progress_icon.setAnchor(1, 0)



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
            self.timerprogress = self.current_time/self.countdown
            ring.fill_percentage(self.timerprogress)

            #self.timer.SetText(OptimizationScene.format_time(self.current_time), False)

    def RenderBackground(self, screen):
        self.frame.RenderWithAlpha(screen)
        self.title.RenderWithAlpha(screen)

    def Render(self, screen):
        self.RenderBackground(screen)
        self.RenderTimer(screen)
        
        self.RenderBody(screen)

        if self.popup_active:
            self.RenderPopup(screen)
            return
        self.RenderCortain(screen)
        self.RenderTimeoutAlert(screen)
    
    def RenderBody(screen):
        pass

    def RenderTimer(self, screen):
        self.timerBackground.RenderWithAlpha(screen)
        #pygame.draw.rect(screen, [0x00, 0x5F, 0xFF], (0, 77, self.timerprogress*1280, 38))
        interval = (int(self.timerprogress*35))/35
        pygame.draw.rect(screen, [0xf7, 0x5a, 0xff], (0, 77, interval*1280, 38))
        pygame.draw.rect(screen, [0x21, 0x1c, 0x7F], (0, 77, 1280, 38), 2)
        

    # should display the results
    # then shutdown this scene and change it to next one
    def FinishOptimization(self):
        self.state = STATUS.FINISHING
        #self.BlinkTimer()
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
        performance_text = ""
        bonus_text = ""
        if self.score < 0.2:
            performance_text = "Optimization Shut Down"
            bonus_text = "-10 seconds"
        elif self.score < 0.4:
            performance_text = "Sluggish Performance"
            bonus_text = "Continue The Test"
        elif self.score < 0.6:
            performance_text = "Poor Execution"
            bonus_text = "Idleness Is Fatal Only To The Mediocre"
        elif self.score < 0.8:
            performance_text = "Broadcast Reach Enhanced"
            bonus_text = "10 seconds bonus"
        else:
            performance_text = "Edition Optimized!"
            bonus_text = "20 seconds bonus"
        self.popup_description.SetText(performance_text)
        self.bonus_text.SetText(bonus_text)

        mimo.set_buttons_enable_status(True, False)
        mimo.set_material_buttons_mode([6,0])
        mimo.set_material_buttons_light([6, 0x27, 0xff, 0x93])
        mimo.set_material_buttons_active_status([6, 1])



    def RenderPopup(self, screen):
        self.results_background.RenderWithAlpha(screen)
        self.popup_description.render(screen)
        self.bonus_text.render(screen)

        self.right_progress_label.RenderWithAlpha(screen)
        self.right_progress_icon.RenderWithAlpha(screen)
