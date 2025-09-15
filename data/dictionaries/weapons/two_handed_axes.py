"""
This file contains all data for Two-Handed Axes.
Philosophy: Mid bleed, High single target damage, High aoe bleed, Mid aoe damage.
"""

# --- Common Two-Handed Axes (Levels 1-15) ---

LUMBERJACKS_GREATAXE = {
    'id': 'wpn_2h_axe_001',
    'display_name': "Lumberjack's Greataxe",
    'level_req': 1,
    'rarity': 'Common',
    'min_damage': 14,
    'max_damage': 21,
    'speed': 3.7,
    'stats': {},
    'effects': []
}

BRIGANDS_BATTLEAXE = {
    'id': 'wpn_2h_axe_002',
    'display_name': "Brigand's Battleaxe",
    'level_req': 7,
    'rarity': 'Common',
    'min_damage': 21,
    'max_damage': 32,
    'speed': 3.8,
    'stats': {'strength': 2},
    'effects': []
}

HEADSMANS_AXE = {
    'id': 'wpn_2h_axe_003',
    'display_name': "Headsman's Axe",
    'level_req': 13,
    'rarity': 'Common',
    'min_damage': 30,
    'max_damage': 45,
    'speed': 3.9,
    'stats': {'strength': 4},
    'effects': []
}


# --- Uncommon Two-Handed Axes (Levels 15-30) ---

GASHING_BARDICHE = {
    'id': 'wpn_2h_axe_004',
    'display_name': 'Gashing Bardiche',
    'level_req': 18,
    'rarity': 'Uncommon',
    'min_damage': 40,
    'max_damage': 60,
    'speed': 3.7,
    'stats': {'strength': 7},
    'effects': [
        {'type': 'on_crit_bleed', 'tick_damage': 8, 'duration': 6}
    ]
}

RECKLESS_CLEAVER = {
    'id': 'wpn_2h_axe_005',
    'display_name': 'Reckless Cleaver',
    'level_req': 24,
    'rarity': 'Uncommon',
    'min_damage': 51,
    'max_damage': 77,
    'speed': 3.8,
    'stats': {'strength': 9, 'constitution': 5},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'reckless_swing', 'mod': 'increase_damage', 'percent': 0.15}
    ]
}

DOUBLE_BITTED_TERROR = {
    'id': 'wpn_2h_axe_006',
    'display_name': 'Double-Bitted Terror',
    'level_req': 29,
    'rarity': 'Uncommon',
    'min_damage': 60,
    'max_damage': 90,
    'speed': 3.9,
    'stats': {'strength': 11},
    'effects': [
        {'type': 'bonus_crit_chance', 'amount': 0.03}
    ]
}


# --- Rare Two-Handed Axes (Levels 30-45) ---

WHIRLWIND_AXE = {
    'id': 'wpn_2h_axe_007',
    'display_name': 'Whirlwind Axe',
    'level_req': 36,
    'rarity': 'Rare',
    'min_damage': 75,
    'max_damage': 113,
    'speed': 3.6,
    'stats': {'strength': 18, 'dexterity': 7},
    'effects': [
        {'type': 'on_hit_proc', 'chance': 0.10, 'effect': 'haste_self', 'percent': 0.15, 'duration': 5}
    ]
}

BONESNAPPER = {
    'id': 'wpn_2h_axe_008',
    'display_name': 'Bonesnapper',
    'level_req': 42,
    'rarity': 'Rare',
    'min_damage': 88,
    'max_damage': 132,
    'speed': 3.8,
    'stats': {'strength': 22},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'mangle', 'mod': 'increase_bonus_damage', 'percent': 0.20}
    ]
}

HEMOGLOBIN_HARVESTER = {
    'id': 'wpn_2h_axe_009',
    'display_name': 'Hemoglobin Harvester',
    'level_req': 45,
    'rarity': 'Rare',
    'min_damage': 95,
    'max_damage': 143,
    'speed': 3.7,
    'stats': {'strength': 20, 'constitution': 12},
    'effects': [
        {'type': 'on_hit_bleed', 'chance': 0.25, 'tick_damage': 20, 'duration': 9}
    ]
}


# --- Epic Two-Handed Axes (Levels 45-59) ---

SPINAL_REAPER = {
    'id': 'wpn_2h_axe_010',
    'display_name': 'Spinal Reaper',
    'level_req': 51,
    'rarity': 'Epic',
    'min_damage': 112,
    'max_damage': 168,
    'speed': 3.8,
    'stats': {'strength': 33, 'constitution': 15},
    'effects': [
        {'type': 'bonus_damage_vs_bleeding', 'percent': 0.10},
        {'type': 'increase_bleed_damage', 'percent': 0.15}
    ]
}

AVATARS_GREATAXE = {
    'id': 'wpn_2h_axe_011',
    'display_name': "Avatar's Greataxe",
    'level_req': 57,
    'rarity': 'Epic',
    'min_damage': 128,
    'max_damage': 192,
    'speed': 3.9,
    'stats': {'strength': 42},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'avatar_of_slaughter', 'mod': 'increase_duration', 'amount': 5.0}
    ]
}

GOREHOWL = {
    'id': 'wpn_2h_axe_012',
    'display_name': 'Gorehowl',
    'level_req': 59,
    'rarity': 'Epic',
    'min_damage': 135,
    'max_damage': 203,
    'speed': 3.6,
    'stats': {'strength': 45},
    'effects': [
        {'type': 'on_kill_proc', 'effect': 'gain_rampage', 'duration': 8}
    ]
}


# --- Legendary Two-Handed Axes (Level 60) ---

BLOODSTORM = {
    'id': 'wpn_2h_axe_legend_001',
    'display_name': 'Bloodstorm',
    'level_req': 60,
    'rarity': 'Legendary',
    'min_damage': 158,
    'max_damage': 237,
    'speed': 3.7,
    'stats': {'strength': 55, 'constitution': 25},
    'effects': [
        {'type': 'special', 'description': 'Your Whirlwind and Cyclone of Carnage abilities now also apply your Gash bleed to all targets hit.'},
        {'type': 'bonus_crit_damage', 'amount': 0.15}
    ]
}

THE_EXECUTIONER = {
    'id': 'wpn_2h_axe_legend_002',
    'display_name': 'The Executioner',
    'level_req': 60,
    'rarity': 'Legendary',
    'min_damage': 170,
    'max_damage': 255,
    'speed': 4.0,
    'stats': {'strength': 65},
    'effects': [
        {'type': 'special', 'description': 'Killing an enemy with Decapitate resets its cooldown.'},
        {'type': 'bonus_damage_vs_elite', 'percent': 0.10}
    ]
}


# This dictionary is exported for the game to use.
ALL_TWO_HANDED_AXES = {
    'wpn_2h_axe_001': LUMBERJACKS_GREATAXE,
    'wpn_2h_axe_002': BRIGANDS_BATTLEAXE,
    'wpn_2h_axe_003': HEADSMANS_AXE,
    'wpn_2h_axe_004': GASHING_BARDICHE,
    'wpn_2h_axe_005': RECKLESS_CLEAVER,
    'wpn_2h_axe_006': DOUBLE_BITTED_TERROR,
    'wpn_2h_axe_007': WHIRLWIND_AXE,
    'wpn_2h_axe_008': BONESNAPPER,
    'wpn_2h_axe_009': HEMOGLOBIN_HARVESTER,
    'wpn_2h_axe_010': SPINAL_REAPER,
    'wpn_2h_axe_011': AVATARS_GREATAXE,
    'wpn_2h_axe_012': GOREHOWL,
    'wpn_2h_axe_legend_001': BLOODSTORM,
    'wpn_2h_axe_legend_002': THE_EXECUTIONER,
}