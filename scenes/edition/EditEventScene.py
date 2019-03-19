#!/usr/bin/env python

import pygame
import mimo

from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
from utils.NewsProvider import news
from utils import constants
from random import random

from scenes.BaseScene import SceneBase
from scenes.optimizations import get_next_pair

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
        # load event, title and description
        self.current_event = news[0]

        # initialize state
        self.image_positions = [
            { 'x': 400, 'y': 500 },
            { 'x': 400 + 340, 'y': 500 },
            { 'x': 400 + (340 * 2), 'y': 500 },
            { 'x': 400 + (340 * 3), 'y': 500 }
        ]
        self.sequence = [-1, -1, -1, -1]
        self.material = [False, False, False, False, False, False]
        self.busy_slots = 0
        self.popupActive = False
        self.can_optimize = False
        self.showing_minigame_tutorial = False
        self.selected_minigame = ""

        # variables related with the support and damage of the involved subjects
        self.affections = {
            constants.STORY_SUBJECT_1: {
                'support': 0,
                'damage': 0
            },
            constants.STORY_SUBJECT_2: {
                'support': 0,
                'damage': 0
            }
        }

        # setup the layout for the scene
        self.available_minigames = []
        self.SetupPopupLayout()
        self.SetupLayout()

        # setup the layout for the optimization popup

        # load the material for the HOOK
        self.event_mtl = self.current_event['material']

        self.images = []
        for mtl in self.event_mtl:
            self.images.append(utils.Sprite(constants.MATERIAL + mtl['img']))

        material_indexes = [0, 1, 2, 7, 6, 5]
        index = 0
        # set buttons to switch mode
        for material in self.current_event['material']:
            line1_text = utils.align_text(material['label'][0], index < 3, 16, '-')
            line2_text = utils.align_text(material['label'][1], index < 3, 16, '-')
            mimo.lcd_display_at(index, line1_text, 1)
            mimo.lcd_display_at(index, line2_text, 2)

            mimo.set_material_buttons_light([index] + material['color'])
            mimo.set_material_leds_color([material_indexes[index]] + material['color'])
            index += 1

        # reset material buttons
        # lock optimization buttons and knobs
        # set material buttons mode to switch
        # animate emosensemeter...

        # sfx and audio
       
        audio_path = 'assets/audio/SFX/M_OS/'

        self.UI_MatSel = []
        self.UI_MatSel.append(utils.get_sound(audio_path + 'UI_MatSel_01.ogg'))
        self.UI_MatSel.append(utils.get_sound(audio_path + 'UI_MatSel_02.ogg'))
        self.UI_MatSel.append(utils.get_sound(audio_path + 'UI_MatSel_03.ogg'))
        self.UI_MatSel.append(utils.get_sound(audio_path + 'UI_MatSel_04.ogg'))

        self.UI_EndGame = utils.get_sound(audio_path + 'UI_EndGame.ogg')
        self.UI_EndGame.set_volume(1)




    def SetupLayout(self):
        self.info_frame = utils.Sprite(
            constants.SPRITES_EDITION + 'current_news-frame.png',
            constants.VIEWPORT_CENTER_X,
            165
        )
        # por favor agrandar

        self.icon = utils.Sprite(
            constants.EVENTS + self.current_event['ico']
        )
        self.icon.Scale([0.75, 0.75])
        self.icon.SetPosition(280, 165)

        self.fact_title = utils.Text(
            self.current_event['hdl'],
            self.normal_font,
            color = constants.PALETTE_TITLES_DARK_BLUE
        )
        self.fact_title.setAnchor(0, 0)
        self.fact_title.SetPosition(380, 94)


        self.goal_desc = utils.Text(
            'goal: ' + self.current_event['gol'],
            self.normal_font,
            color = constants.PALETTE_TITLES_DARK_BLUE
        )
        self.goal_desc.setAnchor(0, 0)
        self.goal_desc.SetPosition(380, 124)

        self.news_framing = utils.Text(
            'no opinion bias set yet. select material to start framing the news.',
            self.normal_font,
            color = constants.PALETTE_TITLES_DARK_BLUE
        )
        self.news_framing.setAnchor(0, 0)
        self.news_framing.SetPosition(380, 180)
        self.timeline_back = utils.Sprite(

            constants.SPRITES_EDITION + 'storyline-background.png',
            constants.VIEWPORT_CENTER_X,
            606
        )

        self.mtl_slots_frames = [
            utils.Sprite(constants.SPRITES_EDITION + 'mtl_slot.png', 170, 440),
            utils.Sprite(constants.SPRITES_EDITION + 'mtl_slot.png', 483, 440),
            utils.Sprite(constants.SPRITES_EDITION + 'mtl_slot.png', 797, 440),
            utils.Sprite(constants.SPRITES_EDITION + 'mtl_slot.png', 1110, 440)
        ]

        self.news_hook = utils.Text(
            'hook',
            self.subtitle_font,
            color = constants.PALLETE_BACKGROUND_BLUE
        )   
        self.news_hook.SetPosition(170, 604)

        self.news_conflict = utils.Text(
            'plot',
            self.subtitle_font,
            color = constants.PALLETE_BACKGROUND_BLUE
        )
        self.news_conflict.SetPosition(constants.VIEWPORT_CENTER_X, 605)
        self.news_conclusion = utils.Text(
            'conclusion',
            self.subtitle_font,
            color = constants.PALLETE_BACKGROUND_BLUE
        )
        self.news_conclusion.SetPosition(1110, 605)

        #--- aca voy
        self.popupLabel = utils.Text('popup', self.subtitle_font)
        self.popupLabel.setAnchor(0.5, 0)
        self.popupLabel.SetPosition(640, 120)

        # add da ui
        self.SetupUI()
        self.render_right_progress = False
        self.right_progress_label.SetText('press    to finish edition')
        self.right_progress_icon.SetPosition(830, 645)


    def SetupPopupLayout(self):
        self.available_minigames = get_next_pair()
        print("primero esto", self.available_minigames)
        self.popup_background = utils.Sprite(
            constants.SPRITES_EDITION + 'minigames-popup.png',
            constants.VIEWPORT_CENTER_X,
            351
        )

        self.popup_title = utils.Text(
            self.current_event['hdl'],
            self.subtitle_font,
            color = constants.PALLETE_BACKGROUND_BLUE
        )
        self.popup_title.setAnchor(0.5, 0)
        self.popup_title.SetPosition(constants.VIEWPORT_CENTER_X, 100)

        self.popup_framing = utils.Text(
            'audience will TRUST MONTEASALVO\nand LOSE CREDIBILITY in ENVIRONMENTALISTS',
            self.normal_font,
            color= constants.PALETTE_TITLES_DARK_BLUE
        )
        self.popup_framing.setAnchor(0, 0)
        self.popup_framing.SetPosition(
            constants.POPUP_X + 50,
            185
        )

        minigame_data_a = self.available_minigames[0]
        minigame_data_b = self.available_minigames[1]

        # minigame 1
        self.icon_back_a= utils.Sprite(
            'assets/sprites/scenes/edition/icon_frame.png',
            336,
            360
        )
        self.icon_minigame_a = utils.Sprite(
            'assets/minigame_icons/'+minigame_data_a["icon"],
            336,
            360
        )
        self.title_minigame_a = utils.Text(
            minigame_data_a["title"],
            self.subtitle_font,
            336,
            480,
            color= constants.PALETTE_TITLES_DARK_BLUE
        )
        self.description_minigame_a = utils.Text(
            minigame_data_a["description"],
            self.normal_font,
            111,
            500,
            color= constants.PALETTE_TITLES_DARK_BLUE
        )
        self.description_minigame_a.setAnchor(0,0)

        # minigame 2
        self.icon_back_b= utils.Sprite(
            'assets/sprites/scenes/edition/icon_frame.png',
            937,
            360
        )
        self.icon_minigame_b = utils.Sprite(
            'assets/minigame_icons/'+minigame_data_b["icon"],
            937,
            360
        )
        self.title_minigame_b = utils.Text(
            minigame_data_b["title"],
            self.subtitle_font,
            937,
            480,
            color= constants.PALETTE_TITLES_DARK_BLUE
        )

        self.description_minigame_b = utils.Text(
            minigame_data_b["description"],
            self.normal_font,
            712,
            500,
            color= constants.PALETTE_TITLES_DARK_BLUE
        )
        self.description_minigame_b.setAnchor(0,0)


    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                self.assign_material_to_sequence(0)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.assign_material_to_sequence(1)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
                self.assign_material_to_sequence(2)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_o:
                self.assign_material_to_sequence(3)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
                self.assign_material_to_sequence(4)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                self.assign_material_to_sequence(5)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                if self.can_optimize and not self.popupActive:
                    # open the optimization popup

                    self.render_left_progress = True
                    self.OpenPopup()
                elif self.popupActive:
                    if self.showing_minigame_tutorial:
                        self.PlayMinigame(self.selected_minigame)
                    else:
                        self.ShowMinigame(constants.MINIGAME_RIGHT)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                if self.popupActive:
                    self.ShowMinigame(constants.MINIGAME_LEFT)

    def Update(self, dt):
        if not self.popupActive:
            SceneBase.Update(self, dt)

    def RenderBody(self, screen):
        if self.popupActive:
            self.RenderPopup(screen)
            return

        self.info_frame.RenderWithAlpha(screen)
        self.icon.RenderWithAlpha(screen)

        # render texts
        self.fact_title.render(screen)
        self.goal_desc.render(screen)

        for slot in self.mtl_slots_frames:
            # TODO: change the frame of the mtl slot if it is being used
            slot.RenderWithAlpha(screen)

        self.timeline_back.RenderWithAlpha(screen)
        self.news_hook.RenderWithAlpha(screen)
        self.news_conflict.RenderWithAlpha(screen)
        self.news_conclusion.RenderWithAlpha(screen)

        index = 0
        for slot in self.sequence:
            if slot != -1:
                self.images[slot].SetPosition(
                    self.mtl_slots_frames[index].x,
                    self.mtl_slots_frames[index].y
                )
                self.images[slot].RenderWithAlpha(screen)
            index += 1

        if self.can_optimize:
            self.right_progress_label.RenderWithAlpha(screen)
            self.right_progress_icon.RenderWithAlpha(screen)

        self.news_framing.render_multiline_truncated(screen, 680, 52)

        # render countdown
        self.countdown_label.RenderWithAlpha(screen)

        self.RenderCortain(screen)
        self.RenderTimeoutAlert(screen)


    def assign_material_to_sequence(self, index):
        if self.busy_slots == 4 and not self.material[index]: return
        self.material[index] = not self.material[index]
        slot_index = 0

        for slot in self.sequence:
            if not self.material[index] and slot == index:
                self.sequence[slot_index] = -1
                self.set_material_inactive(index, slot_index)
                self.busy_slots -= 1
                self.update_affections(index, False)
                break
            elif slot == -1 and self.material[index]:
                self.sequence[slot_index] = index
                self.set_material_active(index, slot_index)
                self.busy_slots += 1
                self.update_affections(index)
                break
            slot_index += 1

        # ──────────────────────────────────────────────────────────────────────┐
        # we won't have material label updates for the momento
        # next_story_part = 0
        # for used_slot in self.sequence:
        #     if used_slot == -1:
        #         # update the LCDs and the images so they show the material
        #         # available for the free slot
        #         if next_story_part == constants.STORY_CONFLICT_1:
        #             break
        #         elif next_story_part == constants.STORY_CONFLICT_2:
        #             break
        #         else:
        #             break
        #     next_story_part += 1

        # new_mtl = []
        # for mtl in self.event_mtl:
        #     # check which is the next free story slot and update the material
        #     if mtl['story_position'] == next_story_part:
        #         new_mtl.append(mtl)

        # # change the default order of the material
        # # random.shuffle(new_mtl)

        # # replace the images and the texts on the LCD displays with the new material
        # index = 0
        # for mtl_img in self.images:
        #     xxx = index in self.sequence
        #     if not xxx:
        #         self.images[index] = utils.Sprite(
        #             constants.MATERIAL + new_mtl[index]['img']
        #         )
        #         line1_text = utils.align_text(
        #             new_mtl[index]['label'][0],
        #             index < 3, 14, '-'
        #         )
        #         line2_text = utils.align_text(
        #             new_mtl[index]['label'][1],
        #             index < 3, 14, '-'
        #         )
        #         mimo.lcd_display_at(index, line1_text, 1)
        #         mimo.lcd_display_at(index, line2_text, 2)
        #         print("index to change", index, line1_text)

        #         # TODO: update the color for the LEDs
        #     index += 1
        # ──────────────────────────────────────────────────────────────────────┘

        self.can_optimize = self.busy_slots == 4
        # if busy_slots>4 should lock the unselected buttons

    def update_affections(self, index, sum = True):
        sbj_support = None
        sbj_damage = None

        if not self.event_mtl[index]['supports'] == None:
            sbj_support = self.event_mtl[index]['supports']
        if not self.event_mtl[index]['damages'] == None:
            sbj_damage = self.event_mtl[index]['damages']

        if not sbj_support == None:
            self.affections[sbj_support]['support'] += 1 if sum else -1
        if not sbj_damage == None:
            self.affections[sbj_damage]['damage'] += 1 if sum else -1

        sbj1 = self.affections[constants.STORY_SUBJECT_1]
        sbj2 = self.affections[constants.STORY_SUBJECT_2]

        # check which framing rule matches the current state of affections
        for rule in self.current_event['framing']:
            if rule['operator'] == '>':
                if self.affections[rule['left_operate']][rule['property']] \
                        > self.affections[rule['right_operate']][rule['property']]:
                    self.news_framing.SetText(rule['text'])
                    break
            elif rule['operator'] == '=':
                if self.affections[rule['left_operate']][rule['property']] \
                        == self.affections[rule['right_operate']][rule['property']]:
                    self.news_framing.SetText(rule['text'])
                    break
            elif rule['operator'] == 'none':
                self.news_framing.SetText(rule['text'])
                break

    def set_material_active(self, index, slot_index):
        self.UI_MatSel[int(random()*3)].play()
        material = self.current_event['material'][index]
        mimo.set_material_leds_color([8+slot_index]+material['color'])
        line1_text = utils.align_text(material['label'][0], index < 3, 16, '*')
        line2_text = utils.align_text(material['label'][1], index < 3, 16, '*')
        mimo.lcd_display_at(index, line1_text, 1)
        mimo.lcd_display_at(index, line2_text, 2)
       

    def set_material_inactive(self, index, slot_index):
        material = self.current_event['material'][index]
        mimo.set_material_leds_color([8+slot_index, 0,0,0])
        line1_text = utils.align_text(material['label'][0], index < 3, 16, '-')
        line2_text = utils.align_text(material['label'][1], index < 3, 16, '-')
        mimo.lcd_display_at(index, line1_text, 1)
        mimo.lcd_display_at(index, line2_text, 2)

    def OpenPopup(self):
        self.popupActive = True
        self.dirty_rects = [
            (
                constants.POPUP_X,
                constants.POPUP_Y,
                constants.POPUP_WIDTH,
                constants.POPUP_HEIGHT
            ),
            (0, 630, constants.VIEWPORT_WIDTH, 90),
            (
                self.countdown_label.position[0],
                self.countdown_label.position[1],
                self.countdown_label.text.get_width(),
                self.countdown_label.text.get_height()
            )
        ]

        random_color = (
            int(random() * 255),
            int(random() * 255),
            int(random() * 255)
        )
        self.right_progress_label.SetText('press    to '+self.available_minigames[1]["title"])
        self.right_progress_label.setAnchor(0, 0.5)
        self.right_progress_label.SetPosition(760, 675)
        self.right_progress_icon.setAnchor(0.5, 0.5)
        self.right_progress_icon.SetPosition(907, 675)

        random_color = (
            int(random() * 255),
            int(random() * 255),
            int(random() * 255)
        )
        self.left_progress_label.SetText('press    to '+self.available_minigames[0]["title"])
        self.left_progress_label.setAnchor(0, 0.5)
        self.left_progress_label.SetPosition(170, 675)
        self.left_progress_icon.setAnchor(0.5, 0.5)
        self.left_progress_icon.SetPosition(316, 675)
        self.render_right_progress = True

    def ClosePopup(self):
        self.popupActive = False
        self.dirty_rects = [
            (
                constants.POPUP_X,
                constants.POPUP_Y,
                constants.POPUP_WIDTH,
                constants.POPUP_HEIGHT
            ),
            (0, 630, constants.VIEWPORT_WIDTH, 90)
        ]

    def RenderPopup(self, screen):
        self.RenderUI(screen)

        self.popup_background.RenderWithAlpha(screen)
        self.popup_title.render_multiline_truncated(
            screen,
            1089,
            constants.FONT_TITLE * 2 +5
        )

        if not self.showing_minigame_tutorial:
            self.popup_framing.render_multiline_truncated(screen, 1088, 86)
            self.icon_back_a.RenderWithAlpha(screen)
            self.icon_minigame_a.RenderWithAlpha(screen)
            self.title_minigame_a.render(screen)
            self.description_minigame_a.render_multiline_truncated(screen, 450, 300)
            self.icon_back_b.RenderWithAlpha(screen)
            self.icon_minigame_b.RenderWithAlpha(screen)
            self.title_minigame_b.render(screen)
            self.description_minigame_b.render_multiline_truncated(screen, 450, 300)
        else:
            self.minigame_title.RenderWithAlpha(screen)
            self.minigame_optimization_sub.render(screen)
            self.minigame_icon_back.RenderWithAlpha(screen)
            self.minigame_icon.RenderWithAlpha(screen)
            self.minigame_desc.render_multiline_truncated(screen, 350, 500)
            self.minigame_goal_label.render(screen)
            self.minigame_goal.render_multiline_truncated(screen, 350, 500)

    # load images for minigames
    def ShowMinigame(self, side):
        # TODO: load the specific mini-game info. based on the chosen side
        self.showing_minigame_tutorial = True
        selected_minigame = self.available_minigames[side]
        self.selected_minigame = selected_minigame["scene"]

        minigame_color = self.left_progress_label.color \
            if side == constants.MINIGAME_LEFT else self.right_progress_label.color

        self.minigame_title = utils.Text(
            selected_minigame["title"],
            self.subtitle_font,
            color = constants.PALETTE_TITLES_DARK_BLUE
        )
        self.minigame_title.setAnchor(0, 0)
        self.minigame_title.SetPosition(310, 240)

        self.minigame_optimization_sub = utils.Text(
            'optimization',
            self.subtitle_font,
            color = constants.PALLETE_BACKGROUND_TITLE_BLUE
        )
        self.minigame_optimization_sub.SetPosition(constants.VIEWPORT_CENTER_X, 175)

        self.minigame_icon_back = utils.Sprite(
            'assets/sprites/scenes/edition/icon_frame.png',
            110,
            240+87
        )
        self.minigame_icon_back.setAnchor(0,0.5)
        self.minigame_icon = utils.Sprite(
            'assets/minigame_icons/'+selected_minigame["icon"],
            110,
            240+87
        )
        self.minigame_icon.setAnchor(0,0.5)
        
        self.minigame_desc = utils.Text(
            selected_minigame["description"],
            self.normal_font,
            310,
            300,
            color= constants.PALETTE_TITLES_DARK_BLUE
        )
        self.minigame_desc.setAnchor(0,0)


        self.minigame_goal_label = utils.Text(
            'goal:',
            self.subtitle_font,
            300,
            450,
            color= constants.PALETTE_TITLES_DARK_BLUE
        )
        self.minigame_goal_label.setAnchor(1,0)
        self.minigame_goal = utils.Text(
            selected_minigame["goal"],
            self.normal_font,
            310,
            450,
            color= constants.PALETTE_TITLES_DARK_BLUE
        )
        self.minigame_goal.setAnchor(0,0)

        self.right_progress_label.SetColor(minigame_color)
        self.right_progress_label.SetText('press    to start')
        self.right_progress_icon.SetPosition(907, 675)

        self.render_left_progress = False

    def PlayMinigame(self, name):
        self.SwitchToScene(name)