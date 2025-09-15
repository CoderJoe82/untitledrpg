"""
This file contains all data for Bows.
Philosophy: High single target damage, High range, mid bleed, High crit, low aoe.
"""

# --- Common Bows (Levels 1-15) ---

SHORTBOW = {
    'id': 'wpn_bow_001',
    'display_name': 'Shortbow',
    'level_req': 1,
    'rarity': 'Common',
    'min_damage': 7,
    'max_damage': 12,
    'speed': 2.8,
    'stats': {},
    'effects': []
}

HORN_BOW = {
    'id': 'wpn_bow_002',
    'display_name': 'Horn Bow',
    'level_req': 6,
    'rarity': 'Common',
    'min_damage': 11,
    'max_damage': 18,
    'speed': 2.9,
    'stats': {'dexterity': 1},
    'effects': []
}

HUNTERS_RECURVE = {
    'id': 'wpn_bow_003',
    'display_name': "Hunter's Recurve",
    'level_req': 12,
    'rarity': 'Common',
    'min_damage': 16,
    'max_damage': 26,
    'speed': 2.7,
    'stats': {'dexterity': 3},
    'effects': []
}


# --- Uncommon Bows (Levels 15-30) ---

ASHWOOD_LONGBOW = {
    'id': 'wpn_bow_004',
    'display_name': 'Ashwood Longbow',
    'level_req': 17,
    'rarity': 'Uncommon',
    'min_damage': 22,
    'max_damage': 35,
    'speed': 3.0,
    'stats': {'dexterity': 5},
    'effects': [
        {'type': 'bonus_crit_chance', 'amount': 0.02}
    ]
}

ASSASSINS_COMPOSITE_BOW = {
    'id': 'wpn_bow_005',
    'display_name': "Assassin's Composite Bow",
    'level_req': 23,
    'rarity': 'Uncommon',
    'min_damage': 29,
    'max_damage': 46,
    'speed': 2.8,
    'stats': {'dexterity': 8},
    'effects': [
        {'type': 'bonus_crit_damage', 'amount': 0.05}
    ]
}

BARBED_WARBOW = {
    'id': 'wpn_bow_006',
    'display_name': 'Barbed Warbow',
    'level_req': 28,
    'rarity': 'Uncommon',
    'min_damage': 35,
    'max_damage': 55,
    'speed': 3.1,
    'stats': {'dexterity': 7, 'strength': 3},
    'effects': [
        {'type': 'on_crit_bleed', 'tick_damage': 8, 'duration': 6}
    ]
}


# --- Rare Bows (Levels 30-45) ---

SYLVAN_ELM_BOW = {
    'id': 'wpn_bow_007',
    'display_name': 'Sylvan Elm Bow',
    'level_req': 34,
    'rarity': 'Rare',
    'min_damage': 44,
    'max_damage': 70,
    'speed': 2.9,
    'stats': {'dexterity': 15, 'wisdom': 5},
    'effects': [
        {'type': 'on_hit_proc', 'chance': 0.05, 'effect': 'root', 'duration': 2.0}
    ]
}

HEARTSEEKER = {
    'id': 'wpn_bow_008',
    'display_name': 'Heartseeker',
    'level_req': 40,
    'rarity': 'Rare',
    'min_damage': 52,
    'max_damage': 82,
    'speed': 3.0,
    'stats': {'dexterity': 20},
    'effects': [
        {'type': 'bonus_crit_chance', 'amount': 0.05}
    ]
}

SNIPERS_LONGSHOT = {
    'id': 'wpn_bow_009',
    'display_name': "Sniper's Longshot",
    'level_req': 45,
    'rarity': 'Rare',
    'min_damage': 58,
    'max_damage': 92,
    'speed': 3.2,
    'stats': {'dexterity': 18, 'constitution': 8},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'aimed_shot', 'mod': 'increase_crit_damage', 'percent': 0.25}
    ]
}


# --- Epic Bows (Levels 45-59) ---

WINDRUNNERS_GALE = {
    'id': 'wpn_bow_010',
    'display_name': "Windrunner's Gale",
    'level_req': 51,
    'rarity': 'Epic',
    'min_damage': 68,
    'max_damage': 108,
    'speed': 2.7,
    'stats': {'dexterity': 30, 'wisdom': 10},
    'effects': [
        {'type': 'on_kill_proc', 'effect': 'increase_movement_speed', 'percent': 0.30, 'duration': 8}
    ]
}

VENOMSTRIKE = {
    'id': 'wpn_bow_011',
    'display_name': 'Venomstrike',
    'level_req': 57,
    'rarity': 'Epic',
    'min_damage': 78,
    'max_damage': 124,
    'speed': 2.9,
    'stats': {'dexterity': 38},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'serpent_sting', 'mod': 'can_crit'},
        {'type': 'increase_dot_damage', 'damage_type': 'Poison', 'percent': 0.15}
    ]
}

EAGLE_EYE_BOW = {
    'id': 'wpn_bow_012',
    'display_name': 'Eagle-Eye Bow',
    'level_req': 59,
    'rarity': 'Epic',
    'min_damage': 83,
    'max_damage': 132,
    'speed': 3.1,
    'stats': {'dexterity': 42},
    'effects': [
        {'type': 'increase_range', 'amount': 5},
        {'type': 'bonus_crit_damage', 'amount': 0.20}
    ]
}


# --- Legendary Bows (Level 60) ---

WHISPER_OF_THE_WIND = {
    'id': 'wpn_bow_legend_001',
    'display_name': 'Whisper of the Wind',
    'level_req': 60,
    'rarity': 'Legendary',
    'min_damage': 95,
    'max_damage': 150,
    'speed': 2.8,
    'stats': {'dexterity': 55, 'wisdom': 20},
    'effects': [
        {'type': 'special', 'description': 'Your Aimed Shot critical hits cause the target to bleed for 50% of the damage dealt over 8 seconds.'},
        {'type': 'on_hit_proc', 'chance': 0.10, 'effect': 'increase_haste', 'percent': 0.20, 'duration': 6}
    ]
}

LONGSHOT_THE_HORIZONS_REACH = {
    'id': 'wpn_bow_legend_002',
    'display_name': "Longshot, the Horizon's Reach",
    'level_req': 60,
    'rarity': 'Legendary',
    'min_damage': 105,
    'max_damage': 165,
    'speed': 3.2,
    'stats': {'dexterity': 60},
    'effects': [
        {'type': 'special', 'description': 'Each consecutive Steady Shot against the same target increases the damage of your next Aimed Shot against it by 10%, stacking up to 5 times.'},
        {'type': 'increase_range', 'amount': 10}
    ]
}


# This dictionary is exported for the game to use.
ALL_BOWS = {
    'wpn_bow_001': SHORTBOW,
    'wpn_bow_002': HORN_BOW,
    'wpn_bow_003': HUNTERS_RECURVE,
    'wpn_bow_004': ASHWOOD_LONGBOW,
    'wpn_bow_005': ASSASSINS_COMPOSITE_BOW,
    'wpn_bow_006': BARBED_WARBOW,
    'wpn_bow_007': SYLVAN_ELM_BOW,
    'wpn_bow_008': HEARTSEEKER,
    'wpn_bow_009': SNIPERS_LONGSHOT,
    'wpn_bow_010': WINDRUNNERS_GALE,
    'wpn_bow_011': VENOMSTRIKE,
    'wpn_bow_012': EAGLE_EYE_BOW,
    'wpn_bow_legend_001': WHISPER_OF_THE_WIND,
    'wpn_bow_legend_002': LONGSHOT_THE_HORIZONS_REACH,
}