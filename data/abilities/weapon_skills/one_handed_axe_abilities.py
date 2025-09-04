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