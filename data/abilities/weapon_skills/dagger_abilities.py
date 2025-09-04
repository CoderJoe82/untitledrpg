"""
This file contains all data for Dagger-based abilities.

Philosophy: High bleed (DoT) damage, low AoE, mid single-target damage, and very
low debuffing capability. The dagger wielder is a master of attrition, stacking
multiple bleeds to bring down even the toughest foes.
"""

# -----------------------------------------------------------------------------
# TIER 1: APPRENTICE (Level 1-14)
# -----------------------------------------------------------------------------

STAB = {
    'id': 'stab', 'display_name': 'Stab',
    'description': 'A quick, basic stab that deals physical damage. Generates combo points.',
    'level_req': 1, 'skill_req': 1, 'stamina_cost': 15, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 10, 'max_damage': 14}]
}

PUNCTURE = {
    'id': 'puncture', 'display_name': 'Puncture',
    'description': 'A precise strike that bypasses armor to inflict a bleeding wound, dealing damage over time.',
    'level_req': 4, 'skill_req': 5, 'stamina_cost': 20, 'cooldown': 6.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'dot', 'damage_type': 'Bleed', 'tick_damage': 5, 'duration': 12.0, 'interval': 1.0}]
}

QUICK_STEP = {
    'id': 'quick_step', 'display_name': 'Quick Step',
    'description': 'Perform a short, quick dash in the direction you are moving. Does not break stealth.',
    'level_req': 8, 'skill_req': 10, 'stamina_cost': 10, 'cooldown': 10.0, 'casting_time': 0.0, 'target_type': 'movement', 'range': 8,
    'effects': [{'type': 'movement', 'effect': 'dash'}]
}

GOUGE = {
    'id': 'gouge', 'display_name': 'Gouge',
    'description': 'A cheap shot that deals minor damage and briefly dazes the target. Attacking the target will break the daze.',
    'level_req': 12, 'skill_req': 15, 'stamina_cost': 25, 'cooldown': 15.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 5, 'max_damage': 8},
        {'type': 'debuff', 'effect': 'daze', 'duration': 4.0, 'break_on_damage': True}
    ]
}

# -----------------------------------------------------------------------------
# TIER 2: ADEPT (Level 15-29)
# -----------------------------------------------------------------------------

FAN_OF_KNIVES = {
    'id': 'fan_of_knives', 'display_name': 'Fan of Knives',
    'description': 'You throw daggers in a cone in front of you, dealing low damage to all targets hit. Your primary AoE tool.',
    'level_req': 16, 'skill_req': 20, 'stamina_cost': 35, 'cooldown': 8.0, 'casting_time': 0.0, 'target_type': 'cone', 'range': 8,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 20, 'max_damage': 25, 'cone_angle': 90}]
}

RUPTURE = {
    'id': 'rupture', 'display_name': 'Rupture',
    'description': 'A vicious finishing move that inflicts a powerful, long-lasting bleed on the target.',
    'level_req': 20, 'skill_req': 25, 'stamina_cost': 30, 'cooldown': 4.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'dot', 'damage_type': 'Bleed', 'tick_damage': 12, 'duration': 18.0, 'interval': 1.0}]
}

EXPOSE_WEAKNESS = {
    'id': 'expose_weakness', 'display_name': 'Expose Weakness',
    'description': 'You study the target, exposing a flaw that increases the damage they take from all your Bleed effects for a time.',
    'level_req': 24, 'skill_req': 30, 'stamina_cost': 20, 'cooldown': 20.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'debuff', 'stat': 'Bleed_Damage_Taken', 'amount': 0.20, 'duration': 15.0}] # Target takes 20% more damage from Bleeds
}

SHADOW_STRIKE = {
    'id': 'shadow_strike', 'display_name': 'Shadow Strike',
    'description': 'Strike from the shadows, dealing 150% weapon damage. Damage is increased if you are behind the target.',
    'level_req': 28, 'skill_req': 35, 'stamina_cost': 40, 'cooldown': 12.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'synergy_damage', 'damage_type': 'Physical', 'base_multiplier': 1.5, 'synergy_target': 'behind', 'bonus_multiplier': 0.5}]
}

# -----------------------------------------------------------------------------
# TIER 3: MASTER (Level 30-44)
# -----------------------------------------------------------------------------

POISONED_BLADE = {
    'id': 'poisoned_blade', 'display_name': 'Poisoned Blade',
    'description': 'Coat your daggers in a deadly poison. For 15 seconds, your attacks have a chance to apply a Poison DoT.',
    'level_req': 32, 'skill_req': 40, 'stamina_cost': 50, 'cooldown': 45.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'proc_dot_on_hit', 'proc_chance': 0.30, 'dot_id': 'deadly_poison', 'duration': 15.0}]
}

HEMORRHAGE = {
    'id': 'hemorrhage', 'display_name': 'Hemorrhage',
    'description': 'Your critical strikes with daggers now also cause the target to bleed for 25% of the damage dealt over 6 seconds.',
    'level_req': 36, 'skill_req': 45, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'trigger': 'on_crit', 'effect': 'crit_to_bleed', 'conversion_rate': 0.25, 'duration': 6.0}]
}

FLURRY_OF_STEEL = {
    'id': 'flurry_of_steel', 'display_name': 'Flurry of Steel',
    'description': 'Unleash a rapid series of 5 strikes over 2 seconds against a single target.',
    'level_req': 40, 'skill_req': 50, 'stamina_cost': 60, 'cooldown': 20.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'channeled_damage', 'damage_type': 'Physical', 'tick_damage': 25, 'duration': 2.0, 'interval': 0.4}]
}

CRIPPLING_POISON = {
    'id': 'crippling_poison', 'display_name': 'Crippling Poison',
    'description': 'Coat your daggers in a slowing poison. For 15 seconds, your attacks have a chance to slow the target\'s movement speed.',
    'level_req': 44, 'skill_req': 55, 'stamina_cost': 50, 'cooldown': 45.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'proc_debuff_on_hit', 'proc_chance': 0.50, 'debuff': 'slow', 'debuff_amount': 0.40, 'duration': 15.0}]
}

# -----------------------------------------------------------------------------
# TIER 4: GRANDMASTER (Level 45-60)
# -----------------------------------------------------------------------------

BLOODLETTING = {
    'id': 'bloodletting', 'display_name': 'Bloodletting',
    'description': 'A powerful cooldown that causes all of your active Bleed effects on the target to tick 100% faster for 8 seconds.',
    'level_req': 48, 'skill_req': 60, 'stamina_cost': 40, 'cooldown': 90.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'debuff', 'effect': 'dot_haste', 'dot_type': 'Bleed', 'haste_percent': 1.0, 'duration': 8.0}]
}

EVISCERATE = {
    'id': 'eviscerate', 'display_name': 'Eviscerate',
    'description': 'A brutal finishing move that deals massive damage, increased by 50% if the target is bleeding.',
    'level_req': 52, 'skill_req': 65, 'stamina_cost': 75, 'cooldown': 10.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'synergy_damage', 'damage_type': 'Physical', 'min_damage': 200, 'max_damage': 250, 'synergy_target': 'bleeding', 'bonus_multiplier': 0.5}]
}

VANISH = {
    'id': 'vanish', 'display_name': 'Vanish',
    'description': 'Instantly disappear from sight, entering stealth and clearing all movement-impairing effects. Your first attack from Vanish is a guaranteed critical strike.',
    'level_req': 56, 'skill_req': 70, 'stamina_cost': 30, 'cooldown': 180.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'invisibility', 'duration': 10.0}, {'type': 'buff', 'effect': 'guaranteed_crit', 'charges': 1}]
}

EXSANGUINATE = {
    'id': 'exsanguinate', 'display_name': 'Exsanguinate',
    'description': 'The ultimate bleed ability. Inflicts a horrific wound that deals extreme damage over a short duration and reduces all healing the target receives.',
    'level_req': 60, 'skill_req': 75, 'stamina_cost': 100, 'cooldown': 120.0, 'casting_time': 1.0, 'target_type': 'single', 'range': 'melee',
    'effects': [
        {'type': 'dot', 'damage_type': 'Bleed', 'tick_damage': 100, 'duration': 8.0, 'interval': 1.0},
        {'type': 'debuff', 'stat': 'Healing_Received', 'amount': -0.50, 'duration': 8.0}
    ]
}

# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------
DAGGER_ABILITIES = {
    'stab': STAB, 'puncture': PUNCTURE, 'quick_step': QUICK_STEP, 'gouge': GOUGE,
    'fan_of_knives': FAN_OF_KNIVES, 'rupture': RUPTURE, 'expose_weakness': EXPOSE_WEAKNESS, 'shadow_strike': SHADOW_STRIKE,
    'poisoned_blade': POISONED_BLADE, 'hemorrhage': HEMORRHAGE, 'flurry_of_steel': FLURRY_OF_STEEL, 'crippling_poison': CRIPPLING_POISON,
    'bloodletting': BLOODLETTING, 'eviscerate': EVISCERATE, 'vanish': VANISH, 'exsanguinate': EXSANGUINATE,
}