"""
This file contains all data for Lightning school abilities.

Philosophy: High single-target damage, mid AoE damage, low DoT damage. Spells
often feature control elements (stuns) or self-buffs (speed/crits).
"""

# -----------------------------------------------------------------------------
# TIER 1: APPRENTICE (Level 1-14)
# -----------------------------------------------------------------------------

SPARK = {
    'id': 'spark', 'display_name': 'Spark',
    'description': 'Fires a quick spark of lightning at an enemy. A fast, efficient, and reliable attack.',
    'level_req': 1, 'mana_cost': 12, 'cooldown': 0.0, 'casting_time': 0.8, 'target_type': 'single', 'range': 28,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Lightning', 'min_damage': 10, 'max_damage': 14}]
}

SHOCK = {
    'id': 'shock', 'display_name': 'Shock',
    'description': 'Instantly jolts a target, dealing minor damage and briefly interrupting their actions.',
    'level_req': 4, 'mana_cost': 20, 'cooldown': 12.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 20,
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Lightning', 'min_damage': 5, 'max_damage': 8},
        {'type': 'debuff', 'effect': 'interrupt', 'duration': 0.5} # A micro-stun
    ]
}

LIGHTNING_SHIELD = {
    'id': 'lightning_shield', 'display_name': 'Lightning Shield',
    'description': 'Surrounds you with a shield of electricity, increasing Lightning resistance and shocking melee attackers.',
    'level_req': 8, 'mana_cost': 45, 'cooldown': 30.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'buff', 'stat': 'Lightning_Resistance', 'amount': 25, 'duration': 60.0},
        {'type': 'retaliation_damage', 'damage_type': 'Lightning', 'min_damage': 6, 'max_damage': 9, 'duration': 60.0}
    ]
}

CHARGED_BOLT = {
    'id': 'charged_bolt', 'display_name': 'Charged Bolt',
    'description': 'Gathers energy for a moment before unleashing a powerful bolt of lightning at a single target.',
    'level_req': 12, 'mana_cost': 35, 'cooldown': 3.0, 'casting_time': 1.5, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Lightning', 'min_damage': 30, 'max_damage': 45}]
}

# -----------------------------------------------------------------------------
# TIER 2: ADEPT (Level 15-29)
# -----------------------------------------------------------------------------

CHAIN_LIGHTNING = {
    'id': 'chain_lightning', 'display_name': 'Chain Lightning',
    'description': 'Strikes a target with lightning that then arcs to several nearby enemies, dealing reduced damage to each subsequent target.',
    'level_req': 16, 'mana_cost': 50, 'cooldown': 8.0, 'casting_time': 1.6, 'target_type': 'single', 'range': 25,
    'effects': [{'type': 'chain_damage', 'damage_type': 'Lightning', 'min_damage': 40, 'max_damage': 55, 'max_jumps': 3, 'jump_range': 10, 'damage_falloff': 0.30}] # Each jump does 30% less damage
}

STATIC_FIELD = {
    'id': 'static_field', 'display_name': 'Static Field',
    'description': 'Creates a crackling field of energy around the caster that periodically damages a random nearby enemy.',
    'level_req': 20, 'mana_cost': 60, 'cooldown': 20.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'aura_damage', 'damage_type': 'Lightning', 'min_damage': 20, 'max_damage': 25, 'duration': 15.0, 'interval': 1.5, 'radius': 12}]
}

CONDUCTIVITY = {
    'id': 'conductivity', 'display_name': 'Conductivity',
    'description': 'Curses a target, making them highly conductive and increasing the critical strike chance of your spells against them.',
    'level_req': 24, 'mana_cost': 40, 'cooldown': 15.0, 'casting_time': 0.5, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'debuff', 'stat': 'Crit_Chance_Taken', 'amount': 0.15, 'duration': 12.0}] # Spells have +15% crit chance against this target
}

LIGHTNING_RUSH = {
    'id': 'lightning_rush', 'display_name': 'Lightning Rush',
    'description': 'Dissipate into pure energy and reappear at a target location. The signature mobility spell of a storm caster.',
    'level_req': 28, 'mana_cost': 30, 'cooldown': 18.0, 'casting_time': 0.0, 'target_type': 'aoe_ground', 'range': 20,
    'effects': [{'type': 'movement', 'effect': 'teleport'}]
}

# -----------------------------------------------------------------------------
# TIER 3: MASTER (Level 30-44)
# -----------------------------------------------------------------------------

SUPERCHARGE = {
    'id': 'supercharge', 'display_name': 'Supercharge',
    'description': 'Overload your body with electrical energy, dramatically increasing your spell casting speed for a short time.',
    'level_req': 32, 'mana_cost': 80, 'cooldown': 75.0, 'casting_time': 1.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'stat': 'Haste_Percent', 'amount': 0.30, 'duration': 15.0}] # 30% faster casting
}

THUNDERSTORM = {
    'id': 'thunderstorm', 'display_name': 'Thunderstorm',
    'description': 'Calls down a storm over a target area, striking random enemies within it with bolts of lightning over several seconds.',
    'level_req': 36, 'mana_cost': 130, 'cooldown': 40.0, 'casting_time': 2.5, 'target_type': 'aoe_ground', 'range': 35,
    'effects': [{'type': 'random_aoe_damage', 'damage_type': 'Lightning', 'min_damage': 50, 'max_damage': 60, 'duration': 8.0, 'interval': 1.0, 'radius': 10}]
}

LIGHTNING_ROD = {
    'id': 'lightning_rod', 'display_name': 'Lightning Rod',
    'description': 'Summons a rod that attracts your lightning spells. After absorbing enough energy or after a duration, the rod explodes, dealing damage based on the energy absorbed.',
    'level_req': 40, 'mana_cost': 75, 'cooldown': 60.0, 'casting_time': 1.0, 'target_type': 'aoe_ground', 'range': 25,
    'effects': [{'type': 'summon_synergy_object', 'name': 'Lightning Rod', 'duration': 15.0, 'max_charges': 4, 'explosion_radius': 8}]
}

BALL_LIGHTNING = {
    'id': 'ball_lightning', 'display_name': 'Ball Lightning',
    'description': 'Launches a slow-moving ball of electricity that zaps any enemy it passes near.',
    'level_req': 44, 'mana_cost': 90, 'cooldown': 12.0, 'casting_time': 1.8, 'target_type': 'projectile', 'range': 30,
    'effects': [{'type': 'moving_aoe_damage', 'damage_type': 'Lightning', 'tick_damage': 40, 'duration': 10.0, 'interval': 0.8, 'radius': 4, 'projectile_speed': 5}]
}

# -----------------------------------------------------------------------------
# TIER 4: GRANDMASTER (Level 45-60)
# -----------------------------------------------------------------------------

STATIC_OVERLOAD = {
    'id': 'static_overload', 'display_name': 'Static Overload',
    'description': 'Your direct damage lightning spells have a chance to overload the target, causing the spell to strike a second time for a fraction of the damage, instantly.',
    'level_req': 48, 'mana_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'enhances_spell': 'all_lightning_direct', 'proc_chance': 0.20, 'damage_multiplier': 0.50}] # 20% chance for a second hit at 50% power
}

THUNDERSTRIKE = {
    'id': 'thunderstrike', 'display_name': 'Thunderstrike',
    'description': 'Call upon the heavens to smite a single target with an immense bolt of pure lightning. Deals massive damage, but has a long cast time.',
    'level_req': 52, 'mana_cost': 150, 'cooldown': 20.0, 'casting_time': 3.5, 'target_type': 'single', 'range': 40,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Lightning', 'min_damage': 400, 'max_damage': 500}]
}

RIDE_THE_LIGHTNING = {
    'id': 'ride_the_lightning', 'display_name': 'Ride the Lightning',
    'description': 'An advanced version of Lightning Rush. You can now hold up to two charges of the spell, and it leaves a trail of static that damages enemies.',
    'level_req': 56, 'mana_cost': 30, 'cooldown': 1.0, 'casting_time': 0.0, 'target_type': 'aoe_ground', 'range': 25,
    'effects': [{'type': 'movement_charge_system', 'effect': 'teleport', 'max_charges': 2, 'recharge_time': 18.0},
                {'type': 'ground_effect', 'damage_type': 'Lightning', 'tick_damage': 30, 'duration': 4.0}]
}

EYE_OF_THE_STORM = {
    'id': 'eye_of_the_storm', 'display_name': 'Eye of the Storm',
    'description': 'Become the calm center of a raging storm. While you channel this spell, you gain immense defensive bonuses and lightning automatically strikes nearby enemies.',
    'level_req': 58, 'mana_cost': 50, 'mana_upkeep': 40, 'cooldown': 90.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'channeled_aura_damage', 'damage_type': 'Lightning', 'min_damage': 100, 'max_damage': 120, 'interval': 1.2, 'radius': 15},
        {'type': 'channeled_buff', 'stat': 'Toughness', 'amount': 100, 'duration': -1}
    ]
}

MAELSTROM = {
    'id': 'maelstrom', 'display_name': 'Maelstrom',
    'description': 'The ultimate storm spell. Summons a swirling vortex of wind and lightning at a location that pulls enemies toward its center and relentlessly electrocutes them.',
    'level_req': 60, 'mana_cost': 300, 'cooldown': 180.0, 'casting_time': 4.0, 'target_type': 'aoe_ground', 'range': 35,
    'effects': [
        {'type': 'dot', 'damage_type': 'Lightning', 'tick_damage': 60, 'duration': 8.0, 'interval': 0.8, 'radius': 12},
        {'type': 'debuff', 'effect': 'pull_to_center', 'strength': 5, 'duration': 8.0, 'radius': 12}
    ]
}

# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------
LIGHTNING_ABILITIES = {
    'spark': SPARK, 'shock': SHOCK, 'lightning_shield': LIGHTNING_SHIELD, 'charged_bolt': CHARGED_BOLT,
    'chain_lightning': CHAIN_LIGHTNING, 'static_field': STATIC_FIELD, 'conductivity': CONDUCTIVITY, 'lightning_rush': LIGHTNING_RUSH,
    'supercharge': SUPERCHARGE, 'thunderstorm': THUNDERSTORM, 'lightning_rod': LIGHTNING_ROD, 'ball_lightning': BALL_LIGHTNING,
    'static_overload': STATIC_OVERLOAD, 'thunderstrike': THUNDERSTRIKE, 'ride_the_lightning': RIDE_THE_LIGHTNING,
    'eye_of_the_storm': EYE_OF_THE_STORM, 'maelstrom': MAELSTROM,
}