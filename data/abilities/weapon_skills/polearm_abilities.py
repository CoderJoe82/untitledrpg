"""
This file contains all data for Polearm abilities (Spears, Glaives, etc.).

Philosophy: Mid single-target damage, low AoE damage, low bleed DoT, and high
critical bonus. The polearm master is an opportunist who controls the battlefield
with reach and precision, waiting for the perfect moment to land a devastating
critical strike.
"""

# -----------------------------------------------------------------------------
# TIER 1: APPRENTICE (Level 1-14)
# -----------------------------------------------------------------------------

THRUST = {
    'id': 'thrust', 'display_name': 'Thrust',
    'description': 'A quick, long-reaching thrust that deals physical damage.',
    'level_req': 1, 'skill_req': 1, 'stamina_cost': 18, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee_long', # Special range
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 16, 'max_damage': 21}]
}

PRECISION_STRIKE = {
    'id': 'precision_strike', 'display_name': 'Precision Strike',
    'description': 'A deliberate, aimed strike that has a 25% increased chance to be a critical hit.',
    'level_req': 4, 'skill_req': 5, 'stamina_cost': 25, 'cooldown': 6.0, 'casting_time': 0.5, 'target_type': 'single', 'range': 'melee_long',
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 20, 'max_damage': 25, 'bonus_crit_chance': 0.25}]
}

SWEEP = {
    'id': 'sweep', 'display_name': 'Sweep',
    'description': 'Swing your weapon in a wide arc, striking up to 3 enemies in front of you.',
    'level_req': 8, 'skill_req': 10, 'stamina_cost': 30, 'cooldown': 10.0, 'casting_time': 0.0, 'target_type': 'cone', 'range': 'melee',
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 18, 'max_damage': 22, 'max_targets': 3, 'cone_angle': 120}]
}

BRACE = {
    'id': 'brace', 'display_name': 'Brace',
    'description': 'Set your weapon against the ground, preparing to receive a charge. The next enemy to attack you in melee is knocked down.',
    'level_req': 12, 'skill_req': 15, 'stamina_cost': 10, 'cooldown': 25.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'retaliation_knockdown', 'charges': 1, 'duration': 10.0}]
}

# -----------------------------------------------------------------------------
# TIER 2: ADEPT (Level 15-29)
# -----------------------------------------------------------------------------

SKEWER = {
    'id': 'skewer', 'display_name': 'Skewer',
    'description': 'A brutal thrust that causes the enemy to bleed. If this ability is a critical strike, the bleed damage is doubled.',
    'level_req': 16, 'skill_req': 20, 'stamina_cost': 25, 'cooldown': 12.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee_long',
    'effects': [{'type': 'dot_crit_synergy', 'damage_type': 'Bleed', 'tick_damage': 8, 'duration': 9.0, 'interval': 1.0}]
}

KEEN_EDGE = {
    'id': 'keen_edge', 'display_name': 'Keen Edge',
    'description': 'Your disciplined training has taught you to find weaknesses. Increases your critical strike chance with all polearms by 5%.',
    'level_req': 20, 'skill_req': 25, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'stat': 'Crit_Chance', 'amount': 0.05}]
}

LUNGE = {
    'id': 'lunge', 'display_name': 'Lunge',
    'description': 'Lunge forward, piercing through enemies in a line and dealing moderate damage.',
    'level_req': 24, 'skill_req': 30, 'stamina_cost': 35, 'cooldown': 15.0, 'casting_time': 0.0, 'target_type': 'line', 'range': 12,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 40, 'max_damage': 50, 'line_width': 3}]
}

LEG_SWEEP = {
    'id': 'leg_sweep', 'display_name': 'Leg Sweep',
    'description': 'Use the butt of your weapon to sweep the target\'s legs, knocking them down for 2 seconds.',
    'level_req': 28, 'skill_req': 35, 'stamina_cost': 20, 'cooldown': 30.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 'melee',
    'effects': [{'type': 'debuff', 'effect': 'knockdown', 'duration': 2.0}]
}

# -----------------------------------------------------------------------------
# TIER 3: MASTER (Level 30-44)
# -----------------------------------------------------------------------------

DEADLY_CALM = {
    'id': 'deadly_calm', 'display_name': 'Deadly Calm',
    'description': 'Enter a state of perfect focus for 10 seconds, increasing your critical strike chance by 30%.',
    'level_req': 32, 'skill_req': 40, 'stamina_cost': 30, 'cooldown': 90.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'stat': 'Crit_Chance', 'amount': 0.30, 'duration': 10.0}]
}

IMPALE = {
    'id': 'impale', 'display_name': 'Impale',
    'description': 'You now aim for vital organs. The damage bonus from your critical strikes is increased by an additional 25%.',
    'level_req': 36, 'skill_req': 45, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'stat': 'Crit_Damage_Multiplier', 'amount': 0.25}]
}

PHALANX_BREAKER = {
    'id': 'phalanx_breaker', 'display_name': 'Phalanx Breaker',
    'description': 'A powerful, armor-piercing thrust that ignores 75% of the target\'s Toughness.',
    'level_req': 40, 'skill_req': 50, 'stamina_cost': 45, 'cooldown': 20.0, 'casting_time': 1.0, 'target_type': 'single', 'range': 'melee_long',
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 120, 'max_damage': 140, 'armor_penetration': 0.75}]
}

VAULT = {
    'id': 'vault', 'display_name': 'Vault',
    'description': 'Use your polearm to vault to a target location, giving you superior mobility on the battlefield.',
    'level_req': 44, 'skill_req': 55, 'stamina_cost': 15, 'cooldown': 25.0, 'casting_time': 0.0, 'target_type': 'aoe_ground', 'range': 20,
    'effects': [{'type': 'movement', 'effect': 'leap_to_location'}]
}

# -----------------------------------------------------------------------------
# TIER 4: GRANDMASTER (Level 45-60)
# -----------------------------------------------------------------------------

HEARTSEEKER = {
    'id': 'heartseeker', 'display_name': 'Heartseeker',
    'description': 'A deadly finishing move. Deals massive damage, and is a guaranteed critical strike on targets below 25% health.',
    'level_req': 48, 'skill_req': 60, 'stamina_cost': 50, 'cooldown': 15.0, 'casting_time': 1.0, 'target_type': 'single', 'range': 'melee_long',
    'effects': [{'type': 'execute_damage', 'damage_type': 'Physical', 'min_damage': 300, 'max_damage': 350, 'health_threshold': 0.25, 'guaranteed_crit': True}]
}

FLOWING_STRIKES = {
    'id': 'flowing_strikes', 'display_name': 'Flowing Strikes',
    'description': 'Your combat style is a deadly dance. Each critical strike you land reduces the cooldown of Deadly Calm by 5 seconds.',
    'level_req': 52, 'skill_req': 65, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'trigger': 'on_crit', 'effect': 'cooldown_reduction', 'spell_id': 'deadly_calm', 'reduction_amount': 5.0}]
}

WINDSWEPT_ASSAULT = {
    'id': 'windswept_assault', 'display_name': 'Windswept Assault',
    'description': 'The ultimate offensive cooldown. For 12 seconds, every successful attack is a guaranteed critical strike.',
    'level_req': 56, 'skill_req': 70, 'stamina_cost': 40, 'cooldown': 180.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'guaranteed_crit', 'duration': 12.0}]
}

DRAGONSONG_DIVE = {
    'id': 'dragonsong_dive', 'display_name': 'Dragonsong Dive',
    'description': 'Leap high into the air and dive upon a single target like a dragon, impaling them with your weapon. This attack is a guaranteed critical strike and deals extreme damage.',
    'level_req': 60, 'skill_req': 75, 'stamina_cost': 100, 'cooldown': 120.0, 'casting_time': 2.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 600, 'max_damage': 700, 'guaranteed_crit': True}]
}

# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------
POLEARM_ABILITIES = {
    'thrust': THRUST, 'precision_strike': PRECISION_STRIKE, 'sweep': SWEEP, 'brace': BRACE,
    'skewer': SKEWER, 'keen_edge': KEEN_EDGE, 'lunge': LUNGE, 'leg_sweep': LEG_SWEEP,
    'deadly_calm': DEADLY_CALM, 'impale': IMPALE, 'phalanx_breaker': PHALANX_BREAKER, 'vault': VAULT,
    'heartseeker': HEARTSEEKER, 'flowing_strikes': FLOWING_STRIKES, 'windswept_assault': WINDSWEPT_ASSAULT, 'dragonsong_dive': DRAGONSONG_DIVE,
}