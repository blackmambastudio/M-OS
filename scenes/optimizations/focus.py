#!/usr/bin/env python3
import pygame

from .OptimizationScene import OptimizationScene
from utils import utils
from random import random
from utils import constants
import mimo

class FocusScene(OptimizationScene):
    def __init__(self):
        self.minigametitle = 'focus.opt'
        OptimizationScene.__init__(self)
        self.pieces = []
        self.rendering_order = [0,1,2,3,4]
        self.render_background = True
        self.background = utils.Sprite(
            constants.SPRITES_FOCUS + 'focus-background.png', 
            1280/2,
            720/2
        )
        self.pieces.append(
            utils.Sprite(constants.SPRITES_FOCUS + 'focus-pieceA.png', 418, 336)
        )
        self.pieces.append(
            utils.Sprite(constants.SPRITES_FOCUS + 'focus-pieceB.png', 640, 331)
        )
        self.pieces.append(
            utils.Sprite(constants.SPRITES_FOCUS + 'focus-pieceC.png', 859, 336)
        )
        self.pieces.append(
            utils.Sprite(constants.SPRITES_FOCUS + 'focus-pieceD.png', 533, 447)
        )
        self.pieces.append(
            utils.Sprite(constants.SPRITES_FOCUS + 'focus-pieceE.png', 747, 447)
        )

        self.customRotation = 0
        self.correct_pieces = 0
        self.current_time = 20000

        for piece in self.pieces:
            rotation = int(random()*4)
            if rotation == 0:
                rotation += 1
            piece.Rotate(rotation*90)
            if rotation == 0:
                self.correct_pieces += 1

        self.locked_pieces = [False, False, False, False, False]

        # sfx and audio
        audio_path = 'assets/audio/SFX/Focus/'
        self.MG2_Turn = utils.get_sound(audio_path + 'MG2_Turn.ogg')
        self.MG2_Turn.set_volume(0.4)

        self.MG2_Pos = []
        self.MG2_Pos.append(utils.get_sound(audio_path + 'MG2_Pos_01.ogg'))
        self.MG2_Pos.append(utils.get_sound(audio_path + 'MG2_Pos_02.ogg'))
        self.MG2_Pos.append(utils.get_sound(audio_path + 'MG2_Pos_03.ogg'))
        self.MG2_Pos.append(utils.get_sound(audio_path + 'MG2_Pos_04.ogg'))
        self.MG2_Pos.append(utils.get_sound(audio_path + 'MG2_Pos_05.ogg'))

        self.sfx_pieces = []
        self.sfx_pieces.append(utils.get_sound(audio_path + 'MG2_SFX_A.ogg'))
        self.sfx_pieces.append(utils.get_sound(audio_path + 'MG2_SFX_B.ogg'))
        self.sfx_pieces.append(utils.get_sound(audio_path + 'MG2_SFX_C.ogg'))
        self.sfx_pieces.append(utils.get_sound(audio_path + 'MG2_SFX_D.ogg'))
        self.sfx_pieces.append(utils.get_sound(audio_path + 'MG2_SFX_E.ogg'))

        for sfx in self.sfx_pieces:
            sfx.set_volume(0)
            sfx.play(-1)


        self.UI_OptWin = utils.get_sound('assets/audio/SFX/M_OS/UI_OptWin.ogg')
        self.UI_OptWin.set_volume(0.5)

        self.UI_OptFail = utils.get_sound('assets/audio/SFX/M_OS/UI_OptFail.ogg')
        self.UI_OptFail.set_volume(1)


        # base loop
        utils.play_music(audio_path + 'MG2_BasicLoop.ogg', -1, 0.08)

    def SetupMimo(self):
        OptimizationScene.SetupMimo(self)
        mimo.set_buttons_enable_status(False, True)
        mimo.set_independent_lights(True, False)
        mimo.set_optimization_buttons_mode([0,1, 1,1, 2,1, 3,1, 4,1])
        mimo.set_optimization_buttons_active_status([0,0, 1,0, 2,0, 3,0, 4,0, 5,0])


    def ProcessInputOpt(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d and not self.locked_pieces[0]:
                self.SpinPiece(0)
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f and not self.locked_pieces[1]:
                self.SpinPiece(1)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_g and not self.locked_pieces[2]:
                self.SpinPiece(2)
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c and not self.locked_pieces[3]:
                self.SpinPiece(3)
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_v and not self.locked_pieces[4]:
                self.SpinPiece(4)


    def Update(self, dt):
        OptimizationScene.Update(self, dt)
        self.background.opacity = (0.5 + self.correct_pieces*0.1)*255
        
        self.dirty_rects = [(0, 77, 1280, 38), (490, 10, 300, 50)]
        for index, locked in enumerate(self.locked_pieces):
            if locked:
                piece = self.pieces[index]
                piece.Rotate(piece.rotation)
                self.dirty_rects.append(piece.GetClipRect())

        if self.render_background:
            self.dirty_rects = [(0,0,1280,720)]
            self.render_background = False


    def StopTransition(self):
        self.transition_cortain = False
        self.render_background = True


    def RenderBackground(self, screen):
        for rect in self.dirty_rects:
            self.frame.RenderWithAlpha(screen)
            self.title.RenderWithAlpha(screen)
            self.background.RenderWithAlpha(screen, rect, rect)

    def RenderBody(self, screen):
        for index in self.rendering_order:
            self.pieces[index].RenderWithAlpha(screen)

    def SpinPiece(self, index):
        piece = self.pieces[index]
        self.MG2_Turn.play()
        self.AddTween('easeOutCubic', 0.5, piece, 'rotation', piece.rotation, piece.rotation+90, 0, 6)
        self.locked_pieces[index] = True
        self.AddTrigger(0.5, self, 'UnlockPiece', index)
        if piece.rotation%360 == 0: # dont fix this
            self.sfx_pieces[self.correct_pieces-1].set_volume(0) # in milliseconds
            self.correct_pieces -= 1

        self.rendering_order.remove(index)
        self.rendering_order.append(index)

    def UnlockPiece(self, index):
        self.render_background = True
        self.locked_pieces[index] = False
        self.pieces[index].Rotate(round(self.pieces[index].rotation))
        if self.pieces[index].rotation == 0:
            self.MG2_Pos[self.correct_pieces].play()
            self.MG2_Pos[self.correct_pieces].set_volume(0.6)
            #self.sfx_pieces[self.correct_pieces].play(-1)
            self.sfx_pieces[self.correct_pieces].set_volume(0.6)
            self.correct_pieces += 1
            
        
        if self.correct_pieces == 5:
            print("you win!")
            self.FinishOptimization()
            

    def FinishOptimization(self):
        utils.stop_music()
        for sfx in self.sfx_pieces:
            sfx.stop()
        if self.correct_pieces == 5:
            self.UI_OptWin.play()
        else:
             self.UI_OptFail.play()
        self.score = self.correct_pieces/5

        OptimizationScene.FinishOptimization(self)

        for index in range(0, 5):
            self.sfx_pieces[index].fadeout(1500)



    def DisplayResults(self):
        OptimizationScene.DisplayResults(self)
        self.render_background = True