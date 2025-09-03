"""
This file contains all data for One-Handed Mace abilities.

Philosophy: Mid single-target damage, very low AoE damage, mid physical debuffs,
and low critical bonuses. The mace wielder is a brawler and a controller,
excelling at disabling a single target by shattering their defenses and stunning them.
"""

# -----------------------------------------------------------------------------
# TIER 1: APPRENTICE (Level 1-14)
# -----------------------------------------------------------------------------

BLUDGEON = {
    'id': 'bludgeon', 'display_name': 'Bludgeon',
    'description': 'A straightforward, heavy blow that deals physical damage.',
    'level_req': 1, 'stamina_cost': 20, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 16, 'max_damage': 22}]
}

SHATTER_ARMOR = {
    'id': 'shatter_armor', 'display_name': 'Shatter Armor',
    'description': 'A forceful impact that weakens the target\'s armor, reducing their Toughness. Stacks up to 3 times. The signature mace debuff.',
    'level_req': 4, 'stamina_cost': 15, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'debuff', 'stat': 'Toughness', 'amount': -25, 'duration': 20.0, 'max_stacks': 3}]
}

DAZING_BLOW = {
    'id': 'dazing_blow', 'display_name': 'Dazing Blow',
    'description': 'A solid strike to the head that briefly dazes the target.',
    'level_req': 8, 'stamina_cost': 25, 'cooldown': 18.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'debuff', 'effect': 'daze', 'duration': 3.0}]
}

SHIELD_BASH = {
    'id': 'shield_bash', 'display_name': 'Shield Bash',
    'description': 'Slam your shield into an enemy, dealing minor damage and interrupting their spellcast. Requires a shield.',
    'level_req': 12, 'stamina_cost': 10, 'cooldown': 12.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 5, 'max_damage': 8, 'requires_item_type': 'shield'},
        {'type': 'debuff', 'effect': 'interrupt', 'duration': 0.5, 'requires_item_type': 'shield'}
    ]
}

# -----------------------------------------------------------------------------
# TIER 2: ADEPT (Level 15-29)
# -----------------------------------------------------------------------------

CRUSHING_BLOW = {
    'id': 'crushing_blow', 'display_name': 'Crushing Blow',
    'description': 'A powerful overhead smash that deals bonus damage to targets affected by your Shatter Armor.',
    'level_req': 16, 'stamina_cost': 35, 'cooldown': 8.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'synergy_damage', 'damage_type': 'Physical', 'min_damage': 50, 'max_damage': 65, 'synergy_target': 'debuffed_by_shatter_armor', 'bonus_multiplier': 0.25}]
}

GROUND_SLAM = {
    'id': 'ground_slam', 'display_name': 'Ground Slam',
    'description': 'Slam your mace into the ground, sending a shockwave that damages and slows enemies in a short cone.',
    'level_req': 20, 'stamina_cost': 40, 'cooldown': 15.0, 'casting_time': 0.0, 'target_type': 'cone', 'range': 6,
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 20, 'max_damage': 25, 'cone_angle': 60},
        {'type': 'debuff', 'effect': 'slow', 'amount': 0.30, 'duration': 6.0, 'cone_angle': 60}
    ]
}

CONCUSS = {
    'id': 'concuss', 'display_name': 'Concuss',
    'description': 'A jarring blow that rattles the target, reducing the speed of their attacks for a short time.',
    'level_req': 24, 'stamina_cost': 20, 'cooldown': 12.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'debuff', 'stat': 'Haste_Percent', 'amount': -0.20, 'duration': 10.0}] # 20% slower attacks
}

BONEBREAKER = {
    'id': 'bonebreaker', 'display_name': 'Bonebreaker',
    'description': 'Your expertise with blunt weapons is terrifying. Your critical strikes now also reduce the target\'s movement speed by 50% for 4 seconds.',
    'level_req': 28, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'trigger': 'on_crit', 'effect': 'slow', 'amount': 0.50, 'duration': 4.0}]
}

# -----------------------------------------------------------------------------
# TIER 3: MASTER (Level 30-44)
# -----------------------------------------------------------------------------

HAMMER_OF_JUSTICE = {
    'id': 'hammer_of_justice', 'display_name': 'Hammer of Justice',
    'description': 'A holy or lawful strike that stuns the target for 4 seconds.',
    'level_req': 32, 'stamina_cost': 30, 'cooldown': 45.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'debuff', 'effect': 'stun', 'duration': 4.0}]
}

ARMOR_COLLAPSE = {
    'id': 'armor_collapse', 'display_name': 'Armor Collapse',
    'description': 'A devastating blow that completely ignores all of the target\'s Toughness for 8 seconds.',
    'level_req': 36, 'stamina_cost': 40, 'cooldown': 60.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'debuff', 'stat': 'Toughness_Ignore', 'amount': 1.0, 'duration': 8.0}] # Ignore 100% of Toughness
}

PUNISH = {
    'id': 'punish', 'display_name': 'Punish',
    'description': 'An attack that deals bonus damage for each of your active debuffs on the target.',
    'level_req': 40, 'stamina_cost': 35, 'cooldown': 10.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'finisher_damage', 'damage_type': 'Physical', 'min_damage': 60, 'max_damage': 70, 'consumes_stack': 'own_debuffs', 'bonus_damage_per_stack': 0.20}]
}

UNYIELDING = {
    'id': 'unyielding', 'display_name': 'Unyielding',
    'description': 'Brace yourself for impact, reducing all damage taken by 30% for 8 seconds.',
    'level_req': 44, 'stamina_cost': 20, 'cooldown': 120.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'stat': 'Damage_Reduction', 'amount': 0.30, 'duration': 8.0}]
}

# -----------------------------------------------------------------------------
# TIER 4: GRANDMASTER (Level 45-60)
# -----------------------------------------------------------------------------

SKULLCRACKER = {
    'id': 'skullcracker', 'display_name': 'Skullcracker',
    'description': 'A massive, telegraphed blow that deals extreme damage, but can only be used on a stunned or dazed target.',
    'level_req': 48, 'stamina_cost': 60, 'cooldown': 20.0, 'casting_time': 1.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'synergy_damage', 'damage_type': 'Physical', 'min_damage': 350, 'max_damage': 400, 'synergy_target': ['stunned', 'dazed']}]
}

MASTER_OF_CONTROL = {
    'id': 'master_of_control', 'display_name': 'Master of Control',
    'description': 'Your control over the battlefield is absolute. The duration of all your Stun and Daze effects is increased by 1 second.',
    'level_req': 52, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'stat': 'Stun_Daze_Duration', 'amount': 1.0}]
}

UNSTOPPABLE_FORCE = {
    'id': 'unstoppable_force', 'display_name': 'Unstoppable Force',
    'description': 'The ultimate offensive cooldown. For 12 seconds, you become immune to all crowd control effects and your attacks automatically apply a stack of Shatter Armor.',
    'level_req': 56, 'stamina_cost': 50, 'cooldown': 180.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'buff', 'effect': 'cc_immunity', 'duration': 12.0},
        {'type': 'buff', 'effect': 'auto_apply_debuff_on_hit', 'debuff_id': 'shatter_armor', 'duration': 12.0}
    ]
}

EARTHSHATTER = {
    'id': 'earthshatter', 'display_name': 'Earthshatter',
    'description': 'Slam your mace into the ground with titanic force, dealing moderate damage and stunning all nearby enemies for 4 seconds.',
    'level_req': 60, 'stamina_cost': 100, 'cooldown': 120.0, 'casting_time': 1.5, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 150, 'max_damage': 180, 'radius': 10},
        {'type': 'debuff', 'effect': 'stun', 'duration': 4.0, 'radius': 10}
    ]
}

# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------
ONE_HANDED_MACE_ABILITIES = {
    'bludgeon': BLUDGEON, 'shatter_armor': SHATTER_ARMOR, 'dazing_blow': DAZING_BLOW, 'shield_bash': SHIELD_BASH,
    'crushing_blow': CRUSHING_BLOW, 'ground_slam': GROUND_SLAM, 'concuss': CONCUSS, 'bonebreaker': BONEBREAKER,
    'hammer_of_justice': HAMMER_OF_JUSTICE, 'armor_collapse': ARMOR_COLLAPSE, 'punish': PUNISH, 'unyielding': UNYIELDING,
    'skullcracker': SKULLCRACKER, 'master_of_control': MASTER_OF_CONTROL, 'unstoppable_force': UNSTOPPABLE_FORCE, 'earthshatter': EARTHSHATTER,
}