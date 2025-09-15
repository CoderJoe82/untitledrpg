"""
This file contains all data for Polearms.
Philosophy: High single target, Low Aoe, long melee range, high crit.
"""

# --- Common Polearms (Levels 1-15) ---

IRON_SPEAR = {
    'id': 'wpn_polearm_001',
    'display_name': 'Iron Spear',
    'level_req': 1,
    'rarity': 'Common',
    'min_damage': 9,
    'max_damage': 15,
    'speed': 3.2,
    'stats': {},
    'effects': []
}

ASHWOOD_PIKE = {
    'id': 'wpn_polearm_002',
    'display_name': 'Ashwood Pike',
    'level_req': 6,
    'rarity': 'Common',
    'min_damage': 13,
    'max_damage': 21,
    'speed': 3.3,
    'stats': {'dexterity': 1},
    'effects': []
}

MILITIA_HALBERD = {
    'id': 'wpn_polearm_003',
    'display_name': 'Militia Halberd',
    'level_req': 12,
    'rarity': 'Common',
    'min_damage': 19,
    'max_damage': 30,
    'speed': 3.4,
    'stats': {'dexterity': 3},
    'effects': []
}


# --- Uncommon Polearms (Levels 15-30) ---

SHARPENED_GLAIVE = {
    'id': 'wpn_polearm_004',
    'display_name': 'Sharpened Glaive',
    'level_req': 17,
    'rarity': 'Uncommon',
    'min_damage': 26,
    'max_damage': 41,
    'speed': 3.1,
    'stats': {'dexterity': 5},
    'effects': [
        {'type': 'bonus_crit_chance', 'amount': 0.03}
    ]
}

LEGIONNAIRES_LANCE = {
    'id': 'wpn_polearm_005',
    'display_name': "Legionnaire's Lance",
    'level_req': 23,
    'rarity': 'Uncommon',
    'min_damage': 34,
    'max_damage': 53,
    'speed': 3.5,
    'stats': {'dexterity': 6, 'strength': 3},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'brace', 'mod': 'deal_damage_on_proc', 'percent': 1.5}
    ]
}

BARBED_TRIDENT = {
    'id': 'wpn_polearm_006',
    'display_name': 'Barbed Trident',
    'level_req': 28,
    'rarity': 'Uncommon',
    'min_damage': 41,
    'max_damage': 64,
    'speed': 3.3,
    'stats': {'dexterity': 9},
    'effects': [
        {'type': 'on_crit_bleed', 'tick_damage': 10, 'duration': 6}
    ]
}


# --- Rare Polearms (Levels 30-45) ---

PHALANX_PIKE = {
    'id': 'wpn_polearm_007',
    'display_name': 'Phalanx Pike',
    'level_req': 34,
    'rarity': 'Rare',
    'min_damage': 52,
    'max_damage': 81,
    'speed': 3.2,
    'stats': {'dexterity': 15},
    'effects': [
        {'type': 'bonus_crit_damage', 'amount': 0.15}
    ]
}

IMPALER = {
    'id': 'wpn_polearm_008',
    'display_name': 'Impaler',
    'level_req': 40,
    'rarity': 'Rare',
    'min_damage': 61,
    'max_damage': 95,
    'speed': 3.4,
    'stats': {'dexterity': 18, 'strength': 7},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'skewer', 'mod': 'increase_crit_damage_multiplier', 'amount': 1.0}
    ]
}

WYVERN_CLAW_GUISARME = {
    'id': 'wpn_polearm_009',
    'display_name': 'Wyvern-Claw Guisarme',
    'level_req': 45,
    'rarity': 'Rare',
    'min_damage': 68,
    'max_damage': 106,
    'speed': 3.3,
    'stats': {'dexterity': 22},
    'effects': [
        {'type': 'on_crit_proc', 'effect': 'reduce_armor', 'amount': 100, 'duration': 8}
    ]
}


# --- Epic Polearms (Levels 45-59) ---

AEGIS_PIERCER = {
    'id': 'wpn_polearm_010',
    'display_name': 'Aegis Piercer',
    'level_req': 51,
    'rarity': 'Epic',
    'min_damage': 82,
    'max_damage': 128,
    'speed': 3.5,
    'stats': {'dexterity': 33},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'phalanx_breaker', 'mod': 'increase_armor_pen', 'percent': 0.25}
    ]
}

GALE_STRIKE_HALBERD = {
    'id': 'wpn_polearm_011',
    'display_name': 'Gale-Strike Halberd',
    'level_req': 57,
    'rarity': 'Epic',
    'min_damage': 94,
    'max_damage': 147,
    'speed': 3.2,
    'stats': {'dexterity': 40, 'strength': 15},
    'effects': [
        {'type': 'on_crit_proc', 'effect': 'increase_haste', 'percent': 0.25, 'duration': 6}
    ]
}

DRAGONSLAYERS_LANCE = {
    'id': 'wpn_polearm_012',
    'display_name': "Dragonslayer's Lance",
    'level_req': 59,
    'rarity': 'Epic',
    'min_damage': 100,
    'max_damage': 156,
    'speed': 3.4,
    'stats': {'dexterity': 45},
    'effects': [
        {'type': 'bonus_crit_chance', 'amount': 0.05},
        {'type': 'bonus_crit_damage', 'amount': 0.20}
    ]
}


# --- Legendary Polearms (Level 60) ---

SKY_PIERCER = {
    'id': 'wpn_polearm_legend_001',
    'display_name': 'Sky-Piercer',
    'level_req': 60,
    'rarity': 'Legendary',
    'min_damage': 118,
    'max_damage': 184,
    'speed': 3.3,
    'stats': {'dexterity': 65},
    'effects': [
        {'type': 'special', 'description': 'Your critical strikes with Thrust and Precision Strike have a 20% chance to reset their own cooldown.'},
        {'type': 'bonus_crit_damage', 'amount': 0.25}
    ]
}

THE_BLACK_REAPING = {
    'id': 'wpn_polearm_legend_002',
    'display_name': 'The Black Reaping',
    'level_req': 60,
    'rarity': 'Legendary',
    'min_damage': 112,
    'max_damage': 175,
    'speed': 3.1,
    'stats': {'dexterity': 50, 'strength': 20},
    'effects': [
        {'type': 'special', 'description': 'Your Sweep ability now applies a bleed to all targets hit. Critical strikes against bleeding targets root them for 2 seconds.'},
    ]
}


# This dictionary is exported for the game to use.
ALL_POLEARMS = {
    'wpn_polearm_001': IRON_SPEAR,
    'wpn_polearm_002': ASHWOOD_PIKE,
    'wpn_polearm_003': MILITIA_HALBERD,
    'wpn_polearm_004': SHARPENED_GLAIVE,
    'wpn_polearm_005': LEGIONNAIRES_LANCE,
    'wpn_polearm_006': BARBED_TRIDENT,
    'wpn_polearm_007': PHALANX_PIKE,
    'wpn_polearm_008': IMPALER,
    'wpn_polearm_009': WYVERN_CLAW_GUISARME,
    'wpn_polearm_010': AEGIS_PIERCER,
    'wpn_polearm_011': GALE_STRIKE_HALBERD,
    'wpn_polearm_012': DRAGONSLAYERS_LANCE,
    'wpn_polearm_legend_001': SKY_PIERCER,
    'wpn_polearm_legend_002': THE_BLACK_REAPING,
}