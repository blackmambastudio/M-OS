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

        #musique
        self.MX = []
        self.MX.append('assets/audio/MX/DirtySoil.ogg')
        self.MX.append('assets/audio/MX/DystopianBallad.ogg')
        self.MX.append('assets/audio/MX/LazyBartender.ogg')
        self.MX.append('assets/audio/MX/LostInParadise.ogg')
        self.MX.append('assets/audio/MX/PapayaJuice.ogg')
        self.MX.append('assets/audio/MX/RetroDance.ogg')
        self.MX.append('assets/audio/MX/SunnyBeach.ogg')
        self.MX.append('assets/audio/MX/TimeTraveler.ogg')
        self.MX.append('assets/audio/MX/WeirdJungle.ogg')
        self.MX.append('assets/audio/MX/WhereAreYou.ogg')

        self.SetupMimo()

        # initialize state
        # setup the layout for the scene
        self.SetupLayout()
        
        # load event, title, description, objective and material
        # currento_evento = int(random.random() * 4)

        if constants.currento_evento == 3:
            constants.currento_evento = -1
        constants.currento_evento += 1
        self.LoadEvent(news[constants.currento_evento])

    def SetupMimo(self):
        mimo.set_led_brightness(150)
        mimo.set_buttons_enable_status(True, False)
        mimo.set_material_ligths_on([0,0, 1,0, 2,0, 3,0, 4,0, 5,0, 6,0, 7,0, 8,0, 9,0, 10, 0, 11, 0, 12, 0, 13, 0, 14, 0, 15, 0, 16, 0, 17, 0, 18, 0, 19, 0, 20, 0, 21, 0, 22, 0, 23, 0, 24, 0, 25, 0, 26,0, 27,0])
        mimo.set_optimization_ligths_on([0,0, 1,0, 2,0, 3,0, 4,0])
    
        mimo.set_material_buttons_mode([0,1, 1,1, 2,1, 3,1, 4,1, 5,1, 6,0, 7,0])
        mimo.set_independent_lights(True, True)
        mimo.set_material_leds_color([7, 0xf7, 0x5a, 0xff])
                

    def SetupLayout(self):
        utils.play_music(self.MX[(int(random.random()*10))], -1, 0.1, 0.6)
        # add da fact
        self.fact_title = utils.Text(
            '',
            self.title_font,
            color = constants.PALETTE_TITLES_DARK_BLUE
        )
        self.fact_title.setAnchor(0.5, 0)
        self.fact_title.SetPosition(constants.VIEWPORT_CENTER_X, 100)

        self.current_evt_frame = utils.Sprite(
            constants.SPRITES_EDITION + 'current-nws.png'
        )
        self.current_evt_frame.setAnchor(0.5, 0.5)
        self.current_evt_frame.SetPosition(constants.VIEWPORT_CENTER_X, 303)

        self.fact_summary = utils.Text('', self.normal_font,
            color = constants.PALETTE_TITLES_DARK_BLUE)
        self.fact_summary.setAnchor(0.5, 0)
        self.fact_summary.SetPosition(constants.VIEWPORT_CENTER_X, 463)

        # self.fact_argument = utils.Text('', self.normal_font,
        #     color = constants.PALETTE_TITLES_DARK_BLUE)
        # self.fact_argument.setAnchor(0.5, 0)
        # self.fact_argument.SetPosition(constants.VIEWPORT_CENTER_X, 496)

        # add da goal
        goal_layout = {
            'title': { 'en': 'goal', 'es': 'objetivo' },
            'width': { 'en': 115, 'es': 198 }
        }
        self.goal_title = utils.Text(
            goal_layout['title'][constants.language] + ':',
            self.subtitle_font,
            color = constants.PALLETE_BACKGROUND_BLUE
        )
        self.goal_title.setAnchor(0, 0)
        self.goal_title.SetPosition(78, 554)

        self.goal_desc = utils.Text('', self.subtitle_font, color = constants.PALLETE_BACKGROUND_BLUE)
        self.goal_desc.setAnchor(0, 0)
        self.goal_desc.SetPosition(78 + goal_layout['width'][constants.language], 554)

        # background for other news:
        self.back_news = []
        for i in range(1, 3):
            temp = utils.Sprite(
                constants.SPRITES_EDITION + 'next-nws.png'
            )
            temp.setAnchor(0.5, 0.5)
            temp.SetPosition(constants.VIEWPORT_CENTER_X+273*i, 303)
            self.back_news.append(temp)

        # add da ui
        self.SetupUI()

    def ProcessInput(self, events, pressed_keys):
        if self.closing: return
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                self.CloseEvent(0.5)
                self.UI_SwitchScene = utils.get_sound('assets/audio/SFX/Scanning/MG1_ObjSort.ogg')
                self.UI_SwitchScene.play()
                self.AddTrigger(0.51, self, 'SwitchToScene', "Edit")

    def Update(self, dt):
        SceneBase.Update(self, dt)

    def RenderBody(self, screen):

        # for back_image in self.back_news:
        #     back_image.RenderWithAlpha(screen)

        # render the layout
        self.fact_title.render(screen)
        self.current_evt_frame.RenderWithAlpha(screen)
        self.icon.RenderWithAlpha(screen)
        self.fact_summary.render(screen)
        # self.fact_argument.render(screen)

        pygame.draw.rect(screen, constants.PALLETE_BACKGROUND_TITLE_BLUE, (0, 540, 1280, 70))
        self.goal_title.render(screen)
        self.goal_desc.render(screen)


    def LoadEvent(self, event):
        self.current_event = event

        self.icon = utils.Sprite(
            constants.EVENTS + self.current_event['ico']
        )

        self.icon.setAnchor(0.5, 0.5)
        self.icon.SetPosition(constants.VIEWPORT_CENTER_X, 303)

        self.fact_title.SetText(self.current_event['hdl'][constants.language])
        self.fact_summary.SetText(self.current_event['ovw'][constants.language])
        # self.fact_argument.SetText(self.current_event['arg'][constants.language])
        self.goal_desc.SetText(self.current_event['gol'][constants.language])

        # change the default order of the material
        random.shuffle(self.current_event['material'])


        #mimo.termal_print(self.current_event['hdl'].upper())
        #### imprimir la noticia en pantalla?