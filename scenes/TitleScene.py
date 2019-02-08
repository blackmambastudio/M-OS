#!/usr/bin/env python

import pygame

from .BaseScene import SceneBase
from .GameScene import GameScene

class TitleScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                self.SwitchToScene(GameScene)
    
    def Update(self, dt):
        SceneBase.Update(self, dt)
    
    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((0x1B, 0x0C, 0x00))
