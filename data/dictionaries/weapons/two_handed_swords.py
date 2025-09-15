"""
This file contains all data for Two-Handed Swords.
Philosophy: High single target damage -> High aoe damage.
"""

# --- Common Two-Handed Swords (Levels 1-15) ---

TRAINING_GREATSWORD = {
    'id': 'wpn_2h_sword_001',
    'display_name': 'Training Greatsword',
    'level_req': 1,
    'rarity': 'Common',
    'min_damage': 12,
    'max_damage': 19,
    'speed': 3.6,
    'stats': {},
    'effects': []
}

MILITIA_CLAYMORE = {
    'id': 'wpn_2h_sword_002',
    'display_name': 'Militia Claymore',
    'level_req': 7,
    'rarity': 'Common',
    'min_damage': 19,
    'max_damage': 29,
    'speed': 3.5,
    'stats': {'strength': 2},
    'effects': []
}

MERCENARYS_ZWEIHANDER = {
    'id': 'wpn_2h_sword_003',
    'display_name': "Mercenary's Zweihander",
    'level_req': 13,
    'rarity': 'Common',
    'min_damage': 27,
    'max_damage': 41,
    'speed': 3.7,
    'stats': {'strength': 3, 'constitution': 1},
    'effects': []
}


# --- Uncommon Two-Handed Swords (Levels 15-30) ---

HEADSMANS_GREATSWORD = {
    'id': 'wpn_2h_sword_004',
    'display_name': "Headsman's Greatsword",
    'level_req': 18,
    'rarity': 'Uncommon',
    'min_damage': 36,
    'max_damage': 55,
    'speed': 3.8,
    'stats': {'strength': 6},
    'effects': [
        {'type': 'bonus_crit_damage', 'amount': 0.05}
    ]
}

BATTLEFIELD_REAVER = {
    'id': 'wpn_2h_sword_005',
    'display_name': 'Battlefield Reaver',
    'level_req': 24,
    'rarity': 'Uncommon',
    'min_damage': 48,
    'max_damage': 72,
    'speed': 3.6,
    'stats': {'strength': 8, 'constitution': 4},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'sweeping_cleave', 'mod': 'increase_damage', 'percent': 0.10}
    ]
}

HIGHLAND_FLAMBERGE = {
    'id': 'wpn_2h_sword_006',
    'display_name': 'Highland Flamberge',
    'level_req': 29,
    'rarity': 'Uncommon',
    'min_damage': 57,
    'max_damage': 86,
    'speed': 3.7,
    'stats': {'strength': 10},
    'effects': [
        {'type': 'on_hit_bleed', 'chance': 0.05, 'tick_damage': 10, 'duration': 6}
    ]
}


# --- Rare Two-Handed Swords (Levels 30-45) ---

TITANS_BLADE = {
    'id': 'wpn_2h_sword_007',
    'display_name': "Titan's Blade",
    'level_req': 35,
    'rarity': 'Rare',
    'min_damage': 70,
    'max_damage': 105,
    'speed': 3.8,
    'stats': {'strength': 15, 'constitution': 7},
    'effects': [
        {'type': 'on_hit_proc', 'chance': 0.10, 'effect': 'stun', 'duration': 1.0}
    ]
}

COLOSSAL_SWORD_OF_SMASHING = {
    'id': 'wpn_2h_sword_008',
    'display_name': 'Colossal Sword of Smashing',
    'level_req': 41,
    'rarity': 'Rare',
    'min_damage': 83,
    'max_damage': 125,
    'speed': 3.9,
    'stats': {'strength': 20},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'colossus_smash', 'mod': 'increase_duration', 'amount': 2.0}
    ]
}

DOOMBLADE = {
    'id': 'wpn_2h_sword_009',
    'display_name': 'Doomblade',
    'level_req': 45,
    'rarity': 'Rare',
    'min_damage': 91,
    'max_damage': 137,
    'speed': 3.6,
    'stats': {'strength': 18, 'dexterity': 8},
    'effects': [
        {'type': 'bonus_damage_vs_debuffed', 'debuff_type': 'armor_reduction', 'percent': 0.08}
    ]
}


# --- Epic Two-Handed Swords (Levels 45-59) ---

VORTEX_GREATSWORD = {
    'id': 'wpn_2h_sword_010',
    'display_name': 'Vortex Greatsword',
    'level_req': 50,
    'rarity': 'Epic',
    'min_damage': 105,
    'max_damage': 158,
    'speed': 3.7,
    'stats': {'strength': 28, 'constitution': 15},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'bladestorm', 'mod': 'pull_enemies_in', 'strength': 5}
    ]
}

CALAMITYS_EDGE = {
    'id': 'wpn_2h_sword_011',
    'display_name': "Calamity's Edge",
    'level_req': 56,
    'rarity': 'Epic',
    'min_damage': 122,
    'max_damage': 183,
    'speed': 3.8,
    'stats': {'strength': 35, 'dexterity': 10},
    'effects': [
        {'type': 'bonus_crit_damage', 'amount': 0.20},
        {'type': 'on_crit_proc', 'effect': 'deal_fire_damage', 'min_damage': 30, 'max_damage': 40}
    ]
}

THE_DECIMATOR = {
    'id': 'wpn_2h_sword_012',
    'display_name': 'The Decimator',
    'level_req': 59,
    'rarity': 'Epic',
    'min_damage': 130,
    'max_damage': 195,
    'speed': 3.9,
    'stats': {'strength': 40},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'execute', 'mod': 'increase_damage', 'percent': 0.15},
    ]
}


# --- Legendary Two-Handed Swords (Level 60) ---

APOCALYPSE = {
    'id': 'wpn_2h_sword_legend_001',
    'display_name': 'Apocalypse',
    'level_req': 60,
    'rarity': 'Legendary',
    'min_damage': 150,
    'max_damage': 225,
    'speed': 3.8,
    'stats': {'strength': 50, 'constitution': 25},
    'effects': [
        {'type': 'special', 'description': 'Your Mortal Strike ability now strikes up to 2 additional nearby targets for 50% damage.'},
        {'type': 'on_kill_proc', 'effect': 'leave_ desecrated_ground', 'damage_type': 'Dark', 'tick_damage': 40, 'duration': 8, 'radius': 6}
    ]
}

WORLDBREAKER = {
    'id': 'wpn_2h_sword_legend_002',
    'display_name': 'Worldbreaker',
    'level_req': 60,
    'rarity': 'Legendary',
    'min_damage': 160,
    'max_damage': 240,
    'speed': 4.0,
    'stats': {'strength': 60},
    'effects': [
        {'type': 'special', 'description': 'Your Execute ability can now be used on targets below 30% health and refunds half its cost if the target does not die.'},
        {'type': 'bonus_damage_vs_elite', 'percent': 0.10}
    ]
}


# This dictionary is exported for the game to use.
ALL_TWO_HANDED_SWORDS = {
    'wpn_2h_sword_001': TRAINING_GREATSWORD,
    'wpn_2h_sword_002': MILITIA_CLAYMORE,
    'wpn_2h_sword_003': MERCENARYS_ZWEIHANDER,
    'wpn_2h_sword_004': HEADSMANS_GREATSWORD,
    'wpn_2h_sword_005': BATTLEFIELD_REAVER,
    'wpn_2h_sword_006': HIGHLAND_FLAMBERGE,
    'wpn_2h_sword_007': TITANS_BLADE,
    'wpn_2h_sword_008': COLOSSAL_SWORD_OF_SMASHING,
    'wpn_2h_sword_009': DOOMBLADE,
    'wpn_2h_sword_010': VORTEX_GREATSWORD,
    'wpn_2h_sword_011': CALAMITYS_EDGE,
    'wpn_2h_sword_012': THE_DECIMATOR,
    'wpn_2h_sword_legend_001': APOCALYPSE,
    'wpn_2h_sword_legend_002': WORLDBREAKER,
}