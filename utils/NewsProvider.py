from . import constants


news = [
    {
        'id': 0,
        'hdl': {
            'en': 'industrial disaster at monteasalvo\'s labs',
            'es': 'manifestación de indígenas'
        },
        'ovw': {
            'en': 'monteasalvo\'s reputation...enviromental alert...salunio river at risk',
            'es': 'cientos de indígenas se manifiestan frente a la sede del gobierno'
        },
        'gol': {
            'en': 'whitewash monteasalvo\'s reputation',
            'es': 'generar rechazo hacia indígenas'
        },
        'ico': 'biohazard.png',
        'material': [
            {
                'label': {
                    'en': ['community in', 'danger'],
                    'es': ['DESPLAZAMIENTO', 'FORZOSO']
                },
                'color': [0xf7, 0x5a, 0xff],
                'img': 'biohazard.png'
            },
            {
                'label': {
                    'en': ['deny risky alert', constants.EMPTY_LCD_LABEL],
                    'es': ['EXTERMINIO', 'CULTURAL']
                },
                'color': [0x27, 0xff, 0x93],
                'img': 'expert_deny.png'
            },
            {
                'label': {
                    'en': ['activist', 'overreact'],
                    'es': ['SOCIEDAD', 'RETROGRADA']
                },
                'color': [0x8b, 0x27, 0xff],
                'img': 'environmentalists_protests.png',
                'target': 1
            },
            {
                'label': {
                    'en': ['leakage', 'contained'],
                    'es': ['EXIGENCIAS', 'DESMEDIDAS']
                },
                'color': [0x00, 0x5f, 0xff],
                'img': 'laboratories.png',
                'target': 2
            },
            {
                'label': {
                    'en': ['severe ecosystem', 'damage'],
                    'es': ['ACTOS', 'TERRORISTAS']
                },
                'color': [0x11, 0xf4, 0xb3],
                'img': 'forest.png',
                'target': 2
            },
            {
                'label': {
                    'en': ['20 dead', '65 injured'],
                    'es': ['GOBIERNO', 'BONDADOSO']
                },
                'color': [0xc6, 0x99, 0xff],
                'img': 'hospital.png',
                'target': 3
            }
        ]
    }
]