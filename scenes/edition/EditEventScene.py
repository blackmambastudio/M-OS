#!/usr/bin/env python

import pygame
import mimo

from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
from utils.NewsProvider import news

from scenes.BaseScene import SceneBase
from scenes.optimizations import get_next_optimization_scene

# Edit Scene
# PLAY STATUS #2
# should load material into the slots, 
# in screen should display info about the news
# when player selects a material, it should be assigned 
# and displayed in screen,
# main screen should also display info about implications of the
# selected material
#
# when player will be ready the next screen should be optimization

class EditEventScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        titlefont = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 44)
        self.title = utils.Text("Edit event scene", titlefont)
        self.title.SetPosition(1280/2, 546)

        self.sequence = [-1, -1, -1, -1]
        self.material = [False, False, False, False, False, False]
        self.busy_slots = 0

        # reset material buttons
        # lock optimization buttons and knobs
        # set material buttons mode to switch
        # animate emosensemeter...


        # load event, title and description
        self.current_event = news[0]



    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                print("select material A")
                self.assign_material_to_sequence(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                print("select material B")
                self.assign_material_to_sequence(1)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                print("select material C")
                self.assign_material_to_sequence(2)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_o:
                print("select material D")
                self.assign_material_to_sequence(3)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
                print("select material E")
                self.assign_material_to_sequence(4)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                print("select material F")
                self.assign_material_to_sequence(5)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                print("temporal next scene")
                next_scene = get_next_optimization_scene("some_value")
                self.SwitchToScene(next_scene)

    def Update(self, dt):
        SceneBase.Update(self, dt)
    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
        self.title.RenderWithAlpha(screen)
    

    def assign_material_to_sequence(self, index):
        if self.busy_slots == 4 and not self.material[index]: return

        self.material[index] = not self.material[index]
        slot_index = 0

        for slot in self.sequence:
            if slot == -1 and self.material[index]:
                self.sequence[slot_index] = index
                self.set_material_active(index, slot_index)
                self.busy_slots += 1
                break
            elif not self.material[index] and slot == index:
                self.sequence[slot_index] = -1
                self.set_material_inactive(index, slot_index)
                self.busy_slots -= 1
                break

            slot_index += 1
        
        # if busy_slots>4 should lock the unselected buttons


    def set_material_active(self, index, slot_index):
        material = self.current_event["material"][index]
        mimo.set_material_leds_color([8+slot_index]+material["color"])
        line1_text = utils.align_text(material["label"][0], index<3, 14, '*')
        line2_text = utils.align_text(material["label"][1], index<3, 14, '*')
        mimo.lcd_display_at(index, line1_text, 1)
        mimo.lcd_display_at(index, line2_text, 2)

    def set_material_inactive(self, index, slot_index):
        print("inactive", index, slot_index)
        material = self.current_event["material"][index]
        mimo.set_material_leds_color([8+slot_index, 0,0,0])
        line1_text = utils.align_text(material["label"][0], index<3, 14, ' ')
        line2_text = utils.align_text(material["label"][1], index<3, 14, ' ')
        mimo.lcd_display_at(index, line1_text, 1)
        mimo.lcd_display_at(index, line2_text, 2)

