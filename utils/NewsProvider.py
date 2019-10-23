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
        # 'arg': {
        #     'en': 'environmentalist warning',
        #     'es': 'ambientalistas protestan contra farmacéutica'
        # },
        'gol': {
            'en': 'whitewash monteasalvo\'s reputation',
            'es': 'generar rechazo hacia indígenas'
        },
        'ico': 'biohazard.png',
        'framing': [
            {
                'operator': '<',
                'value': 16,
                'text': {
                    'en': 'audience will trust monteasalvo and lose credibility in environmentalists',
                    'es': 'la audiencia rechazará a los manifestantes'
                }
            },
            {
                'operator': '>',
                'value': 15,
                'text': {
                    'en': 'audience will support the environmentalists and protest against monteasalvo',
                    'es': 'la audiencia apoyará a los manifestantes'
                }
            },
            {
                'operator': 'none',
                'text': {
                    'en': 'audience won\'t pay attention to the news',
                    'es': 'la audiencia no prestará atención a la noticia'
                }
            }
        ],
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
    },
    {
        'id': 1,
        'hdl': {
            'en': 'Governor facing sexual harassment allegations',
            'es': 'Gobernador involucrado en escándalo sexual'
        },
        'ovw': {
            'en': 'Governor\'s Reputation...Sexual Harassment Allegations...Abuse of Power',
            'es': 'gobernador machete...acusado de acoso...abuso de poder político'
        },
        'arg': {
            'en': 'Governor\'s politics have brought positive impact to Wigsthon’s community',
            'es': 'el gobernador ha hecho cosas muy buenas por la comunidad en su gobierno'
        },
        'gol': {
            'en': 'Divert attention from the accusations',
            'es': 'desviar atención respecto al caso de acoso'
        },
        'ico': 'judge.png',
        'framing': [
            {
                # :) || :(
                'operator': '>',
                'left_operate': constants.STORY_SUBJECT_1,
                'right_operate': constants.STORY_SUBJECT_2,
                'property': 'support',
                'text': {
                    'en': 'audience will support the governor and believe the victim is lying',
                    'es': 'la gente apoyará al gobernador y creerá que la víctima miente'
                }
            },
            {
                # :( || :)
                'operator': '>',
                'left_operate': constants.STORY_SUBJECT_2,
                'right_operate': constants.STORY_SUBJECT_1,
                'property': 'support',
                'text': {
                    'en': 'people will feel sorry for the victim and governor\'s popularity will fall considerably',
                    'es': 'la gente sentirá pena por la víctima y la popularidad del gobernador caerá considerablemente'
                }
            },
            {
                # :) || :)
                'operator': '>',
                'left_operate': constants.STORY_SUBJECT_1,
                'right_operate': constants.STORY_SUBJECT_2,
                'property': 'damage',
                'text': {
                    'en': 'People will think the accusation is a political move from the oppositors',
                    'es': 'la gente creerá que la acusación es una jugada política de la oposición'
                }
            },
            {
                # :| || :|
                'operator': 'none',
                'text': {
                    'en': 'audience will feel apathetic about the subject',
                    'es': 'la gente será apática respecto al caso de acoso'
                }
            }
        ],
        'material': [
            {
                'label': {
                    'en': ['Object to', 'Accusations'],
                    'es': ['gobernador', 'alega calumnia']
                },
                'color': [0xf7, 0x5a, 0xff],
                'img': 'politician_angry.png',
                'supports': constants.STORY_SUBJECT_1,
                'damages': constants.STORY_SUBJECT_2
            },
            {
                'label': {
                    'en': ['Governor Denies', constants.EMPTY_LCD_LABEL],
                    'es': ['gobernador', 'desmiente']
                },
                'color': [0x27, 0xff, 0x93],
                'img': 'politician_interview.png',
                'supports': constants.STORY_SUBJECT_1,
                'damages': None
            },
            {
                'label': {
                    'en': ['Victim', 'Testifying'],
                    'es': ['testimonio', 'mujer asustada']
                },
                'color': [0x8b, 0x27, 0xff],
                'img': 'woman_crying.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': constants.STORY_SUBJECT_1
            },
            {
                'label': {
                    'en': ['Victim Dubious', 'Background'],
                    'es': ['mujer tiene', 'dudoso pasado']
                },
                'color': [0x00, 0x5f, 0xff],
                'img': 'prostitutes.png',
                'supports': None,
                'damages': constants.STORY_SUBJECT_2
            },
            {
                'label': {
                    'en': ['Wigsthon\'s', 'Welfare Politics'],
                    'es': ['buenas politicas', 'gobernador']
                },
                'color': [0x11, 0xf4, 0xb3],
                'img': 'city.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': None
            },
            {
                'label': {
                    'en': ['Economic Support', 'Plan'],
                    'es': ['plan apoyo', 'economico']
                },
                'color': [0xc6, 0x99, 0xff],
                'img': 'people_poor.png',
                'supports': constants.STORY_SUBJECT_1,
                'damages': None
            }
        ]
    },
    {
        'id': 2,
        'hdl': {
            'en': 'MCorp announce MES™',
            'es': 'MCorp anuncia el lanzamiento de MES™'
        },
        'ovw': {
            'en': 'MCorp Technologies...MES™ Release...Game Changer for Entertainment Business',
            'es': 'MCorp...lanzamiento de MES™...revolución en la industria del entretenimiento'
        },
        'arg': {
            'en': 'Unlawful gathering of personal information',
            'es': 'recopilación ilegal de información personal'
        },
        'gol': {
            'en': 'Encourage Device Purchase',
            'es': 'estimular compra del dispositivo'
        },
        'ico': 'surveillance.png',
        'framing': [
            {
                # :) || :(
                'operator': '>',
                'left_operate': constants.STORY_SUBJECT_1,
                'right_operate': constants.STORY_SUBJECT_2,
                'property': 'support',
                'text': {
                    'en': 'People will buy the Magic Entertainment System™',
                    'es': 'la audiencia comprará el Magic Entertainment System™'
                }
            },
            {
                # :( || :)
                'operator': '>',
                'left_operate': constants.STORY_SUBJECT_2,
                'right_operate': constants.STORY_SUBJECT_1,
                'property': 'support',
                'text': {
                    'en': 'People will feel unsure buying the Magic Entertainment System™',
                    'es': 'la audiencia dudará en comprar el Magic Entertainment System™'
                }
            },
            {
                # :) || :)
                'operator': '>',
                'left_operate': constants.STORY_SUBJECT_2,
                'right_operate': constants.STORY_SUBJECT_1,
                'property': 'damage',
                'text': {
                    'en': "People will distrust the resistance",
                    'es': 'la audiencia desconfiará de la resistencia'
                }
            },
            {
                # :| || :|
                'operator': 'none',
                'text': {
                    'en': 'People will ignore the subject',
                    'es': 'la audiencia ignorará la noticia'
                }
            }
        ],
        'material': [
            {
                'label': {
                    'en': ['Entertainment', 'Game Changer'],
                    'es': ['revolucion', 'entretenimiento']
                },
                'color': [0xf7, 0x5a, 0xff],
                'img': 'people_happy.png',
                'supports': constants.STORY_SUBJECT_1,
                'damages': None
            },
            {
                'label': {
                    'en': ['Privacy', 'Violation'],
                    'es': ['violacion', 'privacidad']
                },
                'color': [0x27, 0xff, 0x93],
                'img': 'friends_talking.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': constants.STORY_SUBJECT_1
            },
            {
                'label': {
                    'en': ['Undercover', 'transmission'],
                    'es': ['envio', 'clandestino']
                },
                'color': [0x8b, 0x27, 0xff],
                'img': 'satellite.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': constants.STORY_SUBJECT_1
            },
            {
                'label': {
                    'en': ['Customized', 'Entertainment'],
                    'es': ['entretenimiento', 'personalizado']
                },
                'color': [0x00, 0x5f, 0xff],
                'img': 'subject_playing.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': None
            },
            {
                'label': {
                    'en': ['Happy Living', ''],
                    'es': ['vida feliz', '']
                },
                'color': [0x11, 0xf4, 0xb3],
                'img': 'friends_happy.png',
                'supports': constants.STORY_SUBJECT_1,
                'damages': None
            },
            {
                'label': {
                    'en': ['Mcorp Defamation', 'Plan'],
                    'es': ['plan difamacion', 'resistencia']
                },
                'color': [0xc6, 0x99, 0xff],
                'img': 'logo_resistance.png',
                'supports': constants.STORY_SUBJECT_1,
                'damages': constants.STORY_SUBJECT_2
            }
        ]
    },
    {
        'id': 3,
        'hdl': {
            'en': 'Migrant Crisis in Hunuragha',
            'es': 'crisis migratoria en hunuragha'
        },
        'ovw': {
            'en': 'Platanalians...Instability in Hunuragha...Sickness and criminal acts uprising',
            'es': 'plataneros...inestabilidad en hunuragha...enfermedades y actos delictivos en alza'
        },
        'arg': {
            'en': 'Migration consecuences of actions taken by the highest spheres of society',
            'es': 'migración es consecuencia del abuso del poder en el sector privado'
        },
        'gol': {
            'en': 'Generate rejection towards Migrants',
            'es': 'generar rechazo hacia inmigrantes'
        },
        'ico': 'migrants.png',
        'framing': [
            {
                # :) || :(
                'operator': '>',
                'left_operate': constants.STORY_SUBJECT_1,
                'right_operate': constants.STORY_SUBJECT_2,
                'property': 'support',
                'text': {
                    'en': 'People will fear immigrants arrival',
                    'es': 'la gente temerá por la llegada de los inmigrantes'
                }
            },
            {
                # :( || :)
                'operator': '>',
                'left_operate': constants.STORY_SUBJECT_1,
                'right_operate': constants.STORY_SUBJECT_2,
                'property': 'damage',
                'text': {
                    'en': 'People will blame immigrants for crisis',
                    'es': 'la gente culpará a los inmigrantes de la crisis'
                }
            },
            {
                # :) || :)
                'operator': '>',
                'left_operate': constants.STORY_SUBJECT_2,
                'right_operate': constants.STORY_SUBJECT_1,
                'property': 'support',
                'text': {
                    'en': "People will question the company’s intention",
                    'es': "la gente cuestionará los motivos de la inmigración"
                }
            },
            {
                # :| || :|
                'operator': 'none',
                'text': {
                    'en': 'audience won\'t pay attention to the news',
                    'es': 'la gente no prestará atención a la noticia'
                }
            }
        ],
        'material': [
            {
                'label': {
                    'en': ['Petty Crime', ''],
                    'es': ['delincuencia', 'comun']
                },
                'color': [0xf7, 0x5a, 0xff],
                'img': 'criminal.png',
                'supports': None,
                'damages': constants.STORY_SUBJECT_2
            },
            {
                'label': {
                    'en': ['Busy ER', ''],
                    'es': ['urgencias', 'saturadas']
                },
                'color': [0x27, 0xff, 0x93],
                'img': 'ER_busy.png',
                'supports': None,
                'damages': constants.STORY_SUBJECT_2
            },
            {
                'label': {
                    'en': ['Human Rights', 'Organization'],
                    'es': ['organizacion de', 'derechos humanos']
                },
                'color': [0x8b, 0x27, 0xff],
                'img': 'humanrights_logo.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': constants.STORY_SUBJECT_1
            },
            {
                'label': {
                    'en': ['Platanalian\'s', 'exodus'],
                    'es': ['exodo platanero', '']
                },
                'color': [0x00, 0x5f, 0xff],
                'img': 'border_crossing.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': None
            },
            {
                'label': {
                    'en': ['Platanalian', 'Testimony'],
                    'es': ['testimonio de', 'platanero']
                },
                'color': [0x11, 0xf4, 0xb3],
                'img': 'platanalian_testimony.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': constants.STORY_SUBJECT_1
            },
            {
                'label': {
                    'en': ['M.i.M.o v0.1', 'Evidence'],
                    'es': ['evidencia de', 'M.i.M.o v0.1']
                },
                'color': [0xc6, 0x99, 0xff],
                'img': 'electronic_garbage.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': constants.STORY_SUBJECT_1
            }
        ]
    }
]