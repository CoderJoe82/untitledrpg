"""
This file contains all data for Mage Foci (Staves, Wands, Orbs, etc.).
Philosophy: Focus on mana management, spell empowerment, and utility over raw damage.
"""

# --- Common Foci (Levels 1-15) ---

APPRENTICES_STAFF = {
    'id': 'foci_staff_001',
    'display_name': "Apprentice's Staff",
    'level_req': 1,
    'type': 'Staff',
    'rarity': 'Common',
    'min_damage': 9,
    'max_damage': 14,
    'speed': 3.4,
    'stats': {'intellect': 1},
    'effects': []
}

CARVED_WAND = {
    'id': 'foci_wand_001',
    'display_name': 'Carved Wand',
    'level_req': 6,
    'type': 'Wand',
    'rarity': 'Common',
    'min_damage': 8,
    'max_damage': 13,
    'speed': 2.0,
    'stats': {'intellect': 2},
    'effects': []
}

ACOLYTES_BATTLESTAFF = {
    'id': 'foci_staff_002',
    'display_name': "Acolyte's Battlestaff",
    'level_req': 12,
    'type': 'Staff',
    'rarity': 'Common',
    'min_damage': 18,
    'max_damage': 27,
    'speed': 3.6,
    'stats': {'intellect': 3, 'wisdom': 1},
    'effects': []
}


# --- Uncommon Foci (Levels 15-30) ---

STAFF_OF_THE_ADEPT = {
    'id': 'foci_staff_003',
    'display_name': 'Staff of the Adept',
    'level_req': 17,
    'type': 'Staff',
    'rarity': 'Uncommon',
    'min_damage': 25,
    'max_damage': 38,
    'speed': 3.5,
    'stats': {'intellect': 6},
    'effects': [
        {'type': 'increase_max_mana', 'amount': 50}
    ]
}

TOME_OF_INSIGHT = {
    'id': 'foci_offhand_001',
    'display_name': 'Tome of Insight',
    'level_req': 23,
    'type': 'Tome', # Off-hand item
    'rarity': 'Uncommon',
    'stats': {'intellect': 5, 'wisdom': 5},
    'effects': [
        {'type': 'increase_mana_regen', 'percent': 0.10}
    ]
}

WAND_OF_MANA_TAPPING = {
    'id': 'foci_wand_002',
    'display_name': 'Wand of Mana Tapping',
    'level_req': 28,
    'type': 'Wand',
    'rarity': 'Uncommon',
    'min_damage': 24,
    'max_damage': 36,
    'speed': 2.1,
    'stats': {'intellect': 9},
    'effects': [
        {'type': 'on_kill_proc', 'effect': 'restore_mana', 'percent': 0.05}
    ]
}


# --- Rare Foci (Levels 30-45) ---

ROD_OF_SPELL_ABSORPTION = {
    'id': 'foci_wand_003',
    'display_name': 'Rod of Spell Absorption',
    'level_req': 34,
    'type': 'Wand',
    'rarity': 'Rare',
    'min_damage': 32,
    'max_damage': 48,
    'speed': 2.2,
    'stats': {'intellect': 12, 'constitution': 6},
    'effects': [
        {'type': 'on_successful_interrupt', 'effect': 'restore_mana', 'percent': 0.15}
    ]
}

ARCHMAGES_STAFF_OF_POWER = {
    'id': 'foci_staff_004',
    'display_name': "Archmage's Staff of Power",
    'level_req': 40,
    'type': 'Staff',
    'rarity': 'Rare',
    'min_damage': 58,
    'max_damage': 87,
    'speed': 3.7,
    'stats': {'intellect': 20, 'wisdom': 10},
    'effects': [
        {'type': 'reduce_mana_cost_all', 'percent': 0.05}
    ]
}

ORB_OF_THE_INFINITE_VOID = {
    'id': 'foci_offhand_002',
    'display_name': 'Orb of the Infinite Void',
    'level_req': 45,
    'type': 'Orb', # Off-hand item
    'rarity': 'Rare',
    'stats': {'intellect': 18},
    'effects': [
        {'type': 'on_cast_proc', 'chance': 0.02, 'effect': 'free_cast'},
        {'type': 'increase_max_mana', 'amount': 100}
    ]
}


# --- Epic Foci (Levels 45-59) ---

STAFF_OF_THE_ETHEREAL = {
    'id': 'foci_staff_005',
    'display_name': 'Staff of the Ethereal',
    'level_req': 51,
    'type': 'Staff',
    'rarity': 'Epic',
    'min_damage': 78,
    'max_damage': 117,
    'speed': 3.6,
    'stats': {'intellect': 30, 'wisdom': 15, 'constitution': 10},
    'effects': [
        {'type': 'on_cast_proc', 'chance': 0.10, 'effect': 'gain_absorption_shield', 'amount': 200, 'duration': 10}
    ]
}

SCEPTER_OF_DOMINION = {
    'id': 'foci_wand_004',
    'display_name': 'Scepter of Dominion',
    'level_req': 57,
    'type': 'Wand',
    'rarity': 'Epic',
    'min_damage': 60,
    'max_damage': 90,
    'speed': 2.0,
    'stats': {'intellect': 40},
    'effects': [
        {'type': 'increase_spell_crit_chance', 'amount': 0.05},
        {'type': 'increase_buff_duration', 'percent': 0.15}
    ]
}

CRYSTAL_OF_FORGOTTEN_MEMORIES = {
    'id': 'foci_offhand_003',
    'display_name': 'Crystal of Forgotten Memories',
    'level_req': 59,
    'type': 'Orb',
    'rarity': 'Epic',
    'stats': {'intellect': 25, 'wisdom': 25},
    'effects': [
        {'type': 'ability_mod', 'ability_id': 'any_cooldown_spell', 'mod': 'reduce_cooldown_on_crit', 'amount': 1.0}
    ]
}


# --- Legendary Foci (Level 60) ---

STAFF_OF_THE_TIME_WINDER = {
    'id': 'foci_staff_legend_001',
    'display_name': 'Staff of the Time-Winder',
    'level_req': 60,
    'type': 'Staff',
    'rarity': 'Legendary',
    'min_damage': 105,
    'max_damage': 158,
    'speed': 3.5,
    'stats': {'intellect': 60, 'wisdom': 30},
    'effects': [
        {'type': 'special', 'description': 'Your damaging spells have a chance to grant you a charge of Temporal Shift, making your next spell with a cast time instant.'}
    ]
}

SOUL_EATER_PRISM = {
    'id': 'foci_offhand_legend_001',
    'display_name': 'Soul-Eater Prism',
    'level_req': 60,
    'type': 'Orb',
    'rarity': 'Legendary',
    'stats': {'intellect': 45, 'constitution': 25},
    'effects': [
        {'type': 'special', 'description': 'When you kill an enemy, you steal a remnant of their soul, restoring 10% of your maximum mana and granting a stacking spell damage buff for a short time.'}
    ]
}


# This dictionary is exported for the game to use.
ALL_MAGE_FOCI = {
    'foci_staff_001': APPRENTICES_STAFF,
    'foci_wand_001': CARVED_WAND,
    'foci_staff_002': ACOLYTES_BATTLESTAFF,
    'foci_staff_003': STAFF_OF_THE_ADEPT,
    'foci_offhand_001': TOME_OF_INSIGHT,
    'foci_wand_002': WAND_OF_MANA_TAPPING,
    'foci_wand_003': ROD_OF_SPELL_ABSORPTION,
    'foci_staff_004': ARCHMAGES_STAFF_OF_POWER,
    'foci_offhand_002': ORB_OF_THE_INFINITE_VOID,
    'foci_staff_005': STAFF_OF_THE_ETHEREAL,
    'foci_wand_004': SCEPTER_OF_DOMINION,
    'foci_offhand_003': CRYSTAL_OF_FORGOTTEN_MEMORIES,
    'foci_staff_legend_001': STAFF_OF_THE_TIME_WINDER,
    'foci_offhand_legend_001': SOUL_EATER_PRISM,
}