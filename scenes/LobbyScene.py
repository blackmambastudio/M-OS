#!/usr/bin/env python

import pygame

from .BaseScene import SceneBase
from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
import mimo

# Lobby Scene
# should display a summary of the player performance
# if is the first time this scene is displayed, 
# explains what the user will do, 
# the player will have only 3 mins to complete the task
# depending on his perfomance he will earn more time to continue playing
# 

# players in line should have a simple manual explaining how to play
# and the objective

# next scene will be printing news

class LobbyScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)

    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self, dt):
        SceneBase.Update(self, dt)
    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
    

