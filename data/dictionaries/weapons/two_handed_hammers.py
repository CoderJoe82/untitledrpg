"""
This file contains all data for Two-Handed Hammers.
Philosophy: High single target damage, mid aoe damage, High cc, High stun.
"""

# --- Common Two-Handed Hammers (Levels 1-15) ---

HEAVY_SLEDGEHAMMER = {
    'id': 'wpn_2h_hammer_001',
    'display_name': 'Heavy Sledgehammer',
    'level_req': 1,
    'rarity': 'Common',
    'min_damage': 15,
    'max_damage': 23,
    'speed': 3.8,
    'stats': {},
    'effects': []
}

IRON_MAUL = {
    'id': 'wpn_2h_hammer_002',
    'display_name': 'Iron Maul',
    'level_req': 7,
    'rarity': 'Common',
    'min_damage': 22,
    'max_damage': 34,
    'speed': 3.9,
    'stats': {'strength': 2},
    'effects': []
}

SPIKED_GREATHAMMER = {
    'id': 'wpn_2h_hammer_003',
    'display_name': 'Spiked Greathammer',
    'level_req': 13,
    'rarity': 'Common',
    'min_damage': 31,
    'max_damage': 47,
    'speed': 4.0,
    'stats': {'strength': 4},
    'effects': []
}


# --- Uncommon Two-Handed Hammers (Levels 15-30) ---

STAGGERING_RAM = {
    'id': 'wpn_2h_hammer_004',
    'display_name': 'Staggering Ram',
    'level_req': 18,
    'rarity': 'Uncommon',
    'min_damage': 41,
    'max_damage': 62,
    'speed': 3.8,
    'stats': {'strength': 7},
    'effects': [
        {'type': 'on_hit_proc', 'chance': 0.10, 'effect': 'knockback', 'distance': 3}
    ]
}

TREMOR_MAUL = {
    'id': 'wpn_2h_hammer_005',
    'display_name': 'Tremor Maul',
    'level_req': 24,
    'rarity': 'Uncommon',
    'min_damage': 53,
    'max_damage': 80,
    'speed': 3.9,
    'stats': {'strength': 9, 'constitution': 5},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'ground_tremor', 'mod': 'increase_slow', 'percent': 0.15}
    ]
}

BELL_RINGER = {
    'id': 'wpn_2h_hammer_006',
    'display_name': 'Bell-Ringer',
    'level_req': 29,
    'rarity': 'Uncommon',
    'min_damage': 62,
    'max_damage': 93,
    'speed': 4.0,
    'stats': {'strength': 11},
    'effects': [
        {'type': 'on_crit_proc', 'effect': 'daze', 'duration': 2.5}
    ]
}


# --- Rare Two-Handed Hammers (Levels 30-45) ---

HAMMER_OF_SUNDERING = {
    'id': 'wpn_2h_hammer_007',
    'display_name': 'Hammer of Sundering',
    'level_req': 35,
    'rarity': 'Rare',
    'min_damage': 78,
    'max_damage': 117,
    'speed': 3.8,
    'stats': {'strength': 18},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'sundering_blow', 'mod': 'aoe_debuff', 'radius': 5, 'percent_effectiveness': 0.50}
    ]
}

EARTHQUAKE_STOMPER = {
    'id': 'wpn_2h_hammer_008',
    'display_name': 'Earthquake Stomper',
    'level_req': 41,
    'rarity': 'Rare',
    'min_damage': 92,
    'max_damage': 138,
    'speed': 3.9,
    'stats': {'strength': 22, 'constitution': 10},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'earthquake', 'mod': 'increase_knockdown_chance', 'percent': 0.15}
    ]
}

JUGGERNAUTS_CRUSHER = {
    'id': 'wpn_2h_hammer_009',
    'display_name': "Juggernaut's Crusher",
    'level_req': 45,
    'rarity': 'Rare',
    'min_damage': 100,
    'max_damage': 150,
    'speed': 4.0,
    'stats': {'strength': 20, 'constitution': 15},
    'effects': [
        {'type': 'on_hit_proc', 'chance': 0.10, 'effect': 'stun', 'duration': 2.0}
    ]
}


# --- Epic Two-Handed Hammers (Levels 45-59) ---

DOOMHAMMER = {
    'id': 'wpn_2h_hammer_010',
    'display_name': 'Doomhammer',
    'level_req': 51,
    'rarity': 'Epic',
    'min_damage': 118,
    'max_damage': 177,
    'speed': 3.7,
    'stats': {'strength': 35, 'dexterity': 10},
    'effects': [
        {'type': 'on_hit_proc', 'chance': 0.15, 'effect': 'chain_lightning', 'max_jumps': 2, 'damage_percent': 0.30}
    ]
}

THE_STUPEFIER = {
    'id': 'wpn_2h_hammer_011',
    'display_name': 'The Stupefier',
    'level_req': 57,
    'rarity': 'Epic',
    'min_damage': 135,
    'max_damage': 203,
    'speed': 3.9,
    'stats': {'strength': 45},
    'effects': [
        {'type': 'on_crit_proc', 'effect': 'stun', 'duration': 3.0}
    ]
}

MOUNTAIN_CRACKER = {
    'id': 'wpn_2h_hammer_012',
    'display_name': 'Mountain-Cracker',
    'level_req': 59,
    'rarity': 'Epic',
    'min_damage': 142,
    'max_damage': 213,
    'speed': 4.0,
    'stats': {'strength': 48, 'constitution': 20},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'thunderclap', 'mod': 'add_daze', 'duration': 4.0}
    ]
}


# --- Legendary Two-Handed Hammers (Level 60) ---

THE_SUNDERING = {
    'id': 'wpn_2h_hammer_legend_001',
    'display_name': 'The Sundering',
    'level_req': 60,
    'rarity': 'Legendary',
    'min_damage': 165,
    'max_damage': 248,
    'speed': 3.8,
    'stats': {'strength': 60, 'constitution': 30},
    'effects': [
        {'type': 'special', 'description': 'Your Meteor Strike stuns for 2 seconds longer and leaves behind a patch of consecrated ground that weakens enemy armor.'}
    ]
}

WORLDBREAKER_MAUL = {
    'id': 'wpn_2h_hammer_legend_002',
    'display_name': 'Worldbreaker Maul',
    'level_req': 60,
    'rarity': 'Legendary',
    'min_damage': 175,
    'max_damage': 263,
    'speed': 4.0,
    'stats': {'strength': 70},
    'effects': [
        {'type': 'special', 'description': 'Your single-target stun effects have a 25% chance to spread to a nearby enemy.'},
        {'type': 'bonus_damage_vs_cc', 'cc_type': ['stun', 'daze'], 'percent': 0.15}
    ]
}


# This dictionary is exported for the game to use.
ALL_TWO_HANDED_HAMMERS = {
    'wpn_2h_hammer_001': HEAVY_SLEDGEHAMMER,
    'wpn_2h_hammer_002': IRON_MAUL,
    'wpn_2h_hammer_003': SPIKED_GREATHAMMER,
    'wpn_2h_hammer_004': STAGGERING_RAM,
    'wpn_2h_hammer_005': TREMOR_MAUL,
    'wpn_2h_hammer_006': BELL_RINGER,
    'wpn_2h_hammer_007': HAMMER_OF_SUNDERING,
    'wpn_2h_hammer_008': EARTHQUAKE_STOMPER,
    'wpn_2h_hammer_009': JUGGERNAUTS_CRUSHER,
    'wpn_2h_hammer_010': DOOMHAMMER,
    'wpn_2h_hammer_011': THE_STUPEFIER,
    'wpn_2h_hammer_012': MOUNTAIN_CRACKER,
    'wpn_2h_hammer_legend_001': THE_SUNDERING,
    'wpn_2h_hammer_legend_002': WORLDBREAKER_MAUL,
}