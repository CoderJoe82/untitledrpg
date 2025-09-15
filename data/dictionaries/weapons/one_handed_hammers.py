"""
This file contains all data for One-Handed Hammers.
Philosophy: Mid single target damage, Low aoe damage, mid cc, mid stun.
"""

# --- Common One-Handed Hammers (Levels 1-15) ---

RUSTY_MALLET = {
    'id': 'wpn_1h_hammer_001',
    'display_name': 'Rusty Mallet',
    'level_req': 1,
    'rarity': 'Common',
    'min_damage': 8,
    'max_damage': 13,
    'speed': 2.8,
    'stats': {},
    'effects': []
}

BLACKSMITHS_HAMMER = {
    'id': 'wpn_1h_hammer_002',
    'display_name': "Blacksmith's Hammer",
    'level_req': 6,
    'rarity': 'Common',
    'min_damage': 11,
    'max_damage': 17,
    'speed': 2.9,
    'stats': {'strength': 1},
    'effects': []
}

GUARDSMANS_WARHAMMER = {
    'id': 'wpn_1h_hammer_003',
    'display_name': "Guardsman's Warhammer",
    'level_req': 12,
    'rarity': 'Common',
    'min_damage': 16,
    'max_damage': 24,
    'speed': 3.0,
    'stats': {'strength': 3},
    'effects': []
}


# --- Uncommon One-Handed Hammers (Levels 15-30) ---

BONECRACKER = {
    'id': 'wpn_1h_hammer_004',
    'display_name': 'Bonecracker',
    'level_req': 17,
    'rarity': 'Uncommon',
    'min_damage': 22,
    'max_damage': 33,
    'speed': 2.8,
    'stats': {'strength': 4, 'constitution': 2},
    'effects': [
        {'type': 'on_hit_proc', 'chance': 0.05, 'effect': 'daze', 'duration': 2}
    ]
}

CONCUSSIVE_MACE = {
    'id': 'wpn_1h_hammer_005',
    'display_name': 'Concussive Mace',
    'level_req': 23,
    'rarity': 'Uncommon',
    'min_damage': 29,
    'max_damage': 44,
    'speed': 3.0,
    'stats': {'strength': 8},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'concuss', 'mod': 'increase_duration', 'amount': 2.0}
    ]
}

HEAVY_IRON_GAVEL = {
    'id': 'wpn_1h_hammer_006',
    'display_name': 'Heavy Iron Gavel',
    'level_req': 28,
    'rarity': 'Uncommon',
    'min_damage': 35,
    'max_damage': 53,
    'speed': 3.1,
    'stats': {'strength': 7, 'constitution': 5},
    'effects': [
        {'type': 'on_hit_proc', 'chance': 0.10, 'effect': 'slow_attack_speed', 'percent': 0.10, 'duration': 5}
    ]
}


# --- Rare One-Handed Hammers (Levels 30-45) ---

STONEMASONS_MAUL = {
    'id': 'wpn_1h_hammer_007',
    'display_name': "Stonemason's Maul",
    'level_req': 34,
    'rarity': 'Rare',
    'min_damage': 45,
    'max_damage': 67,
    'speed': 2.9,
    'stats': {'strength': 12, 'constitution': 6},
    'effects': [
        {'type': 'on_hit_proc', 'chance': 0.08, 'effect': 'stun', 'duration': 1.5}
    ]
}

HAMMER_OF_JUDGMENT = {
    'id': 'wpn_1h_hammer_008',
    'display_name': 'Hammer of Judgment',
    'level_req': 40,
    'rarity': 'Rare',
    'min_damage': 53,
    'max_damage': 80,
    'speed': 3.0,
    'stats': {'strength': 18},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'hammer_of_justice', 'mod': 'increase_duration', 'amount': 1.0}
    ]
}

SKULL_RATTLER = {
    'id': 'wpn_1h_hammer_009',
    'display_name': 'Skull-Rattler',
    'level_req': 45,
    'rarity': 'Rare',
    'min_damage': 59,
    'max_damage': 89,
    'speed': 2.8,
    'stats': {'strength': 15, 'dexterity': 8},
    'effects': [
        {'type': 'on_crit_proc', 'effect': 'daze', 'duration': 3.0}
    ]
}


# --- Epic One-Handed Hammers (Levels 45-59) ---

EARTHSHAKER = {
    'id': 'wpn_1h_hammer_010',
    'display_name': 'Earthshaker',
    'level_req': 51,
    'rarity': 'Epic',
    'min_damage': 72,
    'max_damage': 108,
    'speed': 3.1,
    'stats': {'strength': 28, 'constitution': 15},
    'effects': [
        {'type': 'on_crit_proc', 'effect': 'aoe_slow', 'radius': 6, 'percent': 0.30, 'duration': 5}
    ]
}

UNSTOPPABLE_JUSTICE = {
    'id': 'wpn_1h_hammer_011',
    'display_name': 'Unstoppable Justice',
    'level_req': 57,
    'rarity': 'Epic',
    'min_damage': 82,
    'max_damage': 123,
    'speed': 3.0,
    'stats': {'strength': 35, 'constitution': 18},
    'effects': [
        {'type': 'on_stun_proc', 'effect': 'increase_haste', 'percent': 0.20, 'duration': 6}
    ]
}

THE_PACIFIER = {
    'id': 'wpn_1h_hammer_012',
    'display_name': 'The Pacifier',
    'level_req': 59,
    'rarity': 'Epic',
    'min_damage': 86,
    'max_damage': 129,
    'speed': 2.9,
    'stats': {'strength': 40},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'dazing_blow', 'mod': 'change_to_stun', 'duration': 2.0}
    ]
}


# --- Legendary One-Handed Hammers (Level 60) ---

THE_GAVEL_OF_TYRANNY = {
    'id': 'wpn_1h_hammer_legend_001',
    'display_name': 'The Gavel of Tyranny',
    'level_req': 60,
    'rarity': 'Legendary',
    'min_damage': 102,
    'max_damage': 153,
    'speed': 3.0,
    'stats': {'strength': 50, 'constitution': 25},
    'effects': [
        {'type': 'special', 'description': 'Your stun effects last 1 second longer. When you stun a target, their Toughness is reduced by 50% for the duration.'}
    ]
}

WORLDFORGERS_ANVIL = {
    'id': 'wpn_1h_hammer_legend_002',
    'display_name': "Worldforger's Anvil",
    'level_req': 60,
    'rarity': 'Legendary',
    'min_damage': 98,
    'max_damage': 148,
    'speed': 2.8,
    'stats': {'strength': 45, 'dexterity': 10},
    'effects': [
        {'type': 'special', 'description': 'When you successfully stun a single target, a shockwave erupts, dazing all other nearby enemies for 3 seconds.'}
    ]
}


# This dictionary is exported for the game to use.
ALL_ONE_HANDED_HAMMERS = {
    'wpn_1h_hammer_001': RUSTY_MALLET,
    'wpn_1h_hammer_002': BLACKSMITHS_HAMMER,
    'wpn_1h_hammer_003': GUARDSMANS_WARHAMMER,
    'wpn_1h_hammer_004': BONECRACKER,
    'wpn_1h_hammer_005': CONCUSSIVE_MACE,
    'wpn_1h_hammer_006': HEAVY_IRON_GAVEL,
    'wpn_1h_hammer_007': STONEMASONS_MAUL,
    'wpn_1h_hammer_008': HAMMER_OF_JUDGMENT,
    'wpn_1h_hammer_009': SKULL_RATTLER,
    'wpn_1h_hammer_010': EARTHSHAKER,
    'wpn_1h_hammer_011': UNSTOPPABLE_JUSTICE,
    'wpn_1h_hammer_012': THE_PACIFIER,
    'wpn_1h_hammer_legend_001': THE_GAVEL_OF_TYRANNY,
    'wpn_1h_hammer_legend_002': WORLDFORGERS_ANVIL,
}