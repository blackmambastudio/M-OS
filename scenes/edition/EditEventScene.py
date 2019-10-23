#!/usr/bin/env python

import pygame
import mimo

from utils import utils
from utils import neopixelmatrix as graphics
from utils import ringpixel as ring
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

    def hook(self, right_mtl, mtl):
        if right_mtl:
            return 7 if mtl['target'] == 1 else 4
        else:
            return 2

    def plot(self, right_mtl, mtl):
        if right_mtl:
            return 5 if mtl['target'] == 2 else 4
        else:
            return 1

    def conclusion(self, right_mtl, mtl):
        if right_mtl:
            return 7 if mtl['target'] == 3 else 4
        else:
            return 2

    def __init__(self):
        SceneBase.__init__(self)

        self.impact = 0
        self.mtl_switcher = {
            0: self.hook,
            1: self.plot,
            2: self.plot,
            3: self.conclusion
        }

        # Cargar el arreglo de direcciones pa' la musique
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

        # Cargar arreglos de SFX
        audio_path = 'assets/audio/SFX/M_OS/'

        self.UI_MatSel = []
        self.UI_MatSel.append(utils.get_sound(audio_path + 'UI_MatSel_01.ogg'))
        self.UI_MatSel.append(utils.get_sound(audio_path + 'UI_MatSel_02.ogg'))
        self.UI_MatSel.append(utils.get_sound(audio_path + 'UI_MatSel_03.ogg'))
        self.UI_MatSel.append(utils.get_sound(audio_path + 'UI_MatSel_04.ogg'))

        self.UI_EndGame = utils.get_sound(audio_path + 'UI_EndGame.ogg')
        self.UI_EndGame.set_volume(1)

        self.UI_SwitchScene = utils.get_sound('assets/audio/SFX/Scanning/MG1_ObjSort.ogg')

        # Preparar la máquina para la destrucción
        self.SetupMimo()

        # load event, title and description
        self.current_event = news[constants.currento_evento]
        self.current_frame = ''

        constants.currento_evento += 1
        if constants.currento_evento == 3:
            constants.currento_evento = 0

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
        self.SetupLayout()

        # obtener el material del hecho
        self.event_mtl = self.current_event['material']

        self.images = []
        for mtl in self.event_mtl:
            self.images.append(utils.Sprite(constants.MATERIAL + mtl['img']))

        material_indexes = [0, 1, 2, 4, 5, 6]
        index = 0
        # set buttons to switch mode
        for material in self.current_event['material']:
            line1_text = utils.align_text(material['label'][constants.language][0], index < 3, 16, '-')
            line2_text = utils.align_text(material['label'][constants.language][1], index < 3, 16, '-')
            
            mimo.set_material_buttons_light([index] + material['color'])
            #mimo.set_material_leds_color([material_indexes[index]] + material['color'])
            
            mimo.lcd_display_at(index, line1_text, 1)
            mimo.lcd_display_at(index, line2_text, 2)

            index += 1

        # reset material buttons
        # lock optimization buttons and knobs
        # set material buttons mode to switch
        # animate emosensemeter...

    def SetupMimo(self):
        mimo.set_led_brightness(150)
        mimo.set_buttons_enable_status(True, False)
        mimo.set_independent_lights(False, True)
        mimo.set_material_buttons_mode([0,0, 1,0, 2,0, 3,0, 4,0, 5,0, 6,0, 7,0])
        mimo.set_material_buttons_active_status([0,0, 1,0, 2,0, 3,0, 4,0, 5,0, 6,0, 7,0])

    def SetupLayout(self):
        # Poner a sonar una rola
        utils.play_music(self.MX[(int(random() * 10))], -1, 0.1, 0.6)

        # El marco para la información
        self.info_frame = utils.Sprite(
            constants.SPRITES_EDITION + 'current_news-frame.png',
            constants.VIEWPORT_CENTER_X,
            182
        )

        # El icono del hecho
        self.icon = utils.Sprite(
            constants.EVENTS + self.current_event['ico']
        )
        self.icon.Scale([0.75, 0.75])
        self.icon.SetPosition(146, 183)

        # El título del hecho y el objetivo a alcanzar con la noticia
        self.fact_title = utils.Text(
            ('fact' if constants.language == 'en' else 'hecho') +
                ': ' + self.current_event['ovw'][constants.language] +
                '\n\n' +
                ('goal' if constants.language == 'en' else 'objetivo') +
                ': ' + self.current_event['gol'][constants.language],
            self.normal_font,
            color = constants.PALETTE_TITLES_DARK_BLUE
        )
        self.fact_title.setAnchor(0, 0)
        self.fact_title.SetPosition(274, 84)

        # TODO: reemplazar esto por un número o una barra que muestre el impacto que está generando la edición
        # El sesgo generado
        default_text = 'no opinion bias set yet. select material to start framing the news.'
        if constants.language == 'es':
            default_text = 'seleccione material para generar una opinión'
        self.news_framing = utils.Text(
            default_text,
            self.normal_font,
            color = constants.PALLETE_KING_BLUE
        )
        self.news_framing.setAnchor(0, 0)
        self.news_framing.SetPosition(274, 218)

        # El fondo para la trama
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

        story_layout = {
            '1': {
                'en': ['hook', 170],
                'es': ['gancho', 170]
            },
            '2': {
                'en': ['plot', constants.VIEWPORT_CENTER_X],
                'es': ['argumento', constants.VIEWPORT_CENTER_X]
            },
            '3': {
                'en': ['conclusion', 1110],
                'es': ['conclusión', 1110]
            }
        }
        self.news_hook = utils.Text(
            story_layout['1'][constants.language][0],
            self.subtitle_font,
            color = constants.PALLETE_BACKGROUND_BLUE
        )   
        self.news_hook.SetPosition(story_layout['1'][constants.language][1], 605)

        self.news_conflict = utils.Text(
            story_layout['2'][constants.language][0],
            self.subtitle_font,
            color = constants.PALLETE_BACKGROUND_BLUE
        )
        self.news_conflict.SetPosition(story_layout['2'][constants.language][1], 605)

        self.news_conclusion = utils.Text(
            story_layout['3'][constants.language][0],
            self.subtitle_font,
            color = constants.PALLETE_BACKGROUND_BLUE
        )
        self.news_conclusion.SetPosition(story_layout['3'][constants.language][1], 605)

        #--- aca voy
        self.popupLabel = utils.Text('popup', self.subtitle_font)
        self.popupLabel.setAnchor(0.5, 0)
        self.popupLabel.SetPosition(640, 120)

        # add da ui
        finish_edition_layout = {
            'text': {
                'en': 'press    to finish edition',
                'es': 'presiona    para terminar de editar'
            },
            'icon': {
                'en': 853,
                'es': 704
            }
        }
        self.SetupUI()
        self.render_right_progress = False
        self.right_progress_label.SetText(finish_edition_layout['text'][constants.language])
        self.right_progress_icon.SetPosition(
            finish_edition_layout['icon'][constants.language],
            645
        )

    def SetupPopupLayout(self):
        self.available_minigames = get_next_pair()
        self.popup_background = utils.Sprite(
            constants.SPRITES_EDITION + 'minigames-popup.png',
            constants.VIEWPORT_CENTER_X,
            351
        )

        self.popup_title = utils.Text(
            self.current_event['hdl'][constants.language],
            self.subtitle_font,
            color = constants.PALLETE_BACKGROUND_BLUE
        )
        self.popup_title.setAnchor(0.5, 0)
        self.popup_title.SetPosition(constants.VIEWPORT_CENTER_X, 100)

        self.popup_framing = utils.Text(
            self.current_frame,
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
            minigame_data_a["title"][constants.language],
            self.subtitle_font,
            336,
            480,
            color= constants.PALETTE_TITLES_DARK_BLUE
        )
        self.description_minigame_a = utils.Text(
            minigame_data_a["pitch"][constants.language],
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
            minigame_data_b["title"][constants.language],
            self.subtitle_font,
            937,
            480,
            color= constants.PALETTE_TITLES_DARK_BLUE
        )

        self.description_minigame_b = utils.Text(
            minigame_data_b["pitch"][constants.language],
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
                    self.UI_SwitchScene.play()
                    self.OpenPopup()
                elif self.popupActive:
                    if self.showing_minigame_tutorial:
                        self.UI_SwitchScene.play()
                        self.PlayMinigame(self.selected_minigame)
                    else:
                        self.UI_SwitchScene.play()
                        self.ShowMinigame(constants.MINIGAME_RIGHT)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                if self.popupActive:
                    self.UI_SwitchScene.play()
                    self.ShowMinigame(constants.MINIGAME_LEFT)

    def Update(self, dt):
        SceneBase.Update(self, dt)
        if self.showing_minigame_tutorial:
            self.minigame_preview.updateFrame(dt)

            ring.fill_percentage(self.percentage)

    def RenderBody(self, screen):
        if self.popupActive:
            self.RenderPopup(screen)
            return

        self.info_frame.RenderWithAlpha(screen)
        self.icon.RenderWithAlpha(screen)

        # render texts
        self.fact_title.render_multiline_truncated( screen, 954 )

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

        self.news_framing.render_multiline_truncated( screen, 954 )

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
                self.update_affections(slot_index, index, False)
                break
            elif slot == -1 and self.material[index]:
                self.sequence[slot_index] = index
                self.set_material_active(index, slot_index)
                self.busy_slots += 1
                self.update_affections(slot_index, index)
                break
            slot_index += 1

        self.can_optimize = self.busy_slots == 4

        mimo.set_material_buttons_light([6, 0xf7, 0x5a, 0xff])
        mimo.set_material_buttons_active_status([6, int(self.can_optimize)])
        # if busy_slots>4 should lock the unselected buttons

    def update_affections(self, slot_index, index, sum = True):
        right_mtl = False

        if 'target' in self.event_mtl[index]:
            right_mtl = True

        val = self.mtl_switcher.get(slot_index)(right_mtl, self.event_mtl[index])
        self.impact += val if sum else -val

        self.news_framing.SetText('Impacto: %d' % self.impact)

    def set_material_active(self, index, slot_index):
        self.UI_MatSel[int(random()*3)].play()
        material = self.current_event['material'][index]
        mimo.set_material_leds_color([24+slot_index]+material['color'])
        line1_text = utils.align_text(material['label'][constants.language][0], index < 3, 16, '*')
        line2_text = utils.align_text(material['label'][constants.language][1], index < 3, 16, '*')
        mimo.lcd_display_at(index, line1_text, 1)
        mimo.lcd_display_at(index, line2_text, 2)

    def set_material_inactive(self, index, slot_index):
        material = self.current_event['material'][index]
        mimo.set_material_leds_color([24+slot_index, 0,0,0])
        line1_text = utils.align_text(
            material['label'][constants.language][0],
            index < 3,
            16,
            '-'
        )
        line2_text = utils.align_text(
            material['label'][constants.language][1],
            index < 3,
            16,
            '-'
        )
        mimo.lcd_display_at(index, line1_text, 1)
        mimo.lcd_display_at(index, line2_text, 2)

    def OpenPopup(self):
        self.SetupPopupLayout()
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
        right_label_layout = {
            'text': {
                'en': 'press    to ',
                'es': 'presiona    para '
            },
            'pos': {
                'en': 907,
                'es': 969
            }
        }
        self.right_progress_label.SetText(
            right_label_layout['text'][constants.language] + self.available_minigames[1]["title"][constants.language]
        )
        self.right_progress_label.setAnchor(0, 0.5)
        self.right_progress_label.SetPosition(760, 675)
        self.right_progress_icon.setAnchor(0.5, 0.5)
        self.right_progress_icon.SetPosition(
            right_label_layout['pos'][constants.language],
            675
        )

        random_color = (
            int(random() * 255),
            int(random() * 255),
            int(random() * 255)
        )
        left_label_layout = {
            'text': {
                'en': 'press    to ',
                'es': 'presiona    para '
            },
            'pos': {
                'en': [170, 316],
                'es': [80, 290]
            }
        }
        self.left_progress_label.SetText(
            left_label_layout['text'][constants.language] + self.available_minigames[0]["title"][constants.language]
        )
        self.left_progress_label.setAnchor(0, 0.5)
        self.left_progress_label.SetPosition(
            left_label_layout['pos'][constants.language][0],
            675
        )
        self.left_progress_icon.setAnchor(0.5, 0.5)
        self.left_progress_icon.SetPosition(
            left_label_layout['pos'][constants.language][1],
            675
        )
        self.render_right_progress = True
        
        mimo.set_material_buttons_light([7, 0x8b, 0x27, 0xff, 6, 0xf7, 0x5a, 0xff])
        mimo.set_material_buttons_active_status([6,1, 7,1])


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
            self.minigame_preview.RenderFrame(screen)

    # load images for minigames
    def ShowMinigame(self, side):
        # TODO: load the specific mini-game info. based on the chosen side
        self.showing_minigame_tutorial = True
        selected_minigame = self.available_minigames[side]
        self.selected_minigame = selected_minigame["scene"]

        minigame_color = self.left_progress_label.color \
            if side == constants.MINIGAME_LEFT else self.right_progress_label.color

        self.minigame_title = utils.Text(
            selected_minigame["title"][constants.language],
            self.subtitle_font,
            color = constants.PALETTE_TITLES_DARK_BLUE
        )
        self.minigame_title.setAnchor(0, 0)
        self.minigame_title.SetPosition(310, 240)

        self.minigame_optimization_sub = utils.Text(
            'optimization' if constants.language == 'en' else 'optimización',
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
            selected_minigame["description"][constants.language],
            self.normal_font,
            310,
            300,
            color= constants.PALETTE_TITLES_DARK_BLUE
        )
        self.minigame_desc.setAnchor(0,0)


        self.minigame_goal_label = utils.Text(
            'goal:' if constants.language == 'en' else 'objetivo:',
            self.subtitle_font,
            300,
            450,
            color= constants.PALETTE_TITLES_DARK_BLUE
        )
        self.minigame_goal_label.setAnchor(1,0)
        self.minigame_goal = utils.Text(
            selected_minigame["goal"][constants.language],
            self.normal_font,
            310,
            450,
            color= constants.PALETTE_TITLES_DARK_BLUE
        )
        self.minigame_goal.setAnchor(0,0)

        self.minigame_preview = utils.Sprite(
            'assets/minigame_icons/'+selected_minigame["preview"],
            selected_minigame["preview_x"],
            selected_minigame["preview_y"]
        )
        self.minigame_preview.frameDelay = selected_minigame["preview_rate"]
        self.minigame_preview.frameWidth = selected_minigame["preview_width"]
        self.minigame_preview.frameHeight = selected_minigame["preview_height"]
        self.minigame_preview.animationFrames = selected_minigame["preview_frames"]
        self.minigame_preview.setAnchor(0,0)

        self.percentage = 0

        start_label = {
            'title': {
                'en': 'press    to start',
                'es': 'presiona    para empezar'
            },
            'pos': {
                'en': 907,
                'es': 968
            }
        }
        self.right_progress_label.SetColor(minigame_color)
        self.right_progress_label.SetText(start_label['title'][constants.language])
        self.right_progress_icon.SetPosition(
            start_label['pos'][constants.language],
            675
        )

        self.render_left_progress = False

        mimo.set_material_buttons_active_status([6,1, 7,0])

    def PlayMinigame(self, name):
        print(name)
        self.CloseEvent(1.1)
        self.AddTween("easeInSine", 1.1, self, "percentage", 0, 1.1, 0)
        self.AddTrigger(1.2, self, 'SwitchToScene', name)