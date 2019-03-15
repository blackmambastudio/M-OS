#!/usr/bin/env python
import pygame
import pytweening

from utils import utils
from utils import constants

class SceneBase:
    def __init__(self):
        self.next = self
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
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        if next_scene == None:
            self.next = None
            return
        self.next = next_scene()

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
        self.ui_backgroun = utils.Sprite(constants.SPRITES_UI_BG, 0, 32)
        self.ui_backgroun.setAnchor(0, 0)

        self.editLabel = utils.Text("press    to start editing", self.subtitle_font)
        self.editLabel.setAnchor(1, 1)
        self.editLabel.SetPosition(
            constants.VIEWPORT_WIDTH - constants.VIEWPORT_PADDING_X,
            constants.VIEWPORT_HEIGHT - constants.VIEWPORT_PADDING_Y
        )
        self.editSprite = utils.Sprite( "assets/sprites/mtlL3.png", 885, 675)
