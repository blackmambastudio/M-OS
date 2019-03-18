#!/usr/bin/env python

import pygame
import mimo
import random

from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
from utils.NewsProvider import news
from utils import constants

from scenes.BaseScene import SceneBase

# StartEvent Scene
# PLAY STATUS #1
# should start and print a new mission to accomplish to the player

# next scene will be edit 

class BeginEventScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        
        # initialize state

        # setup the layout for the scene
        self.SetupLayout()
        
        # load event, title, description, objective and material
        self.LoadEvent(news[0])
        
        

    def SetupLayout(self):
        # add da fact
        self.fact_title = utils.Text(
            '',
            self.title_font,
            color = constants.PALETTE_PINK
        )
        self.fact_title.setAnchor(0, 0)
        self.fact_title.SetPosition(constants.VIEWPORT_PADDING_X, 82)

        self.current_evt_frame = utils.Sprite(
            constants.SPRITES_EDITION + 'current-nws.png',
            constants.VIEWPORT_CENTER_X,
            263
        )

        self.fact_summary = utils.Text('', self.subtitle_font)
        self.fact_summary.setAnchor(0, 0)
        self.fact_summary.SetPosition(constants.VIEWPORT_PADDING_X, 416)

        # add da goal
        self.goal_frame = utils.Sprite(
            constants.SPRITES_EDITION + 'goal-lines.png',
            constants.VIEWPORT_CENTER_X,
            541
        )
        self.goal_title = utils.Text('goal', self.title_font, color = constants.PALETTE_PINK)
        self.goal_title.setAnchor(0.5, 0)
        self.goal_title.SetPosition(constants.VIEWPORT_CENTER_X, 518)

        self.goal_desc = utils.Text('', self.subtitle_font)
        self.goal_desc.setAnchor(0.5, 0)
        self.goal_desc.SetPosition(constants.VIEWPORT_CENTER_X, 584)

        # add da ui
        self.SetupUI()

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                self.CloseEvent()
                self.AddTrigger(0.16, self, 'SwitchToScene', "Edit")

    def Update(self, dt):
        SceneBase.Update(self, dt)

    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))

        # render the layout
        self.fact_title.render_multiline_truncated(
            screen,
            constants.VIEWPORT_WIDTH - 32,
            constants.FONT_TITLE * 2
        )
        self.icon.RenderWithAlpha(screen)
        self.current_evt_frame.RenderWithAlpha(screen)
        self.fact_summary.render_multiline_truncated(
            screen,
            constants.VIEWPORT_WIDTH - 32,
            constants.FONT_TITLE * 3
        )
        self.goal_frame.RenderWithAlpha(screen)
        self.goal_title.renderWithChromaticDistortion(screen)
        self.goal_desc.render_multiline(screen)

        self.RenderUI(screen)
        self.RenderCortain(screen)


    def LoadEvent(self, event):
        self.current_event = event

        self.icon = utils.Sprite(
            constants.EVENTS + self.current_event['ico'],
            constants.VIEWPORT_CENTER_X,
            263
        )
        self.fact_title.SetText(self.current_event['hdl'])
        self.fact_summary.SetText(self.current_event['ovw'] \
            + '\n' + self.current_event['arg'])
        self.goal_desc.SetText(self.current_event['gol'])

        # change the default order of the material
        random.shuffle(self.current_event['material'])

        index = 0
        material_indexes = [0, 1, 2, 7, 6, 5]
        mimo.set_independent_lights(True, True)

        # set buttons to switch mode
        for material in self.current_event['material']:
            # if material['story_position'] == constants.STORY_HOOK:
            line1_text = utils.align_text(material['label'][0], index < 3, 16, '-')
            line2_text = utils.align_text(material['label'][1], index < 3, 16, '-')
            mimo.lcd_display_at(index, line1_text, 1)
            mimo.lcd_display_at(index, line2_text, 2)

            mimo.set_material_buttons_light([index] + material['color'])
            mimo.set_material_leds_color([material_indexes[index]] + material['color'])
            index += 1

        mimo.termal_print(self.current_event['hdl'].upper())
