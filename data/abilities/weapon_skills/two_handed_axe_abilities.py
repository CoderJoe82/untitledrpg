"""
This file contains all data for Two-Handed Axe abilities.

Philosophy: High single-target damage, high AoE damage, high bleed damage, and
mid wielder defense loss. The two-handed axe wielder is a reckless berserker,
sacrificing their own defense to unleash unparalleled carnage.
"""

# -----------------------------------------------------------------------------
# TIER 1: APPRENTICE (Level 1-14)
# -----------------------------------------------------------------------------

BRUTAL_CHOP = {
    'id': 'brutal_chop', 'display_name': 'Brutal Chop',
    'description': 'A heavy, savage chop that deals high physical damage.',
    'level_req': 1, 'skill_req': 1, 'stamina_cost': 28, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 30, 'max_damage': 38}]
}

GASH = {
    'id': 'gash', 'display_name': 'Gash',
    'description': 'Tear a gruesome wound in the target, causing them to bleed heavily over time.',
    'level_req': 4, 'skill_req': 5, 'stamina_cost': 20, 'cooldown': 8.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'dot', 'damage_type': 'Bleed', 'tick_damage': 10, 'duration': 12.0, 'interval': 1.0}]
}

RECKLESS_SWING = {
    'id': 'reckless_swing', 'display_name': 'Reckless Swing',
    'description': 'A wide, wild swing that hits all enemies in front of you but lowers your Toughness for a short time.',
    'level_req': 8, 'skill_req': 10, 'stamina_cost': 35, 'cooldown': 10.0, 'casting_time': 0.0, 'target_type': 'cone', 'range': 'melee',
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 25, 'max_damage': 30, 'cone_angle': 120},
        {'type': 'debuff', 'stat': 'Toughness', 'amount': -100, 'duration': 5.0, 'target': 'self'} # Self-debuff
    ]
}

INTIMIDATING_SHOUT = {
    'id': 'intimidating_shout', 'display_name': 'Intimidating Shout',
    'description': 'Let out a terrifying shout, reducing the physical damage dealt by all nearby enemies.',
    'level_req': 12, 'skill_req': 15, 'stamina_cost': 15, 'cooldown': 30.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'debuff', 'stat': 'Physical_Damage_Dealt', 'amount': -0.10, 'duration': 10.0, 'radius': 15}]
}

# -----------------------------------------------------------------------------
# TIER 2: ADEPT (Level 15-29)
# -----------------------------------------------------------------------------

MANGLE = {
    'id': 'mangle', 'display_name': 'Mangle',
    'description': 'A devastating strike that deals 30% bonus damage to targets that are already bleeding.',
    'level_req': 16, 'skill_req': 20, 'stamina_cost': 30, 'cooldown': 6.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'synergy_damage', 'damage_type': 'Physical', 'min_damage': 70, 'max_damage': 85, 'synergy_target': 'bleeding', 'bonus_multiplier': 0.30}]
}

WHIRLWIND = {
    'id': 'whirlwind', 'display_name': 'Whirlwind',
    'description': 'Become a cyclone of steel, striking all nearby enemies for high damage.',
    'level_req': 20, 'skill_req': 25, 'stamina_cost': 50, 'cooldown': 12.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 50, 'max_damage': 60, 'radius': 8}]
}

BLOOD_FRENZY = {
    'id': 'blood_frenzy', 'display_name': 'Blood Frenzy',
    'description': 'The scent of blood drives you into a frenzy. For every enemy that you are bleeding within 10 yards, your attack speed is increased by 5%.',
    'level_req': 24, 'skill_req': 30, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'effect': 'haste_per_bleeding_target', 'percent_per_target': 0.05, 'radius': 10}]
}

DEATH_WISH = {
    'id': 'death_wish', 'display_name': 'Death Wish',
    'description': 'Embrace your own mortality for 10 seconds, increasing all damage you deal by 20% but also increasing all damage you take by 10%.',
    'level_req': 28, 'skill_req': 35, 'stamina_cost': 10, 'cooldown': 60.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'buff', 'stat': 'All_Damage_Dealt', 'amount': 0.20, 'duration': 10.0},
        {'type': 'buff', 'stat': 'Damage_Taken', 'amount': 0.10, 'duration': 10.0}
    ]
}

# -----------------------------------------------------------------------------
# TIER 3: MASTER (Level 30-44)
# -----------------------------------------------------------------------------

BERSERKER_RAGE = {
    'id': 'berserker_rage', 'display_name': 'Berserker Rage',
    'description': 'Enter a state of pure rage, becoming immune to Fear and Daze effects and increasing your critical strike chance for 12 seconds.',
    'level_req': 32, 'skill_req': 40, 'stamina_cost': 20, 'cooldown': 90.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'buff', 'effect': 'cc_immunity', 'immunity_type': ['fear', 'daze'], 'duration': 12.0},
        {'type': 'buff', 'stat': 'Crit_Chance', 'amount': 0.15, 'duration': 12.0}
    ]
}

ARTERIAL_CUT = {
    'id': 'arterial_cut', 'display_name': 'Arterial Cut',
    'description': 'A masterful, brutal strike that severs an artery, inflicting a devastating bleed that deals more damage the lower the target\'s health is.',
    'level_req': 36, 'skill_req': 45, 'stamina_cost': 35, 'cooldown': 20.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'execute_dot', 'damage_type': 'Bleed', 'base_tick_damage': 20, 'duration': 9.0, 'interval': 1.0}]
}

EARTHSPLITTER = {
    'id': 'earthsplitter', 'display_name': 'Earthsplitter',
    'description': 'Slam your axe into the ground with such force that it shatters the earth in a line, dealing heavy damage to all enemies caught in the fissure.',
    'level_req': 40, 'skill_req': 50, 'stamina_cost': 60, 'cooldown': 25.0, 'casting_time': 1.0, 'target_type': 'line', 'range': 20,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 120, 'max_damage': 150, 'line_width': 5}]
}

TASTE_FOR_BLOOD = {
    'id': 'taste_for_blood', 'display_name': 'Taste for Blood',
    'description': 'Killing an enemy that is bleeding sends you into a fervor, refunding 20% of your max stamina and resetting the cooldown of Whirlwind.',
    'level_req': 44, 'skill_req': 55, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'trigger': 'on_kill_bleeding_target', 'effect': 'resource_and_cooldown'}]
}

# -----------------------------------------------------------------------------
# TIER 4: GRANDMASTER (Level 45-60)
# -----------------------------------------------------------------------------

DECAPITATE = {
    'id': 'decapitate', 'display_name': 'Decapitate',
    'description': 'Attempt to take the enemy\'s head. Deals massive damage, with a small chance to instantly kill non-boss enemies below 20% health.',
    'level_req': 48, 'skill_req': 60, 'stamina_cost': 50, 'cooldown': 15.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'execute_damage', 'damage_type': 'Physical', 'min_damage': 450, 'max_damage': 550, 'health_threshold': 0.20, 'instant_kill_chance': 0.15}]
}

ONSLAUGHT = {
    'id': 'onslaught', 'display_name': 'Onslaught',
    'description': 'Your critical strikes with two-handed axes are so vicious they cause all of your active Bleeds on the target to instantly tick one time.',
    'level_req': 52, 'skill_req': 65, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'trigger': 'on_crit', 'effect': 'force_dot_tick', 'dot_type': 'Bleed'}]
}

AVATAR_OF_SLAUGHTER = {
    'id': 'avatar_of_slaughter', 'display_name': 'Avatar of Slaughter',
    'description': 'The ultimate berserker state. For 15 seconds, you deal 40% more damage, you are immune to all crowd control, but your Toughness is reduced to 0.',
    'level_req': 56, 'skill_req': 70, 'stamina_cost': 40, 'cooldown': 180.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'buff', 'stat': 'All_Damage_Dealt', 'amount': 0.40, 'duration': 15.0},
        {'type': 'buff', 'effect': 'cc_immunity', 'duration': 15.0},
        {'type': 'buff', 'stat': 'Toughness_Set_To_Zero', 'duration': 15.0}
    ]
}

CYCLONE_OF_CARNAGE = {
    'id': 'cyclone_of_carnage', 'display_name': 'Cyclone of Carnage',
    'description': 'Unleash a devastating spinning attack that deals massive damage and applies Gash to all enemies hit. You move slower while channeling.',
    'level_req': 60, 'skill_req': 75, 'stamina_cost': 120, 'cooldown': 120.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'channeled_aoe_damage', 'damage_type': 'Physical', 'tick_damage': 120, 'duration': 6.0, 'interval': 1.0, 'radius': 10},
        {'type': 'channeled_aoe_dot', 'dot_id': 'gash', 'duration': 6.0, 'interval': 1.0, 'radius': 10},
        {'type': 'debuff', 'effect': 'slow', 'amount': 0.30, 'target': 'self'}
    ]
}

# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------
TWO_HANDED_AXE_ABILITIES = {
    'brutal_chop': BRUTAL_CHOP, 'gash': GASH, 'reckless_swing': RECKLESS_SWING, 'intimidating_shout': INTIMIDATING_SHOUT,
    'mangle': MANGLE, 'whirlwind': WHIRLWIND, 'blood_frenzy': BLOOD_FRENZY, 'death_wish': DEATH_WISH,
    'berserker_rage': BERSERKER_RAGE, 'arterial_cut': ARTERIAL_CUT, 'earthsplitter': EARTHSPLITTER, 'taste_for_blood': TASTE_FOR_BLOOD,
    'decapitate': DECAPITATE, 'onslaught': ONSLAUGHT, 'avatar_of_slaughter': AVATAR_OF_SLAUGHTER, 'cyclone_of_carnage': CYCLONE_OF_CARNAGE,
}