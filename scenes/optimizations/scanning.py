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
        self.line_color = 0xfff
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
        self.countdown_shadow = 0
        self.guess_mode = 2
        self.guess_direction = 1
        self.guess_color = False
        
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

        self.progress = utils.Text(
            'Nivel 1',
            self.normal_font,
            color = constants.PALETTE_TEXT_CYAN
        )
        self.progress.SetPosition(640, 160)

        # sfx and audio
        audio_path = 'assets/audio/SFX/Scanning/'
        self.MG1_ObjSort = utils.get_sound(audio_path + 'MG1_ObjSort.ogg')
        self.MG1_ObjSort.set_volume(0.6)

        audio_path = 'assets/audio/SFX/Scanning/'
        self.MG1_Sweep = utils.get_sound(audio_path + 'MG1_Sweep.ogg')
        self.MG1_Sweep.set_volume(1.0)

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
        if self.index < -12:
            self.playing = False
            graphics.clear()
            self.detected_contact = False
        elif self.index > 19:
            self.playing = False
            graphics.clear()
            self.detected_contact = False

        self.countdown_shadow -= 1
        

    def RenderBody(self, screen):
        index = 0
        for figure in FIGURES[self.level]:
            self.DrawFigure(screen, figure, index)
            index += 1
        
        if self.detected_contact:
            if self.countdown_shadow <= 0:
                self.display_figure_shadow()

        self.progress.RenderWithAlpha(screen)

        if self.playing == False: return
        self.draw_color_line(0xfff&self.line_color, self.index)
        self.draw_color_line(0xddd&self.line_color, self.index-self.direction)
        self.draw_color_line(0xbbb&self.line_color, self.index-self.direction*2)
        self.draw_color_line(0x999&self.line_color, self.index-self.direction*3)
        self.draw_color_line(0x777&self.line_color, self.index-self.direction*4)
        self.draw_color_line(0x555&self.line_color, self.index-self.direction*5)
        self.draw_color_line(0x333&self.line_color, self.index-self.direction*6)
        self.draw_color_line(0x111&self.line_color, self.index-self.direction*7)
        self.draw_color_line(0x0&self.line_color, self.index-self.direction*8)
        
        if self.guess_color and not self.detected_contact:
            for j in range(0, 8):
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
                    if self.radar_matrix[y][x]==1:
                        self.Lock()
        graphics.render()

    def display_figure_shadow(self):
        color = [0x111, 0x222, 0x333, 0x444, 0xaaa, 0xddd, 0xfff, 0xfff, 0xfff, 0xfff, 0xfff, 0xfff, 0xfff, 0xfff, 0xddd, 0xddd, 0xbbb, 0x999, 0x999, 0x666, 0x666, 0x111, 0x0][-self.countdown_shadow]
        graphics.setColor(color&self.line_color)
        for j in range(0, 8):
            y = j
            for i in range(0, 8):
                x = i
                if self.radar_matrix[y][x] == 1:
                    graphics.plot(x, y)

    def Lock(self):
        if self.detected_contact: return
        self.detected_contact = True
        self.countdown_shadow = 4
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
        self.line_color = 0xfff
        if mode == 1:
            self.line_color = 0xf0f if direction == 1 else 0x0f0
        else:
            self.line_color = 0x0ff if direction == 1 else 0x80f

        self.mode = mode
        self.direction = int(direction)
        if self.direction == 1:
            self.index = -1
        else:
            self.index = 8
            
        self.playing = True
        self.detected_contact = False

        self.guess_color = mode == self.guess_mode and direction == self.guess_direction


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
        x = 4 - int(len(self.figure[0])/2)
        y = 4 - int(len(self.figure)/2)
        for j in range(0,len(self.figure)):
            for i in range(0, len(self.figure[0])):
                self.radar_matrix[j+y][i+x] = self.figure[j][i]

        # f0f pink #2
        # mode 1, direction 1

        # 0f0 green #1
        # mode 1, direction -1

        # 0ff blue #0
        # mode 2, direction 1

        # 80f purple #3
        # mode 2, direction -1

        if self.displayed_figure_index == 0:
            self.guess_mode = 2
            self.guess_direction = 1
        elif self.displayed_figure_index == 1:
            self.guess_mode = 1
            self.guess_direction = -1
        elif self.displayed_figure_index == 2:
            self.guess_mode = 1
            self.guess_direction = 1
        elif self.displayed_figure_index == 3:
            self.guess_mode = 2
            self.guess_direction = -1

        self.MG1_ObjSort.play()
        # display options in screen 


    def GuessFigure(self, index):
        if index == self.displayed_figure_index:
            self.level += 1
            self.MG1_Success.play()
            self.progress.SetText('Nivel {}'.format(self.level + 1))
        else:
            self.fails += 1
            self.MG1_Failed.play()
            self.progress.SetText('Nivel {}'.format(self.level + 1))
            if self.fails >= 10:
                self.score = self.level/5
                self.FinishOptimization()
            return
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