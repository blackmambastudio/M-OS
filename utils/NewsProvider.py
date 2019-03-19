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
                'color': [0, 255, 255],
                'img': 'biohazard.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': None
            },
            {
                'label': ['deny risky alert', constants.EMPTY_LCD_LABEL],
                'color': [255, 255, 255],
                'img': 'expert_deny.png',
                'supports': constants.STORY_SUBJECT_1,
                'damages': None
            },
            {
                'label': ['activist', 'overreact'],
                'color': [255, 255, 255],
                'img': 'environmentalists_protests.png',
                'supports': constants.STORY_SUBJECT_1,
                'damages': constants.STORY_SUBJECT_2
            },
            {
                'label': ['leakage', 'contained'],
                'color': [255, 255, 255],
                'img': 'laboratories.png',
                'supports': constants.STORY_SUBJECT_1,
                'damages': None
            },
            {
                'label': ['severe ecosystem', 'damage'],
                'color': [255, 255, 255],
                'img': 'forest.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': constants.STORY_SUBJECT_1
            },
            {
                'label': ['20 dead', '65 injured'],
                'color': [255, 255, 255],
                'img': 'hospital.png',
                'supports': constants.STORY_SUBJECT_2,
                'damages': constants.STORY_SUBJECT_1
            }
        ]
    },
]

