from . import constants


news = [
    {
        'id': 0,
        'hdl': {
            'en': 'industrial disaster at monteasalvo\'s labs',
            'es': 'manifestación de nativos'
        },
        'ovw': {
            'en': 'monteasalvo\'s reputation...enviromental alert...salunio river at risk',
            'es': 'cientos de nativos se manifiestan frente a la sede del gobierno'
        },
        'gol': {
            'en': 'whitewash monteasalvo\'s reputation',
            'es': 'generar rechazo hacia nativos'
        },
        'ico': 'biohazard.png',
        'framing': {
            'bad': {
                'en': '???',
                'es': 'la audiencia mostrará apoyo a los nativos'
            },
            'good': {
                'en': '???',
                'es': 'la audiencia tendrá dudas acerca de las demandas de los nativos'
            },
            'excellent': {
                'en': '???',
                'es': 'la audiencia rechazará a los manifestantes y apoyará la posición del gobierno'
            },
        },
        'material': [
            {
                'label': {
                    'en': ['community in', 'danger'],
                    'es': ['DESPLAZAMIENTO', 'FORZOSO']
                },
                'detail': {
                    'en': '???',
                    'es': 'Incendio forestal obliga a los habitantes del bosque Texlamu a abandonar sus hogares.'
                },
                'color': [0xf7, 0x5a, 0xff],
                'img': 'biohazard.png'
            },
            {
                'label': {
                    'en': ['deny risky alert', constants.EMPTY_LCD_LABEL],
                    'es': ['EXTERMINIO', 'CULTURAL']
                },
                'detail': {
                    'en': '???',
                    'es': 'Civilización ancestral en riesgo de desaparecer por completo.'
                },
                'color': [0x27, 0xff, 0x93],
                'img': 'expert_deny.png'
            },
            {
                'label': {
                    'en': ['activist', 'overreact'],
                    'es': ['SOCIEDAD', 'RETROGRADA']
                },
                'detail': {
                    'en': '???',
                    'es': 'Los nativos Kayoc son una sociedad atrasada y vulnera los derechos fundamentales.'
                },
                'color': [0x8b, 0x27, 0xff],
                'img': 'environmentalists_protests.png',
                'target': 2
            },
            {
                'label': {
                    'en': ['leakage', 'contained'],
                    'es': ['EXIGENCIAS', 'DESMEDIDAS']
                },
                'detail': {
                    'en': '???',
                    'es': 'Las demandas de los protestantes son abusivas y sin fundamento.'
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
                'detail': {
                    'en': '???',
                    'es': 'Nativos Kayoc, primeros sospechosos en recientes ataques en la ciudad.'
                },
                'color': [0x11, 0xf4, 0xb3],
                'img': 'forest.png',
                'target': 1
            },
            {
                'label': {
                    'en': ['20 dead', '65 injured'],
                    'es': ['GOBIERNO', 'BONDADOSO']
                },
                'detail': {
                    'en': '???',
                    'es': 'Los aportes y políticas del gobierno ya son suficientemente generosas.'
                },
                'color': [0xc6, 0x99, 0xff],
                'img': 'hospital.png',
                'target': 3
            }
        ]
    },
    {
        'id': 2,
        'hdl': {
            'en': 'industrial disaster at monteasalvo\'s labs',
            'es': 'Texlamu sigue ardiendo'
        },
        'ovw': {
            'en': 'monteasalvo\'s reputation...enviromental alert...salunio river at risk',
            'es': 'Bosque Texlamu cumple 29 días en llamas.'
        },
        'gol': {
            'en': 'whitewash monteasalvo\'s reputation',
            'es': 'Justificar la quema del bosque y para permitir su destrucción.'
        },
        'ico': 'biohazard.png',
        'framing': {
            'bad': {
                'en': '???',
                'es': 'la audiencia hará protestas para que se detenga la quema'
            },
            'good': {
                'en': '???',
                'es': 'la audiencia no hará nada respecto a la quema'
            },
            'excellent': {
                'en': '???',
                'es': 'aumentará el favoritismo de la audiencia hacia las compañías involucradas en la quema'
            },
        },
        'material': [
            {
                'label': {
                    'en': ['community in', 'danger'],
                    'es': ['AFECTACIÓN', 'AMBIENTAL']
                },
                'detail': {
                    'en': '???',
                    'es': 'La quema descontrolada de árboles causará daños irreparables al ecosistema.'
                },
                'color': [0xf7, 0x5a, 0xff],
                'img': 'politician_angry.png'
            },
            {
                'label': {
                    'en': ['deny risky alert', constants.EMPTY_LCD_LABEL],
                    'es': ['FAUNA', 'VULNERABLE']
                },
                'detail': {
                    'en': '???',
                    'es': 'Cientos de especies endémicas de la región se encuentran en peligro de desaparecer.'
                },
                'color': [0x27, 0xff, 0x93],
                'img': 'politician_interview.png'
            },
            {
                'label': {
                    'en': ['activist', 'overreact'],
                    'es': ['PLAGAS', 'PELIGROSAS']
                },
                'detail': {
                    'en': '???',
                    'es': 'El bosque Texlamu es una cuna de enfermedades y plagas que afectan la producción agrícola.'
                },
                'color': [0x8b, 0x27, 0xff],
                'img': 'woman_crying.png',
                'target': 2
            },
            {
                'label': {
                    'en': ['leakage', 'contained'],
                    'es': ['IMPULSO', 'ECONÓMICO']
                },
                'detail': {
                    'en': '???',
                    'es': 'La desaparición del bosque traerá beneficios económicos nunca antes vistos.'
                },
                'color': [0x00, 0x5f, 0xff],
                'img': 'prostitutes.png',
                'target': 3
            },
            {
                'label': {
                    'en': ['severe ecosystem', 'damage'],
                    'es': ['GENERACIÓN', 'EMPLEO']
                },
                'detail': {
                    'en': '???',
                    'es': 'La recuperación del espacio generará miles de empleos directos y más a futuro. .'
                },
                'color': [0x11, 0xf4, 0xb3],
                'img': 'city.png',
                'target': 2
            },
            {
                'label': {
                    'en': ['20 dead', '65 injured'],
                    'es': ['INCENDIO', 'CONTROLADO']
                },
                'detail': {
                    'en': '???',
                    'es': 'Los subversivos exageran, la situación nunca se ha salido de control.'
                },
                'color': [0xc6, 0x99, 0xff],
                'img': 'people_poor.png',
                'target': 1
            }
        ]
    }
]