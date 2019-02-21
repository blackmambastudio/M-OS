#!/usr/bin/env python
import pygame

from scenes.BaseScene import SceneBase
from utils import utils
from random import random

class FocusScene(SceneBase):
    def __init__(self):
        SceneBase.__init__(self)
        self.pieces = []
        self.background = utils.Sprite('assets/sprites/tv_control_room.png', 1280/2, 720/2)
        self.pieces.append(utils.Sprite('assets/sprites/tv_control_room-pieceA-1.png', 224, 246))
        self.pieces.append(utils.Sprite('assets/sprites/tv_control_room-pieceB-1.png', 640, 246))
        self.pieces.append(utils.Sprite('assets/sprites/tv_control_room-pieceC-1.png', 1056, 246))
        self.pieces.append(utils.Sprite('assets/sprites/tv_control_room-pieceD-1.png', 432, 496))
        self.pieces.append(utils.Sprite('assets/sprites/tv_control_room-pieceE-1.png', 848, 496))

        self.customRotation = 0
        self.correct_pieces = 0

        for piece in self.pieces:
            rotation = int(random()*4)
            piece.Rotate(rotation*90)
            if rotation == 0:
                self.correct_pieces += 1

        self.locked_pieces = [False, False, False, False, False]

        # sfx and audio
        audio_path = 'assets/audio/SFX/Focus/'
        self.ui_turn = utils.get_sound(audio_path + 'UI_Turn.ogg')
        self.ui_turn.set_volume(0.5)

        self.ui_pos = []
        self.ui_pos.append(utils.get_sound(audio_path + 'UI_Pos_01.ogg'))
        self.ui_pos.append(utils.get_sound(audio_path + 'UI_Pos_02.ogg'))
        self.ui_pos.append(utils.get_sound(audio_path + 'UI_Pos_03.ogg'))
        self.ui_pos.append(utils.get_sound(audio_path + 'UI_Pos_04.ogg'))
        self.ui_pos.append(utils.get_sound(audio_path + 'UI_Pos_05.ogg'))

        self.sfx_pieces = []
        self.sfx_pieces.append(utils.get_sound(audio_path + 'SFX_A.ogg'))
        self.sfx_pieces.append(utils.get_sound(audio_path + 'SFX_B.ogg'))
        self.sfx_pieces.append(utils.get_sound(audio_path + 'SFX_C.ogg'))
        self.sfx_pieces.append(utils.get_sound(audio_path + 'SFX_D.ogg'))
        self.sfx_pieces.append(utils.get_sound(audio_path + 'SFX_E.ogg'))

        # base loop
        utils.play_music(audio_path + 'SFX_BasicLoop.ogg', -1, 0.1)



    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d and not self.locked_pieces[0]:
                print("d pressed")
                self.SpinPiece(0)
            
            if event.type == pygame.KEYUP and event.key == pygame.K_d:
                print("d released")
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f and not self.locked_pieces[1]:
                print("f pressed")
                self.SpinPiece(1)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_g and not self.locked_pieces[2]:
                print("g pressed")
                self.SpinPiece(2)
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c and not self.locked_pieces[3]:
                print("c pressed")
                self.SpinPiece(3)
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_v and not self.locked_pieces[4]:
                print("x pressed")
                self.SpinPiece(4)


    def Update(self, dt):
        SceneBase.Update(self, dt)

        self.background.opacity = (0.5 + self.correct_pieces*0.1)*255

        for index, locked in enumerate(self.locked_pieces):
            if locked:
                piece = self.pieces[index]
                piece.Rotate(piece.rotation)

    
    def Render(self, screen):
        screen.fill((0x1B, 0x0C, 0x43))
        self.background.RenderWithAlpha(screen)
        for piece in self.pieces:
            piece.RenderWithAlpha(screen)


    def SpinPiece(self, index):
        piece = self.pieces[index]
        self.ui_turn.play()
        self.AddTween('easeOutCubic', 0.5, piece, 'rotation', piece.rotation, piece.rotation+90, 0)
        self.locked_pieces[index] = True
        self.AddTrigger(0.5, self, 'UnlockPiece', index)
        if piece.rotation%360 == 0: # dont fix this
            self.sfx_pieces[index].fadeout(500) # in milliseconds
            self.correct_pieces -= 1


    def UnlockPiece(self, index):
        self.locked_pieces[index] = False
        self.pieces[index].Rotate(round(self.pieces[index].rotation))
        if self.pieces[index].rotation == 0:
            self.ui_pos[index].play()
            self.sfx_pieces[index].play(-1)
            self.correct_pieces += 1
        
        if self.correct_pieces == 5:
            print("you win!")

