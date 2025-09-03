"""
This file contains all data for One-Handed Sword abilities.

Philosophy: High single-target damage, mid AoE damage, very low bleeding DoT,
and low debuff/CC. The sword wielder is a master of direct combat, excelling in
duels and skirmishes through consistent, powerful strikes.
"""

# -----------------------------------------------------------------------------
# TIER 1: APPRENTICE (Level 1-14)
# -----------------------------------------------------------------------------

HEROIC_STRIKE = {
    'id': 'heroic_strike', 'display_name': 'Heroic Strike',
    'description': 'A strong, direct attack that deals significant physical damage to a single target.',
    'level_req': 1, 'stamina_cost': 20, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 18, 'max_damage': 24}]
}

CLEAVE = {
    'id': 'cleave', 'display_name': 'Cleave',
    'description': 'A wide swing that strikes your primary target and up to 2 additional enemies in front of you.',
    'level_req': 4, 'stamina_cost': 25, 'cooldown': 6.0, 'casting_time': 0.0, 'target_type': 'cone', 'range': 'melee',
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 15, 'max_damage': 20, 'max_targets': 3, 'cone_angle': 90}]
}

DEFENSIVE_STANCE = {
    'id': 'defensive_stance', 'display_name': 'Defensive Stance',
    'description': 'Assume a defensive posture, reducing all damage you take by 15% but also reducing your damage dealt by 10%. Lasts until cancelled.',
    'level_req': 8, 'stamina_cost': 10, 'cooldown': 2.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'toggle_buff', 'buff_id': 'defensive_stance', 'damage_reduction': 0.15, 'damage_dealt_reduction': 0.10}]
}

PUMMEL = {
    'id': 'pummel', 'display_name': 'Pummel',
    'description': 'Strike the target with your weapon hilt, interrupting their spellcast and preventing them from casting from that school of magic for a short time.',
    'level_req': 12, 'stamina_cost': 15, 'cooldown': 12.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'debuff', 'effect': 'interrupt', 'duration': 0.5}, {'type': 'debuff', 'effect': 'school_lockout', 'duration': 4.0}]
}

# -----------------------------------------------------------------------------
# TIER 2: ADEPT (Level 15-29)
# -----------------------------------------------------------------------------

SUNDER_ARMOR = {
    'id': 'sunder_armor', 'display_name': 'Sunder Armor',
    'description': 'A forceful blow that weakens the target\'s armor, reducing their Toughness. Stacks up to 3 times.',
    'level_req': 16, 'stamina_cost': 15, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'debuff', 'stat': 'Toughness', 'amount': -20, 'duration': 20.0, 'max_stacks': 3}]
}

WHIRLWIND = {
    'id': 'whirlwind', 'display_name': 'Whirlwind',
    'description': 'Unleash a spinning attack, striking all nearby enemies for moderate physical damage.',
    'level_req': 20, 'stamina_cost': 40, 'cooldown': 10.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 30, 'max_damage': 35, 'radius': 6}]
}

DEEP_WOUNDS = {
    'id': 'deep_wounds', 'display_name': 'Deep Wounds',
    'description': 'Your critical strikes with sword abilities cause the target to bleed for 30% of the damage dealt over 6 seconds.',
    'level_req': 24, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'trigger': 'on_crit', 'effect': 'crit_to_bleed', 'conversion_rate': 0.30, 'duration': 6.0}]
}

BLADE_RUSH = {
    'id': 'blade_rush', 'display_name': 'Blade Rush',
    'description': 'Charge to an enemy, striking them for high damage and rooting them in place for 1 second.',
    'level_req': 28, 'stamina_cost': 30, 'cooldown': 15.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 20,
    'effects': [
        {'type': 'movement', 'effect': 'dash_to_target'},
        {'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 40, 'max_damage': 50},
        {'type': 'debuff', 'effect': 'root', 'duration': 1.0}
    ]
}

# -----------------------------------------------------------------------------
# TIER 3: MASTER (Level 30-44)
# -----------------------------------------------------------------------------

SWORDSMANS_PRECISION = {
    'id': 'swordsmans_precision', 'display_name': "Swordsman's Precision",
    'description': 'Your expertise with a blade increases your critical strike chance with one-handed swords by 5%.',
    'level_req': 32, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'stat': 'Crit_Chance', 'amount': 0.05}]
}

CONCUSSIVE_BLOW = {
    'id': 'concussive_blow', 'display_name': 'Concussive Blow',
    'description': 'A stunning blow to the head that incapacitates the target for 3 seconds.',
    'level_req': 36, 'stamina_cost': 25, 'cooldown': 30.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'debuff', 'effect': 'stun', 'duration': 3.0}]
}

RETALIATION = {
    'id': 'retaliation', 'display_name': 'Retaliation',
    'description': 'Enter a state of total focus for 12 seconds. Any time an enemy strikes you in melee, you instantly counter-attack.',
    'level_req': 40, 'stamina_cost': 20, 'cooldown': 120.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'retaliation', 'duration': 12.0}]
}

BLADE_FLURRY = {
    'id': 'blade_flurry', 'display_name': 'Blade Flurry',
    'description': 'A major offensive cooldown. Increases your attack speed by 30% for 15 seconds.',
    'level_req': 44, 'stamina_cost': 30, 'cooldown': 90.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'stat': 'Haste_Percent', 'amount': 0.30, 'duration': 15.0}]
}

# -----------------------------------------------------------------------------
# TIER 4: GRANDMASTER (Level 45-60)
# -----------------------------------------------------------------------------

EXECUTE = {
    'id': 'execute', 'display_name': 'Execute',
    'description': 'Attempt to finish off a foe, dealing massive damage to targets below 20% health.',
    'level_req': 48, 'stamina_cost': 40, 'cooldown': 5.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'execute_damage', 'damage_type': 'Physical', 'min_damage': 250, 'max_damage': 300, 'health_threshold': 0.20}]
}

RIPOSTE = {
    'id': 'riposte', 'display_name': 'Riposte',
    'description': 'Your mastery of swordplay gives you a chance to riposte when you parry an attack, dealing a high-damage counter-attack that cannot be blocked, dodged, or parried.',
    'level_req': 52, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'trigger': 'on_parry', 'effect': 'counter_attack', 'proc_chance': 1.0}] # 100% chance on parry
}

SHIELD_WALL = {
    'id': 'shield_wall', 'display_name': 'Shield Wall',
    'description': 'The ultimate defensive ability. Reduces all damage taken by 50% for 10 seconds. Requires a shield.',
    'level_req': 56, 'stamina_cost': 20, 'cooldown': 180.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'stat': 'Damage_Reduction', 'amount': 0.50, 'duration': 10.0, 'requires_item_type': 'shield'}]
}

BLADESTORM = {
    'id': 'bladestorm', 'display_name': 'Bladestorm',
    'description': 'Become an unstoppable storm of steel, striking all nearby enemies repeatedly for 6 seconds. You are immune to crowd control effects during Bladestorm.',
    'level_req': 60, 'stamina_cost': 100, 'cooldown': 120.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'channeled_aoe_damage', 'damage_type': 'Physical', 'tick_damage': 80, 'duration': 6.0, 'interval': 1.0, 'radius': 8},
        {'type': 'buff', 'effect': 'cc_immunity', 'duration': 6.0}
    ]
}

# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------
ONE_HANDED_SWORD_ABILITIES = {
    'heroic_strike': HEROIC_STRIKE, 'cleave': CLEAVE, 'defensive_stance': DEFENSIVE_STANCE, 'pummel': PUMMEL,
    'sunder_armor': SUNDER_ARMOR, 'whirlwind': WHIRLWIND, 'deep_wounds': DEEP_WOUNDS, 'blade_rush': BLADE_RUSH,
    'swordsmans_precision': SWORDSMANS_PRECISION, 'concussive_blow': CONCUSSIVE_BLOW, 'retaliation': RETALIATION, 'blade_flurry': BLADE_FLURRY,
    'execute': EXECUTE, 'riposte': RIPOSTE, 'shield_wall': SHIELD_WALL, 'bladestorm': BLADESTORM,
}