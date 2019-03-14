#!/usr/bin/env python

import pygame
import mimo
import random
from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
from utils.NewsProvider import news

from scenes.BaseScene import SceneBase
from scenes.edition.EditEventScene import EditEventScene

# StartEvent Scene
# PLAY STATUS #1
# should start and print a new mission to accomplish to the player

# next scene will be edit 

class BeginEventScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        
        titlefont = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 44)
        subtitlefont = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 36)
        descfont = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 22)
        
        self.title = utils.Text("Start event scene", titlefont)
        self.title.setAnchor(0.5, 0)
        self.title.SetPosition(1024/2, 30)

        # description area
        self.descriptionLabel = utils.Text("new event", subtitlefont)
        self.descriptionLabel.setAnchor(1, 0)
        self.descriptionLabel.SetPosition(1170, 100)

        self.description = utils.Text("", descfont, color=(0,255,255))
        self.description.setAnchor(1, 0)
        self.description.SetPosition(1180, 130)

        # objective area
        self.objectiveLabel = utils.Text("objective", subtitlefont)
        self.objectiveLabel.setAnchor(0.5, 1)
        self.objectiveLabel.SetPosition(1024/2, 470)

        self.objective = utils.Text("", descfont, color=(0,255,255))
        self.objective.SetPosition(1024/2, 500)

        # next screen area
        self.editLabel = utils.Text("press     to edit event", descfont)
        self.editLabel.setAnchor(1, 0.5)
        self.editLabel.SetPosition(1200, 600)
        self.editSprite = utils.Sprite("assets/sprites/mtlL3.png", 1000, 600)
        
        # load event, title, description, objective and material
        self.LoadEvent(news[0])


    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                self.SwitchToScene(EditEventScene)
                

    def Update(self, dt):
        SceneBase.Update(self, dt)


    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
        self.title.renderWithChromaticDistortion(screen)
        self.descriptionLabel.renderWithChromaticDistortion(screen)
        self.description.render_multiline(screen)
        self.objectiveLabel.renderWithChromaticDistortion(screen)
        self.objective.render_multiline(screen)
        self.editLabel.render(screen)
        self.editSprite.RenderWithAlpha(screen)
        self.icon.RenderWithAlpha(screen)
    

    def LoadEvent(self, event):
        self.current_event = event
        self.icon = utils.Sprite(self.current_event["icon"], 320, 250)
        self.description.SetText(self.current_event["description"])
        self.title.SetText(self.current_event["title"])
        self.objective.SetText(self.current_event["objective"])
        random.shuffle(self.current_event["material"])
        index = 0
        material_indexes = [0,1,2,7,6,5]
        mimo.set_independent_lights(True, True)
        # set buttons to switch mode
        for material in self.current_event["material"]:
            line1_text = utils.align_text(material["label"][0], index<3, 14, '-')
            line2_text = utils.align_text(material["label"][1], index<3, 14, '-')
            mimo.lcd_display_at(index, line1_text, 1)
            mimo.lcd_display_at(index, line2_text, 2)

            mimo.set_material_buttons_light([index]+material["color"])
            mimo.set_material_leds_color([material_indexes[index]]+material["color"])
            index += 1

        mimo.termal_print(self.current_event["title"].upper())
