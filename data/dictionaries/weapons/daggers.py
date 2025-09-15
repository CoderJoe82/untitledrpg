"""
This file contains all data for Daggers.
Philosophy: High bleed (DoT) damage, low AoE, mid single-target damage.
"""

# --- Common Daggers (Levels 1-15) ---

SHARPENED_STILETTO = {
    'id': 'wpn_dag_001',
    'display_name': 'Sharpened Stiletto',
    'level_req': 1,
    'rarity': 'Common',
    'min_damage': 4,
    'max_damage': 7,
    'speed': 1.6,
    'stats': {},
    'effects': []
}

QUICK_BLADE = {
    'id': 'wpn_dag_002',
    'display_name': 'Quick Blade',
    'level_req': 5,
    'rarity': 'Common',
    'min_damage': 6,
    'max_damage': 10,
    'speed': 1.5,
    'stats': {'dexterity': 1},
    'effects': []
}

PARING_KNIFE = {
    'id': 'wpn_dag_003',
    'display_name': 'Paring Knife',
    'level_req': 9,
    'rarity': 'Common',
    'min_damage': 8,
    'max_damage': 13,
    'speed': 1.7,
    'stats': {'dexterity': 2},
    'effects': []
}


# --- Uncommon Daggers (Levels 15-30) ---

THORNED_KRIS = {
    'id': 'wpn_dag_004',
    'display_name': 'Thorned Kris',
    'level_req': 15,
    'rarity': 'Uncommon',
    'min_damage': 12,
    'max_damage': 18,
    'speed': 1.7,
    'stats': {'dexterity': 4},
    'effects': [
        {'type': 'on_hit_bleed', 'chance': 0.10, 'tick_damage': 4, 'duration': 6}
    ]
}

SURGICAL_DIRK = {
    'id': 'wpn_dag_005',
    'display_name': 'Surgical Dirk',
    'level_req': 21,
    'rarity': 'Uncommon',
    'min_damage': 18,
    'max_damage': 25,
    'speed': 1.6,
    'stats': {'dexterity': 6, 'strength': 2},
    'effects': [
        {'type': 'bonus_crit_chance', 'amount': 0.02}
    ]
}

MAIN_GAUCHE = {
    'id': 'wpn_dag_006',
    'display_name': 'Main Gauche',
    'level_req': 26,
    'rarity': 'Uncommon',
    'min_damage': 22,
    'max_damage': 30,
    'speed': 1.8,
    'stats': {'dexterity': 5, 'constitution': 5},
    'effects': []
}


# --- Rare Daggers (Levels 30-45) ---

GUTTING_KNIFE = {
    'id': 'wpn_dag_007',
    'display_name': 'Gutting Knife',
    'level_req': 32,
    'rarity': 'Rare',
    'min_damage': 29,
    'max_damage': 39,
    'speed': 1.8,
    'stats': {'dexterity': 10, 'constitution': 5},
    'effects': [
        {'type': 'on_hit_bleed', 'chance': 0.20, 'tick_damage': 10, 'duration': 9}
    ]
}

VIPERS_FANG = {
    'id': 'wpn_dag_008',
    'display_name': "Viper's Fang",
    'level_req': 38,
    'rarity': 'Rare',
    'min_damage': 35,
    'max_damage': 46,
    'speed': 1.5,
    'stats': {'dexterity': 14},
    'effects': [
        {'type': 'on_hit_dot', 'damage_type': 'Poison', 'chance': 0.15, 'tick_damage': 12, 'duration': 8}
    ]
}

ASSASSINS_STILETTO = {
    'id': 'wpn_dag_009',
    'display_name': "Assassin's Stiletto",
    'level_req': 43,
    'rarity': 'Rare',
    'min_damage': 40,
    'max_damage': 52,
    'speed': 1.6,
    'stats': {'dexterity': 16},
    'effects': [
        {'type': 'bonus_crit_damage', 'amount': 0.10}
    ]
}


# --- Epic Daggers (Levels 45-59) ---

BLOODLETTER = {
    'id': 'wpn_dag_010',
    'display_name': 'Bloodletter',
    'level_req': 48,
    'rarity': 'Epic',
    'min_damage': 46,
    'max_damage': 60,
    'speed': 1.7,
    'stats': {'dexterity': 20, 'constitution': 10},
    'effects': [
        {'type': 'increase_bleed_damage', 'percent': 0.15},
        {'type': 'on_hit_bleed', 'chance': 0.25, 'tick_damage': 20, 'duration': 12}
    ]
}

SHADOWSPIKE = {
    'id': 'wpn_dag_011',
    'display_name': 'Shadowspike',
    'level_req': 54,
    'rarity': 'Epic',
    'min_damage': 55,
    'max_damage': 72,
    'speed': 1.6,
    'stats': {'dexterity': 28},
    'effects': [
        {'type': 'bonus_damage_from_behind', 'percent': 0.10},
        {'type': 'bonus_crit_chance', 'amount': 0.05}
    ]
}

WIDOWMAKER = {
    'id': 'wpn_dag_012',
    'display_name': 'Widowmaker',
    'level_req': 58,
    'rarity': 'Epic',
    'min_damage': 61,
    'max_damage': 80,
    'speed': 1.8,
    'stats': {'dexterity': 25, 'strength': 12},
    'effects': [
        {'type': 'on_kill_proc', 'effect': 'increase_haste', 'percent': 0.20, 'duration': 8}
    ]
}


# --- Legendary Daggers (Level 60) ---

THE_WEIDLING_FLESH = {
    'id': 'wpn_dag_legend_001',
    'display_name': 'The Widling Flesh',
    'level_req': 60,
    'rarity': 'Legendary',
    'min_damage': 70,
    'max_damage': 92,
    'speed': 1.8,
    'stats': {'dexterity': 40, 'constitution': 20},
    'effects': [
        {'type': 'special', 'description': 'Critical strikes cause all of your active Bleed effects on the target to instantly tick one time.'},
        {'type': 'increase_bleed_duration', 'percent': 0.25}
    ]
}

HEARTSBANE = {
    'id': 'wpn_dag_legend_002',
    'display_name': 'Heartsbane',
    'level_req': 60,
    'rarity': 'Legendary',
    'min_damage': 75,
    'max_damage': 98,
    'speed': 1.6,
    'stats': {'dexterity': 45},
    'effects': [
        {'type': 'special', 'description': 'Your attacks against bleeding targets have a 10% chance to be an automatic critical strike.'},
        {'type': 'bonus_crit_damage', 'amount': 0.15}
    ]
}


# This dictionary is exported for the game to use.
ALL_DAGGERS = {
    'wpn_dag_001': SHARPENED_STILETTO,
    'wpn_dag_002': QUICK_BLADE,
    'wpn_dag_003': PARING_KNIFE,
    'wpn_dag_004': THORNED_KRIS,
    'wpn_dag_005': SURGICAL_DIRK,
    'wpn_dag_006': MAIN_GAUCHE,
    'wpn_dag_007': GUTTING_KNIFE,
    'wpn_dag_008': VIPERS_FANG,
    'wpn_dag_009': ASSASSINS_STILETTO,
    'wpn_dag_010': BLOODLETTER,
    'wpn_dag_011': SHADOWSPIKE,
    'wpn_dag_012': WIDOWMAKER,
    'wpn_dag_legend_001': THE_WEIDLING_FLESH,
    'wpn_dag_legend_002': HEARTSBANE,
}