WARRIOR = {
    'id': 'warrior',
    'display_name': 'Warrior',
    'description': (
        "Masters of martial combat, Warriors thrive in the heart of battle. They rely "
        "on their strength, endurance, and mastery of weapons to overcome their foes. "
        "A Warrior is a bulwark on the battlefield, protecting their allies and "
        "cleaving through enemy lines."
    ),
    'stats': {
        'strength': 3, 'dexterity': 1, 'constitution': 2, 'intellect': 0, 'wisdom': 0, 'charisma': 0, 'faith': 0,
    },
    'resistances': {
        'Toughness': 15, # The defining trait of a Warrior
        'Fire': 5,
    },
    'abilities': []
}

MAGE = {
    'id': 'mage',
    'display_name': 'Mage',
    'description': (
        "Mages are scholars of the arcane, wielding raw elemental power to reshape "
        "the battlefield. They are powerful but fragile, preferring to keep their "
        "distance while unleashing devastating spells of fire, frost, and lightning."
    ),
    'stats': {
        'strength': 0, 'dexterity': 0, 'constitution': 0, 'intellect': 4, 'wisdom': 2, 'charisma': 0, 'faith': 0,
    },
    'resistances': {
        'Frost': 10,
        'Fire': 10,
        'Lightning': 10,
    },
    'abilities': []
}

PALADIN = {
    'id': 'paladin',
    'display_name': 'Paladin',
    'description': (
        "A holy warrior bound by an oath, the Paladin is a beacon of light and faith "
        "in a dark world. They blend martial prowess with divine magic to protect the "
        "innocent, smite their enemies, and inspire their allies with righteous power."
    ),
    'stats': {
        'strength': 2, 'dexterity': 0, 'constitution': 1, 'intellect': 0, 'wisdom': 1, 'charisma': 1, 'faith': 2,
    },
    'resistances': {
        'Toughness': 5,
        'Light': 15,
        'Faith': 10,
        'Chaos': 2, # A small, innate resistance due to their divine connection
    },
    'abilities': []
}

RANGER = {
    'id': 'ranger',
    'display_name': 'Ranger',
    'description': (
        "At home in the wilds, the Ranger is a peerless archer, tracker, and survivalist. "
        "They are masters of precision and patience, using their knowledge of the terrain "
        "and their deadly aim to eliminate threats before they ever get close."
    ),
    'stats': {
        'strength': 1, 'dexterity': 3, 'constitution': 1, 'intellect': 0, 'wisdom': 2, 'charisma': 0, 'faith': 0,
    },
    'resistances': {
        'Toughness': 2, # A small amount from a rugged life
        'Nature': 15,
        'Frost': 5,
    },
    'abilities': []
}

DRUID = {
    'id': 'druid',
    'display_name': 'Druid',
    'description': (
        "Druids are the guardians of nature's balance. They draw power from the living "
        "world, calling upon the ferocity of beasts, the resilience of the forest, "
        "and the fury of storms. They can be a gentle healer or a fearsome opponent."
    ),
    'stats': {
        'strength': 1, 'dexterity': 0, 'constitution': 1, 'intellect': 1, 'wisdom': 2, 'charisma': 0, 'faith': 2,
    },
    'resistances': {
        'Nature': 20,
        'Lightning': 5,
        'Poison': 15, # I am adding Poison here as a resistance type, it fits the theme well
    },
    'abilities': []
}

PRIEST = {
    'id': 'priest',
    'display_name': 'Priest',
    'description': (
        "A conduit for the divine, the Priest is a master of healing and restorative "
        "magic. They devote themselves to a higher power, using their faith to mend "
        "wounds, purge darkness, and shield their allies from harm."
    ),
    'stats': {
        'strength': 0, 'dexterity': 0, 'constitution': 1, 'intellect': 1, 'wisdom': 2, 'charisma': 1, 'faith': 3,
    },
    'resistances': {
        'Light': 10,
        'Darkness': 10,
        'Faith': 20,
        'Chaos': 5, # Their deep faith provides stronger protection against chaos
    },
    'abilities': []
}


# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------

# This dictionary provides easy access to any class's data.
# Example: CLASSES['warrior']['stats']
CLASSES = {
    'warrior': WARRIOR,
    'mage': MAGE,
    'paladin': PALADIN,
    'ranger': RANGER,
    'druid': DRUID,
    'priest': PRIEST,
}