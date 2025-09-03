"""
This file contains all data for Two-Handed Hammer abilities.

Philosophy: Mid single-target damage, mid AoE damage, and very high AoE debuffs.
The hammer wielder is a master of battlefield control, using concussive force to
stun, slow, and shatter the defenses of entire groups of enemies.
"""

# -----------------------------------------------------------------------------
# TIER 1: APPRENTICE (Level 1-14)
# -----------------------------------------------------------------------------

HEAVY_SLAM = {
    'id': 'heavy_slam', 'display_name': 'Heavy Slam',
    'description': 'A powerful, direct smash that deals physical damage.',
    'level_req': 1, 'stamina_cost': 26, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 28, 'max_damage': 35}]
}

SUNDERING_BLOW = {
    'id': 'sundering_blow', 'display_name': 'Sundering Blow',
    'description': 'A forceful blow that weakens the target\'s armor, reducing their Toughness. A core debuff.',
    'level_req': 4, 'stamina_cost': 20, 'cooldown': 4.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'debuff', 'stat': 'Toughness', 'amount': -80, 'duration': 15.0}]
}

GROUND_TREMOR = {
    'id': 'ground_tremor', 'display_name': 'Ground Tremor',
    'description': 'Slam your hammer into the ground, causing a tremor that damages and slows all nearby enemies.',
    'level_req': 8, 'stamina_cost': 35, 'cooldown': 12.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 20, 'max_damage': 25, 'radius': 8},
        {'type': 'debuff', 'effect': 'slow', 'amount': 0.30, 'duration': 6.0, 'radius': 8}
    ]
}

BULL_RUSH = {
    'id': 'bull_rush', 'display_name': 'Bull Rush',
    'description': 'Charge forward, knocking back the first enemy you hit.',
    'level_req': 12, 'stamina_cost': 20, 'cooldown': 20.0, 'casting_time': 0.0, 'target_type': 'movement', 'range': 15,
    'effects': [{'type': 'movement', 'effect': 'charge_with_knockback'}]
}

# -----------------------------------------------------------------------------
# TIER 2: ADEPT (Level 15-29)
# -----------------------------------------------------------------------------

STAGGERING_SWEEP = {
    'id': 'staggering_sweep', 'display_name': 'Staggering Sweep',
    'description': 'A wide, low swing aimed at the legs of all enemies in front of you, dealing damage and reducing their attack speed.',
    'level_req': 16, 'stamina_cost': 40, 'cooldown': 15.0, 'casting_time': 0.0, 'target_type': 'cone', 'range': 'melee',
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 40, 'max_damage': 50, 'cone_angle': 120},
        {'type': 'debuff', 'stat': 'Haste_Percent', 'amount': -0.25, 'duration': 8.0, 'cone_angle': 120}
    ]
}

HAMMER_TOSS = {
    'id': 'hammer_toss', 'display_name': 'Hammer Toss',
    'description': 'Hurl your hammer at a distant enemy, dealing damage and stunning them briefly upon impact.',
    'level_req': 20, 'stamina_cost': 30, 'cooldown': 25.0, 'casting_time': 1.0, 'target_type': 'single', 'range': 25,
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 50, 'max_damage': 60},
        {'type': 'debuff', 'effect': 'stun', 'duration': 1.5}
    ]
}

REVERBERATION = {
    'id': 'reverberation', 'display_name': 'Reverberation',
    'description': 'The force of your blows is staggering. Your critical strikes with two-handed hammers now also daze the target for 3 seconds.',
    'level_req': 24, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'trigger': 'on_crit', 'effect': 'daze', 'duration': 3.0}]
}

IRON_WILL = {
    'id': 'iron_will', 'display_name': 'Iron Will',
    'description': 'Fortify your resolve, granting you a temporary shield that absorbs a moderate amount of damage.',
    'level_req': 28, 'stamina_cost': 10, 'cooldown': 60.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'damage_shield', 'shield_amount': 300}]
}

# -----------------------------------------------------------------------------
# TIER 3: MASTER (Level 30-44)
# -----------------------------------------------------------------------------

THUNDERCLAP = {
    'id': 'thunderclap', 'display_name': 'Thunderclap',
    'description': 'A deafening clap that echoes around you, dealing minor damage but massively reducing the movement speed of all nearby enemies.',
    'level_req': 32, 'stamina_cost': 45, 'cooldown': 20.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 30, 'max_damage': 40, 'radius': 15},
        {'type': 'debuff', 'effect': 'slow', 'amount': 0.60, 'duration': 8.0, 'radius': 15}
    ]
}

EARTHQUAKE = {
    'id': 'earthquake', 'display_name': 'Earthquake',
    'description': 'Smash the ground repeatedly, creating a violent earthquake at a target location. Enemies inside are damaged, slowed, and have a chance to be knocked down with each pulse.',
    'level_req': 36, 'stamina_cost': 80, 'cooldown': 45.0, 'casting_time': 0.0, 'target_type': 'aoe_ground', 'range': 20,
    'effects': [{'type': 'channeled_aoe_debuff', 'damage_type': 'Physical', 'tick_damage': 40, 'duration': 8.0, 'interval': 1.0, 'radius': 10, 'debuff': 'slow', 'debuff_amount': 0.25, 'knockdown_chance': 0.20}]
}

AFTERSHOCK = {
    'id': 'aftershock', 'display_name': 'Aftershock',
    'description': 'The concussive force of your hammer is relentless. Your single-target Stun effects now also create a small Ground Tremor at the target\'s location.',
    'level_req': 40, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'trigger': 'on_stun', 'effect': 'proc_aoe', 'ability_id': 'ground_tremor'}]
}

UNSTOPPABLE_ADVANCE = {
    'id': 'unstoppable_advance', 'display_name': 'Unstoppable Advance',
    'description': 'Become an unstoppable juggernaut for 10 seconds, becoming immune to all slows and roots.',
    'level_req': 44, 'stamina_cost': 20, 'cooldown': 90.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'cc_immunity', 'immunity_type': ['slow', 'root'], 'duration': 10.0}]
}

# -----------------------------------------------------------------------------
# TIER 4: GRANDMASTER (Level 45-60)
# -----------------------------------------------------------------------------

METEOR_STRIKE = {
    'id': 'meteor_strike', 'display_name': 'Meteor Strike',
    'description': 'Leap into the air and come crashing down at a target location, dealing massive damage and stunning all enemies in a wide area.',
    'level_req': 48, 'stamina_cost': 80, 'cooldown': 60.0, 'casting_time': 1.0, 'target_type': 'aoe_ground', 'range': 25,
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 250, 'max_damage': 300, 'radius': 10},
        {'type': 'debuff', 'effect': 'stun', 'duration': 3.0, 'radius': 10}
    ]
}

CRIPPLING_WAVE = {
    'id': 'crippling_wave', 'display_name': 'Crippling Wave',
    'description': 'Send a wave of force rippling through the ground. All enemies hit take moderate damage and have their damage dealt reduced by 25% for 8 seconds.',
    'level_req': 52, 'stamina_cost': 60, 'cooldown': 30.0, 'casting_time': 0.0, 'target_type': 'line', 'range': 20,
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 100, 'max_damage': 120, 'line_width': 6},
        {'type': 'debuff', 'stat': 'All_Damage_Dealt', 'amount': -0.25, 'duration': 8.0, 'line_width': 6}
    ]
}

AVATAR_OF_THE_MOUNTAIN = {
    'id': 'avatar_of_the_mountain', 'display_name': 'Avatar of the Mountain',
    'description': 'The ultimate defensive cooldown. For 15 seconds, your Toughness is doubled and you are immune to all crowd control effects.',
    'level_req': 56, 'stamina_cost': 40, 'cooldown': 180.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'buff', 'stat': 'Toughness_Multiplier', 'amount': 2.0, 'duration': 15.0},
        {'type': 'buff', 'effect': 'cc_immunity', 'duration': 15.0}
    ]
}

PULVERIZE = {
    'id': 'pulverize', 'display_name': 'Pulverize',
    'description': 'The ultimate debuff. Pulverize the target\'s defenses, causing them to take 30% increased damage from ALL sources for 10 seconds.',
    'level_req': 60, 'stamina_cost': 100, 'cooldown': 120.0, 'casting_time': 1.5, 'target_type': 'single', 'range': 'melee',
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 200, 'max_damage': 250},
        {'type': 'debuff', 'stat': 'Damage_Taken', 'amount': 0.30, 'duration': 10.0}
    ]
}

# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------
TWO_HANDED_HAMMER_ABILITIES = {
    'heavy_slam': HEAVY_SLAM, 'sundering_blow': SUNDERING_BLOW, 'ground_tremor': GROUND_TREMOR, 'bull_rush': BULL_RUSH,
    'staggering_sweep': STAGGERING_SWEEP, 'hammer_toss': HAMMER_TOSS, 'reverberation': REVERBERATION, 'iron_will': IRON_WILL,
    'thunderclap': THUNDERCLAP, 'earthquake': EARTHQUAKE, 'aftershock': AFTERSHOCK, 'unstoppable_advance': UNSTOPPABLE_ADVANCE,
    'meteor_strike': METEOR_STRIKE, 'crippling_wave': CRIPPLING_WAVE, 'avatar_of_the_mountain': AVATAR_OF_THE_MOUNTAIN, 'pulverize': PULVERIZE,
}