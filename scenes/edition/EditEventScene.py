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
        self.selected_minigame = -1

        # setup the layout for the scene
        self.SetupLayout()

        # setup the layout for the optimization popup
        self.SetupPopupLayout()

        # load the material for the HOOK
        self.event_mtl = self.current_event['material']

        self.images = []
        for mtl in self.event_mtl:
            if mtl['story_position'] == constants.STORY_HOOK:
                self.images.append(utils.Sprite(constants.MATERIAL + mtl['img']))

        # reset material buttons
        # lock optimization buttons and knobs
        # set material buttons mode to switch
        # animate emosensemeter...

    def SetupLayout(self):
        self.info_frame = utils.Sprite(
            constants.SPRITES_EDITION + 'info-frame.png',
            364,
            240
        )
        self.fact_title = utils.Text(
            self.current_event['hdl'],
            self.subtitle_font,
            color = constants.PALETTE_PINK
        )
        self.fact_title.setAnchor(0, 0)
        self.fact_title.SetPosition(78, 94)

        self.goal_desc = utils.Text(
            'goal: ' + self.current_event['gol'],
            self.normal_font
        )
        self.goal_desc.setAnchor(0, 0)
        self.goal_desc.SetPosition(56, 207)

        self.news_framing = utils.Text(
            'no opinion bias set yet. select material to start framing the news.',
            self.normal_font,
            color = constants.PALETTE_CYAN
        )
        self.news_framing.setAnchor(0, 0)
        self.news_framing.SetPosition(56, 271)

        self.anchor_frame = utils.Sprite(
            constants.SPRITES_EDITION + 'anchor-frame.png',
            983,
            233
        )

        self.mtl_slots_frames = [
            utils.Sprite(constants.SPRITES_EDITION + 'mtl_slot.png', 170, 513),
            utils.Sprite(constants.SPRITES_EDITION + 'mtl_slot.png', 483, 513),
            utils.Sprite(constants.SPRITES_EDITION + 'mtl_slot.png', 797, 513),
            utils.Sprite(constants.SPRITES_EDITION + 'mtl_slot.png', 1110, 513)
        ]

        self.storyline_bg = utils.Sprite(
            constants.SPRITES_EDITION + 'storyline-background.png',
            constants.VIEWPORT_CENTER_X,
            612
        )

        self.news_hook = utils.Text(
            'hook',
            self.normal_font,
            color = constants.PALETTE_BLUE
        )
        self.news_hook.SetPosition(170, 612)
        self.news_conflict = utils.Text(
            'plot',
            self.normal_font,
            color = constants.PALETTE_BLUE
        )
        self.news_conflict.SetPosition(constants.VIEWPORT_CENTER_X, 612)
        self.news_conclusion = utils.Text(
            'conclusion',
            self.normal_font,
            color = constants.PALETTE_BLUE
        )
        self.news_conclusion.SetPosition(1110, 612)

        self.popupLabel = utils.Text('popup', self.subtitle_font)
        self.popupLabel.setAnchor(0.5, 0)
        self.popupLabel.SetPosition(640, 120)

        # add da ui
        self.SetupUI()
        self.right_progress_label.SetText('press    to finish edition')
        self.right_progress_icon.SetPosition(900, 675)

    def SetupPopupLayout(self):
        self.popup_background = utils.Sprite(
            constants.SPRITES_EDITION + 'optimization_background.png',
            constants.VIEWPORT_CENTER_X,
            351
        )

        self.popup_title = utils.Text(
            self.current_event['hdl'],
            self.title_font,
            color = constants.PALETTE_PINK
        )
        self.popup_title.setAnchor(0, 0)
        self.popup_title.SetPosition(constants.POPUP_X + 16, 96)

        self.popup_framing = utils.Text(
            'audience will TRUST MONTEASALVO\nand LOSE CREDIBILITY in ENVIRONMENTALISTS',
            self.subtitle_font
        )
        self.popup_framing.setAnchor(0, 0)
        self.popup_framing.SetPosition(
            constants.POPUP_X + 16,
            205
        )

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

    def Render(self, screen):
        if self.popupActive:
            self.RenderPopup(screen)
            return

        screen.fill((0x1B, 0x0C, 0x43))

        self.info_frame.RenderWithAlpha(screen)

        # render texts
        self.fact_title.render_multiline_truncated(screen, 616, 94)
        self.goal_desc.render_multiline_truncated(screen, 617, 52)
        self.news_framing.render_multiline_truncated(screen, 617, 52)

        self.anchor_frame.RenderWithAlpha(screen)

        self.storyline_bg.RenderWithAlpha(screen)
        for slot in self.mtl_slots_frames:
            # TODO: change the frame of the mtl slot if it is being used
            slot.RenderWithAlpha(screen)

        self.news_hook.RenderWithAlpha(screen)
        self.news_conflict.RenderWithAlpha(screen)
        self.news_conclusion.RenderWithAlpha(screen)

        self.ui_background.RenderWithAlpha(screen)

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

        # render countdown
        self.countdown_label.RenderWithAlpha(screen)
        self.RenderCortain(screen)

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

        print('current mtl sequence: >>>>>>>>>>>>>>>>>>>>>>>>>')
        print(self.sequence)

        next_story_part = 0
        for used_slot in self.sequence:
            if used_slot == -1:
                # update the LCDs and the images so they show the material
                # available for the free slot
                if next_story_part == constants.STORY_CONFLICT_1:
                    break
                elif next_story_part == constants.STORY_CONFLICT_2:
                    break
                else:
                    break
            next_story_part += 1

        new_mtl = []
        for mtl in self.event_mtl:
            # check which is the next free story slot and update the material
            if mtl['story_position'] == next_story_part:
                new_mtl.append(mtl)

        # change the default order of the material
        # random.shuffle(new_mtl)

        # replace the images and the texts on the LCD displays with the new material
        index = 0
        for mtl_img in self.images:
            xxx = index in self.sequence
            if not xxx:
                self.images[index] = utils.Sprite(
                    constants.MATERIAL + new_mtl[index]['img']
                )
                line1_text = utils.align_text(
                    new_mtl[index]['label'][0],
                    index < 3, 14, '-'
                )
                line2_text = utils.align_text(
                    new_mtl[index]['label'][1],
                    index < 3, 14, '-'
                )
                mimo.lcd_display_at(index, line1_text, 1)
                mimo.lcd_display_at(index, line2_text, 2)
                print("index to change", index, line1_text)

                # TODO: update the color for the LEDs
            else:
                print('gonorrea!')
            index += 1

        self.can_optimize = self.busy_slots == 4
        # if busy_slots>4 should lock the unselected buttons

    def set_material_active(self, index, slot_index):
        material = self.current_event['material'][index]
        mimo.set_material_leds_color([8+slot_index]+material['color'])
        #line1_text = utils.align_text(material['label'][0], index<3, 14, '*')
        #line2_text = utils.align_text(material['label'][1], index<3, 14, '*')
        #mimo.lcd_display_at(index, line1_text, 1)
        #mimo.lcd_display_at(index, line2_text, 2)

    def set_material_inactive(self, index, slot_index):
        material = self.current_event['material'][index]
        mimo.set_material_leds_color([8+slot_index, 0,0,0])
        #line1_text = utils.align_text(material['label'][0], index<3, 14, ' ')
        #line2_text = utils.align_text(material['label'][1], index<3, 14, ' ')
        #mimo.lcd_display_at(index, line1_text, 1)
        #mimo.lcd_display_at(index, line2_text, 2)

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
            (self.countdown_label.position[0], self.countdown_label.position[1], self.countdown_label.text.get_width(), self.countdown_label.text.get_height())
        ]

        random_color = (
            int(random() * 255),
            int(random() * 255),
            int(random() * 255)
        )
        self.right_progress_label.SetColor(random_color)
        self.right_progress_label.SetText('press    to play')
        self.right_progress_icon.SetPosition(1094, 675)

        random_color = (
            int(random() * 255),
            int(random() * 255),
            int(random() * 255)
        )
        self.left_progress_label.SetColor(random_color)
        self.left_progress_label.SetText('press    to play')

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
            constants.FONT_TITLE * 2
        )

        if not self.showing_minigame_tutorial:
            self.popup_framing.render_multiline_truncated(screen, 1088, 86)
        else:
            self.minigame_title.RenderWithAlpha(screen)

    def ShowMinigame(self, side):
        # TODO: load the specific mini-game info. based on the chosen side
        self.showing_minigame_tutorial = True
        self.selected_minigame = side

        minigame_color = self.left_progress_label.color \
            if side == constants.MINIGAME_LEFT else self.right_progress_label.color

        self.minigame_title = utils.Text(
            'mini-game-name',
            self.subtitle_font,
            color = constants.PALETTE_PINK
        )
        self.minigame_title.setAnchor(0, 0)
        self.minigame_title.SetPosition(306, 206)

        self.right_progress_label.SetColor(minigame_color)
        self.right_progress_label.SetText('press    to start')
        self.right_progress_icon.SetPosition(1056, 675)

        self.render_left_progress = False

    def PlayMinigame(self, side):
        # TODO: load the specific mini-game based on the chosen side
        next_scene = get_next_optimization_scene('some_value')
        self.SwitchToScene("Focus")