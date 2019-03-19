#!/usr/bin/env python3
import pygame

from .OptimizationScene import OptimizationScene, STATUS
from utils import utils, constants
from utils import neopixelmatrix as graphics
from random import random, shuffle
import mimo
import pygame

class ScanningScene(OptimizationScene):
    def __init__(self):
        self.minigametitle = 'scanner.opt'
        OptimizationScene.__init__(self)
        
        self.coldown = 0
        
        self.index = 8
        self.line_color = 0xf0f
        self.playing = False
        self.direction = 1
        self.mode = 1
        self.speed = 0.02
        self.level = 0
        self.displayed_figure_index = -1
        self.fails = 0
        self.detected_contact = False
        self.countdown = 45000
        self.current_time = 45000
        
        self.colors = [
            [0x00, 0x5f, 0xff], #blue 
            [0x27, 0xff, 0x93], #green
            [0xf7, 0x5a, 0xff], #pink
            [0x8b, 0x27, 0xff], #purple
            [0xea, 0xe1, 0xf3]  #white
        ]
        led_lights = []
        index = 0
        for color in self.colors:
            led_lights += [index] + color
            index += 1
        mimo.set_optimization_leds_color(led_lights)

        self.radar_matrix = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
        ]

        # load assets
        self.piece_sprites = []
        self.piece_sprites.append(utils.Sprite(constants.SPRITES_SCANNING + 'piece_blue.png', 0, 0))
        self.piece_sprites.append(utils.Sprite(constants.SPRITES_SCANNING + 'piece_green.png', 0, 0))
        self.piece_sprites.append(utils.Sprite(constants.SPRITES_SCANNING + 'piece_pink.png', 0, 0))
        self.piece_sprites.append(utils.Sprite(constants.SPRITES_SCANNING + 'piece_purple.png', 0, 0))
        self.piece_sprites.append(utils.Sprite(constants.SPRITES_SCANNING + 'piece_white.png', 0, 0))
        index = 0
            
        # sfx and audio
        audio_path = 'assets/audio/SFX/Scanning/'
        self.MG1_ObjSort = utils.get_sound(audio_path + 'MG1_ObjSort.ogg')
        self.MG1_ObjSort.set_volume(0.08)

        audio_path = 'assets/audio/SFX/Scanning/'
        self.MG1_Sweep = utils.get_sound(audio_path + 'MG1_Sweep.ogg')
        self.MG1_Sweep.set_volume(0.6)

        audio_path = 'assets/audio/SFX/Scanning/'
        self.MG1_Success = utils.get_sound(audio_path + 'MG1_Success.ogg')
        self.MG1_Success.set_volume(1)

        audio_path = 'assets/audio/SFX/Scanning/'
        self.MG1_Failed = utils.get_sound(audio_path + 'MG1_Failed.ogg')
        self.MG1_Failed.set_volume(1)

        self.NextFigure()

    def SetupMimo(self):
        mimo.set_led_brightness(150)
        mimo.set_tunners_enable_status(True)
        mimo.set_independent_lights(False, True)
        mimo.set_buttons_enable_status(False, True)
        mimo.set_optimization_buttons_mode([0,1, 1,1, 2,1, 3,1, 4,1])
        mimo.set_optimization_buttons_active_status([0,0, 1,0, 2,0, 3,0, 4,0, 5,0])


        
    def ProcessInputOpt(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                self.GuessFigure(0)
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                self.GuessFigure(2)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                self.GuessFigure(4)
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                self.GuessFigure(1)
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
                self.GuessFigure(3)


    def Update(self, dt):
        OptimizationScene.Update(self, dt)
        if not self.playing: return
        
        self.coldown += dt
        if self.coldown > self.speed:
            self.coldown = 0
            self.UpdateLineMov()

    def UpdateLineMov(self):
        self.index += self.direction
        if self.index < -8:
            self.playing = False
        elif self.index > 15:
            self.playing = False

        

    def RenderBody(self, screen):
        index = 0
        for figure in FIGURES[self.level]:
            self.DrawFigure(screen, figure, index)
            index += 1

        if self.playing == False: return
        self.draw_color_line(0xfff&self.line_color, self.index)
        self.draw_color_line(0xddd&self.line_color, self.index-self.direction)
        self.draw_color_line(0xbbb&self.line_color, self.index-self.direction*2)
        self.draw_color_line(0x999&self.line_color, self.index-self.direction*3)
        self.draw_color_line(0x777&self.line_color, self.index-self.direction*4)
        self.draw_color_line(0x555&self.line_color, self.index-self.direction*5)
        self.draw_color_line(0x333&self.line_color, self.index-self.direction*6)
        self.draw_color_line(0x111&self.line_color, self.index-self.direction*7)
        
        graphics.setColor(0)
        for j in range(0, 8):
            lock = False
            y = j
            for i in range(0, 8):
                x = i
                if self.mode == 2:
                    y = i
                    x = j
                    if self.direction == -1:
                        y = 7-y
                elif self.direction == -1:
                    x = 7-x

                if self.radar_matrix[y][x]==1 or lock:
                    lock = True
                    if not self.detected_contact and graphics._buffer[y][x] !=0:
                        self.Lock()
                    graphics.plot(x, y)

        graphics.render()
        

    def Lock(self):
        if self.detected_contact: return
        self.detected_contact = True
        print("detected collision")

    def draw_color_line(self, color, idx):
        if idx < 0 or idx > 7: return
        graphics.setColor(color)
        if self.mode == 1:
            graphics.plotLine(idx, 0, idx, 7)
        elif self.mode == 2:
            graphics.plotLine(0, idx, 7, idx)


    def DrawFigure(self, screen, figure, index):
        for j in range(0, len(figure)):
            for i in range(0, len(figure[0])):
                if figure[j][i] == 1:
                    self.piece_sprites[index].Render(screen, (150+220*(index)+i*40, 350+j*40))


    def NewScan(self, mode, direction):
        self.MG1_Sweep.play()
        self.line_color = [0xf00, 0xff0, 0x0f0, 0x0ff, 0x00f, 0xf0f, 0xfff][int(random()*7)]
        self.mode = mode
        self.direction = int(direction)
        if self.direction == 1:
            self.index = -1
        else:
            self.index = 8
            
        self.playing = True
        self.detected_contact = False


    def SwipeHorizontal(self, distance):
        if self.state == STATUS.FINISHING: return
        if self.playing or abs(distance)>10: return
        self.speed = 0.02
        self.NewScan(1, distance/abs(distance))

    def SwipeVertical(self, distance):
        if self.state == STATUS.FINISHING: return
        if self.playing or abs(distance)>10: return
        self.speed = 0.02
        self.NewScan(2, distance/abs(distance))

    def NextFigure(self):
        self.radar_matrix = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
        ]
        shuffle(FIGURES[self.level])
        self.displayed_figure_index = int(random()*len(FIGURES[self.level]))
        self.figure = FIGURES[self.level][self.displayed_figure_index]
        x = 1 + int(random()*(6-len(self.figure[0])))
        y = 1+ int(random()*(6-len(self.figure[0])))
        for j in range(0,len(self.figure)):
            for i in range(0, len(self.figure[0])):
                self.radar_matrix[j+y][i+x] = self.figure[j][i]

        self.MG1_ObjSort.play()
        # display options in screen 


    def GuessFigure(self, index):
        if index == self.displayed_figure_index:
            self.level += 1
            self.MG1_Success.play()
        else:
            self.fails += 1
            self.MG1_Failed.play()
            if self.fails >= 3:
                self.score = self.level/5
                self.FinishOptimization()
        if self.level >= len(FIGURES):
            self.level -= 1
            self.score = self.level/5
            self.FinishOptimization()
        else:
            self.NextFigure()

FIGURES = [
    # first level
    [[
        [0,1,0],
        [1,1,1]
    ],[
        [0,1],
        [1,1],
        [0,1]
    ],[
        [1,0],
        [1,1],
        [1,0]
    ],[
        [1,1,1],
        [0,1,0]
    ],[
        [1,0,0],
        [1,1,1]
    ]],
    # second level
    [[
        [0,1,0],
        [1,1,1]
    ],[
        [0,1,1],
        [1,1,0]
    ],[
        [1,1,0],
        [0,1,1]
    ],[
        [0,1,1],
        [0,1,1]
    ],[
        [0,0,1],
        [1,1,1]
    ]],
    # third level
    [[
        [0,1,0],
        [1,1,1],
        [0,1,0]
    ],[
        [1,1,0],
        [0,1,0],
        [0,1,1]
    ],[
        [1,1,1],
        [0,1,0],
        [0,1,0]
    ],[
        [1,1,1],
        [1,0,0],
        [1,0,0]
    ],[
        [1,1,0],
        [1,0,0],
        [1,1,0]
    ]],
    # third level
    [[
        [0,0,0,0],
        [1,0,0,1],
        [1,1,1,1]
    ],[
        [0,1,1,0],
        [0,1,1,1],
        [0,0,1,0]
    ],[
        [0,1,0,0],
        [1,1,1,1],
        [0,0,1,0]
    ],[
        [0,0,0,1],
        [1,1,1,1],
        [0,0,0,1]
    ],[
        [0,0,1,1],
        [0,1,1,1],
        [0,0,0,1]
    ]]
]