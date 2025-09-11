"""
This file contains all data for Arcane school abilities.

Philosophy: High single-target damage, mid AoE damage, and mid crit damage.
The Arcane mage is a master of raw magical power, focusing on overwhelming
single targets with precise, high-damage spells and devastating criticals.
"""

# -----------------------------------------------------------------------------
# TIER 1: APPRENTICE (Level 1-14)
# -----------------------------------------------------------------------------

ARCANE_BOLT = {
    'id': 'arcane_bolt', 'display_name': 'Arcane Bolt',
    'description': 'Launches a bolt of pure magical energy at a target, dealing Arcane damage.',
    'level_req': 1, 'mana_cost': 15, 'cooldown': 0.0, 'casting_time': 1.4, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Arcane', 'min_damage': 14, 'max_damage': 18}]
}

ARCANE_INTELLECT = {
    'id': 'arcane_intellect', 'display_name': 'Arcane Intellect',
    'description': 'Magically enhances the mind of a friendly target, increasing their Intellect for a very long duration.',
    'level_req': 4, 'mana_cost': 20, 'cooldown': 0.0, 'casting_time': 1.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'buff', 'stat': 'intellect', 'amount': 10, 'duration': 1800.0}] # 30 minutes
}

MANA_SHIELD = {
    'id': 'mana_shield', 'display_name': 'Mana Shield',
    'description': 'Creates a shield that consumes your Mana to absorb incoming damage. A core defensive spell for the Arcane mage.',
    'level_req': 8, 'mana_cost': 10, 'cooldown': 5.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'mana_to_damage_shield', 'conversion_rate': 2.0, 'duration': 60.0}] # 1 point of damage consumes 2 mana
}

ARCANE_EXPLOSION = {
    'id': 'arcane_explosion', 'display_name': 'Arcane Explosion',
    'description': 'Causes an instant explosion of arcane energy around the caster, damaging all nearby enemies.',
    'level_req': 12, 'mana_cost': 40, 'cooldown': 8.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Arcane', 'min_damage': 20, 'max_damage': 25, 'radius': 10}]
}

# -----------------------------------------------------------------------------
# TIER 2: ADEPT (Level 15-29)
# -----------------------------------------------------------------------------

ARCANE_MISSILES = {
    'id': 'arcane_missiles', 'display_name': 'Arcane Missiles',
    'description': 'Channels a stream of 5 magical missiles into a target over 2.5 seconds. Each missile deals Arcane damage.',
    'level_req': 16, 'mana_cost': 60, 'cooldown': 6.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'channeled_damage', 'damage_type': 'Arcane', 'tick_damage': 15, 'duration': 2.5, 'interval': 0.5}]
}

BLINK = {
    'id': 'blink', 'display_name': 'Blink',
    'description': 'Teleports the caster a short distance forward, breaking out of stuns and roots. The signature Arcane mobility spell.',
    'level_req': 20, 'mana_cost': 30, 'cooldown': 15.0, 'casting_time': 0.0, 'target_type': 'movement', 'range': 18,
    'effects': [{'type': 'movement', 'effect': 'teleport_forward', 'clears_roots': True, 'clears_stuns': True}]
}

COUNTERSPELL = {
    'id': 'counterspell', 'display_name': 'Counterspell',
    'description': 'Instantly interrupts an enemy\'s spellcast, preventing them from casting any spell from that school of magic for a short time.',
    'level_req': 24, 'mana_cost': 25, 'cooldown': 20.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'debuff', 'effect': 'interrupt', 'duration': 0.5}, {'type': 'debuff', 'effect': 'school_lockout', 'duration': 6.0}]
}

ARCANE_BLAST = {
    'id': 'arcane_blast', 'display_name': 'Arcane Blast',
    'description': 'Blasts a target for high Arcane damage. Each cast increases the damage of your next Arcane Blast but also its mana cost. Stacks up to 4 times.',
    'level_req': 28, 'mana_cost': 50, 'cooldown': 0.0, 'casting_time': 2.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'stacking_damage', 'damage_type': 'Arcane', 'min_damage': 60, 'max_damage': 70, 'damage_increase_per_stack': 0.15, 'mana_increase_per_stack': 0.50, 'max_stacks': 4}]
}

# -----------------------------------------------------------------------------
# TIER 3: MASTER (Level 30-44)
# -----------------------------------------------------------------------------

PRESENCE_OF_MIND = {
    'id': 'presence_of_mind', 'display_name': 'Presence of Mind',
    'description': 'Empowers your mind, making your next spell with a cast time under 10 seconds become an instant cast.',
    'level_req': 32, 'mana_cost': 30, 'cooldown': 120.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'instant_cast', 'charges': 1, 'duration': 15.0}]
}

NETHER_TEMPEST = {
    'id': 'nether_tempest', 'display_name': 'Nether Tempest',
    'description': 'Places a storm of arcane energy on a target that deals damage over time. Each time it deals damage, it also damages one other nearby enemy.',
    'level_req': 36, 'mana_cost': 75, 'cooldown': 12.0, 'casting_time': 1.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'cleave_dot', 'damage_type': 'Arcane', 'tick_damage': 25, 'duration': 12.0, 'interval': 1.0, 'cleave_range': 8}]
}

SPELLSTEAL = {
    'id': 'spellsteal', 'display_name': 'Spellsteal',
    'description': 'Steals one beneficial Magic effect from an enemy and applies it to yourself.',
    'level_req': 40, 'mana_cost': 50, 'cooldown': 25.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'buff_steal', 'steal_type': 'magic', 'count': 1}]
}

ARCANE_POTENCY = {
    'id': 'arcane_potency', 'display_name': 'Arcane Potency',
    'description': 'Your mastery of arcane energies increases the damage dealt by all your critical strikes by 25%.',
    'level_req': 44, 'mana_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'stat': 'Crit_Damage_Multiplier', 'amount': 0.25}]
}

# -----------------------------------------------------------------------------
# TIER 4: GRANDMASTER (Level 45-60)
# -----------------------------------------------------------------------------

ARCANE_POWER = {
    'id': 'arcane_power', 'display_name': 'Arcane Power',
    'description': 'The ultimate damage cooldown. For 15 seconds, your spells deal 30% more damage but cost 30% more mana.',
    'level_req': 48, 'mana_cost': 100, 'cooldown': 180.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'buff', 'stat': 'Arcane_Damage_Percent', 'amount': 0.30, 'duration': 15.0},
        {'type': 'buff', 'stat': 'Mana_Cost_Percent', 'amount': 0.30, 'duration': 15.0}
    ]
}

ARCANE_BARRAGE = {
    'id': 'arcane_barrage', 'display_name': 'Arcane Barrage',
    'description': 'Instantly fires a barrage of arcane energy at a target. Consumes your Arcane Blast charges to deal bonus damage for each charge consumed.',
    'level_req': 52, 'mana_cost': 40, 'cooldown': 4.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'finisher_damage', 'damage_type': 'Arcane', 'min_damage': 80, 'max_damage': 100, 'consumes_stack': 'arcane_blast', 'bonus_damage_per_stack': 0.25}]
}

PRISMATIC_BARRIER = {
    'id': 'prismatic_barrier', 'display_name': 'Prismatic Barrier',
    'description': 'A superior defensive shield that reduces all magic damage taken by 20% and reduces the duration of harmful magic effects against you.',
    'level_req': 56, 'mana_cost': 80, 'cooldown': 30.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'buff', 'stat': 'Magic_Damage_Reduction', 'amount': 0.20, 'duration': 60.0},
        {'type': 'buff', 'stat': 'Debuff_Duration_Reduction', 'amount': 0.25, 'duration': 60.0}
    ]
}

TIME_WARP = {
    'id': 'time_warp', 'display_name': 'Time Warp',
    'description': 'Distorts time in a large area, increasing the casting and attack speed of all allies within it by 30% for 40 seconds.',
    'level_req': 58, 'mana_cost': 200, 'cooldown': 300.0, 'casting_time': 1.5, 'target_type': 'aoe_ground', 'range': 30,
    'effects': [{'type': 'ground_buff', 'stat': 'Haste_Percent', 'amount': 0.30, 'duration': 40.0, 'radius': 25}]
}

ARCANE_OBLITERATION = {
    'id': 'arcane_obliteration', 'display_name': 'Arcane Obliteration',
    'description': 'The ultimate expression of arcane power. After a long cast, you unleash a beam of pure energy that obliterates a single target, dealing massive Arcane damage. The damage is increased by your current percentage of Mana.',
    'level_req': 60, 'mana_cost': 250, 'cooldown': 120.0, 'casting_time': 4.0, 'target_type': 'single', 'range': 40,
    'effects': [{'type': 'mana_scaled_damage', 'damage_type': 'Arcane', 'min_damage': 500, 'max_damage': 600, 'mana_scaling_percent': 0.50}] # Deals bonus damage equal to 50% of current mana percentage
}

# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------
ARCANE_ABILITIES = {
    'arcane_bolt': ARCANE_BOLT, 'arcane_intellect': ARCANE_INTELLECT, 'mana_shield': MANA_SHIELD, 'arcane_explosion': ARCANE_EXPLOSION,
    'arcane_missiles': ARCANE_MISSILES, 'blink': BLINK, 'counterspell': COUNTERSPELL, 'arcane_blast': ARCANE_BLAST,
    'presence_of_mind': PRESENCE_OF_MIND, 'nether_tempest': NETHER_TEMPEST, 'spellsteal': SPELLSTEAL, 'arcane_potency': ARCANE_POTENCY,
    'arcane_power': ARCANE_POWER, 'arcane_barrage': ARCANE_BARRAGE, 'prismatic_barrier': PRISMATIC_BARRIER,
    'time_warp': TIME_WARP, 'arcane_obliteration': ARCANE_OBLITERATION,
}