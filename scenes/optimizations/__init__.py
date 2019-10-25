from random import random, shuffle

# this function reads some input and determine which
# optimization game should be played


minigames = [{
    "scene": "Focus",
    "icon": "focus.png",
    "title": {
        'en': "focus",
        'es': "Overclock"
    },
    'pitch': {
        'en': '???',
        'es': 'Modifica el circuito correctamente para mejorar la eficiencia de MiMo'
    },
    "description": {
        'en': "Rotate the images using the triangular inputs",
        'es': '''- Gira las figuras usando los botones triangulares.
- Conecta las líneas del circuito antes de que la máquina se sobrecargue.'''
    },
    "goal": {
        'en': "Connect all circuits before the time runs out",
        'es': 'Ajusta el cableado interno de MiMo para hacerle overclock y reforzar el impacto de la noticia.'
    },
    "preview": "focus_preview.png",
    "preview_width": 320,
    "preview_height": 358,
    "preview_frames": [0,1,2,3,4,5],
    "preview_x": 816,
    "preview_y": 227,
    "preview_rate": 0.75
},{
    "scene": "Scanning",
    "icon": "scanning.png",
    "title": {
        'en': "scanning",
        'es': 'scanner'
    },
    'pitch': {
        'en': '???',
        'es': 'identifica las figuras escondidas para incrementar el alcance de MiMo'
    },
    "description": {
        'en': "Use the knobs to scan the panel and triangular inputs to select the correct shape",
        'es': '''- Usa las perillas para escanear el panel central.
- El color del barrido revelará la figura oculta.
- Selecciona la figura descubierta usando los botones triangulares.'''
    },
    "goal": {
        'en': "Guess as many shapes as possible in the given time",
        'es': 'Mejora el alcance de la transmisión identificando las figuras que corrompen el algoritmo geométrico de MiMo.'
    },
    "preview": "scanning_preview.png",
    "preview_width": 388,
    "preview_height": 318,
    "preview_frames": [0,1,2,3,4,5],
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
