"""
This file contains all data for Frost school abilities.

Philosophy: High crowd control, low single/AoE damage, high critical strike
potential. The core gameplay revolves around slowing, freezing, and then
"shattering" frozen targets with critical hits for burst damage.
"""

# -----------------------------------------------------------------------------
# TIER 1: APPRENTICE (Level 1-14)
# -----------------------------------------------------------------------------

FROSTBOLT = {
    'id': 'frostbolt', 'display_name': 'Frostbolt',
    'description': 'Launches a bolt of ice that deals minor damage and slows the target\'s movement speed.',
    'level_req': 1, 'mana_cost': 11, 'cooldown': 0.0, 'casting_time': 1.2, 'target_type': 'single', 'range': 30,
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Frost', 'min_damage': 7, 'max_damage': 10},
        {'type': 'debuff', 'effect': 'slow', 'amount': 0.30, 'duration': 8.0} # 30% slow
    ]
}

FROST_NOVA = {
    'id': 'frost_nova', 'display_name': 'Frost Nova',
    'description': 'An instant blast of ice erupts from the caster, freezing all nearby enemies in place.',
    'level_req': 4, 'mana_cost': 22, 'cooldown': 20.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'debuff', 'effect': 'root', 'duration': 6.0, 'radius': 10}] # Root = cannot move
}

ICE_ARMOR = {
    'id': 'ice_armor', 'display_name': 'Ice Armor',
    'description': 'Forms a barrier of frost around you, increasing your Toughness and slowing any enemy that strikes you in melee.',
    'level_req': 8, 'mana_cost': 40, 'cooldown': 5.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'buff', 'stat': 'Toughness', 'amount': 20, 'duration': 300.0}, # 5 minutes
        {'type': 'retaliation_debuff', 'effect': 'slow', 'amount': 0.25, 'duration': 4.0}
    ]
}

ICE_LANCE = {
    'id': 'ice_lance', 'display_name': 'Ice Lance',
    'description': 'Fires a shard of pure ice. Deals minimal damage, but deals triple damage to Frozen targets.',
    'level_req': 12, 'mana_cost': 15, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'synergy_damage', 'damage_type': 'Frost', 'min_damage': 5, 'max_damage': 7, 'synergy_target': 'frozen', 'damage_multiplier': 3.0}]
}

# -----------------------------------------------------------------------------
# TIER 2: ADEPT (Level 15-29)
# -----------------------------------------------------------------------------

CONE_OF_COLD = {
    'id': 'cone_of_cold', 'display_name': 'Cone of Cold',
    'description': 'Blasts enemies in a cone in front of you, dealing damage and slowing them significantly.',
    'level_req': 16, 'mana_cost': 55, 'cooldown': 12.0, 'casting_time': 0.0, 'target_type': 'cone', 'range': 12,
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Frost', 'min_damage': 15, 'max_damage': 20, 'cone_angle': 60},
        {'type': 'debuff', 'effect': 'slow', 'amount': 0.50, 'duration': 8.0, 'cone_angle': 60}
    ]
}

FROSTBITE = {
    'id': 'frostbite', 'display_name': 'Frostbite',
    'description': 'Your chilling effects have a chance to freeze the target solid for a short duration.',
    'level_req': 20, 'mana_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'enhances_spell': 'all_frost_slows', 'proc_chance': 0.15, 'effect': 'root', 'duration': 3.0}]
}

BLIZZARD = {
    'id': 'blizzard', 'display_name': 'Blizzard',
    'description': 'Summons a torrential ice storm over a target area, dealing continuous damage and slowing all enemies within it.',
    'level_req': 24, 'mana_cost': 150, 'cooldown': 30.0, 'casting_time': 2.0, 'target_type': 'aoe_ground', 'range': 35,
    'effects': [{'type': 'channeled_dot', 'damage_type': 'Frost', 'tick_damage': 12, 'duration': 8.0, 'interval': 1.0, 'radius': 10, 'debuff': 'slow', 'debuff_amount': 0.40}]
}

ICE_BARRIER = {
    'id': 'ice_barrier', 'display_name': 'Ice Barrier',
    'description': 'Instantly shields you with a layer of ice that absorbs a significant amount of damage. Lasts until broken.',
    'level_req': 28, 'mana_cost': 60, 'cooldown': 45.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'damage_shield', 'shield_amount': 200}]
}

# -----------------------------------------------------------------------------
# TIER 3: MASTER (Level 30-44)
# -----------------------------------------------------------------------------

DEEP_FREEZE = {
    'id': 'deep_freeze', 'display_name': 'Deep Freeze',
    'description': 'Encase a target in a block of ice, stunning them completely. Can only be used on targets that are already Frozen.',
    'level_req': 32, 'mana_cost': 50, 'cooldown': 35.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'synergy_debuff', 'synergy_target': 'frozen', 'effect': 'stun', 'duration': 5.0}]
}

SHATTER = {
    'id': 'shatter', 'display_name': 'Shatter',
    'description': 'Your mastery of ice allows your spells to find weak points in frozen foes. Greatly increases the critical strike chance of all your spells against Frozen targets.',
    'level_req': 36, 'mana_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'stat': 'Crit_Chance_vs_Frozen', 'amount': 0.50}] # +50% crit chance
}

FROZEN_ORB = {
    'id': 'frozen_orb', 'display_name': 'Frozen Orb',
    'description': 'Launches a swirling orb of ice that travels forward, continuously firing Ice Lances at nearby enemies.',
    'level_req': 40, 'mana_cost': 100, 'cooldown': 60.0, 'casting_time': 1.5, 'target_type': 'projectile', 'range': 40,
    'effects': [{'type': 'moving_turret', 'damage_type': 'Frost', 'min_damage': 15, 'max_damage': 20, 'duration': 10.0, 'interval': 0.75, 'radius': 15, 'projectile_speed': 8}]
}

ICY_VEINS = {
    'id': 'icy_veins', 'display_name': 'Icy Veins',
    'description': 'Cold energy flows through you, increasing your spell casting speed by 30% for a short duration.',
    'level_req': 44, 'mana_cost': 70, 'cooldown': 90.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'stat': 'Haste_Percent', 'amount': 0.30, 'duration': 20.0}]
}

# -----------------------------------------------------------------------------
# TIER 4: GRANDMASTER (Level 45-60)
# -----------------------------------------------------------------------------

GLACIAL_SPIKE = {
    'id': 'glacial_spike', 'display_name': 'Glacial Spike',
    'description': 'Conjures a massive spike of ice over 4 seconds. Casting Frostbolt reduces the cast time. Deals extreme damage and freezes the target solid.',
    'level_req': 48, 'mana_cost': 120, 'cooldown': 20.0, 'casting_time': 4.0, 'target_type': 'single', 'range': 35,
    'effects': [
        {'type': 'synergy_cast_time', 'synergy_spell': 'frostbolt', 'reduction_per_cast': 0.5},
        {'type': 'direct_damage', 'damage_type': 'Frost', 'min_damage': 300, 'max_damage': 350},
        {'type': 'debuff', 'effect': 'root', 'duration': 8.0}
    ]
}

COLD_SNAP = {
    'id': 'cold_snap', 'display_name': 'Cold Snap',
    'description': 'Instantly resets the cooldowns on all of your Frost spells (except Cold Snap itself). A powerful tool for emergencies or opportunities.',
    'level_req': 52, 'mana_cost': 25, 'cooldown': 300.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'cooldown_reset', 'school': 'Frost'}]
}

ICE_BLOCK = {
    'id': 'ice_block', 'display_name': 'Ice Block',
    'description': 'You entomb yourself in a block of ice, becoming immune to all damage and debuffs for 10 seconds. You cannot move or act while encased.',
    'level_req': 56, 'mana_cost': 50, 'cooldown': 240.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'immunity', 'duration': 10.0}]
}

COMET_STORM = {
    'id': 'comet_storm', 'display_name': 'Comet Storm',
    'description': 'Calls down a series of icy comets to bombard a target area, dealing damage and chilling enemies caught in the blast.',
    'level_req': 58, 'mana_cost': 200, 'cooldown': 60.0, 'casting_time': 2.0, 'target_type': 'aoe_ground', 'range': 40,
    'effects': [{'type': 'repeating_aoe_damage', 'damage_type': 'Frost', 'min_damage': 80, 'max_damage': 100, 'radius': 8, 'repeats': 3, 'delay_between': 1.0}]
}

FROZEN_HEART = {
    'id': 'frozen_heart', 'display_name': 'Frozen Heart',
    'description': 'The ultimate expression of control. Summons a massive pillar of ice at a location that pulses, applying a stack of Deep Chill to all enemies in a huge radius. At 5 stacks, the enemy is frozen solid in a block of ice for 15 seconds.',
    'level_req': 60, 'mana_cost': 250, 'cooldown': 180.0, 'casting_time': 3.0, 'target_type': 'aoe_ground', 'range': 30,
    'effects': [{'type': 'summon_debuff_totem', 'name': 'Heart of Winter', 'duration': 10.0, 'interval': 2.0, 'radius': 20, 'debuff': 'Deep_Chill', 'max_stacks': 5}]
}


# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------
FROST_ABILITIES = {
    'frostbolt': FROSTBOLT, 'frost_nova': FROST_NOVA, 'ice_armor': ICE_ARMOR, 'ice_lance': ICE_LANCE,
    'cone_of_cold': CONE_OF_COLD, 'frostbite': FROSTBITE, 'blizzard': BLIZZARD, 'ice_barrier': ICE_BARRIER,
    'deep_freeze': DEEP_FREEZE, 'shatter': SHATTER, 'frozen_orb': FROZEN_ORB, 'icy_veins': ICY_VEINS,
    'glacial_spike': GLACIAL_SPIKE, 'cold_snap': COLD_SNAP, 'ice_block': ICE_BLOCK, 'comet_storm': COMET_STORM,
    'frozen_heart': FROZEN_HEART,
}