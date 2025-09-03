"""
This file contains all data for Bow abilities.

Philosophy: High single-target damage, mid AoE damage, mid bleed, and low CC.
The archer is a master of ranged combat, focusing on taking down key targets
from a distance with powerful, precise shots and sustained pressure.
"""

# -----------------------------------------------------------------------------
# TIER 1: APPRENTICE (Level 1-14)
# -----------------------------------------------------------------------------

STEADY_SHOT = {
    'id': 'steady_shot', 'display_name': 'Steady Shot',
    'description': 'A carefully aimed shot that deals moderate physical damage. Can be cast while moving.',
    'level_req': 1, 'stamina_cost': 15, 'cooldown': 0.0, 'casting_time': 1.5, 'target_type': 'single', 'range': 40,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 15, 'max_damage': 20}]
}

SERPENT_STING = {
    'id': 'serpent_sting', 'display_name': 'Serpent Sting',
    'description': 'Fires a stinging arrow that poisons the target, dealing Nature damage over time.',
    'level_req': 4, 'stamina_cost': 20, 'cooldown': 6.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 40,
    'effects': [{'type': 'dot', 'damage_type': 'Poison', 'tick_damage': 6, 'duration': 15.0, 'interval': 1.0}]
}

DISENGAGE = {
    'id': 'disengage', 'display_name': 'Disengage',
    'description': 'Leap backwards a short distance, creating space between you and your enemy.',
    'level_req': 8, 'stamina_cost': 10, 'cooldown': 20.0, 'casting_time': 0.0, 'target_type': 'movement', 'range': 15,
    'effects': [{'type': 'movement', 'effect': 'leap_backward'}]
}

AIMED_SHOT = {
    'id': 'aimed_shot', 'display_name': 'Aimed Shot',
    'description': 'A powerful, aimed shot that deals high physical damage. Must be standing still to cast.',
    'level_req': 12, 'stamina_cost': 35, 'cooldown': 4.0, 'casting_time': 2.5, 'target_type': 'single', 'range': 40,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 40, 'max_damage': 55}]
}

# -----------------------------------------------------------------------------
# TIER 2: ADEPT (Level 15-29)
# -----------------------------------------------------------------------------

MULTI_SHOT = {
    'id': 'multi_shot', 'display_name': 'Multi-Shot',
    'description': 'Fires a spray of arrows, hitting your target and up to 3 nearby enemies for reduced damage.',
    'level_req': 16, 'stamina_cost': 40, 'cooldown': 8.0, 'casting_time': 0.0, 'target_type': 'cone', 'range': 35,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 25, 'max_damage': 30, 'max_targets': 4, 'cone_angle': 60}]
}

BARBED_ARROW = {
    'id': 'barbed_arrow', 'display_name': 'Barbed Arrow',
    'description': 'Fires a cruel arrow that causes the target to bleed heavily, dealing damage over time.',
    'level_req': 20, 'stamina_cost': 25, 'cooldown': 10.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 40,
    'effects': [{'type': 'dot', 'damage_type': 'Bleed', 'tick_damage': 15, 'duration': 12.0, 'interval': 1.0}]
}

CONCUSSIVE_SHOT = {
    'id': 'concussive_shot', 'display_name': 'Concussive Shot',
    'description': 'Fire a blunt arrow that dazes the target, slowing their movement speed significantly for 6 seconds.',
    'level_req': 24, 'stamina_cost': 15, 'cooldown': 15.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 40,
    'effects': [{'type': 'debuff', 'effect': 'slow', 'amount': 0.50, 'duration': 6.0}]
}

HUNTERS_MARK = {
    'id': 'hunters_mark', 'display_name': "Hunter's Mark",
    'description': 'Mark a target, causing them to take 10% increased damage from all of your attacks for a long duration.',
    'level_req': 28, 'stamina_cost': 10, 'cooldown': 3.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 50,
    'effects': [{'type': 'debuff', 'stat': 'Damage_Taken_From_Caster', 'amount': 0.10, 'duration': 180.0}]
}

# -----------------------------------------------------------------------------
# TIER 3: MASTER (Level 30-44)
# -----------------------------------------------------------------------------

VOLLEY = {
    'id': 'volley', 'display_name': 'Volley',
    'description': 'Fire a volley of arrows at a target location, dealing continuous damage to enemies within the area.',
    'level_req': 32, 'stamina_cost': 60, 'cooldown': 45.0, 'casting_time': 0.0, 'target_type': 'aoe_ground', 'range': 40,
    'effects': [{'type': 'channeled_dot', 'damage_type': 'Physical', 'tick_damage': 20, 'duration': 6.0, 'interval': 1.0, 'radius': 8}]
}

PIERCING_SHOT = {
    'id': 'piercing_shot', 'display_name': 'Piercing Shot',
    'description': 'A powerful shot that ignores 50% of the target\'s Toughness.',
    'level_req': 36, 'stamina_cost': 40, 'cooldown': 12.0, 'casting_time': 2.0, 'target_type': 'single', 'range': 40,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 80, 'max_damage': 100, 'armor_penetration': 0.50}]
}

RAPID_FIRE = {
    'id': 'rapid_fire', 'display_name': 'Rapid Fire',
    'description': 'Enter a state of heightened focus, increasing your attack speed by 40% for 12 seconds.',
    'level_req': 40, 'stamina_cost': 30, 'cooldown': 90.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'stat': 'Haste_Percent', 'amount': 0.40, 'duration': 12.0}]
}

BINDING_SHOT = {
    'id': 'binding_shot', 'display_name': 'Binding Shot',
    'description': 'Fires a tethering arrow at the ground. Enemies that move too far from the arrow are rooted in place for 4 seconds.',
    'level_req': 44, 'stamina_cost': 25, 'cooldown': 45.0, 'casting_time': 0.0, 'target_type': 'aoe_ground', 'range': 35,
    'effects': [{'type': 'ground_debuff', 'effect': 'tether_root', 'duration': 10.0, 'radius': 8, 'tether_length': 10, 'root_duration': 4.0}]
}

# -----------------------------------------------------------------------------
# TIER 4: GRANDMASTER (Level 45-60)
# -----------------------------------------------------------------------------

MASTER_MARKSMAN = {
    'id': 'master_marksman', 'display_name': 'Master Marksman',
    'description': 'Your mastery of the bow is unparalleled. Your Aimed Shot now has a 20% chance to fire again instantly at no cost.',
    'level_req': 48, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'enhances_spell': 'aimed_shot', 'effect': 'proc_free_cast', 'proc_chance': 0.20}]
}

KILL_SHOT = {
    'id': 'kill_shot', 'display_name': 'Kill Shot',
    'description': 'Attempt to finish off a wounded target, dealing massive damage to enemies below 20% health.',
    'level_req': 52, 'stamina_cost': 20, 'cooldown': 8.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 45,
    'effects': [{'type': 'execute_damage', 'damage_type': 'Physical', 'min_damage': 300, 'max_damage': 350, 'health_threshold': 0.20}]
}

TRUESHOT = {
    'id': 'trueshot', 'display_name': 'Trueshot',
    'description': 'The ultimate archery cooldown. For 15 seconds, your attack speed is increased by 30% and your critical strike chance is increased by 20%.',
    'level_req': 56, 'stamina_cost': 50, 'cooldown': 180.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'buff', 'stat': 'Haste_Percent', 'amount': 0.30, 'duration': 15.0},
        {'type': 'buff', 'stat': 'Crit_Chance', 'amount': 0.20, 'duration': 15.0}
    ]
}

WINDBURST = {
    'id': 'windburst', 'display_name': 'Windburst',
    'description': 'Fire an arrow infused with the power of wind. Deals high damage, knocks the target back, and leaves a trail of wind that increases the movement speed of allies who walk through it.',
    'level_req': 60, 'stamina_cost': 75, 'cooldown': 45.0, 'casting_time': 1.5, 'target_type': 'single', 'range': 40,
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Nature', 'min_damage': 200, 'max_damage': 220},
        {'type': 'debuff', 'effect': 'knockback', 'distance': 15},
        {'type': 'ground_buff', 'stat': 'Movement_Speed', 'amount': 0.30, 'duration': 8.0}
    ]
}

# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------
BOW_ABILITIES = {
    'steady_shot': STEADY_SHOT, 'serpent_sting': SERPENT_STING, 'disengage': DISENGAGE, 'aimed_shot': AIMED_SHOT,
    'multi_shot': MULTI_SHOT, 'barbed_arrow': BARBED_ARROW, 'concussive_shot': CONCUSSIVE_SHOT, 'hunters_mark': HUNTERS_MARK,
    'volley': VOLLEY, 'piercing_shot': PIERCING_SHOT, 'rapid_fire': RAPID_FIRE, 'binding_shot': BINDING_SHOT,
    'master_marksman': MASTER_MARKSMAN, 'kill_shot': KILL_SHOT, 'trueshot': TRUESHOT, 'windburst': WINDBURST,
}