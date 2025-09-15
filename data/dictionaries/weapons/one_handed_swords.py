"""
This file contains all data for One-Handed Swords.
Philosophy: Low Bleed -> Strong single target -> Mid aoe.
"""

# --- Common One-Handed Swords (Levels 1-15) ---

RUSTY_BROADSWORD = {
    'id': 'wpn_1h_sword_001',
    'display_name': 'Rusty Broadsword',
    'level_req': 1,
    'rarity': 'Common',
    'min_damage': 7,
    'max_damage': 11,
    'speed': 2.6,
    'stats': {},
    'effects': []
}

SOLDIERS_SHORTWWORD = {
    'id': 'wpn_1h_sword_002',
    'display_name': "Soldier's Shortsword",
    'level_req': 6,
    'rarity': 'Common',
    'min_damage': 10,
    'max_damage': 16,
    'speed': 2.4,
    'stats': {'strength': 1},
    'effects': []
}

GUARD_CAPTAINS_ARMING_SWORD = {
    'id': 'wpn_1h_sword_003',
    'display_name': "Guard Captain's Arming Sword",
    'level_req': 11,
    'rarity': 'Common',
    'min_damage': 14,
    'max_damage': 22,
    'speed': 2.7,
    'stats': {'strength': 2},
    'effects': []
}


# --- Uncommon One-Handed Swords (Levels 15-30) ---

WARFORGED_LONGSWORD = {
    'id': 'wpn_1h_sword_004',
    'display_name': 'Warforged Longsword',
    'level_req': 16,
    'rarity': 'Uncommon',
    'min_damage': 20,
    'max_damage': 31,
    'speed': 2.8,
    'stats': {'strength': 4, 'constitution': 2},
    'effects': []
}

GLEAMING_SCIMITAR = {
    'id': 'wpn_1h_sword_005',
    'display_name': 'Gleaming Scimitar',
    'level_req': 22,
    'rarity': 'Uncommon',
    'min_damage': 27,
    'max_damage': 40,
    'speed': 2.5,
    'stats': {'strength': 5, 'dexterity': 3},
    'effects': [
        {'type': 'bonus_crit_chance', 'amount': 0.01}
    ]
}

EXECUTIONERS_BLADE = {
    'id': 'wpn_1h_sword_006',
    'display_name': "Executioner's Blade",
    'level_req': 28,
    'rarity': 'Uncommon',
    'min_damage': 34,
    'max_damage': 51,
    'speed': 2.9,
    'stats': {'strength': 8},
    'effects': [
        {'type': 'bonus_damage_vs_low_health', 'threshold': 0.25, 'percent': 0.05}
    ]
}


# --- Rare One-Handed Swords (Levels 30-45) ---

RUNE_ETCHED_CLAYMORE = {
    'id': 'wpn_1h_sword_007',
    'display_name': 'Rune-Etched Claymore',
    'level_req': 33,
    'rarity': 'Rare',
    'min_damage': 42,
    'max_damage': 64,
    'speed': 2.6,
    'stats': {'strength': 11, 'intellect': 5},
    'effects': [
        {'type': 'on_hit_proc', 'chance': 0.05, 'effect': 'deal_arcane_damage', 'min_damage': 15, 'max_damage': 20}
    ]
}

SERRATED_BASTARD_SWORD = {
    'id': 'wpn_1h_sword_008',
    'display_name': 'Serrated Bastard Sword',
    'level_req': 39,
    'rarity': 'Rare',
    'min_damage': 50,
    'max_damage': 76,
    'speed': 2.8,
    'stats': {'strength': 15},
    'effects': [
        {'type': 'on_hit_bleed', 'chance': 0.10, 'tick_damage': 8, 'duration': 6} # Low bleed chance
    ]
}

KNIGHTLY_RAPIER = {
    'id': 'wpn_1h_sword_009',
    'display_name': 'Knightly Rapier',
    'level_req': 44,
    'rarity': 'Rare',
    'min_damage': 57,
    'max_damage': 85,
    'speed': 2.4,
    'stats': {'strength': 12, 'dexterity': 12},
    'effects': [
        {'type': 'on_parry_proc', 'effect': 'increase_crit_chance', 'percent': 0.25, 'duration': 5}
    ]
}


# --- Epic One-Handed Swords (Levels 45-59) ---

BLADE_OF_A_THOUSAND_CUTS = {
    'id': 'wpn_1h_sword_010',
    'display_name': 'Blade of a Thousand Cuts',
    'level_req': 49,
    'rarity': 'Epic',
    'min_damage': 66,
    'max_damage': 98,
    'speed': 2.5,
    'stats': {'strength': 22, 'dexterity': 15},
    'effects': [
        {'type': 'on_hit_proc', 'chance': 0.15, 'effect': 'strike_again', 'damage_multiplier': 0.40}
    ]
}

AEGIS_EDGE = {
    'id': 'wpn_1h_sword_011',
    'display_name': 'Aegis Edge',
    'level_req': 55,
    'rarity': 'Epic',
    'min_damage': 75,
    'max_damage': 112,
    'speed': 2.8,
    'stats': {'strength': 20, 'constitution': 20},
    'effects': [
        {'type': 'on_block_proc', 'effect': 'gain_absorption_shield', 'amount': 150, 'duration': 10}
    ]
}

WHIRLWIND_SABER = {
    'id': 'wpn_1h_sword_012',
    'display_name': 'Whirlwind Saber',
    'level_req': 59,
    'rarity': 'Epic',
    'min_damage': 81,
    'max_damage': 120,
    'speed': 2.6,
    'stats': {'strength': 30},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'whirlwind', 'mod': 'increase_radius', 'percent': 0.20},
        {'type': 'ability_mod', 'ability_id': 'cleave', 'mod': 'add_target', 'amount': 1}
    ]
}


# --- Legendary One-Handed Swords (Level 60) ---

LIONS_FANG = {
    'id': 'wpn_1h_sword_legend_001',
    'display_name': "Lion's Fang",
    'level_req': 60,
    'rarity': 'Legendary',
    'min_damage': 95,
    'max_damage': 140,
    'speed': 2.7,
    'stats': {'strength': 40, 'constitution': 25},
    'effects': [
        {'type': 'special', 'description': 'Parrying an attack makes your next Heroic Strike a guaranteed critical strike.'},
        {'type': 'increase_threat_generation', 'percent': 0.15}
    ]
}

STORMWEAVER = {
    'id': 'wpn_1h_sword_legend_002',
    'display_name': 'Stormweaver',
    'level_req': 60,
    'rarity': 'Legendary',
    'min_damage': 90,
    'max_damage': 135,
    'speed': 2.5,
    'stats': {'strength': 35, 'dexterity': 20},
    'effects': [
        {'type': 'special', 'description': 'Your Cleave and Whirlwind abilities call down a bolt of lightning on each target hit, dealing additional Nature damage.'},
        {'type': 'on_hit_proc', 'chance': 0.10, 'effect': 'increase_haste', 'percent': 0.15, 'duration': 6}
    ]
}


# This dictionary is exported for the game to use.
ALL_ONE_HANDED_SWORDS = {
    'wpn_1h_sword_001': RUSTY_BROADSWORD,
    'wpn_1h_sword_002': SOLDIERS_SHORTWWORD,
    'wpn_1h_sword_003': GUARD_CAPTAINS_ARMING_SWORD,
    'wpn_1h_sword_004': WARFORGED_LONGSWORD,
    'wpn_1h_sword_005': GLEAMING_SCIMITAR,
    'wpn_1h_sword_006': EXECUTIONERS_BLADE,
    'wpn_1h_sword_007': RUNE_ETCHED_CLAYMORE,
    'wpn_1h_sword_008': SERRATED_BASTARD_SWORD,
    'wpn_1h_sword_009': KNIGHTLY_RAPIER,
    'wpn_1h_sword_010': BLADE_OF_A_THOUSAND_CUTS,
    'wpn_1h_sword_011': AEGIS_EDGE,
    'wpn_1h_sword_012': WHIRLWIND_SABER,
    'wpn_1h_sword_legend_001': LIONS_FANG,
    'wpn_1h_sword_legend_002': STORMWEAVER,
}