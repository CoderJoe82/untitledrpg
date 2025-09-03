"""
This file contains all data for Light school abilities.

Philosophy: High single-target damage, low direct AoE, and low crowd control.
The defining mechanic is converting a portion of damage dealt into protective
absorption shields for the caster and their allies.
"""

# -----------------------------------------------------------------------------
# TIER 1: APPRENTICE (Level 1-14)
# -----------------------------------------------------------------------------

SMITE = {
    'id': 'smite', 'display_name': 'Smite',
    'description': 'Smites an enemy with holy light, dealing a low amount of Light damage. Your primary attack.',
    'level_req': 1, 'mana_cost': 12, 'cooldown': 0.0, 'casting_time': 1.1, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Light', 'min_damage': 9, 'max_damage': 13}]
}

AEGIS_OF_LIGHT = {
    'id': 'aegis_of_light', 'display_name': 'Aegis of Light',
    'description': 'For the next 10 seconds, 20% of all single-target Light damage you deal grants you an absorption shield.',
    'level_req': 3, 'mana_cost': 25, 'cooldown': 30.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'damage_to_shield', 'conversion_rate': 0.20, 'duration': 10.0}]
}

HOLY_FIRE = {
    'id': 'holy_fire', 'display_name': 'Holy Fire',
    'description': 'Engulfs an enemy in holy flames, dealing instant damage and minor burning damage over time.',
    'level_req': 6, 'mana_cost': 20, 'cooldown': 8.0, 'casting_time': 0.5, 'target_type': 'single', 'range': 25,
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Light', 'min_damage': 15, 'max_damage': 20},
        {'type': 'dot', 'damage_type': 'Light', 'tick_damage': 3, 'duration': 6.0, 'interval': 1.0}
    ]
}

RADIANT_BURST = {
    'id': 'radiant_burst', 'display_name': 'Radiant Burst',
    'description': 'An instant burst of light erupts from the caster, dealing minor damage to all nearby enemies.',
    'level_req': 9, 'mana_cost': 30, 'cooldown': 12.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Light', 'min_damage': 18, 'max_damage': 22, 'radius': 8}]
}

SEAL_OF_JUDGMENT = {
    'id': 'seal_of_judgment', 'display_name': 'Seal of Judgment',
    'description': 'Places a seal on the target. Your attacks against this target have a chance to deal bonus Light damage.',
    'level_req': 13, 'mana_cost': 15, 'cooldown': 3.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'debuff', 'effect': 'bonus_damage_chance', 'proc_chance': 0.25, 'min_damage': 10, 'max_damage': 15, 'duration': 30.0}]
}

# -----------------------------------------------------------------------------
# TIER 2: ADEPT (Level 15-29)
# -----------------------------------------------------------------------------

DENOUNCE = {
    'id': 'denounce', 'display_name': 'Denounce',
    'description': 'A powerful denouncement that deals significant Light damage to a single target.',
    'level_req': 16, 'mana_cost': 45, 'cooldown': 4.0, 'casting_time': 1.8, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Light', 'min_damage': 50, 'max_damage': 65}]
}

PURIFY = {
    'id': 'purify', 'display_name': 'Purify',
    'description': 'Cleanses a friendly target, removing one harmful Magic and one Curse effect.',
    'level_req': 19, 'mana_cost': 25, 'cooldown': 8.0, 'casting_time': 0.5, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'cleanse', 'cleanse_type': ['magic', 'curse'], 'count': 1}]
}

CONSECRATION = {
    'id': 'consecration', 'display_name': 'Consecration',
    'description': 'Sanctifies a piece of ground, dealing Light damage over time to any enemy that stands within it.',
    'level_req': 23, 'mana_cost': 70, 'cooldown': 20.0, 'casting_time': 0.0, 'target_type': 'aoe_ground', 'range': 10,
    'effects': [{'type': 'ground_dot', 'damage_type': 'Light', 'tick_damage': 12, 'duration': 10.0, 'interval': 1.0, 'radius': 8}]
}

SHIELD_OF_THE_RIGHTEOUS = {
    'id': 'shield_of_the_righteous', 'display_name': 'Shield of the Righteous',
    'description': 'Instantly grants you a strong absorption shield. Does not rely on dealing damage.',
    'level_req': 27, 'mana_cost': 50, 'cooldown': 45.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'damage_shield', 'shield_amount': 250}]
}

# -----------------------------------------------------------------------------
# TIER 3: MASTER (Level 30-44)
# -----------------------------------------------------------------------------

SPEAR_OF_LIGHT = {
    'id': 'spear_of_light', 'display_name': 'Spear of Light',
    'description': 'Hurls a spear of pure light at an enemy, dealing high damage and briefly dazing them.',
    'level_req': 31, 'mana_cost': 90, 'cooldown': 15.0, 'casting_time': 2.2, 'target_type': 'single', 'range': 35,
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Light', 'min_damage': 140, 'max_damage': 170},
        {'type': 'debuff', 'effect': 'daze', 'duration': 3.0}
    ]
}

DIVINE_FAVOR = {
    'id': 'divine_favor', 'display_name': 'Divine Favor',
    'description': 'Calls upon a higher power, increasing your critical strike chance with all spells by 25% for 15 seconds.',
    'level_req': 35, 'mana_cost': 60, 'cooldown': 90.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'stat': 'Crit_Chance', 'amount': 0.25, 'duration': 15.0}]
}

DIVINE_AEGIS = {
    'id': 'divine_aegis', 'display_name': 'Divine Aegis',
    'description': 'For the next 10 seconds, 25% of all single-target Light damage you deal now grants an absorption shield to all nearby party members.',
    'level_req': 39, 'mana_cost': 100, 'cooldown': 120.0, 'casting_time': 1.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'damage_to_group_shield', 'conversion_rate': 0.25, 'duration': 10.0, 'radius': 25}]
}

RAY_OF_HOPE = {
    'id': 'ray_of_hope', 'display_name': 'Ray of Hope',
    'description': 'Channels a beam of light onto a friendly target, healing them and increasing all healing they receive for a short time.',
    'level_req': 43, 'mana_cost': 40, 'mana_upkeep': 20, 'cooldown': 10.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [
        {'type': 'channeled_hot', 'tick_healing': 50, 'duration': -1, 'interval': 1.0},
        {'type': 'buff', 'stat': 'Healing_Received', 'amount': 0.15, 'duration': 5.0}
    ]
}

# -----------------------------------------------------------------------------
# TIER 4: GRANDMASTER (Level 45-60)
# -----------------------------------------------------------------------------

DIVINE_INSPIRATION = {
    'id': 'divine_inspiration', 'display_name': 'Divine Inspiration',
    'description': 'Your direct damage critical strikes with Light spells grant you a small absorption shield.',
    'level_req': 47, 'mana_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'trigger': 'on_crit', 'effect': 'crit_to_shield', 'conversion_rate': 0.50}] # Shield is 50% of the damage dealt
}

FINAL_RECKONING = {
    'id': 'final_reckoning', 'display_name': 'Final Reckoning',
    'description': 'Calls down a pillar of holy fire to strike a target after a 3-second delay, dealing massive damage to the target and minor damage to nearby enemies.',
    'level_req': 50, 'mana_cost': 180, 'cooldown': 45.0, 'casting_time': 2.0, 'target_type': 'single', 'range': 35,
    'effects': [{'type': 'delayed_damage', 'delay': 3.0, 'damage_type': 'Light', 'min_damage': 350, 'max_damage': 400, 'splash_radius': 6, 'splash_multiplier': 0.25}]
}

GUARDIAN_SPIRIT = {
    'id': 'guardian_spirit', 'display_name': 'Guardian Spirit',
    'description': 'Summons a guardian spirit to watch over a friendly target. If the target takes fatal damage, the spirit is consumed to prevent death, healing them and granting a massive shield.',
    'level_req': 54, 'mana_cost': 150, 'cooldown': 300.0, 'casting_time': 1.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'buff', 'effect': 'cheat_death', 'duration': 120.0, 'heal_percent': 0.40, 'shield_percent_of_max_health': 0.50}]
}

LIGHTS_JUDGMENT = {
    'id': 'lights_judgment', 'display_name': "Light's Judgment",
    'description': 'Channel a continuous torrent of holy energy into a single target, dealing heavy damage over 5 seconds.',
    'level_req': 58, 'mana_cost': 200, 'cooldown': 30.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'channeled_dot', 'damage_type': 'Light', 'tick_damage': 80, 'duration': 5.0, 'interval': 1.0}]
}

AVENGING_WRATH = {
    'id': 'avenging_wrath', 'display_name': 'Avenging Wrath',
    'description': 'The ultimate expression of divine power. For 20 seconds, your damage is increased by 30% and your single-target Light spells also heal a nearby injured ally for a portion of the damage dealt.',
    'level_req': 60, 'mana_cost': 100, 'cooldown': 180.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'buff', 'stat': 'Light_Damage_Percent', 'amount': 0.30, 'duration': 20.0},
        {'type': 'buff', 'effect': 'damage_to_cleave_heal', 'conversion_rate': 0.25, 'duration': 20.0, 'radius': 20}
    ]
}

# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------
LIGHT_ABILITIES = {
    'smite': SMITE, 'aegis_of_light': AEGIS_OF_LIGHT, 'holy_fire': HOLY_FIRE, 'radiant_burst': RADIANT_BURST,
    'seal_of_judgment': SEAL_OF_JUDGMENT, 'denounce': DENOUNCE, 'purify': PURIFY, 'consecration': CONSECRATION,
    'shield_of_the_righteous': SHIELD_OF_THE_RIGHTEOUS, 'spear_of_light': SPEAR_OF_LIGHT, 'divine_favor': DIVINE_FAVOR,
    'divine_aegis': DIVINE_AEGIS, 'ray_of_hope': RAY_OF_HOPE, 'divine_inspiration': DIVINE_INSPIRATION,
    'final_reckoning': FINAL_RECKONING, 'guardian_spirit': GUARDIAN_SPIRIT, 'lights_judgment': LIGHTS_JUDGMENT,
    'avenging_wrath': AVENGING_WRATH,
}