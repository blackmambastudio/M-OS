#!/usr/bin/env python

import pygame
import mimo

from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
from utils import constants

from scenes.BaseScene import SceneBase

# Introduction Scene
# Available actions: back / next
# Description: "cinematic explain the player the ludovic experiment"
# Next: material section tutorial


class IntroductionScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.HWSetup()

        subtitlefont = pygame.font.Font(constants.VCR_OSD_MONO, constants.FONT_SUBTITLE)
        self.subtitle = utils.Text("", subtitlefont)
        self.subtitle.SetPosition(constants.VIEWPORT_CENTER_X, 610)

        self.intro_subtitles = [
            {
                "text": "M corp le da la bienvenida y agradece su participacion\nen esta prueba de seleccion.",
                "image": ""
            },
            {
                "text": "Esta prueba evaluara su capacidad para editar y presentar\nnoticias segun las necesidades propuestas por las directivas.",
                "image": ""
            },
            {
                "text": "Ante usted tiene la mas reciente version de nuestro modulador\n de mentes, M.i.M.o 3.2.\n\nRecibira una induccion basica y suficiente para operar esta maquina.",
                "image": ""
            },
            {
                "text": "Toda la operacion que haga sobre la maquina sera grabada\ny almacenada para nuestro posterior analisis.",
                "image": ""
            },
        ]
        self.intro_subtitles_index = -1
        self.textLoader = None
        self.LoadNextSubtitle()


    def HWSetup(self):
        mimo.set_led_brightness(50)
        mimo.set_material_buttons_light([3, 255, 80, 80, 4, 80, 255, 80])
        mimo.set_material_buttons_mode([3, 1, 4, 1])
        mimo.set_material_buttons_lock_status([0,1, 1,1, 2,1, 5,1, 6,1, 7,1])
        mimo.set_tunners_enable_status(False)
        mimo.set_buttons_enable_status(True, False)
    

    def LoadNextSubtitle(self):
        if self.intro_subtitles_index + 1 == len(self.intro_subtitles):
            self.SwitchToScene("TutorialMat")
            return

        self.intro_subtitles_index += 1
        self.textLoader = utils.TextLoader(self.intro_subtitles[self.intro_subtitles_index]["text"], 0.04, False)

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                self.Next()
    
    def Next(self):
        if self.textLoader.finished:
            self.LoadNextSubtitle()
        else: 
            self.textLoader.complete()
            self.subtitle.SetText(self.textLoader.current_text)


    def Update(self, dt):
        SceneBase.Update(self, dt)
        if self.textLoader.update(dt):
            self.subtitle.SetText(self.textLoader.current_text)

    
    def Render(self, screen):
        screen.fill(constants.PALLETE_BACKGROUND_BLUE)
        self.subtitle.render_multiline(screen)
        graphics.render()

