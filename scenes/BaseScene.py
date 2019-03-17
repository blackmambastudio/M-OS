#!/usr/bin/env python
import pygame
import pytweening

from utils import utils
from utils import constants
import math
import mimo

class SceneBase:
    def __init__(self):
        # initialize state
        self.next = None
        self.time_triggers = []
        self.tweens = []
        self.dirty_rects = [(
            0,
            0,
            constants.VIEWPORT_WIDTH,
            constants.VIEWPORT_HEIGHT
        )]

        self.title_font = pygame.font.Font(
            constants.VCR_OSD_MONO,
            constants.FONT_TITLE
        )
        self.subtitle_font = pygame.font.Font(
            constants.VCR_OSD_MONO,
            constants.FONT_SUBTITLE
        )
        self.normal_font = pygame.font.Font(
            constants.VCR_OSD_MONO,
            constants.FONT_NORMAL
        )
        self.small_font = pygame.font.Font(
            constants.VCR_OSD_MONO,
            constants.FONT_SMALL
        )

        self.render_right_progress = True
        self.render_left_progress = False

        self.transition_cortain = False
        self.height_cortain = 360
        self.AddTrigger(0.1, self, 'OpenEvent')

        self.countdown_label = utils.Text("00:00", self.title_font)
        self.countdown_label.SetPosition(constants.VIEWPORT_CENTER_X, 50)
        self.countdown_in_red = False

        # timer popup elements
        self.timeout_popup_active = False
        self.popup_timer_title = utils.Text("Alert", self.title_font, color=[0xff, 0xff, 0xff])
        self.popup_timer_title.SetPosition(constants.VIEWPORT_CENTER_X, 180)
        
        self.popup_timer_description = utils.Text("60 seconds to finish", self.normal_font, color=[0xff, 0xff, 0xff])
        self.popup_timer_description.SetPosition(constants.VIEWPORT_CENTER_X, 506)
        self.timeoutends_popup_active = False

        self.popup_timerends_title = utils.Text("Time's over", self.title_font, color=[0xff, 0xff, 0xff])
        self.popup_timerends_title.SetPosition(constants.VIEWPORT_CENTER_X, 180)
        
        self.popup_timerends_description = utils.Text("leave the machine de inmediati!", self.normal_font, color=[0xff, 0xff, 0xff])
        self.popup_timerends_description.SetPosition(constants.VIEWPORT_CENTER_X, 506)
        
        # -- end popup elements

    def ProcessInput(self, events, keys):
        pass


    def Update(self, dt):
        self.dirty_rects = [(
            0,
            0,
            constants.VIEWPORT_WIDTH,
            constants.VIEWPORT_HEIGHT
        )]
        self.CheckTriggers(dt)
        self.CheckTweens(dt)


    def Render(self, screen):
        self.RenderBody(screen)
        self.RenderUI(screen)
        self.RenderCortain(screen)
        self.RenderTimeoutAlert(screen)

    def RenderBody(self, screen):
        pass

    def RenderCortain(self, screen):
        if self.transition_cortain or self.height_cortain>=360:
            pygame.draw.rect(screen, [0x1B, 0x0C, 0x43], (0, 0, 1280,self.height_cortain))
            pygame.draw.rect(screen, [0x1B, 0x0C, 0x43], (0, 720, 1280,-self.height_cortain))

    # in milliseconds
    def format_time(time):
        time = int(time)
        to_string = ""
        mins = time//60
        seconds = math.ceil(time%60)
        if mins < 10:
            to_string += "0"
        to_string += str(mins) + ":"
        if seconds < 10:
            to_string += "0"
        to_string += str(seconds)
        return to_string 

    def SwitchToScene(self, next_scene):
        if next_scene == None:
            self.next = None
            return
        self.next = next_scene

    def Terminate(self):
        self.SwitchToScene(None)

    def AddTrigger(self, timeout, obj, func, *params):
        self.time_triggers.append([timeout, obj, func, params])

    def CheckTriggers(self, dt):
        for trigger in self.time_triggers:
            trigger[0] -= dt
            if trigger[0] <= 0:
                getattr(trigger[1], trigger[2])(*trigger[3])
                self.time_triggers.remove(trigger)

    def AddTween(self, tween, timeout, obj, prop, start, end, delay=0):
        new_tween = utils.Tween(getattr(pytweening, tween), timeout, obj, prop, start, end, delay)
        self.tweens.append(new_tween)

    def CheckTweens(self, dt):
        for tween in self.tweens:
            tween.Update(dt)
            if tween.Finished():
                self.tweens.remove(tween)

    def getDirtyRects(self):
        return self.dirty_rects

    def SwipeHorizontal(self, distance):
        pass

    def SwipeVertical(self, distance):
        pass

    def SetupUI(self):
        self.ui_background = utils.Sprite(constants.SPRITES_UI_BG, 0, 32)
        self.ui_background.setAnchor(0, 0)

        self.right_progress_label = utils.Text("press    to start editing", self.subtitle_font)
        self.right_progress_label.setAnchor(1, 1)
        self.right_progress_label.SetPosition(
            constants.VIEWPORT_WIDTH - constants.VIEWPORT_PADDING_X,
            constants.VIEWPORT_HEIGHT - constants.VIEWPORT_PADDING_Y
        )
        self.right_progress_icon = utils.Sprite( "assets/sprites/mtlL3.png", 925, 675)

        self.left_progress_label = utils.Text("press    to stop editing", self.subtitle_font)
        self.left_progress_label.setAnchor(0, 1)
        self.left_progress_label.SetPosition(
            constants.VIEWPORT_PADDING_X,
            constants.VIEWPORT_HEIGHT - constants.VIEWPORT_PADDING_Y
        )
        self.left_progress_icon = utils.Sprite( "assets/sprites/mtlL3.png", 148, 675)

    def RenderUI(self, screen):
        self.ui_background.RenderWithAlpha(screen)

        if self.render_right_progress:
            self.right_progress_label.RenderWithAlpha(screen)
            self.right_progress_icon.RenderWithAlpha(screen)

        if self.render_left_progress:
            self.left_progress_label.RenderWithAlpha(screen)
            self.left_progress_icon.RenderWithAlpha(screen)

        self.countdown_label.RenderWithAlpha(screen)

    def OpenEvent(self):
        self.transition_cortain = True
        self.AddTween("easeInOutSine", 0.15, self, "height_cortain", 360, 0, 0)
        self.AddTrigger(0.16, self, 'StopTransition')

    def CloseEvent(self):
        self.transition_cortain = True
        self.AddTween("easeInOutSine", 0.15, self, "height_cortain", 0, 360, 0)
        self.AddTrigger(0.16, self, 'StopTransition')

    def StopTransition(self):
        self.transition_cortain = False
    
    def display_timeout_alert(self):
        self.countdown_label.SetColor([0xff, 0x00, 0x00])
        self.countdown_in_red = True
        self.timeout_popup_active = True
        self.AddTrigger(3, self, 'CloseTimeoutAlert')
        

    def time_up(self):
        self.timeoutends_popup_active = True
        mimo.shutdown()

    def set_countdown(self, time):
        countdown_time = time
        if countdown_time<60 and not self.countdown_in_red:
            self.countdown_label.SetColor([0xff, 0x00, 0x00])
            self.countdown_in_red = True
        self.countdown_label.SetText(SceneBase.format_time(countdown_time), False)
        

    def RenderTimeoutAlert(self, screen):
        # display popup if applies
        if not self.timeout_popup_active: return
        pygame.draw.rect(screen, [0x0f, 0x0, 0x0], (100, 120, 1080,480))
        self.popup_timer_title.render(screen)
        self.popup_timer_description.render(screen)

    def CloseTimeoutAlert(self):
        self.timeout_popup_active = False

    def RenderTimeoutEnds(self, screen):
        if not self.timeoutends_popup_active: return
        pygame.draw.rect(screen, [0x0f, 0x0, 0x0], (100, 120, 1080,480))
        self.popup_timerends_title.render(screen)
        self.popup_timerends_description.render(screen)