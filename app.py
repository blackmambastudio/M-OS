#!/usr/bin/env python

import os
import sys
import time
import serial
import pygame

from scenes.BootScene import BootScene
from scenes.EditScene import EditScene
from scenes.SubmitScene import SubmitScene
from scenes.OptimizationScene import OptimizationScene
from scenes.ResultsScene import ResultsScene
from scenes.TutorialScene import TutorialScene
from scenes.StartEventScene import StartEventScene

from scenes.optimizations.focus import FocusScene

import mimo

SCENES = {
    "Boot": BootScene,
    "Edit": EditScene,
    "Submit": SubmitScene,
    "Optimization": OptimizationScene,
    "Results": ResultsScene,
    "Tutorial": TutorialScene,
    "Start": StartEventScene,

    "Focus": FocusScene
}

init_scene = "Boot"
using_emulator = False


def run_game(width, height, fps, starting_scene):
    pygame.mixer.init(frequency=48000, size=-16, channels=2, buffer=4096)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    active_scene = starting_scene()

    last_time = time.time()

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
        
        active_scene = active_scene.next
        
        pygame.display.flip()
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
