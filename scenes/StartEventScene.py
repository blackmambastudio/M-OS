#!/usr/bin/env python

import pygame

from .BaseScene import SceneBase
from .EditScene import EditScene
from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
import mimo
import random

from utils.NewsProvider import news
# StartEvent Scene
# PLAY STATUS #1
# should start and print a new mission to accomplish to the player

# next scene will be edit 

class StartEventScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        titlefont = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 44)
        descfont = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 22)
        self.title = utils.Text("Start event scene", titlefont)
        self.title.SetPosition(1280/2, 546)
        
        # load event, title and description
        self.current_event = news[0]

        description = self.current_event["description"]
        self.description = utils.Text(description, descfont)
        self.description.SetPosition(1280/2, 50)
        self.title.SetText(self.current_event["title"])

        self.AddTrigger(60, self, 'SwitchToScene', EditScene)
        # load material
        random.shuffle(self.current_event["material"])
        index = 0
        material_indexes = [0,1,2,7,6,5]
        mimo.set_independent_lights(False, True)
        # set buttons to switch mode
        for material in self.current_event["material"]:
            mimo.lcd_display_at(index, material["label"])
            mimo.set_material_buttons_light([index]+material["color"])
            mimo.set_material_leds_color([material_indexes[index]]+material["color"])
            index += 1

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                self.SwitchToScene(EditScene)
                

    def Update(self, dt):
        SceneBase.Update(self, dt)
    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
        self.title.RenderWithAlpha(screen)
        self.description.render_multiline(screen)
    

