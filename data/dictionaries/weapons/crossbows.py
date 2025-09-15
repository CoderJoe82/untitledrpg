"""
This file contains all data for Crossbows.
Philosophy: Mid single target damage, Mid range, mid aoe, mid cc.
"""

# --- Common Crossbows (Levels 1-15) ---

LIGHT_CROSSBOW = {
    'id': 'wpn_xbow_001',
    'display_name': 'Light Crossbow',
    'level_req': 1,
    'rarity': 'Common',
    'min_damage': 10,
    'max_damage': 15,
    'speed': 3.2,
    'stats': {},
    'effects': []
}

HUNTERS_CROSSBOW = {
    'id': 'wpn_xbow_002',
    'display_name': "Hunter's Crossbow",
    'level_req': 6,
    'rarity': 'Common',
    'min_damage': 15,
    'max_damage': 23,
    'speed': 3.3,
    'stats': {'dexterity': 1},
    'effects': []
}

HEAVY_CROSSBOW = {
    'id': 'wpn_xbow_003',
    'display_name': 'Heavy Crossbow',
    'level_req': 12,
    'rarity': 'Common',
    'min_damage': 21,
    'max_damage': 32,
    'speed': 3.5,
    'stats': {'dexterity': 3},
    'effects': []
}


# --- Uncommon Crossbows (Levels 15-30) ---

REPEATING_CROSSBOW = {
    'id': 'wpn_xbow_004',
    'display_name': 'Repeating Crossbow',
    'level_req': 17,
    'rarity': 'Uncommon',
    'min_damage': 28,
    'max_damage': 42,
    'speed': 3.0, # Faster than normal for the level
    'stats': {'dexterity': 5},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'reload_mechanism', 'mod': 'reduce_cooldown', 'amount': 5.0}
    ]
}

SIEGE_BOW = {
    'id': 'wpn_xbow_005',
    'display_name': 'Siege Bow',
    'level_req': 23,
    'rarity': 'Uncommon',
    'min_damage': 38,
    'max_damage': 57,
    'speed': 3.6,
    'stats': {'dexterity': 6, 'strength': 3},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'explosive_bolt', 'mod': 'increase_radius', 'percent': 0.15}
    ]
}

TANGLEFOOT_ARBALEST = {
    'id': 'wpn_xbow_006',
    'display_name': 'Tanglefoot Arbalest',
    'level_req': 28,
    'rarity': 'Uncommon',
    'min_damage': 45,
    'max_damage': 68,
    'speed': 3.5,
    'stats': {'dexterity': 9},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'pinning_shot', 'mod': 'increase_duration', 'amount': 1.0}
    ]
}


# --- Rare Crossbows (Levels 30-45) ---

SHRAPNEL_LAUNCHER = {
    'id': 'wpn_xbow_007',
    'display_name': 'Shrapnel Launcher',
    'level_req': 34,
    'rarity': 'Rare',
    'min_damage': 56,
    'max_damage': 84,
    'speed': 3.4,
    'stats': {'dexterity': 15},
    'effects': [
        {'type': 'on_crit_proc', 'effect': 'apply_bleed', 'tick_damage': 10, 'duration': 6}
    ]
}

TRAPMASTERS_COMPANION = {
    'id': 'wpn_xbow_008',
    'display_name': "Trapmaster's Companion",
    'level_req': 40,
    'rarity': 'Rare',
    'min_damage': 65,
    'max_damage': 98,
    'speed': 3.6,
    'stats': {'dexterity': 18, 'constitution': 8},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'caltrops', 'mod': 'increase_slow', 'percent': 0.15}
    ]
}

PRECISION_ENGINEERED_REPEATER = {
    'id': 'wpn_xbow_009',
    'display_name': 'Precision-Engineered Repeater',
    'level_req': 45,
    'rarity': 'Rare',
    'min_damage': 72,
    'max_damage': 108,
    'speed': 3.2,
    'stats': {'dexterity': 22},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'heavy_repeater', 'mod': 'add_shot', 'amount': 1}
    ]
}


# --- Epic Crossbows (Levels 45-59) ---

THE_INCINERATOR = {
    'id': 'wpn_xbow_010',
    'display_name': 'The Incinerator',
    'level_req': 51,
    'rarity': 'Epic',
    'min_damage': 85,
    'max_damage': 128,
    'speed': 3.5,
    'stats': {'dexterity': 30, 'intellect': 12},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'explosive_bolt', 'mod': 'leave_burning_ground', 'tick_damage': 20, 'duration': 5, 'radius': 4}
    ]
}

CHAIN_REACTION = {
    'id': 'wpn_xbow_011',
    'display_name': 'Chain-Reaction',
    'level_req': 57,
    'rarity': 'Epic',
    'min_damage': 98,
    'max_damage': 147,
    'speed': 3.6,
    'stats': {'dexterity': 40},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'double_tap', 'mod': 'affect_all_shots', 'duration': 5}
    ]
}

FORTRESS_DEFENDER = {
    'id': 'wpn_xbow_012',
    'display_name': 'Fortress Defender',
    'level_req': 59,
    'rarity': 'Epic',
    'min_damage': 105,
    'max_damage': 158,
    'speed': 3.8,
    'stats': {'dexterity': 35, 'constitution': 20},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'snipers_nest', 'mod': 'add_toughness_bonus', 'amount': 150}
    ]
}


# --- Legendary Crossbows (Level 60) ---

BURIZA_DO_KYANON = {
    'id': 'wpn_xbow_legend_001',
    'display_name': 'Buriza-Do Kyanon',
    'level_req': 60,
    'rarity': 'Legendary',
    'min_damage': 120,
    'max_damage': 180,
    'speed': 3.4,
    'stats': {'dexterity': 60, 'strength': 20},
    'effects': [
        {'type': 'special', 'description': 'Your Power Shots now pierce through enemies, hitting all targets in a line.'},
        {'type': 'on_hit_proc', 'chance': 0.35, 'effect': 'freeze', 'duration': 1.5}
    ]
}

THE_ARTIFICERS_MASTERPIECE = {
    'id': 'wpn_xbow_legend_002',
    'display_name': "The Artificer's Masterpiece",
    'level_req': 60,
    'rarity': 'Legendary',
    'min_damage': 115,
    'max_damage': 175,
    'speed': 3.2,
    'stats': {'dexterity': 55, 'intellect': 25},
    'effects': [
        {'type': 'special', 'description': 'Your Ballista Turret is now permanent until destroyed and you can have two active at once.'}
    ]
}


# This dictionary is exported for the game to use.
ALL_CROSSBOWS = {
    'wpn_xbow_001': LIGHT_CROSSBOW,
    'wpn_xbow_002': HUNTERS_CROSSBOW,
    'wpn_xbow_003': HEAVY_CROSSBOW,
    'wpn_xbow_004': REPEATING_CROSSBOW,
    'wpn_xbow_005': SIEGE_BOW,
    'wpn_xbow_006': TANGLEFOOT_ARBALEST,
    'wpn_xbow_007': SHRAPNEL_LAUNCHER,
    'wpn_xbow_008': TRAPMASTERS_COMPANION,
    'wpn_xbow_009': PRECISION_ENGINEERED_REPEATER,
    'wpn_xbow_010': THE_INCINERATOR,
    'wpn_xbow_011': CHAIN_REACTION,
    'wpn_xbow_012': FORTRESS_DEFENDER,
    'wpn_xbow_legend_001': BURIZA_DO_KYANON,
    'wpn_xbow_legend_002': THE_ARTIFICERS_MASTERPIECE,
}