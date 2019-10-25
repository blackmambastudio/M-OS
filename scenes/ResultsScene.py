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
        self.title = utils.Text(
            "Consecuencias",
            titlefont,
            color = constants.PALETTE_TEXT_RED
        )
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

        # obtener las consecuencias con base al puntaje obtenido por el jugador
        session_consequences = []
        consequences = {
            'bad': {
                'en': [],
                'es': [
                    'Continúan las protestas en la sede de gobierno.',
                    'El fuego continúa alimentándose de hectáreas de bosque diariamente.',
                    'Telmar sufre enorme pérdida arqueológica.',
                    'Gobierno invita a los ciudadanos a no preocuparse por la situación.'
                ]
            },
            'good': {
                'en': [],
                'es': [
                    'La sociedad rechaza sistemáticamente a la población nativa.',
                    'El impacto al ecosistema es irreparable.',
                    'Gobierno muestra pruebas de las ayudas que se han brindado a los nativos.',
                    'Los nativos son desplazados y viven en condiciones precarias.'
                ]
            },
            'excellent': {
                'en': [],
                'es': [
                    'La tribu Kayoc es culpada de los recientes actos delictivos en la ciudad.',
                    'Corporacion se compromete a recuperar el espacio del bosque.',
                    'Telmar firma TLC tras sorpresivo hallazgo de fuente de hidrocarburos.',
                    'El hogar nativo de la tribu Kayoc fue consumido por las llamas.',
                    'Ciudadanos toman justicia a mano propia contra los nativos.'
                ]
            }
        }
        if constants.score >= 36:
            session_consequences = consequences['excellent'][constants.language]
        elif constants.score >= 24:
            session_consequences = consequences['good'][constants.language]
        else:
            session_consequences = consequences['bad'][constants.language]

        self.LoadConsequences(session_consequences)

    def LoadConsequences(self, lines):
        consequenceFont = pygame.font.Font(
            "assets/fonts/VCR_OSD_MONO_1.001.ttf",
            constants.FONT_NORMAL
        )
        index = 0
        for line in lines:
            consequence = utils.Text(
                '* ' + line,
                consequenceFont,
                color = constants.PALETTE_TEXT_CYAN
            )
            consequence.SetPosition(32, 250 + index * 40)
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
        screen.fill(constants.PALETTE_TEXT_BLACK)
        self.title.RenderWithAlpha(screen)
        for consequence in self.consequences:
            consequence.RenderWithAlpha(screen)
