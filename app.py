#!/usr/bin/env python

import os
import sys
import time
import serial
import pygame

from scenes.BootScene import BootScene

from scenes.intro.IntroductionScene import IntroductionScene
from scenes.intro.MaterialTutorialScene import MaterialTutorialScene
from scenes.intro.OptimizationTutorialScene import OptimizationTutorialScene

from scenes.edition.BeginEventScene import BeginEventScene
from scenes.edition.EditEventScene import EditEventScene
from scenes.optimizations.OptimizationScene import OptimizationScene
from scenes.edition.FinishEventScene import FinishEventScene
from scenes.ResultsScene import ResultsScene

from scenes.optimizations.focus import FocusScene

from scenes.test.DevTestScene import DevTestScene

import mimo

SCENES = {
    # boot
    "Boot": BootScene,
    # intro scenes
    "Intro": IntroductionScene,
    "TutorialMat": MaterialTutorialScene,
    "TutorialOpt": OptimizationTutorialScene,
    # edit
    "Begin": BeginEventScene,
    "Edit": EditEventScene,
    "Finish": FinishEventScene,
    # optimization
    "Optimization": OptimizationScene,
    "Focus": FocusScene,

    # end game, results
    "Results": ResultsScene,

    # dev test
    "Test": DevTestScene
}

init_scene = "Boot"
using_emulator = False


def run_game(width, height, fps, starting_scene):
    pygame.mixer.init(frequency=48000, size=-16, channels=2, buffer=4096)
    pygame.init()
    pygame.mouse.set_visible(True)
    pygame.mouse.set_pos([1280/2, 720/2])
    screen = pygame.display.set_mode((width, height), 0 , 16)
    clock = pygame.time.Clock()

    active_scene = starting_scene()

    last_time = time.time()

    font = pygame.font.Font("assets/fonts/VCR_OSD_MONO_1.001.ttf", 22)

    while active_scene != None:
        current_time = time.time()
        dt = current_time - last_time
        last_time = current_time

        mimo.update()
        pressed_keys = pygame.key.get_pressed()
        
        # Event filtering 
        filtered_events = []
        for event in pygame.event.get():
            quit_attempt = False
            if event.type == pygame.QUIT:
                quit_attempt = True
            elif event.type == pygame.KEYDOWN:
                alt_pressed = pressed_keys[pygame.K_LALT] or \
                              pressed_keys[pygame.K_RALT]
                if event.key == pygame.K_ESCAPE:
                    quit_attempt = True
                elif event.key == pygame.K_F4 and alt_pressed:
                    quit_attempt = True
            
            if quit_attempt:
                active_scene.Terminate()
            else:
                filtered_events.append(event)
        
        if active_scene:
            active_scene.ProcessInput(filtered_events, pressed_keys)
            active_scene.Update(dt)
            active_scene.Render(screen)
            
            dirty_rects = active_scene.getDirtyRects()
            #fps display active
            fps_text = font.render(str(int(clock.get_fps())), True, pygame.Color('red'))
            screen.blit(fps_text, (50, 20))
            dirty_rects.append((50, 20, 20,20))
            pygame.display.update(dirty_rects)
        
        active_scene = active_scene.next


        clock.tick(fps)

    mimo.shutdown()


if __name__ == '__main__':
    if len(sys.argv)==2:
        using_emulator = sys.argv[1] == "True"
    if len(sys.argv)==3:
        using_emulator = sys.argv[1] == "True"
        init_scene = sys.argv[2]

    mimo.init(emulation=using_emulator)
    if mimo.EMULATOR:
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (641, 50)
    run_game(1280, 720, 60, SCENES[init_scene])
