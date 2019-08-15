from random import random, shuffle

# this function reads some input and determine which
# optimization game should be played


minigames = [{
    "scene": "Focus",
    "icon": "focus.png",
    "title": "focus",
    "description": {
        'en': "Rotate the images using the triangular inputs",
        'es': 'Rota las figuras usando los botones triangulares'
    },
    "goal": {
        'en': "Connect all circuits before the time runs out",
        'es': 'conecta el circuito antes de que termine el tiempo'
    },
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
    "description": {
        'en': "Use the knobs to scan the panel and triangular inputs to select the correct shape",
        'es': 'usa las perillas para escanear y los botones triangulares para escoger la coincidencia'
    },
    "goal": {
        'en': "Guess as many shapes as possible in the given time",
        'es': 'encuentra tantas figuras como sea posible en el tiempo dado'
    },
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
