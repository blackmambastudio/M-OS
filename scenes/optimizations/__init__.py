from random import random, shuffle

# this function reads some input and determine which
# optimization game should be played


minigames = [{
    "scene": "Focus",
    "icon": "focus.png",
    "title": "focus",
    "description": "fix imperfections to augment news reach in high society",
    "goal": "your goal description for focus",
    "preview": "focus_preview.png"
},{
    "scene": "Scanning",
    "icon": "scanning.png",
    "title": "scanning",
    "description": "modulate voices tones to reinforce the produced opinions",
    "goal": "your goal description for Scanning",
    "preview": "focus_preview.png"
}]
shuffle(minigames)

def get_next_optimization_scene(value):
    return minigames

def get_next_pair():
    shuffle(minigames)
    return minigames[:2]
