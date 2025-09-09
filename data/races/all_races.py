from settings import *

HUMAN = {
    'id': 'human',
    'display_name': 'Human',
    'description': (
        "Ambitious, adaptable, and far more numerous than any other race, Humans "
        "are the standard by which all others are often measured. Their relatively "
        "short lifespans drive them to build, explore, and achieve great things in "
        "the time they have. They are a true 'jack-of-all-trades'."
    ),
    'stats': {
        'str': 1,
        'dex': 1,
        'con': 1,
        'int': 1,
        'wis': 1,
        'charisma': 1,
        'faith': 1,
    },
    'resistances': {
        # Humans have no outstanding natural resistances.
    },
    'abilities': [
        {
            'name': 'Quick Learner',
            'description': 'You gain experience points at a slightly faster rate.'
        }
    ],
    'font_color' : SOLAR_FLARE
}

ELF = {
    'id': 'elf',
    'display_name': 'Elf',
    'description': (
        "A graceful and long-lived people, Elves share a deep, intrinsic bond with "
        "the world's ancient forests. They move with a silent quickness and possess "
        "senses far sharper than those of other races. Many see them as aloof, but "
        "they are simply more deliberate, viewing time in centuries, not years."
    ),
    'stats': {
        'str': 0,
        'dex': 2,      # Bonus reflects their natural agility
        'con': -1,     # Penalty reflects their slender build
        'int': 1,
        'wis': 1,
        'charisma': 0,
        'faith': 0,
    },
    'resistances': {
        'nature': 10,
        'spirit': 15,  # Represents their resistance to charms and mental effects
    },
    'abilities': [
        {
            'name': 'Keen Senses',
            'description': 'You have a higher chance to detect hidden traps and secrets in the world.'
        }
    ],
    'font_color' : BRIGHT_LEAF
}

DWARF = {
    'id': 'dwarf',
    'display_name': 'Dwarf',
    'description': (
        "Stout and resilient, the Dwarves are masters of stone and steel, hailing "
        "from mighty halls carved into the hearts of mountains. They are renowned "
        "for their unwavering loyalty, incredible endurance, and the unmatched "
        "quality of their craft. To a Dwarf, a promise is as unbreakable as steel."
    ),
    'stats': {
        'str': 2,      # Bonus reflects their powerful build
        'dex': -1,
        'con': 2,      # Bonus reflects their hardiness
        'int': 0,
        'wis': 0,
        'charisma': -1,
        'faith': 0,
    },
    'resistances': {
        'poison': 20,
        'physical': 10, # Represents their tough, resilient nature
    },
    'abilities': [
        {
            'name': 'Master Craftsman',
            'description': 'You are more effective at smithing and enchanting items.'
        }
    ],
    'font_color' : EMBERGLOW
}

KAELEN = {
    'id': 'kaelen',
    'display_name': 'Kaelen',
    'description': (
        "Often called the 'bridge-builders', the Kaelen are a social and adaptable "
        "people whose cities are marvels of cooperation. Blending human-like versatility "
        "with a unique diplomatic grace, their greatest strength is their unwavering "
        "spirit and ability to find common ground."
    ),
    'stats': {
        'str': 0, 'dex': 0, 'con': 0, 'int': 0, 'wis': 1, 'charisma': 2, 'faith': 0,
    },
    'resistances': { 'spirit': 10 },
    'abilities': [
        {
            'name': 'Natural Diplomat',
            'description': 'You gain better prices from merchants and more favorable outcomes in some dialogues.'
        }
    ],
    'font_color' : SKYFORGE_BLUE
}

SOLIS = {
    'id': 'solis',
    'display_name': 'Solis',
    'description': (
        "The Solis are a vibrant, elven-like people whose lives are deeply connected to the sun "
        "and the open meadows. They are known for their grace and speed, and believe "
        "every day is a gift to be filled with light and purpose."
    ),
    'stats': {
        'str': -1, 'dex': 2, 'con': -1, 'int': 0, 'wis': 1, 'charisma': 1, 'faith': 1,
    },
    'resistances': { 'light': 15, 'nature': 5 },
    'abilities': [
        {
            'name': 'Sun-Kissed',
            'description': 'You move slightly faster during the day and have a natural affinity for light-based magic.'
        }
    ],
    'font_color' : RADIANT_GOLD
}

STONEBORN = {
    'id': 'stoneborn',
    'display_name': 'Stoneborn',
    'description': (
        "Born of stone and soil, the Grave-touched are a steadfast and patient people, "
        "akin to the Dwarves of the deep earth. They see time not in years, but in ages, "
        "and are master artisans, shaping the raw materials of the world with reverence."
    ),
    'stats': {
        'str': 1, 'dex': -2, 'con': 2, 'int': 0, 'wis': 1, 'charisma': 0, 'faith': 1,
    },
    'resistances': { 'poison': 20, 'physical': 5 },
    'abilities': [
        {
            'name': "Stone's Endurance",
            'description': 'You have a higher resistance to being knocked down or staggered.'
        }
    ],
    'font_color' : SANDSTONE_OCHRE
}

SYLVAN = {
    'id': 'sylvan',
    'display_name': 'Sylvan',
    'description': (
        "The Sylvans are a symbiotic people whose physiology is intertwined with the "
        "forest. Their settlements are living cities grown in harmony with the canopy. "
        "They are deeply wise, seeing the world as a single, interconnected organism."
    ),
    'stats': {
        'str': 0, 'dex': 0, 'con': 1, 'int': 0, 'wis': 2, 'charisma': -1, 'faith': 1,
    },
    'resistances': { 'nature': 20, 'poison': 10 },
    'abilities': [
        {
            'name': 'Natural Vigor',
            'description': 'You slowly regenerate a small amount of health over time when outdoors.'
        }
    ],
    'font_color' : ARCANE_ORCHID
}

ALL_RACES = {
    'human': HUMAN,
    'elf': ELF,
    'dwarf': DWARF,
    'kaelen': KAELEN,
    'solis': SOLIS,
    'stoneborn': STONEBORN,
    'sylvan': SYLVAN,
}