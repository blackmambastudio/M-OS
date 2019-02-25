#!/usr/bin/env python

import pygame
import mimo

from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames

from scenes.BaseScene import SceneBase
from scenes.BeginEventScene import BeginEventScene

# Optimization Scene
# Available actions: back / next - optimization buttons and tunner
# Description: "cinematic explain the player the ludovic experiment"
# Next: material section tutorial


class OptimizationTutorialScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.HWSetup()

        self.LoadNextPart()


    def HWSetup(self):
        mimo.set_material_buttons_mode([0,0, 1,0, 2,0, 5,0, 6,0, 7,0])
        mimo.set_material_buttons_lock_status([0,1, 1,1, 2,1, 5,1, 6,1, 7,1])
    

    def LoadNextPart(self):
        pass

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                pass
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                pass
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                pass
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                pass
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_v:
                pass
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                print("nexT?")
                

    def Update(self, dt):
        SceneBase.Update(self, dt)

    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
        graphics.render()

