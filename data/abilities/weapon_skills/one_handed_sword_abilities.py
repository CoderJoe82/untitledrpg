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
    'level_req': 1, 'skill_req': 1, 'stamina_cost': 20, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 18, 'max_damage': 24}]
}

CLEAVE = {
    'id': 'cleave', 'display_name': 'Cleave',
    'description': 'A wide swing that strikes your primary target and up to 2 additional enemies in front of you.',
    'level_req': 4, 'skill_req': 5, 'stamina_cost': 25, 'cooldown': 6.0, 'casting_time': 0.0, 'target_type': 'cone', 'range': 'melee',
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 15, 'max_damage': 20, 'max_targets': 3, 'cone_angle': 90}]
}

DEFENSIVE_STANCE = {
    'id': 'defensive_stance', 'display_name': 'Defensive Stance',
    'description': 'Assume a defensive posture, reducing all damage you take by 15% but also reducing your damage dealt by 10%. Lasts until cancelled.',
    'level_req': 8, 'skill_req': 10, 'stamina_cost': 10, 'cooldown': 2.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'toggle_buff', 'buff_id': 'defensive_stance', 'damage_reduction': 0.15, 'damage_dealt_reduction': 0.10}]
}

PUMMEL = {
    'id': 'pummel', 'display_name': 'Pummel',
    'description': 'Strike the target with your weapon hilt, interrupting their spellcast and preventing them from casting from that school of magic for a short time.',
    'level_req': 12, 'skill_req': 15, 'stamina_cost': 15, 'cooldown': 12.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'debuff', 'effect': 'interrupt', 'duration': 0.5}, {'type': 'debuff', 'effect': 'school_lockout', 'duration': 4.0}]
}

# -----------------------------------------------------------------------------
# TIER 2: ADEPT (Level 15-29)
# -----------------------------------------------------------------------------

SUNDER_ARMOR = {
    'id': 'sunder_armor', 'display_name': 'Sunder Armor',
    'description': 'A forceful blow that weakens the target\'s armor, reducing their Toughness. Stacks up to 3 times.',
    'level_req': 16, 'skill_req': 20, 'stamina_cost': 15, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'debuff', 'stat': 'Toughness', 'amount': -20, 'duration': 20.0, 'max_stacks': 3}]
}

WHIRLWIND = {
    'id': 'whirlwind', 'display_name': 'Whirlwind',
    'description': 'Unleash a spinning attack, striking all nearby enemies for moderate physical damage.',
    'level_req': 20, 'skill_req': 25, 'stamina_cost': 40, 'cooldown': 10.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 30, 'max_damage': 35, 'radius': 6}]
}

DEEP_WOUNDS = {
    'id': 'deep_wounds', 'display_name': 'Deep Wounds',
    'description': 'Your critical strikes with sword abilities cause the target to bleed for 30% of the damage dealt over 6 seconds.',
    'level_req': 24, 'skill_req': 30, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'trigger': 'on_crit', 'effect': 'crit_to_bleed', 'conversion_rate': 0.30, 'duration': 6.0}]
}

BLADE_RUSH = {
    'id': 'blade_rush', 'display_name': 'Blade Rush',
    'description': 'Charge to an enemy, striking them for high damage and rooting them in place for 1 second.',
    'level_req': 28, 'skill_req': 35, 'stamina_cost': 30, 'cooldown': 15.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 20,
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
    'level_req': 32, 'skill_req': 40, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'stat': 'Crit_Chance', 'amount': 0.05}]
}

CONCUSSIVE_BLOW = {
    'id': 'concussive_blow', 'display_name': 'Concussive Blow',
    'description': 'A stunning blow to the head that incapacitates the target for 3 seconds.',
    'level_req': 36, 'skill_req': 45, 'stamina_cost': 25, 'cooldown': 30.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'debuff', 'effect': 'stun', 'duration': 3.0}]
}

RETALIATION = {
    'id': 'retaliation', 'display_name': 'Retaliation',
    'description': 'Enter a state of total focus for 12 seconds. Any time an enemy strikes you in melee, you instantly counter-attack.',
    'level_req': 40, 'skill_req': 50, 'stamina_cost': 20, 'cooldown': 120.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'retaliation', 'duration': 12.0}]
}

BLADE_FLURRY = {
    'id': 'blade_flurry', 'display_name': 'Blade Flurry',
    'description': 'A major offensive cooldown. Increases your attack speed by 30% for 15 seconds.',
    'level_req': 44, 'skill_req': 55, 'stamina_cost': 30, 'cooldown': 90.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'stat': 'Haste_Percent', 'amount': 0.30, 'duration': 15.0}]
}

# -----------------------------------------------------------------------------
# TIER 4: GRANDMASTER (Level 45-60)
# -----------------------------------------------------------------------------

EXECUTE = {
    'id': 'execute', 'display_name': 'Execute',
    'description': 'Attempt to finish off a foe, dealing massive damage to targets below 20% health.',
    'level_req': 48, 'skill_req': 60, 'stamina_cost': 40, 'cooldown': 5.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'execute_damage', 'damage_type': 'Physical', 'min_damage': 250, 'max_damage': 300, 'health_threshold': 0.20}]
}

RIPOSTE = {
    'id': 'riposte', 'display_name': 'Riposte',
    'description': 'Your mastery of swordplay gives you a chance to riposte when you parry an attack, dealing a high-damage counter-attack that cannot be blocked, dodged, or parried.',
    'level_req': 52, 'skill_req': 65, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'trigger': 'on_parry', 'effect': 'counter_attack', 'proc_chance': 1.0}] # 100% chance on parry
}

SHIELD_WALL = {
    'id': 'shield_wall', 'display_name': 'Shield Wall',
    'description': 'The ultimate defensive ability. Reduces all damage taken by 50% for 10 seconds. Requires a shield.',
    'level_req': 56, 'skill_req': 70, 'stamina_cost': 20, 'cooldown': 180.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'stat': 'Damage_Reduction', 'amount': 0.50, 'duration': 10.0, 'requires_item_type': 'shield'}]
}

BLADESTORM = {
    'id': 'bladestorm', 'display_name': 'Bladestorm',
    'description': 'Become an unstoppable storm of steel, striking all nearby enemies repeatedly for 6 seconds. You are immune to crowd control effects during Bladestorm.',
    'level_req': 60, 'skill_req': 75, 'stamina_cost': 100, 'cooldown': 120.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
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

"""
This file contains all data for One-Handed Axe abilities.

Philosophy: High single-target damage, low AoE, mid bleed, and very low CC.
The axe wielder is a ferocious attacker, focusing on overwhelming a single foe
with brutal chops and deep, bleeding wounds.
"""

# -----------------------------------------------------------------------------
# TIER 1: APPRENTICE (Level 1-14)
# -----------------------------------------------------------------------------

SAVAGE_STRIKE = {
    'id': 'savage_strike', 'display_name': 'Savage Strike',
    'description': 'A vicious, overhead chop that deals heavy physical damage to one enemy.',
    'level_req': 1, 'skill_req': 1, 'stamina_cost': 22, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 20, 'max_damage': 26}]
}

RENDING_CHOP = {
    'id': 'rending_chop', 'display_name': 'Rending Chop',
    'description': 'A targeted strike that tears flesh, causing the enemy to bleed for a short duration.',
    'level_req': 4, 'skill_req': 5, 'stamina_cost': 20, 'cooldown': 8.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'dot', 'damage_type': 'Bleed', 'tick_damage': 6, 'duration': 10.0, 'interval': 1.0}]
}

BATTLE_TRANCE = {
    'id': 'battle_trance', 'display_name': 'Battle Trance',
    'description': 'Enter a focused trance for 10 seconds, increasing all physical damage you deal by 10%.',
    'level_req': 8, 'skill_req': 10, 'stamina_cost': 15, 'cooldown': 45.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'stat': 'Physical_Damage_Percent', 'amount': 0.10, 'duration': 10.0}]
}

THROWING_AXE = {
    'id': 'throwing_axe', 'display_name': 'Throwing Axe',
    'description': 'Hurl your axe at a distant enemy to deal minor damage and grab their attention.',
    'level_req': 12, 'skill_req': 15, 'stamina_cost': 10, 'cooldown': 6.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 25,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 10, 'max_damage': 15}]
}

# -----------------------------------------------------------------------------
# TIER 2: ADEPT (Level 15-29)
# -----------------------------------------------------------------------------

MUTILATE = {
    'id': 'mutilate', 'display_name': 'Mutilate',
    'description': 'A brutal strike that deals 25% bonus damage to targets that are already bleeding.',
    'level_req': 16, 'skill_req': 20, 'stamina_cost': 30, 'cooldown': 6.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'synergy_damage', 'damage_type': 'Physical', 'min_damage': 40, 'max_damage': 50, 'synergy_target': 'bleeding', 'bonus_multiplier': 0.25}]
}

WIDE_SWING = {
    'id': 'wide_swing', 'display_name': 'Wide Swing',
    'description': 'A sweeping attack that hits your primary target and one additional nearby enemy.',
    'level_req': 20, 'skill_req': 25, 'stamina_cost': 35, 'cooldown': 10.0, 'casting_time': 0.0, 'target_type': 'cone', 'range': 'melee',
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 25, 'max_damage': 30, 'max_targets': 2, 'cone_angle': 90}]
}

JAGGED_EDGE = {
    'id': 'jagged_edge', 'display_name': 'Jagged Edge',
    'description': 'The vicious edge of your axe is unforgiving. Your normal attacks now have a 15% chance to cause a minor bleed.',
    'level_req': 24, 'skill_req': 30, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'trigger': 'on_hit', 'effect': 'proc_dot_on_hit', 'proc_chance': 0.15, 'dot_id': 'minor_bleed'}]
}

OVERWHELM = {
    'id': 'overwhelm', 'display_name': 'Overwhelm',
    'description': 'An aggressive opening attack that deals 30% more damage to targets above 80% health.',
    'level_req': 28, 'skill_req': 35, 'stamina_cost': 25, 'cooldown': 12.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'synergy_damage', 'damage_type': 'Physical', 'min_damage': 50, 'max_damage': 60, 'synergy_target': 'high_health', 'health_threshold': 0.80, 'bonus_multiplier': 0.30}]
}

# -----------------------------------------------------------------------------
# TIER 3: MASTER (Level 30-44)
# -----------------------------------------------------------------------------

GUSHING_WOUND = {
    'id': 'gushing_wound', 'display_name': 'Gushing Wound',
    'description': 'Twist the axe in the wound, instantly dealing 50% of the remaining damage of all your active Bleeds on the target.',
    'level_req': 32, 'skill_req': 40, 'stamina_cost': 40, 'cooldown': 18.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'synergy_damage', 'consumes': 'bleed_percent', 'damage_multiplier': 0.50}]
}

RAMPAGE = {
    'id': 'rampage', 'display_name': 'Rampage',
    'description': 'A furious offensive cooldown. Increases your attack speed and critical strike chance for 12 seconds.',
    'level_req': 36, 'skill_req': 45, 'stamina_cost': 20, 'cooldown': 90.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'buff', 'stat': 'Haste_Percent', 'amount': 0.20, 'duration': 12.0},
        {'type': 'buff', 'stat': 'Crit_Chance', 'amount': 0.10, 'duration': 12.0}
    ]
}

DEEP_GOUGE = {
    'id': 'deep_gouge', 'display_name': 'Deep Gouge',
    'description': 'A powerful hewing blow that inflicts a severe, long-lasting bleed.',
    'level_req': 40, 'skill_req': 50, 'stamina_cost': 35, 'cooldown': 15.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'dot', 'damage_type': 'Bleed', 'tick_damage': 20, 'duration': 15.0, 'interval': 1.0}]
}

SHATTER_DEFENSES = {
    'id': 'shatter_defenses', 'display_name': 'Shatter Defenses',
    'description': 'A mighty blow that shatters shields and armor, reducing the target\'s Toughness by a large amount for a short time.',
    'level_req': 44, 'skill_req': 55, 'stamina_cost': 25, 'cooldown': 30.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'debuff', 'stat': 'Toughness', 'amount': -100, 'duration': 8.0}]
}

# -----------------------------------------------------------------------------
# TIER 4: GRANDMASTER (Level 45-60)
# -----------------------------------------------------------------------------

DECAPITATE = {
    'id': 'decapitate', 'display_name': 'Decapitate',
    'description': 'Attempt to execute a wounded foe, dealing massive damage to targets below 25% health.',
    'level_req': 48, 'skill_req': 60, 'stamina_cost': 50, 'cooldown': 8.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'execute_damage', 'damage_type': 'Physical', 'min_damage': 300, 'max_damage': 350, 'health_threshold': 0.25}]
}

ARTERIAL_STRIKE = {
    'id': 'arterial_strike', 'display_name': 'Arterial Strike',
    'description': 'Your savage strikes are aimed to kill. Your Bleed effects can now critically strike, dealing 50% bonus damage.',
    'level_req': 52, 'skill_req': 65, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'enhances_spell': 'all_bleeds', 'effect': 'dots_can_crit', 'crit_damage_multiplier': 1.5}]
}

DEATH_WISH = {
    'id': 'death_wish', 'display_name': 'Death Wish',
    'description': 'The ultimate berserker state. For 10 seconds, you deal 30% more physical damage, but you also take 15% more damage from all sources.',
    'level_req': 56, 'skill_req': 70, 'stamina_cost': 10, 'cooldown': 120.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'buff', 'stat': 'Physical_Damage_Percent', 'amount': 0.30, 'duration': 10.0},
        {'type': 'buff', 'stat': 'Damage_Taken', 'amount': 0.15, 'duration': 10.0}
    ]
}

EXECUTIONERS_CHOP = {
    'id': 'executioners_chop', 'display_name': "Executioner's Chop",
    'description': 'A massive, single strike that deals bonus damage for each of your Bleed effects currently active on the target.',
    'level_req': 60, 'skill_req': 75, 'stamina_cost': 80, 'cooldown': 45.0, 'casting_time': 1.5, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'finisher_damage', 'damage_type': 'Physical', 'min_damage': 200, 'max_damage': 220, 'consumes_stack': 'bleed_effects', 'bonus_damage_per_stack': 0.30}] # 30% bonus damage per bleed
}

# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------
ONE_HANDED_AXE_ABILITIES = {
    'savage_strike': SAVAGE_STRIKE, 'rending_chop': RENDING_CHOP, 'battle_trance': BATTLE_TRANCE, 'throwing_axe': THROWING_AXE,
    'mutilate': MUTILATE, 'wide_swing': WIDE_SWING, 'jagged_edge': JAGGED_EDGE, 'overwhelm': OVERWHELM,
    'gushing_wound': GUSHING_WOUND, 'rampage': RAMPAGE, 'deep_gouge': DEEP_GOUGE, 'shatter_defenses': SHATTER_DEFENSES,
    'decapitate': DECAPITATE, 'arterial_strike': ARTERIAL_STRIKE, 'death_wish': DEATH_WISH, 'executioners_chop': EXECUTIONERS_CHOP,
}