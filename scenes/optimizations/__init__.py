from random import random, shuffle

# this function reads some input and determine which
# optimization game should be played


minigames = [{
    "scene": "Focus",
    "icon": "focus.png",
    "title": "focus",
    "description": "fix imperfections to augment news reach in high society",
    "goal": "your goal description for focus",
    "preview": "focus_preview.png",
    "preview_width": 317,
    "preview_height": 374,
    "preview_frames": [0,1,2,3,4,5,6],
    "preview_x": 816,
    "preview_y": 227,
    "preview_rate": 0.75
},{
    "scene": "Scanning",
    "icon": "scanning.png",
    "title": "scanning",
    "description": "modulate voices tones to reinforce the produced opinions",
    "goal": "your goal description for Scanning",
    "preview": "scanning_preview.png",
    "preview_width": 359,
    "preview_height": 286,
    "preview_frames": [0,1,2,3,4,5,6],
    "preview_x": 795,
    "preview_y": 262,
    "preview_rate": 1.2
}]
shuffle(minigames)

def get_next_optimization_scene(value):
    return minigames

def get_next_pair():
    shuffle(minigames)
    return minigames[:2]
