#!/usr/bin/env python

import pygame
import mimo

from utils import utils
from utils import neopixelmatrix as graphics
from utils.NeoSprite import NeoSprite, AnimatedNeoSprite, TextNeoSprite, SpriteFromFrames
from utils import constants

from .BaseScene import SceneBase

# Results Scene
#
# last scene, game over

class ResultsScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.AddTrigger(5, self, 'Terminate')
        titlefont = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 44)
        self.title = utils.Text("Consecuencias", titlefont)
        self.title.SetPosition(1280/2, 100)
        self.UI_EndGame = utils.get_sound('assets/audio/SFX/M_OS/UI_EndGame.ogg')
        self.end_game_played = False
        self.play_ending = False
        
        # these consequences could be loaded from the user tracking system...
        # something that we haven't have already...
        # so after finish the second news the consequences should be calculated and
        # then loaded here. 
        # I suggest no more than 6 consequences... maybe 7 per game. even if could
        # be more too much information could overwhelm the player.
        self.consequences = []

        # self.LoadConsequences([
        #     'Gobierno invita a los ciudadanos a no preocuparse por la situación.',
        #     'El fuego continúa alimentándose de hectáreas de bosque diariamente.',
        #     'El impacto al ecosistema es irreparable.',
        #     'El hogar nativo de la tribu xxx fue consumido por las llamas.',
        #     'Enorme perdida arqueologica.',
        #     'Se firma TLC con Hunuragha.'
        # ])

    def LoadConsequences(self, lines):

        consequenceFont = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", constants.FONT_NORMAL)
        index = 0
        for line in lines:
            consequence = utils.Text('* ' + line, consequenceFont)
            consequence.SetPosition(60, 250 + index*40)
            consequence.setAnchor(0, 0.5)
            consequence.opacity = 0
            self.consequences.append(consequence)
            index += 1

        self.display_consequence_counter = 0
        self.display_consequence_index = 0
        self.play_ending = True
        

    def ProcessInput(self, events, pressed_keys):
        pass

    def Update(self, dt):
        SceneBase.Update(self, dt)
        if self.play_ending:
            self.display_consequence_counter += 5
            self.consequences[self.display_consequence_index].opacity = self.display_consequence_counter
            if self.display_consequence_counter >= 255:
                self.consequences[self.display_consequence_index].opacity = 255
                self.display_consequence_index += 1
                self.display_consequence_counter = 0
                self.play_ending = self.display_consequence_index < len(self.consequences)
    
    def Render(self, screen):
        if not self.end_game_played:
            self.UI_EndGame.play()
            self.end_game_played = True
        screen.fill(constants.PALLETE_BACKGROUND_BLUE)
        self.title.RenderWithAlpha(screen)
        for consequence in self.consequences:
            consequence.RenderWithAlpha(screen)
    

