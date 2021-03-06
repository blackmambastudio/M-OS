import pygame

VIEWPORT_WIDTH = 1280	
VIEWPORT_HEIGHT = 720
VIEWPORT_CENTER_X = VIEWPORT_WIDTH / 2
VIEWPORT_CENTER_Y = VIEWPORT_HEIGHT / 2
VIEWPORT_PADDING_X = 16
VIEWPORT_PADDING_Y = 32

POPUP_X = 74
POPUP_Y = 74
POPUP_WIDTH = 1131
POPUP_HEIGHT = 553

FONT_TITLE = 48 # 48
FONT_SUBTITLE = 36 # 36
FONT_NORMAL = 28 # 24
FONT_SMALL = 18 # 18

FONTS = 'assets/fonts/'
VCR_OSD_MONO = FONTS + 'VCR_OSD_MONO_1.001.ttf'
SPRITES = 'assets/sprites/'
SPRITES_COMMON = SPRITES + 'scenes/common/'
SPRITES_INTRO = SPRITES + 'scenes/intro/'
SPRITES_EDITION = SPRITES + 'scenes/edition/'
SPRITES_OPTIMIZATION = SPRITES + 'scenes/optimization/'
SPRITES_UI_BG = SPRITES_COMMON + 'ui-background.png'
SPRITES_FOCUS = SPRITES + 'minigames/focus/'
SPRITES_SCANNING = SPRITES + 'minigames/scanning/'
MATERIAL = 'assets/material/'
EVENTS = 'assets/events/'

PALETTE_WHITE = (234, 225, 243)
PALETTE_PINK = (241, 100, 243)
PALETTE_CYAN = (163, 223, 224)
PALETTE_BLUE = (9, 9, 67)
PALETTE_TITLES_DARK_BLUE = (0x21, 0x1c, 0x7f)
PALETTE_TITLES_PINK = (0xf1, 0x64, 0xf3)
PALETTE_DARK_BLUE = (0x21, 0x1c, 0x7f)
PALETTE_YELLOW = (237, 225, 74)
PALETTE_GREEN = (77, 232, 140)

PALLETE_KING_BLUE = (0x00, 0x5E, 0xFF)
PALLETE_DARK_BLUE = (0x1D, 0x72, 0xA7)
PALLETE_BACKGROUND_BLUE = (0x20, 0xF5, 0xFF)
PALLETE_BACKGROUND_TITLE_BLUE = (0x00,0x5f,0xff)

# La nueva paleta --------------------------------------------------------------
PALETTE_TEXT_PURPLE = (0xA3, 0x8A, 0xFF)
PALETTE_TEXT_RED = (0xFF, 0x40, 0x7A)
PALETTE_TEXT_CYAN = (0x20, 0xF5, 0xFF)
PALETTE_TEXT_BLACK = (0x04, 0x00, 0x00)
PALETTE_TEXT_WHITE = (0xEA, 0xE1, 0xF3)
# ------------------------------------------------------------------------------

MINIGAME_LEFT = 0
MINIGAME_RIGHT = 1

EMPTY_LCD_LABEL = ''

STORY_HOOK = 0
STORY_CONFLICT_1 = 1
STORY_CONFLICT_2 = 2
STORY_CONCLUSION = 3
STORY_SUBJECT_1 = 'S1'
STORY_SUBJECT_2 = 'S2'

# in minutes
SESSION_TIME = 4.8
#SESSION_TIME = 1.5

# TODO: put the constants related to the keyboard keys that will emulate the buttons
#   in la MiMo.

currento_evento = 0
language = 'es'
score = 0