from settings import *

WARRIOR = {
    'id': 'warrior',
    'display_name': 'Warrior',
    'description': (
        "Masters of martial combat, Warriors thrive in the heart of battle. They rely "
        "on their strength, endurance, and mastery of weapons to overcome their foes. "
        "A Warrior is a bulwark on the battlefield, protecting their allies and "
        "cleaving through enemy lines."
    ),
    'primary_stats': ['Strength', 'Constitution'],
    'stats': {
        'strength': 3, 'dexterity': 1, 'constitution': 2, 'intellect': 0, 'wisdom': 0, 'charisma': 0, 'faith': 0,
    },
    'resistances': {
        'Toughness': 15, # The defining trait of a Warrior
        'Fire': 5,
    },
    'resistance_progression': [
        # Toughness (+3 every 2 levels)
        {'level': 2, 'resistance': 'Toughness', 'amount': 3},
        {'level': 4, 'resistance': 'Toughness', 'amount': 3},
        {'level': 6, 'resistance': 'Toughness', 'amount': 3},
        {'level': 8, 'resistance': 'Toughness', 'amount': 3},
        {'level': 10, 'resistance': 'Toughness', 'amount': 3},
        {'level': 12, 'resistance': 'Toughness', 'amount': 3},
        {'level': 14, 'resistance': 'Toughness', 'amount': 3},
        {'level': 16, 'resistance': 'Toughness', 'amount': 3},
        {'level': 18, 'resistance': 'Toughness', 'amount': 3},
        {'level': 20, 'resistance': 'Toughness', 'amount': 3},
        {'level': 22, 'resistance': 'Toughness', 'amount': 3},
        {'level': 24, 'resistance': 'Toughness', 'amount': 3},
        {'level': 26, 'resistance': 'Toughness', 'amount': 3},
        {'level': 28, 'resistance': 'Toughness', 'amount': 3},
        {'level': 30, 'resistance': 'Toughness', 'amount': 3},
        {'level': 32, 'resistance': 'Toughness', 'amount': 3},
        {'level': 34, 'resistance': 'Toughness', 'amount': 3},
        {'level': 36, 'resistance': 'Toughness', 'amount': 3},
        {'level': 38, 'resistance': 'Toughness', 'amount': 3},
        {'level': 40, 'resistance': 'Toughness', 'amount': 3},
        {'level': 42, 'resistance': 'Toughness', 'amount': 3},
        {'level': 44, 'resistance': 'Toughness', 'amount': 3},
        {'level': 46, 'resistance': 'Toughness', 'amount': 3},
        {'level': 48, 'resistance': 'Toughness', 'amount': 3},
        {'level': 50, 'resistance': 'Toughness', 'amount': 3},
        {'level': 52, 'resistance': 'Toughness', 'amount': 3},
        {'level': 54, 'resistance': 'Toughness', 'amount': 3},
        {'level': 56, 'resistance': 'Toughness', 'amount': 3},
        {'level': 58, 'resistance': 'Toughness', 'amount': 3},
        {'level': 60, 'resistance': 'Toughness', 'amount': 3},
    ],
    'abilities': ['heroic_strike'],
    'font_color' : STEEL_RED
}

MAGE = {
    'id': 'mage',
    'display_name': 'Mage',
    'description': (
        "Mages are scholars of the arcane, wielding raw elemental power to reshape "
        "the battlefield. They are powerful but fragile, preferring to keep their "
        "distance while unleashing devastating spells of fire, frost, and lightning."
    ),
    'primary_stats': ['Intellect', 'Wisdom'],
    'stats': {
        'strength': 0, 'dexterity': 0, 'constitution': 0, 'intellect': 4, 'wisdom': 2, 'charisma': 0, 'faith': 0,
    },
    'resistances': {
        'Frost': 10,
        'Fire': 10,
        'Lightning': 10,
    },
    'resistance_progression': [
        # Primary Resistances (+2 every 6 levels, staggered)
        {'level': 6, 'resistance': 'Fire', 'amount': 2},
        {'level': 8, 'resistance': 'Frost', 'amount': 2},
        {'level': 10, 'resistance': 'Lightning', 'amount': 2},
        {'level': 12, 'resistance': 'Fire', 'amount': 2},
        {'level': 14, 'resistance': 'Frost', 'amount': 2},
        {'level': 16, 'resistance': 'Lightning', 'amount': 2},
        {'level': 18, 'resistance': 'Fire', 'amount': 2},
        {'level': 20, 'resistance': 'Frost', 'amount': 2},
        {'level': 22, 'resistance': 'Lightning', 'amount': 2},
        {'level': 24, 'resistance': 'Fire', 'amount': 2},
        {'level': 26, 'resistance': 'Frost', 'amount': 2},
        {'level': 28, 'resistance': 'Lightning', 'amount': 2},
        {'level': 30, 'resistance': 'Fire', 'amount': 2},
        {'level': 32, 'resistance': 'Frost', 'amount': 2},
        {'level': 34, 'resistance': 'Lightning', 'amount': 2},
        {'level': 36, 'resistance': 'Fire', 'amount': 2},
        {'level': 38, 'resistance': 'Frost', 'amount': 2},
        {'level': 40, 'resistance': 'Lightning', 'amount': 2},
        {'level': 42, 'resistance': 'Fire', 'amount': 2},
        {'level': 44, 'resistance': 'Frost', 'amount': 2},
        {'level': 46, 'resistance': 'Lightning', 'amount': 2},
        {'level': 48, 'resistance': 'Fire', 'amount': 2},
        {'level': 50, 'resistance': 'Frost', 'amount': 2},
        {'level': 52, 'resistance': 'Lightning', 'amount': 2},
        {'level': 54, 'resistance': 'Fire', 'amount': 2},
        {'level': 56, 'resistance': 'Frost', 'amount': 2},
        {'level': 58, 'resistance': 'Lightning', 'amount': 2},
        {'level': 60, 'resistance': 'Fire', 'amount': 2},
        # Minor Resistances (+1 every 10 levels, staggered)
        {'level': 10, 'resistance': 'Light', 'amount': 1},
        {'level': 15, 'resistance': 'Dark', 'amount': 1},
        {'level': 20, 'resistance': 'Light', 'amount': 1},
        {'level': 25, 'resistance': 'Dark', 'amount': 1},
        {'level': 30, 'resistance': 'Light', 'amount': 1},
        {'level': 35, 'resistance': 'Dark', 'amount': 1},
        {'level': 40, 'resistance': 'Light', 'amount': 1},
        {'level': 45, 'resistance': 'Dark', 'amount': 1},
        {'level': 50, 'resistance': 'Light', 'amount': 1},
        {'level': 55, 'resistance': 'Dark', 'amount': 1},
        {'level': 60, 'resistance': 'Light', 'amount': 1},
    ],
    'abilities': ['fire_bolt'],
    'font_color' : ARCANE_VIOLET
}

PALADIN = {
    'id': 'paladin',
    'display_name': 'Paladin',
    'description': (
        "A holy warrior bound by an oath, the Paladin is a beacon of light and faith "
        "in a dark world. They blend martial prowess with divine magic to protect the "
        "innocent, smite their enemies, and inspire their allies with righteous power."
    ),
    'primary_stats': ['Faith', 'Strength', 'Constitution'],
    'stats': {
        'strength': 2, 'dexterity': 0, 'constitution': 1, 'intellect': 0, 'wisdom': 1, 'charisma': 1, 'faith': 2,
    },
    'resistances': {
        'Toughness': 5,
        'Light': 15,
        'Faith': 10,
        'Chaos': 2, # A small, innate resistance due to their divine connection
    },
    'resistance_progression': [
        {'level': 3, 'resistance': 'Light', 'amount': 3},
        {'level': 5, 'resistance': 'Faith', 'amount': 2},
        {'level': 6, 'resistance': 'Light', 'amount': 3},
        {'level': 6, 'resistance': 'Toughness', 'amount': 3},
        {'level': 9, 'resistance': 'Light', 'amount': 3},
        {'level': 10, 'resistance': 'Faith', 'amount': 2},
        {'level': 12, 'resistance': 'Light', 'amount': 3},
        {'level': 12, 'resistance': 'Toughness', 'amount': 3},
        {'level': 15, 'resistance': 'Light', 'amount': 3},
        {'level': 15, 'resistance': 'Faith', 'amount': 2},
        {'level': 15, 'resistance': 'Chaos', 'amount': 1},
        {'level': 18, 'resistance': 'Light', 'amount': 3},
        {'level': 18, 'resistance': 'Toughness', 'amount': 3},
        {'level': 20, 'resistance': 'Faith', 'amount': 2},
        {'level': 21, 'resistance': 'Light', 'amount': 3},
        {'level': 24, 'resistance': 'Light', 'amount': 3},
        {'level': 24, 'resistance': 'Toughness', 'amount': 3},
        {'level': 25, 'resistance': 'Faith', 'amount': 2},
        {'level': 27, 'resistance': 'Light', 'amount': 3},
        {'level': 30, 'resistance': 'Light', 'amount': 3},
        {'level': 30, 'resistance': 'Faith', 'amount': 2},
        {'level': 30, 'resistance': 'Toughness', 'amount': 3},
        {'level': 30, 'resistance': 'Chaos', 'amount': 1},
        {'level': 33, 'resistance': 'Light', 'amount': 3},
        {'level': 35, 'resistance': 'Faith', 'amount': 2},
        {'level': 36, 'resistance': 'Light', 'amount': 3},
        {'level': 36, 'resistance': 'Toughness', 'amount': 3},
        {'level': 39, 'resistance': 'Light', 'amount': 3},
        {'level': 40, 'resistance': 'Faith', 'amount': 2},
        {'level': 42, 'resistance': 'Light', 'amount': 3},
        {'level': 42, 'resistance': 'Toughness', 'amount': 3},
        {'level': 45, 'resistance': 'Light', 'amount': 3},
        {'level': 45, 'resistance': 'Faith', 'amount': 2},
        {'level': 45, 'resistance': 'Chaos', 'amount': 1},
        {'level': 48, 'resistance': 'Light', 'amount': 3},
        {'level': 48, 'resistance': 'Toughness', 'amount': 3},
        {'level': 50, 'resistance': 'Faith', 'amount': 2},
        {'level': 51, 'resistance': 'Light', 'amount': 3},
        {'level': 54, 'resistance': 'Light', 'amount': 3},
        {'level': 54, 'resistance': 'Toughness', 'amount': 3},
        {'level': 55, 'resistance': 'Faith', 'amount': 2},
        {'level': 57, 'resistance': 'Light', 'amount': 3},
        {'level': 60, 'resistance': 'Light', 'amount': 3},
        {'level': 60, 'resistance': 'Faith', 'amount': 2},
        {'level': 60, 'resistance': 'Toughness', 'amount': 3},
        {'level': 60, 'resistance': 'Chaos', 'amount': 1},
    ],
    'abilities': ['smite'],
    'font_color' : DIVINITY_GOLD
}

RANGER = {
    'id': 'ranger',
    'display_name': 'Ranger',
    'description': (
        "At home in the wilds, the Ranger is a peerless archer, tracker, and survivalist. "
        "They are masters of precision and patience, using their knowledge of the terrain "
        "and their deadly aim to eliminate threats before they ever get close."
    ),
    'primary_stats': ['Dexterity', 'Wisdom'],
    'stats': {
        'strength': 1, 'dexterity': 3, 'constitution': 1, 'intellect': 0, 'wisdom': 2, 'charisma': 0, 'faith': 0,
    },
    'resistances': {
        'Toughness': 2, # A small amount from a rugged life
        'Nature': 15,
        'Frost': 5,
    },
    'resistance_progression': [
        {'level': 3, 'resistance': 'Nature', 'amount': 3},
        {'level': 4, 'resistance': 'Toughness', 'amount': 3},
        {'level': 5, 'resistance': 'Frost', 'amount': 2},
        {'level': 6, 'resistance': 'Nature', 'amount': 3},
        {'level': 8, 'resistance': 'Toughness', 'amount': 3},
        {'level': 9, 'resistance': 'Nature', 'amount': 3},
        {'level': 10, 'resistance': 'Frost', 'amount': 2},
        {'level': 12, 'resistance': 'Nature', 'amount': 3},
        {'level': 12, 'resistance': 'Toughness', 'amount': 3},
        {'level': 15, 'resistance': 'Nature', 'amount': 3},
        {'level': 15, 'resistance': 'Frost', 'amount': 2},
        {'level': 16, 'resistance': 'Toughness', 'amount': 3},
        {'level': 18, 'resistance': 'Nature', 'amount': 3},
        {'level': 20, 'resistance': 'Frost', 'amount': 2},
        {'level': 20, 'resistance': 'Toughness', 'amount': 3},
        {'level': 21, 'resistance': 'Nature', 'amount': 3},
        {'level': 24, 'resistance': 'Nature', 'amount': 3},
        {'level': 24, 'resistance': 'Toughness', 'amount': 3},
        {'level': 25, 'resistance': 'Frost', 'amount': 2},
        {'level': 27, 'resistance': 'Nature', 'amount': 3},
        {'level': 28, 'resistance': 'Toughness', 'amount': 3},
        {'level': 30, 'resistance': 'Nature', 'amount': 3},
        {'level': 30, 'resistance': 'Frost', 'amount': 2},
        {'level': 32, 'resistance': 'Toughness', 'amount': 3},
        {'level': 33, 'resistance': 'Nature', 'amount': 3},
        {'level': 35, 'resistance': 'Frost', 'amount': 2},
        {'level': 36, 'resistance': 'Nature', 'amount': 3},
        {'level': 36, 'resistance': 'Toughness', 'amount': 3},
        {'level': 39, 'resistance': 'Nature', 'amount': 3},
        {'level': 40, 'resistance': 'Frost', 'amount': 2},
        {'level': 40, 'resistance': 'Toughness', 'amount': 3},
        {'level': 42, 'resistance': 'Nature', 'amount': 3},
        {'level': 44, 'resistance': 'Toughness', 'amount': 3},
        {'level': 45, 'resistance': 'Nature', 'amount': 3},
        {'level': 45, 'resistance': 'Frost', 'amount': 2},
        {'level': 48, 'resistance': 'Nature', 'amount': 3},
        {'level': 48, 'resistance': 'Toughness', 'amount': 3},
        {'level': 50, 'resistance': 'Frost', 'amount': 2},
        {'level': 51, 'resistance': 'Nature', 'amount': 3},
        {'level': 52, 'resistance': 'Toughness', 'amount': 3},
        {'level': 54, 'resistance': 'Nature', 'amount': 3},
        {'level': 55, 'resistance': 'Frost', 'amount': 2},
        {'level': 56, 'resistance': 'Toughness', 'amount': 3},
        {'level': 57, 'resistance': 'Nature', 'amount': 3},
        {'level': 60, 'resistance': 'Nature', 'amount': 3},
        {'level': 60, 'resistance': 'Frost', 'amount': 2},
        {'level': 60, 'resistance': 'Toughness', 'amount': 3},
    ],
    'abilities': ['steady_shot'],
    'font_color' : HUNTER_GREEN
}

DRUID = {
    'id': 'druid',
    'display_name': 'Druid',
    'description': (
        "Druids are the guardians of nature's balance. They draw power from the living "
        "world, calling upon the ferocity of beasts, the resilience of the forest, "
        "and the fury of storms. They can be a gentle healer or a fearsome opponent."
    ),
    'primary_stats': ['Wisdom', 'Faith'],
    'stats': {
        'strength': 1, 'dexterity': 0, 'constitution': 1, 'intellect': 1, 'wisdom': 2, 'charisma': 0, 'faith': 2,
    },
    'resistances': {
        'Nature': 20,
        'Lightning': 5,
        'Poison': 15, # I am adding Poison here as a resistance type, it fits the theme well
    },
    'resistance_progression': [
        {'level': 3, 'resistance': 'Nature', 'amount': 3},
        {'level': 4, 'resistance': 'Poison', 'amount': 2},
        {'level': 5, 'resistance': 'Lightning', 'amount': 1},
        {'level': 6, 'resistance': 'Nature', 'amount': 3},
        {'level': 8, 'resistance': 'Poison', 'amount': 2},
        {'level': 9, 'resistance': 'Nature', 'amount': 3},
        {'level': 10, 'resistance': 'Lightning', 'amount': 1},
        {'level': 12, 'resistance': 'Nature', 'amount': 3},
        {'level': 12, 'resistance': 'Poison', 'amount': 2},
        {'level': 15, 'resistance': 'Nature', 'amount': 3},
        {'level': 15, 'resistance': 'Lightning', 'amount': 1},
        {'level': 16, 'resistance': 'Poison', 'amount': 2},
        {'level': 18, 'resistance': 'Nature', 'amount': 3},
        {'level': 20, 'resistance': 'Poison', 'amount': 2},
        {'level': 20, 'resistance': 'Lightning', 'amount': 1},
        {'level': 21, 'resistance': 'Nature', 'amount': 3},
        {'level': 24, 'resistance': 'Nature', 'amount': 3},
        {'level': 24, 'resistance': 'Poison', 'amount': 2},
        {'level': 25, 'resistance': 'Lightning', 'amount': 1},
        {'level': 27, 'resistance': 'Nature', 'amount': 3},
        {'level': 28, 'resistance': 'Poison', 'amount': 2},
        {'level': 30, 'resistance': 'Nature', 'amount': 3},
        {'level': 30, 'resistance': 'Lightning', 'amount': 1},
        {'level': 32, 'resistance': 'Poison', 'amount': 2},
        {'level': 33, 'resistance': 'Nature', 'amount': 3},
        {'level': 35, 'resistance': 'Lightning', 'amount': 1},
        {'level': 36, 'resistance': 'Nature', 'amount': 3},
        {'level': 36, 'resistance': 'Poison', 'amount': 2},
        {'level': 39, 'resistance': 'Nature', 'amount': 3},
        {'level': 40, 'resistance': 'Poison', 'amount': 2},
        {'level': 40, 'resistance': 'Lightning', 'amount': 1},
        {'level': 42, 'resistance': 'Nature', 'amount': 3},
        {'level': 44, 'resistance': 'Poison', 'amount': 2},
        {'level': 45, 'resistance': 'Nature', 'amount': 3},
        {'level': 45, 'resistance': 'Lightning', 'amount': 1},
        {'level': 48, 'resistance': 'Nature', 'amount': 3},
        {'level': 48, 'resistance': 'Poison', 'amount': 2},
        {'level': 50, 'resistance': 'Lightning', 'amount': 1},
        {'level': 51, 'resistance': 'Nature', 'amount': 3},
        {'level': 52, 'resistance': 'Poison', 'amount': 2},
        {'level': 54, 'resistance': 'Nature', 'amount': 3},
        {'level': 55, 'resistance': 'Lightning', 'amount': 1},
        {'level': 56, 'resistance': 'Poison', 'amount': 2},
        {'level': 57, 'resistance': 'Nature', 'amount': 3},
        {'level': 60, 'resistance': 'Nature', 'amount': 3},
        {'level': 60, 'resistance': 'Poison', 'amount': 2},
        {'level': 60, 'resistance': 'Lightning', 'amount': 1},
    ],
    'abilities': ['thorn_lash'],
    'font_color' : EARTHEN_TEAL
}

PRIEST = {
    'id': 'priest',
    'display_name': 'Priest',
    'description': (
        "A conduit for the divine, the Priest is a master of healing and restorative "
        "magic. They devote themselves to a higher power, using their faith to mend "
        "wounds, purge darkness, and shield their allies from harm."
    ),
    'primary_stats': ['Faith', 'Wisdom'],
    'stats': {
        'strength': 0, 'dexterity': 0, 'constitution': 1, 'intellect': 1, 'wisdom': 2, 'charisma': 1, 'faith': 3,
    },
    'resistances': {
        'Light': 10,
        'Darkness': 10,
        'Faith': 20,
        'Chaos': 5, # Their deep faith provides stronger protection against chaos
    },
    'resistance_progression': [
        {'level': 3, 'resistance': 'Faith', 'amount': 3},
        {'level': 6, 'resistance': 'Faith', 'amount': 3},
        {'level': 6, 'resistance': 'Light', 'amount': 2},
        {'level': 9, 'resistance': 'Faith', 'amount': 3},
        {'level': 9, 'resistance': 'Dark', 'amount': 2},
        {'level': 10, 'resistance': 'Chaos', 'amount': 1},
        {'level': 12, 'resistance': 'Faith', 'amount': 3},
        {'level': 12, 'resistance': 'Light', 'amount': 2},
        {'level': 15, 'resistance': 'Faith', 'amount': 3},
        {'level': 15, 'resistance': 'Dark', 'amount': 2},
        {'level': 18, 'resistance': 'Faith', 'amount': 3},
        {'level': 18, 'resistance': 'Light', 'amount': 2},
        {'level': 20, 'resistance': 'Chaos', 'amount': 1},
        {'level': 21, 'resistance': 'Faith', 'amount': 3},
        {'level': 21, 'resistance': 'Dark', 'amount': 2},
        {'level': 24, 'resistance': 'Faith', 'amount': 3},
        {'level': 24, 'resistance': 'Light', 'amount': 2},
        {'level': 27, 'resistance': 'Faith', 'amount': 3},
        {'level': 27, 'resistance': 'Dark', 'amount': 2},
        {'level': 30, 'resistance': 'Faith', 'amount': 3},
        {'level': 30, 'resistance': 'Light', 'amount': 2},
        {'level': 30, 'resistance': 'Chaos', 'amount': 1},
        {'level': 33, 'resistance': 'Faith', 'amount': 3},
        {'level': 33, 'resistance': 'Dark', 'amount': 2},
        {'level': 36, 'resistance': 'Faith', 'amount': 3},
        {'level': 36, 'resistance': 'Light', 'amount': 2},
        {'level': 39, 'resistance': 'Faith', 'amount': 3},
        {'level': 39, 'resistance': 'Dark', 'amount': 2},
        {'level': 40, 'resistance': 'Chaos', 'amount': 1},
        {'level': 42, 'resistance': 'Faith', 'amount': 3},
        {'level': 42, 'resistance': 'Light', 'amount': 2},
        {'level': 45, 'resistance': 'Faith', 'amount': 3},
        {'level': 45, 'resistance': 'Dark', 'amount': 2},
        {'level': 48, 'resistance': 'Faith', 'amount': 3},
        {'level': 48, 'resistance': 'Light', 'amount': 2},
        {'level': 50, 'resistance': 'Chaos', 'amount': 1},
        {'level': 51, 'resistance': 'Faith', 'amount': 3},
        {'level': 51, 'resistance': 'Dark', 'amount': 2},
        {'level': 54, 'resistance': 'Faith', 'amount': 3},
        {'level': 54, 'resistance': 'Light', 'amount': 2},
        {'level': 57, 'resistance': 'Faith', 'amount': 3},
        {'level': 57, 'resistance': 'Dark', 'amount': 2},
        {'level': 60, 'resistance': 'Faith', 'amount': 3},
        {'level': 60, 'resistance': 'Light', 'amount': 2},
        {'level': 60, 'resistance': 'Chaos', 'amount': 1},
    ],
    'abilities': ['heal'],
    'font_color' : SERENE_BLUE
}


# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------

# This dictionary provides easy access to any class's data.
# Example: CLASSES['warrior']['stats']
ALL_CLASSES = {
    'warrior': WARRIOR,
    'mage': MAGE,
    'paladin': PALADIN,
    'ranger': RANGER,
    'druid': DRUID,
    'priest': PRIEST,
}