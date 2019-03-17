from . import constants

news = [
    {
        'id': 0,
        'hdl': 'industrial disaster at monteasalvo\’s “health and joy” laboratories',
        'ovw': 'monteasalvo\’s reputation...enviromental alert...salunio river at risk',
        'arg': 'environmentalist warning',
        'gol': 'whitewash monteasalvo\’s reputation',
        'ico': 'biohazard.png',
        'material': [
            # ---- comb 01 -----------------------------------------------------
            {
                'label': ['environmentalists', 'demand'],
                'color': [255, 0, 0],
                'img': 'generic-mtl-HOOK.png',
                'story_position': constants.STORY_HOOK,
                'supports': 's2'
            },
            {
                'label': ['lab\’s negligence', constants.EMPTY_LCD_LABEL],
                'color': [255, 255, 0],
                'img': 'generic-mtl-CON1.png',
                'story_position': constants.STORY_CONFLICT_1,
                'supports': 's2'
            },
            {
                'label': ['environmental', 'impact'],
                'color': [0, 255, 0],
                'img': 'generic-mtl-CON2.png',
                'story_position': constants.STORY_CONFLICT_2,
                'supports': 's2'
            },
            {
                'label': ['community in', 'danger'],
                'color': [0, 255, 255],
                'img': 'generic-mtl-CCLS.png',
                'story_position': constants.STORY_CONCLUSION,
                'supports': 's2'
            },
            # ---- comb 02 -----------------------------------------------------
            {
                'label': ['monteasalvo labs', constants.EMPTY_LCD_LABEL],
                'color': [0, 0, 255],
                'img': 'generic-mtl-HOOK.png',
                'story_position': constants.STORY_HOOK,
                'supports': 's1'
            },
            {
                'label': ['deny risky alert', constants.EMPTY_LCD_LABEL],
                'color': [255, 255, 255],
                'img': 'generic-mtl-CON1.png',
                'story_position': constants.STORY_CONFLICT_1,
                'supports': 's1'
            },
            {
                'label': ['activist', 'overreact'],
                'color': [255, 255, 255],
                'img': 'generic-mtl-CON2.png',
                'story_position': constants.STORY_CONFLICT_2,
                'supports': 's1'
            },
            {
                'label': ['leakage', 'contained'],
                'color': [255, 255, 255],
                'img': 'generic-mtl-CCLS.png',
                'story_position': constants.STORY_CONCLUSION,
                'supports': 's1'
            },
            # ---- comb 03 -----------------------------------------------------
            {
                'label': ['polluted saluino', 'river'],
                'color': [255, 255, 255],
                'img': 'generic-mtl-HOOK.png',
                'story_position': constants.STORY_HOOK,
                'supports': None
            },
            {
                'label': ['chemical', 'leak'],
                'color': [255, 255, 255],
                'img': 'generic-mtl-CON1.png',
                'story_position': constants.STORY_CONFLICT_1,
                'supports': None
            },
            {
                'label': ['severe ecosystem', 'damage'],
                'color': [255, 255, 255],
                'img': 'generic-mtl-CON2.png',
                'story_position': constants.STORY_CONFLICT_2,
                'supports': None
            },
            {
                'label': ['monteasalvo\’s', 'involvement'],
                'color': [255, 255, 255],
                'img': 'generic-mtl-CCLS.png',
                'story_position': constants.STORY_CONCLUSION,
                'supports': None
            },
            # ---- comb 04 -----------------------------------------------------
            {
                'label': ['laboratory', 'incident'],
                'color': [255, 255, 255],
                'img': 'generic-mtl-HOOK.png',
                'story_position': constants.STORY_HOOK,
                'supports': None
            },
            {
                'label': ['environmental', 'impact'],
                'color': [255, 255, 255],
                'img': 'generic-mtl-CON1.png',
                'story_position': constants.STORY_CONFLICT_1,
                'supports': None
            },
            {
                'label': ['environmentalists', 'demand'],
                'color': [255, 255, 255],
                'img': 'generic-mtl-CON2.png',
                'story_position': constants.STORY_CONFLICT_2,
                'supports': 's2'
            },
            {
                'label': ['illegal', 'experimentation'],
                'color': [255, 255, 255],
                'img': 'generic-mtl-CCLS.png',
                'story_position': constants.STORY_CONCLUSION,
                'supports': 's2'
            },
            # ---- comb 05 -----------------------------------------------------
            {
                'label': ['incident', 'consequences'],
                'color': [255, 255, 255],
                'img': 'generic-mtl-HOOK.png',
                'story_position': constants.STORY_HOOK,
                'supports': None
            },
            {
                'label': ['20 dead', '65 injured'],
                'color': [255, 255, 255],
                'img': 'generic-mtl-CON1.png',
                'story_position': constants.STORY_CONFLICT_1,
                'supports': None
            },
            {
                'label': ['monteasalvo labs', constants.EMPTY_LCD_LABEL],
                'color': [255, 255, 255],
                'img': 'generic-mtl-CON2.png',
                'story_position': constants.STORY_CONFLICT_2,
                'supports': 's2'
            },
            {
                'label': ['responsibile for', 'tragedy'],
                'color': [255, 255, 255],
                'img': 'generic-mtl-CCLS.png',
                'story_position': constants.STORY_CONCLUSION,
                'supports': 's2'
            },
            # ---- comb 06 -----------------------------------------------------
            {
                'label': ['activists lie', constants.EMPTY_LCD_LABEL],
                'color': [255, 255, 255],
                'img': 'generic-mtl-HOOK.png',
                'story_position': constants.STORY_HOOK,
                'supports': 's1'
            },
            {
                'label': ['illegal', 'experimentation'],
                'color': [255, 255, 255],
                'img': 'generic-mtl-CON1.png',
                'story_position': constants.STORY_CONFLICT_1,
                'supports': None
            },
            {
                'label': ['monteasalvo\’s', 'ideals'],
                'color': [255, 255, 255],
                'img': 'generic-mtl-CON2.png',
                'story_position': constants.STORY_CONFLICT_2,
                'supports': 's1'
            },
            {
                'label': ['population\’s', 'health'],
                'color': [255, 255, 255],
                'img': 'generic-mtl-CCLS.png',
                'story_position': constants.STORY_CONCLUSION,
                'supports': 's1'
            }
        ],
        'framing': [
            {
                'heavier': 's1',
                'text': 'audience will trust monteasalvo and lose credibility in environmentalists'
            },
            {
                'heavier': 's2',
                'text': 'audience will support the environmentalists and protest against monteasalvo'
            },
            {
                'heavier': None,
                'text': "audience will worry about the disaster but won't do anything"
            }
        ]
    },
]

