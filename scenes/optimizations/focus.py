#!/usr/bin/env python
import pygame

from .OptimizationScene import OptimizationScene
from utils import utils
from random import random

class FocusScene(OptimizationScene):
    def __init__(self):
        OptimizationScene.__init__(self)
        self.pieces = []
        self.rendering_order = [0,1,2,3,4]
        self.render_background = True
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
        if not self.IsPlaying(): return
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
        OptimizationScene.Update(self, dt)
        self.background.opacity = (0.5 + self.correct_pieces*0.1)*255
        
        self.dirty_rects = [(50,20,40,40), (490, 10, 300, 50)]
        for index, locked in enumerate(self.locked_pieces):
            if locked:
                piece = self.pieces[index]
                piece.Rotate(piece.rotation)
                self.dirty_rects.append(piece.GetClipRect())
                
        if self.render_background:
            self.dirty_rects = [(0,0,1280,720)]
            self.render_background = False

    def RenderBackground(self, screen):
        for rect in self.dirty_rects:        
            screen.fill((0x1B, 0x0C, 0x43), rect)
            self.background.RenderWithAlpha(screen, rect, rect)
    
    def Render(self, screen):
        OptimizationScene.Render(self, screen)
        for index in self.rendering_order:
            self.pieces[index].RenderWithAlpha(screen)


    def SpinPiece(self, index):
        piece = self.pieces[index]
        self.ui_turn.play()
        self.AddTween('easeOutCubic', 0.5, piece, 'rotation', piece.rotation, piece.rotation+90, 0)
        self.locked_pieces[index] = True
        self.AddTrigger(0.5, self, 'UnlockPiece', index)
        if piece.rotation%360 == 0: # dont fix this
            self.sfx_pieces[index].fadeout(500) # in milliseconds
            self.correct_pieces -= 1

        self.rendering_order.remove(index)
        self.rendering_order.append(index)


    def UnlockPiece(self, index):
        self.render_background = True
        self.locked_pieces[index] = False
        self.pieces[index].Rotate(round(self.pieces[index].rotation))
        if self.pieces[index].rotation == 0:
            self.ui_pos[index].play()
            self.sfx_pieces[index].play(-1)
            self.correct_pieces += 1
        
        if self.correct_pieces == 5:
            print("you win!")
            self.FinishOptimization()


    def FinishOptimization(self):
        OptimizationScene.FinishOptimization(self)

        for index in range(0, 5):
            self.sfx_pieces[index].fadeout(500)
            
        utils.stop_music()

