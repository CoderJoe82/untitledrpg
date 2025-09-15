"""
This file contains all data for One-Handed Axes.
Philosophy: Mid bleed -> High single target damage -> Mid aoe.
"""

# --- Common One-Handed Axes (Levels 1-15) ---

RUSTY_HATCHET = {
    'id': 'wpn_1h_axe_001',
    'display_name': 'Rusty Hatchet',
    'level_req': 1,
    'rarity': 'Common',
    'min_damage': 8,
    'max_damage': 12,
    'speed': 2.7,
    'stats': {},
    'effects': []
}

WOODSMANS_AXE = {
    'id': 'wpn_1h_axe_002',
    'display_name': "Woodsman's Axe",
    'level_req': 6,
    'rarity': 'Common',
    'min_damage': 12,
    'max_damage': 18,
    'speed': 2.8,
    'stats': {'strength': 1},
    'effects': []
}

RAIDERS_HANDAXE = {
    'id': 'wpn_1h_axe_003',
    'display_name': "Raider's Handaxe",
    'level_req': 12,
    'rarity': 'Common',
    'min_damage': 17,
    'max_damage': 25,
    'speed': 2.6,
    'stats': {'strength': 3},
    'effects': []
}


# --- Uncommon One-Handed Axes (Levels 15-30) ---

BARBED_TOMAHAWK = {
    'id': 'wpn_1h_axe_004',
    'display_name': 'Barbed Tomahawk',
    'level_req': 17,
    'rarity': 'Uncommon',
    'min_damage': 23,
    'max_damage': 34,
    'speed': 2.7,
    'stats': {'strength': 5},
    'effects': [
        {'type': 'on_hit_bleed', 'chance': 0.15, 'tick_damage': 5, 'duration': 6}
    ]
}

BROADHEAD_CLEAVER = {
    'id': 'wpn_1h_axe_005',
    'display_name': 'Broadhead Cleaver',
    'level_req': 23,
    'rarity': 'Uncommon',
    'min_damage': 30,
    'max_damage': 45,
    'speed': 2.9,
    'stats': {'strength': 7, 'constitution': 3},
    'effects': [
        {'type': 'bonus_crit_chance', 'amount': 0.02}
    ]
}

VIKING_BOARDING_AXE = {
    'id': 'wpn_1h_axe_006',
    'display_name': 'Viking Boarding Axe',
    'level_req': 28,
    'rarity': 'Uncommon',
    'min_damage': 36,
    'max_damage': 54,
    'speed': 2.8,
    'stats': {'strength': 9},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'wide_swing', 'mod': 'increase_damage', 'percent': 0.10}
    ]
}


# --- Rare One-Handed Axes (Levels 30-45) ---

RENDING_HATCHET = {
    'id': 'wpn_1h_axe_007',
    'display_name': 'Rending Hatchet',
    'level_req': 34,
    'rarity': 'Rare',
    'min_damage': 46,
    'max_damage': 68,
    'speed': 2.6,
    'stats': {'strength': 13, 'dexterity': 5},
    'effects': [
        {'type': 'on_hit_bleed', 'chance': 0.20, 'tick_damage': 12, 'duration': 8}
    ]
}

HEADTAKER = {
    'id': 'wpn_1h_axe_008',
    'display_name': 'Headtaker',
    'level_req': 40,
    'rarity': 'Rare',
    'min_damage': 54,
    'max_damage': 81,
    'speed': 2.9,
    'stats': {'strength': 18},
    'effects': [
        {'type': 'on_kill_proc', 'effect': 'increase_strength', 'amount': 10, 'duration': 10}
    ]
}

BERSERKERS_AXE = {
    'id': 'wpn_1h_axe_009',
    'display_name': "Berserker's Axe",
    'level_req': 45,
    'rarity': 'Rare',
    'min_damage': 60,
    'max_damage': 90,
    'speed': 2.7,
    'stats': {'strength': 15, 'constitution': 10},
    'effects': [
        {'type': 'bonus_damage_when_low_health', 'threshold': 0.30, 'percent': 0.10}
    ]
}


# --- Epic One-Handed Axes (Levels 45-59) ---

BLOOD_GOUGER = {
    'id': 'wpn_1h_axe_010',
    'display_name': 'Blood-Gouger',
    'level_req': 50,
    'rarity': 'Epic',
    'min_damage': 70,
    'max_damage': 105,
    'speed': 2.8,
    'stats': {'strength': 25, 'constitution': 12},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'mutilate', 'mod': 'increase_bonus_damage', 'percent': 0.15},
        {'type': 'increase_bleed_damage', 'percent': 0.10}
    ]
}

FRENZIED_WAR_AXE = {
    'id': 'wpn_1h_axe_011',
    'display_name': 'Frenzied War Axe',
    'level_req': 56,
    'rarity': 'Epic',
    'min_damage': 80,
    'max_damage': 120,
    'speed': 2.6,
    'stats': {'strength': 30, 'dexterity': 15},
    'effects': [
        {'type': 'on_crit_proc', 'effect': 'increase_haste', 'percent': 0.20, 'duration': 6}
    ]
}

THE_DEMOLISHER = {
    'id': 'wpn_1h_axe_012',
    'display_name': 'The Demolisher',
    'level_req': 59,
    'rarity': 'Epic',
    'min_damage': 85,
    'max_damage': 128,
    'speed': 2.9,
    'stats': {'strength': 38},
    'effects': [
        {'type': 'bonus_damage_vs_debuffed', 'debuff_type': 'armor_reduction', 'percent': 0.12}
    ]
}


# --- Legendary One-Handed Axes (Level 60) ---

HELLSCREAM = {
    'id': 'wpn_1h_axe_legend_001',
    'display_name': 'Hellscream',
    'level_req': 60,
    'rarity': 'Legendary',
    'min_damage': 100,
    'max_damage': 150,
    'speed': 2.8,
    'stats': {'strength': 50, 'constitution': 20},
    'effects': [
        {'type': 'special', 'description': 'Activating Rampage also applies a powerful bleed to your current target.'},
        {'type': 'on_hit_proc', 'chance': 0.05, 'effect': 'fear', 'duration': 2.0}
    ]
}

RAGE_OF_THE_UNBROKEN = {
    'id': 'wpn_1h_axe_legend_002',
    'display_name': 'Rage of the Unbroken',
    'level_req': 60,
    'rarity': 'Legendary',
    'min_damage': 95,
    'max_damage': 145,
    'speed': 2.6,
    'stats': {'strength': 45, 'dexterity': 15},
    'effects': [
        {'type': 'special', 'description': 'Each consecutive strike against the same target increases your damage dealt to it by 2%, stacking up to 10 times.'},
        {'type': 'bonus_crit_chance', 'amount': 0.05}
    ]
}


# This dictionary is exported for the game to use.
ALL_ONE_HANDED_AXES = {
    'wpn_1h_axe_001': RUSTY_HATCHET,
    'wpn_1h_axe_002': WOODSMANS_AXE,
    'wpn_1h_axe_003': RAIDERS_HANDAXE,
    'wpn_1h_axe_004': BARBED_TOMAHAWK,
    'wpn_1h_axe_005': BROADHEAD_CLEAVER,
    'wpn_1h_axe_006': VIKING_BOARDING_AXE,
    'wpn_1h_axe_007': RENDING_HATCHET,
    'wpn_1h_axe_008': HEADTAKER,
    'wpn_1h_axe_009': BERSERKERS_AXE,
    'wpn_1h_axe_010': BLOOD_GOUGER,
    'wpn_1h_axe_011': FRENZIED_WAR_AXE,
    'wpn_1h_axe_012': THE_DEMOLISHER,
    'wpn_1h_axe_legend_001': HELLSCREAM,
    'wpn_1h_axe_legend_002': RAGE_OF_THE_UNBROKEN,
}