"""
This file contains all data for Two-Handed Sword abilities.

Philosophy: High single-target damage, mid AoE damage, mid bleed damage, and
mid crit damage. The two-handed sword wielder is a master of overwhelming force,
delivering devastating blows that can execute single foes or cleave through groups.
"""

# -----------------------------------------------------------------------------
# TIER 1: APPRENTICE (Level 1-14)
# -----------------------------------------------------------------------------

MIGHTY_SWING = {
    'id': 'mighty_swing', 'display_name': 'Mighty Swing',
    'description': 'A powerful swing that deals heavy physical damage to a single target.',
    'level_req': 1, 'skill_req': 1, 'stamina_cost': 25, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 25, 'max_damage': 32}]
}

SWEEPING_CLEAVE = {
    'id': 'sweeping_cleave', 'display_name': 'Sweeping Cleave',
    'description': 'A wide, horizontal slash that damages your primary target and up to 2 other nearby enemies.',
    'level_req': 4, 'skill_req': 5, 'stamina_cost': 30, 'cooldown': 8.0, 'casting_time': 0.0, 'target_type': 'cone', 'range': 'melee',
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 20, 'max_damage': 25, 'max_targets': 3, 'cone_angle': 120}]
}

BATTLE_STANCE = {
    'id': 'battle_stance', 'display_name': 'Battle Stance',
    'description': 'An aggressive combat stance that increases your critical strike chance by 5%, but reduces your Toughness. Lasts until cancelled.',
    'level_req': 8, 'skill_req': 10, 'stamina_cost': 10, 'cooldown': 2.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'toggle_buff', 'buff_id': 'battle_stance', 'crit_chance_increase': 0.05, 'toughness_reduction': -50}]
}

LACERATE = {
    'id': 'lacerate', 'display_name': 'Lacerate',
    'description': 'Tear a deep gash in the enemy, causing them to bleed over a short duration.',
    'level_req': 12, 'skill_req': 15, 'stamina_cost': 20, 'cooldown': 10.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'dot', 'damage_type': 'Bleed', 'tick_damage': 8, 'duration': 9.0, 'interval': 1.0}]
}

# -----------------------------------------------------------------------------
# TIER 2: ADEPT (Level 15-29)
# -----------------------------------------------------------------------------

OVERPOWER = {
    'id': 'overpower', 'display_name': 'Overpower',
    'description': 'Overpower the enemy with a swift, powerful strike that cannot be blocked, dodged, or parried. Can only be used after one of your attacks is dodged.',
    'level_req': 16, 'skill_req': 20, 'stamina_cost': 15, 'cooldown': 1.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'synergy_damage', 'damage_type': 'Physical', 'min_damage': 60, 'max_damage': 75, 'synergy_target': 'enemy_dodge', 'guaranteed_hit': True}]
}

DEEP_WOUNDS = {
    'id': 'deep_wounds', 'display_name': 'Deep Wounds',
    'description': 'Your critical strikes with two-handed sword abilities are so severe they cause the target to bleed for 40% of the damage dealt over 6 seconds.',
    'level_req': 20, 'skill_req': 25, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'trigger': 'on_crit', 'effect': 'crit_to_bleed', 'conversion_rate': 0.40, 'duration': 6.0}]
}

WARBREAKER = {
    'id': 'warbreaker', 'display_name': 'Warbreaker',
    'description': 'Slam your sword into the ground, sending a shockwave that damages and weakens the armor of all enemies in a line.',
    'level_req': 24, 'skill_req': 30, 'stamina_cost': 40, 'cooldown': 20.0, 'casting_time': 0.0, 'target_type': 'line', 'range': 15,
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 40, 'max_damage': 50, 'line_width': 4},
        {'type': 'debuff', 'stat': 'Toughness', 'amount': -75, 'duration': 10.0, 'line_width': 4}
    ]
}

MORTAL_STRIKE = {
    'id': 'mortal_strike', 'display_name': 'Mortal Strike',
    'description': 'A vicious strike that deals heavy damage and reduces the effectiveness of all healing on the target for 8 seconds.',
    'level_req': 28, 'skill_req': 35, 'stamina_cost': 35, 'cooldown': 12.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 80, 'max_damage': 100},
        {'type': 'debuff', 'stat': 'Healing_Received', 'amount': -0.25, 'duration': 8.0}
    ]
}

# -----------------------------------------------------------------------------
# TIER 3: MASTER (Level 30-44)
# -----------------------------------------------------------------------------

COLOSSUS_SMASH = {
    'id': 'colossus_smash', 'display_name': 'Colossus Smash',
    'description': 'A devastating blow that completely shatters the target\'s defenses, allowing you to ignore all of their Toughness for 6 seconds.',
    'level_req': 32, 'skill_req': 40, 'stamina_cost': 30, 'cooldown': 45.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 50, 'max_damage': 60},
        {'type': 'debuff', 'stat': 'Toughness_Ignore_From_Caster', 'amount': 1.0, 'duration': 6.0}
    ]
}

RECKLESSNESS = {
    'id': 'recklessness', 'display_name': 'Recklessness',
    'description': 'Enter a state of pure rage for 12 seconds, increasing your critical strike chance by 25%.',
    'level_req': 36, 'skill_req': 45, 'stamina_cost': 20, 'cooldown': 120.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'stat': 'Crit_Chance', 'amount': 0.25, 'duration': 12.0}]
}

GREATSWORD_MASTER = {
    'id': 'greatsword_master', 'display_name': 'Greatsword Master',
    'description': 'Your mastery of the greatsword is legendary. You deal 10% more damage with two-handed swords, and your critical strikes have a chance to daze the target.',
    'level_req': 40, 'skill_req': 50, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'passive_enhancement', 'stat': 'Two_Handed_Sword_Damage', 'amount': 0.10},
        {'type': 'passive_enhancement', 'trigger': 'on_crit', 'effect': 'daze', 'proc_chance': 0.30, 'duration': 2.0}
    ]
}

SHOCKWAVE = {
    'id': 'shockwave', 'display_name': 'Shockwave',
    'description': 'Slam your sword down to create a cone of force that damages and stuns all enemies in front of you.',
    'level_req': 44, 'skill_req': 55, 'stamina_cost': 40, 'cooldown': 30.0, 'casting_time': 0.0, 'target_type': 'cone', 'range': 12,
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 60, 'max_damage': 70, 'cone_angle': 60},
        {'type': 'debuff', 'effect': 'stun', 'duration': 2.5, 'cone_angle': 60}
    ]
}

# -----------------------------------------------------------------------------
# TIER 4: GRANDMASTER (Level 45-60)
# -----------------------------------------------------------------------------

EXECUTE = {
    'id': 'execute', 'display_name': 'Execute',
    'description': 'Attempt to finish off a foe, dealing massive damage to targets below 20% health. Refunds stamina if the target dies.',
    'level_req': 48, 'skill_req': 60, 'stamina_cost': 50, 'cooldown': 5.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'execute_damage', 'damage_type': 'Physical', 'min_damage': 400, 'max_damage': 500, 'health_threshold': 0.20, 'refund_on_kill': True}]
}

BLADESTORM = {
    'id': 'bladestorm', 'display_name': 'Bladestorm',
    'description': 'Become an unstoppable storm of steel, striking all nearby enemies repeatedly for 6 seconds. You are immune to crowd control effects during Bladestorm.',
    'level_req': 52, 'skill_req': 65, 'stamina_cost': 100, 'cooldown': 90.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'channeled_aoe_damage', 'damage_type': 'Physical', 'tick_damage': 100, 'duration': 6.0, 'interval': 1.0, 'radius': 8},
        {'type': 'buff', 'effect': 'cc_immunity', 'duration': 6.0}
    ]
}

TITANS_GRIP = {
    'id': 'titans_grip', 'display_name': "Titan's Grip",
    'description': 'Your strength is monumental. You can now wield two-handed swords in one hand, allowing you to use a shield or another one-handed weapon alongside it.',
    'level_req': 56, 'skill_req': 70, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'effect': 'allow_one_handing_two_handers'}]
}

DEATH_SENTENCE = {
    'id': 'death_sentence', 'display_name': 'Death Sentence',
    'description': 'The ultimate execution. After a brief delay, you bring your sword down with finality. Deals massive damage, increased by 100% against targets below 25% health.',
    'level_req': 60, 'skill_req': 75, 'stamina_cost': 80, 'cooldown': 120.0, 'casting_time': 1.5, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'execute_damage', 'damage_type': 'Physical', 'min_damage': 500, 'max_damage': 600, 'health_threshold': 0.25, 'bonus_multiplier': 1.0}]
}

# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------
TWO_HANDED_SWORD_ABILITIES = {
    'mighty_swing': MIGHTY_SWING, 'sweeping_cleave': SWEEPING_CLEAVE, 'battle_stance': BATTLE_STANCE, 'lacerate': LACERATE,
    'overpower': OVERPOWER, 'deep_wounds': DEEP_WOUNDS, 'warbreaker': WARBREAKER, 'mortal_strike': MORTAL_STRIKE,
    'colossus_smash': COLOSSUS_SMASH, 'recklessness': RECKLESSNESS, 'greatsword_master': GREATSWORD_MASTER, 'shockwave': SHOCKWAVE,
    'execute': EXECUTE, 'bladestorm': BLADESTORM, 'titans_grip': TITANS_GRIP, 'death_sentence': DEATH_SENTENCE,
}