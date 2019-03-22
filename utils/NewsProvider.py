from . import constants


news = [
    {
        'id': 0,
        'hdl': 'industrial disaster at monteasalvo\'s labs',
        'ovw': 'monteasalvo\'s reputation...enviromental alert...salunio river at risk',
        'arg': 'environmentalist warning',
        'gol': 'whitewash monteasalvo\'s reputation',
        'ico': 'biohazard.png',
        'framing': [
            {
                # :) || :(
                'operator': '>',
                'left_operate': constants.STORY_SUBJECT_1,
                'right_operate': constants.STORY_SUBJECT_2,
                'property': 'support',
                'text': 'audience will trust monteasalvo and lose credibility in environmentalists'
            },
            {
                # :( || :)
                'operator': '>',
                'left_operate': constants.STORY_SUBJECT_2,
                'right_operate': constants.STORY_SUBJECT_1,
                'property': 'support',
                'text': 'audience will support the environmentalists and protest against monteasalvo'
            },
            {
                # :) || :)
                'operator': '=',
                'left_operate': constants.STORY_SUBJECT_1,
                'right_operate': constants.STORY_SUBJECT_2,
                'property': 'support',
                'text': "audience will worry about the disaster but won't do anything"
            },
            {
                # :| || :|
                'operator': 'none',
                'text': 'audience won\'t pay attention to the news'
            }
        ],
        'material': [
            {
                'label': ['community in', 'danger'],
                'color': [0xf7, 0x5a, 0xff],
                'img': 'biohazard.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': None
            },
            {
                'label': ['deny risky alert', constants.EMPTY_LCD_LABEL],
                'color': [0x27, 0xff, 0x93],
                'img': 'expert_deny.png',
                'supports': constants.STORY_SUBJECT_1,
                'damages': None
            },
            {
                'label': ['activist', 'overreact'],
                'color': [0x8b, 0x27, 0xff],
                'img': 'environmentalists_protests.png',
                'supports': constants.STORY_SUBJECT_1,
                'damages': constants.STORY_SUBJECT_2
            },
            {
                'label': ['leakage', 'contained'],
                'color': [0x00, 0x5f, 0xff],
                'img': 'laboratories.png',
                'supports': constants.STORY_SUBJECT_1,
                'damages': None
            },
            {
                'label': ['severe ecosystem', 'damage'],
                'color': [0x11, 0xf4, 0xb3],
                'img': 'forest.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': constants.STORY_SUBJECT_1
            },
            {
                'label': ['20 dead', '65 injured'],
                'color': [0xc6, 0x99, 0xff],
                'img': 'hospital.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': constants.STORY_SUBJECT_1
            }
        ]
    },
    {
        'id': 1,
        'hdl': 'Governor facing sexual harassment allegations',
        'ovw': 'Governor\'s Reputation...Sexual Harassment Allegations...Abuse of Power',
        'arg': 'Governor\'s politics have brought positive impact to Wigsthon’s community',
        'gol': 'Divert attention from the accusations',
        'ico': 'judge.png',
        'framing': [
            {
                # :) || :(
                'operator': '>',
                'left_operate': constants.STORY_SUBJECT_1,
                'right_operate': constants.STORY_SUBJECT_2,
                'property': 'support',
                'text': 'audience will support the governor and believe the victim is lying'
            },
            {
                # :( || :)
                'operator': '>',
                'left_operate': constants.STORY_SUBJECT_2,
                'right_operate': constants.STORY_SUBJECT_1,
                'property': 'support',
                'text': 'people will feel sorry for the victim and governor\'s popularity will fall considerably'
            },
            {
                # :) || :)
                'operator': '>',
                'left_operate': constants.STORY_SUBJECT_1,
                'right_operate': constants.STORY_SUBJECT_2,
                'property': 'damage',
                'text': "People will think the accusation is a political move from the oppositors"
            },
            {
                # :| || :|
                'operator': 'none',
                'text': 'audience will feel apathetic about the subject'
            }
        ],
        'material': [
            {
                'label': ['Object to', 'Accusations'],
                'color': [0xf7, 0x5a, 0xff],
                'img': 'politician_angry.png',
                'supports': constants.STORY_SUBJECT_1,
                'damages': constants.STORY_SUBJECT_2
            },
            {
                'label': ['Governor Denies', constants.EMPTY_LCD_LABEL],
                'color': [0x27, 0xff, 0x93],
                'img': 'politician_interview.png',
                'supports': constants.STORY_SUBJECT_1,
                'damages': None
            },
            {
                'label': ['Victim', 'Testifying'],
                'color': [0x8b, 0x27, 0xff],
                'img': 'woman_crying.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': constants.STORY_SUBJECT_1
            },
            {
                'label': ['Victim Dubious', 'Background'],
                'color': [0x00, 0x5f, 0xff],
                'img': 'prostitutes.png',
                'supports': None,
                'damages': constants.STORY_SUBJECT_2
            },
            {
                'label': ['Wigsthon\'s', 'Welfare Politics'],
                'color': [0x11, 0xf4, 0xb3],
                'img': 'city.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': None
            },
            {
                'label': ['Economic Support', 'Plan'],
                'color': [0xc6, 0x99, 0xff],
                'img': 'people_poor.png',
                'supports': constants.STORY_SUBJECT_1,
                'damages': None
            }
        ]
    },
    {
        'id': 2,
        'hdl': 'MCorp announce MES™',
        'ovw': 'MCorp Technologies...MES™ Release...Game Changer for Entertainment Business',
        'arg': 'Unlawful gathering of personal information',
        'gol': 'Encourage Device Purchase',
        'ico': 'surveillance.png',
        'framing': [
            {
                # :) || :(
                'operator': '>',
                'left_operate': constants.STORY_SUBJECT_1,
                'right_operate': constants.STORY_SUBJECT_2,
                'property': 'support',
                'text': 'People will buy the Magic Entertainment System™'
            },
            {
                # :( || :)
                'operator': '>',
                'left_operate': constants.STORY_SUBJECT_2,
                'right_operate': constants.STORY_SUBJECT_1,
                'property': 'support',
                'text': 'People will feel unsure buying the Magic Entertainment System™'
            },
            {
                # :) || :)
                'operator': '>',
                'left_operate': constants.STORY_SUBJECT_2,
                'right_operate': constants.STORY_SUBJECT_1,
                'property': 'damage',
                'text': "People will distrust the resistance"
            },
            {
                # :| || :|
                'operator': 'none',
                'text': 'People will ignore the subject'
            }
        ],
        'material': [
            {
                'label': ['Entertainment', 'Game Changer'],
                'color': [0xf7, 0x5a, 0xff],
                'img': 'people_happy.png',
                'supports': constants.STORY_SUBJECT_1,
                'damages': None
            },
            {
                'label': ['Privacy', 'Violation'],
                'color': [0x27, 0xff, 0x93],
                'img': 'friends_talking.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': constants.STORY_SUBJECT_1
            },
            {
                'label': ['Undercover', 'transmission'],
                'color': [0x8b, 0x27, 0xff],
                'img': 'satellite.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': constants.STORY_SUBJECT_1
            },
            {
                'label': ['Customized', 'Entertainment'],
                'color': [0x00, 0x5f, 0xff],
                'img': 'subject_playing.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': None
            },
            {
                'label': ['Happy Living', ''],
                'color': [0x11, 0xf4, 0xb3],
                'img': 'friends_happy.png',
                'supports': constants.STORY_SUBJECT_1,
                'damages': None
            },
            {
                'label': ['Mcorp Defamation', 'Plan'],
                'color': [0xc6, 0x99, 0xff],
                'img': 'logo_resistance.png',
                'supports': constants.STORY_SUBJECT_1,
                'damages': constants.STORY_SUBJECT_2
            }
        ]
    },
    {
        'id': 3,
        'hdl': 'Migrant Crisis in Hunuragha',
        'ovw': 'Platanalians...Instability in Hunuragha...Sickness and criminal acts uprising',
        'arg': 'Migration consecuences of actions taken by the highest spheres of society',
        'gol': 'Generate rejection towards Migrants',
        'ico': 'migrants.png',
        'framing': [
            {
                # :) || :(
                'operator': '>',
                'left_operate': constants.STORY_SUBJECT_1,
                'right_operate': constants.STORY_SUBJECT_2,
                'property': 'support',
                'text': 'People will fear immigrants arrival'
            },
            {
                # :( || :)
                'operator': '>',
                'left_operate': constants.STORY_SUBJECT_1,
                'right_operate': constants.STORY_SUBJECT_2,
                'property': 'damage',
                'text': 'People will blame immigrants for crisis'
            },
            {
                # :) || :)
                'operator': '>',
                'left_operate': constants.STORY_SUBJECT_2,
                'right_operate': constants.STORY_SUBJECT_1,
                'property': 'support',
                'text': "People will question the company’s intention"
            },
            {
                # :| || :|
                'operator': 'none',
                'text': 'audience won\'t pay attention to the news'
            }
        ],
        'material': [
            {
                'label': ['Petty Crime', ''],
                'color': [0xf7, 0x5a, 0xff],
                'img': 'criminal.png',
                'supports': None,
                'damages': constants.STORY_SUBJECT_2
            },
            {
                'label': ['Busy ER', ''],
                'color': [0x27, 0xff, 0x93],
                'img': 'ER_busy.png',
                'supports': None,
                'damages': constants.STORY_SUBJECT_2
            },
            {
                'label': ['Human Rights', 'Organization'],
                'color': [0x8b, 0x27, 0xff],
                'img': 'humanrights_logo.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': constants.STORY_SUBJECT_1
            },
            {
                'label': ['Platanalian\'s', 'exodus'],
                'color': [0x00, 0x5f, 0xff],
                'img': 'border_crossing.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': None
            },
            {
                'label': ['Platanalian', 'Testimony'],
                'color': [0x11, 0xf4, 0xb3],
                'img': 'platanalian_testimony.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': constants.STORY_SUBJECT_1
            },
            {
                'label': ['M.i.M.o v0.1', 'Evidence'],
                'color': [0xc6, 0x99, 0xff],
                'img': 'electronic_garbage.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': constants.STORY_SUBJECT_1
            }
        ]
    }
]