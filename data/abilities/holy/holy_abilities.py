"""
This file contains all data for Holy school abilities.

Philosophy: High single-target healing, low AoE healing, high AoE shielding,
and low cleansing capabilities. The playstyle is focused on powerful, focused
heals to save individuals and blanketing the group in proactive shields.
"""

# -----------------------------------------------------------------------------
# TIER 1: APPRENTICE (Level 1-14)
# -----------------------------------------------------------------------------

HEAL = {
    'id': 'heal', 'display_name': 'Heal',
    'description': 'A slow but powerful and efficient spell that heals a single ally for a large amount.',
    'level_req': 1, 'mana_cost': 28, 'cooldown': 0.0, 'casting_time': 2.2, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'direct_heal', 'min_healing': 60, 'max_healing': 75}]
}

POWER_WORD_SHIELD = {
    'id': 'power_word_shield', 'display_name': 'Power Word: Shield',
    'description': 'Instantly shields an ally, absorbing a moderate amount of damage. Cannot be cast on the same target again for a short time.',
    'level_req': 4, 'mana_cost': 25, 'cooldown': 2.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'buff', 'effect': 'damage_shield', 'shield_amount': 50, 'debuff_on_target': 'weakened_soul', 'debuff_duration': 8.0}]
}

HOLY_NOVA = {
    'id': 'holy_nova', 'display_name': 'Holy Nova',
    'description': 'An instant burst of holy energy that deals minor damage to nearby enemies and provides a small amount of healing to nearby allies.',
    'level_req': 8, 'mana_cost': 35, 'cooldown': 10.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Light', 'min_damage': 10, 'max_damage': 15, 'radius': 10},
        {'type': 'direct_heal', 'min_healing': 10, 'max_healing': 15, 'radius': 10}
    ]
}

FLASH_HEAL = {
    'id': 'flash_heal', 'display_name': 'Flash Heal',
    'description': 'A quick but expensive heal for emergencies. Heals a single ally for a moderate amount.',
    'level_req': 12, 'mana_cost': 40, 'cooldown': 0.0, 'casting_time': 1.2, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'direct_heal', 'min_healing': 45, 'max_healing': 55}]
}

# -----------------------------------------------------------------------------
# TIER 2: ADEPT (Level 15-29)
# -----------------------------------------------------------------------------

DISPEL_MAGIC = {
    'id': 'dispel_magic', 'display_name': 'Dispel Magic',
    'description': 'Removes one beneficial Magic effect from an enemy or one harmful Magic effect from an ally.',
    'level_req': 16, 'mana_cost': 20, 'cooldown': 8.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'cleanse', 'cleanse_type': 'magic', 'count': 1}]
}

PRAYER_OF_MENDING = {
    'id': 'prayer_of_mending', 'display_name': 'Prayer of Mending',
    'description': 'Places a ward on an ally that heals them the next time they take damage, then jumps to another nearby injured ally. Jumps up to 5 times.',
    'level_req': 20, 'mana_cost': 40, 'cooldown': 10.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'bouncing_heal', 'min_healing': 30, 'max_healing': 35, 'max_jumps': 5, 'jump_range': 15}]
}

PENANCE = {
    'id': 'penance', 'display_name': 'Penance',
    'description': 'Launches a volley of holy light at a target over 2 seconds. Can be used on an enemy to deal damage or an ally to heal.',
    'level_req': 24, 'mana_cost': 50, 'cooldown': 12.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'channeled_heal_or_damage', 'damage_type': 'Light', 'tick_damage': 20, 'tick_healing': 30, 'duration': 2.0, 'interval': 0.5}]
}

FEAR_WARD = {
    'id': 'fear_ward', 'display_name': 'Fear Ward',
    'description': 'Wards a friendly target, making them immune to the next Fear effect used against them.',
    'level_req': 28, 'mana_cost': 25, 'cooldown': 60.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'buff', 'effect': 'immunity_charge', 'immunity_type': 'fear', 'charges': 1, 'duration': 180.0}]
}

# -----------------------------------------------------------------------------
# TIER 3: MASTER (Level 30-44)
# -----------------------------------------------------------------------------

HOLY_WORD_SERENITY = {
    'id': 'holy_word_serenity', 'display_name': 'Holy Word: Serenity',
    'description': 'An instant, powerful heal with a moderate cooldown. The quintessential life-saving spell.',
    'level_req': 32, 'mana_cost': 80, 'cooldown': 30.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'direct_heal', 'min_healing': 250, 'max_healing': 275}]
}

DIVINITY = {
    'id': 'divinity', 'display_name': 'Divinity',
    'description': 'Your critical heals now grant the target a small absorption shield equal to 30% of the amount healed.',
    'level_req': 36, 'mana_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'trigger': 'on_crit_heal', 'effect': 'crit_to_shield', 'conversion_rate': 0.30}]
}

DIVINE_STAR = {
    'id': 'divine_star', 'display_name': 'Divine Star',
    'description': 'Fires a star of light that travels forward, damaging enemies and shielding allies it passes through, then returns to you.',
    'level_req': 40, 'mana_cost': 75, 'cooldown': 15.0, 'casting_time': 0.0, 'target_type': 'projectile', 'range': 25,
    'effects': [{'type': 'piercing_projectile', 'damage_type': 'Light', 'min_damage': 40, 'max_damage': 50, 'shield_amount': 60}]
}

PAIN_SUPPRESSION = {
    'id': 'pain_suppression', 'display_name': 'Pain Suppression',
    'description': 'Instantly reduces all damage a friendly target takes by 40% for 8 seconds. A powerful defensive cooldown.',
    'level_req': 44, 'mana_cost': 50, 'cooldown': 120.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'buff', 'stat': 'Damage_Reduction', 'amount': 0.40, 'duration': 8.0}]
}

# -----------------------------------------------------------------------------
# TIER 4: GRANDMASTER (Level 45-60)
# -----------------------------------------------------------------------------

CIRCLE_OF_HEALING = {
    'id': 'circle_of_healing', 'display_name': 'Circle of Healing',
    'description': 'Heals the target and up to 4 other injured allies within 15 yards. Your main, though infrequent, AoE heal.',
    'level_req': 48, 'mana_cost': 100, 'cooldown': 12.0, 'casting_time': 1.5, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'smart_aoe_heal', 'min_healing': 80, 'max_healing': 90, 'max_targets': 5, 'radius': 15}]
}

GUARDIAN_SPIRIT = {
    'id': 'guardian_spirit', 'display_name': 'Guardian Spirit',
    'description': 'Summons a guardian spirit to watch over an ally. If the target takes fatal damage, the spirit is consumed to prevent death, healing them for 50% of their maximum health.',
    'level_req': 52, 'mana_cost': 150, 'cooldown': 180.0, 'casting_time': 1.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'buff', 'effect': 'cheat_death', 'duration': 30.0, 'heal_percent': 0.50}]
}

POWER_WORD_BARRIER = {
    'id': 'power_word_barrier', 'display_name': 'Power Word: Barrier',
    'description': 'The ultimate shielding spell. Summons a dome of holy energy at a location. All allies within take 25% reduced damage and are healed over time.',
    'level_req': 56, 'mana_cost': 200, 'cooldown': 180.0, 'casting_time': 1.5, 'target_type': 'aoe_ground', 'range': 30,
    'effects': [
        {'type': 'ground_buff', 'stat': 'Damage_Reduction', 'amount': 0.25, 'duration': 10.0, 'radius': 8},
        {'type': 'ground_hot', 'tick_healing': 50, 'duration': 10.0, 'interval': 1.0, 'radius': 8}
    ]
}

DIVINE_HYMN = {
    'id': 'divine_hymn', 'display_name': 'Divine Hymn',
    'description': 'A powerful AoE healing cooldown. Heals all allies within 40 yards over 8 seconds and increases healing they receive. Requires channeling.',
    'level_req': 58, 'mana_cost': 250, 'cooldown': 180.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'channeled_hot', 'tick_healing': 120, 'duration': 8.0, 'interval': 1.0, 'radius': 40},
        {'type': 'channeled_buff', 'stat': 'Healing_Received', 'amount': 0.10, 'duration': 8.0, 'radius': 40}
    ]
}

APOTHEOSIS = {
    'id': 'apotheosis', 'display_name': 'Apotheosis',
    'description': 'Ascend into a pure holy form for 20 seconds. While in this form, the cooldowns of your Holy Word spells are greatly reduced and your healing is increased.',
    'level_req': 60, 'mana_cost': 100, 'cooldown': 180.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'buff', 'effect': 'empowerment', 'empowers': ['holy_word_serenity'], 'cooldown_reduction_percent': 0.80, 'duration': 20.0},
        {'type': 'buff', 'stat': 'Healing_Done', 'amount': 0.20, 'duration': 20.0}
    ]
}


# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------
HOLY_ABILITIES = {
    'heal': HEAL, 'power_word_shield': POWER_WORD_SHIELD, 'holy_nova': HOLY_NOVA, 'flash_heal': FLASH_HEAL,
    'dispel_magic': DISPEL_MAGIC, 'prayer_of_mending': PRAYER_OF_MENDING, 'penance': PENANCE, 'fear_ward': FEAR_WARD,
    'holy_word_serenity': HOLY_WORD_SERENITY, 'divinity': DIVINITY, 'divine_star': DIVINE_STAR, 'pain_suppression': PAIN_SUPPRESSION,
    'circle_of_healing': CIRCLE_OF_HEALING, 'guardian_spirit': GUARDIAN_SPIRIT, 'power_word_barrier': POWER_WORD_BARRIER,
    'divine_hymn': DIVINE_HYMN, 'apotheosis': APOTHEOSIS,
}