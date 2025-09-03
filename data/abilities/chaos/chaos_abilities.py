"""
This file contains all data for Chaos school abilities.

Philosophy: High-risk, high-reward. This school focuses on unpredictable,
powerful AoE, self-damaging spells, and wild, transformative effects. A Chaos
mage uses their own life force as a weapon and thrives on the edge of disaster.
"""

# -----------------------------------------------------------------------------
# TIER 1: APPRENTICE (Level 1-14)
# -----------------------------------------------------------------------------

CHAOS_BOLT = {
    'id': 'chaos_bolt', 'display_name': 'Chaos Bolt',
    'description': 'Hurls a bolt of chaotic energy that deals a highly variable amount of Chaos damage.',
    'level_req': 1, 'mana_cost': 18, 'cooldown': 0.0, 'casting_time': 1.6, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Chaos', 'min_damage': 5, 'max_damage': 30}] # Very wide damage range
}

BLOOD_RUSH = {
    'id': 'blood_rush', 'display_name': 'Blood Rush',
    'description': 'Sacrifice a portion of your health to instantly deal a burst of Chaos damage to a target.',
    'level_req': 4, 'mana_cost': 10, 'cooldown': 6.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 25,
    'effects': [{'type': 'direct_damage_health_cost', 'damage_type': 'Chaos', 'health_cost_percent': 0.05, 'min_damage': 25, 'max_damage': 30}] # Costs 5% of max HP
}

WARP = {
    'id': 'warp', 'display_name': 'Warp',
    'description': 'Curses a target, causing their next offensive ability to have an unpredictable outcome.',
    'level_req': 8, 'mana_cost': 25, 'cooldown': 20.0, 'casting_time': 1.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'debuff', 'effect': 'randomize_next_ability', 'duration': 10.0}] # e.g., could fizzle, could backfire, could be empowered
}

UNSTABLE_RIFT = {
    'id': 'unstable_rift', 'display_name': 'Unstable Rift',
    'description': 'Tears a hole in reality at a target location, dealing Chaos damage to all enemies within it. Has a small chance to also damage you.',
    'level_req': 12, 'mana_cost': 45, 'cooldown': 10.0, 'casting_time': 2.0, 'target_type': 'aoe_ground', 'range': 30,
    'effects': [{'type': 'chaotic_aoe', 'damage_type': 'Chaos', 'min_damage': 20, 'max_damage': 35, 'radius': 8, 'backfire_chance': 0.10}] # 10% chance to also hit the caster
}

# -----------------------------------------------------------------------------
# TIER 2: ADEPT (Level 15-29)
# -----------------------------------------------------------------------------

LIFE_TAP = {
    'id': 'life_tap', 'display_name': 'Life Tap',
    'description': 'The signature Chaos spell. Convert a large chunk of your health directly into mana.',
    'level_req': 16, 'mana_cost': 0, 'cooldown': 1.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'resource_trade', 'health_cost_percent': 0.15, 'mana_gain_flat': 100}]
}

CHAOS_AURA = {
    'id': 'chaos_aura', 'display_name': 'Chaos Aura',
    'description': 'For 10 seconds, you pulse with chaotic energy. Every pulse has a random effect on a nearby target (enemy or ally).',
    'level_req': 20, 'mana_cost': 60, 'cooldown': 45.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'random_aura', 'duration': 10.0, 'interval': 2.0, 'radius': 15, 'possible_effects': ['minor_damage', 'minor_heal', 'slow_debuff', 'haste_buff']}]
}

HELLFIRE = {
    'id': 'hellfire', 'display_name': 'Hellfire',
    'description': 'Engulf yourself in chaotic flames, dealing massive Chaos damage to all nearby enemies AND yourself every second it is channeled.',
    'level_req': 24, 'mana_cost': 80, 'cooldown': 25.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'channeled_self_damaging_aoe', 'damage_type': 'Chaos', 'tick_damage_enemies': 40, 'tick_damage_self': 20, 'duration': 6.0, 'interval': 1.0, 'radius': 10}]
}

EDGE_OF_INSANITY = {
    'id': 'edge_of_insanity', 'display_name': 'Edge of Insanity',
    'description': 'Your grasp on reality frays. You deal up to 20% more damage the lower your current health is.',
    'level_req': 28, 'mana_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'stat': 'Damage_Bonus_Missing_Health', 'max_bonus': 0.20}]
}

# -----------------------------------------------------------------------------
# TIER 3: MASTER (Level 30-44)
# -----------------------------------------------------------------------------

PANDEMONIUM = {
    'id': 'pandemonium', 'display_name': 'Pandemonium',
    'description': 'Unleash pure chaos, causing all enemies in an area to be afflicted with a random, powerful debilitating effect.',
    'level_req': 32, 'mana_cost': 100, 'cooldown': 60.0, 'casting_time': 2.5, 'target_type': 'aoe_ground', 'range': 30,
    'effects': [{'type': 'random_debuff_aoe', 'radius': 10, 'possible_debuffs': ['stun', 'fear', 'silence', 'polymorph'], 'duration': 4.0}]
}

SHATTERED_SOUL = {
    'id': 'shattered_soul', 'display_name': 'Shattered Soul',
    'description': 'Sacrifice half of your current health to deal that amount as Chaos damage to a single target.',
    'level_req': 36, 'mana_cost': 50, 'cooldown': 12.0, 'casting_time': 1.8, 'target_type': 'single', 'range': 25,
    'effects': [{'type': 'health_to_damage', 'health_cost_percent_current': 0.50}]
}

SUMMON_IMP = {
    'id': 'summon_imp', 'display_name': 'Summon Imp',
    'description': 'Summons a mischievous, chaotic Imp to fight for you. The Imp casts weak Chaos Bolts, but occasionally casts a random powerful spell.',
    'level_req': 40, 'mana_cost': 90, 'cooldown': 120.0, 'casting_time': 1.5, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'summon_chaotic_pet', 'name': 'Chaos Imp', 'duration': 45.0}]
}

RECKLESSNESS = {
    'id': 'recklessness', 'display_name': 'Recklessness',
    'description': 'For 12 seconds, all your spells are guaranteed to be critical strikes, but you also take 50% more damage from all sources.',
    'level_req': 44, 'mana_cost': 75, 'cooldown': 180.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'buff', 'stat': 'Crit_Chance', 'amount': 1.0, 'duration': 12.0},
        {'type': 'buff', 'stat': 'Damage_Taken', 'amount': 0.50, 'duration': 12.0}
    ]
}

# -----------------------------------------------------------------------------
# TIER 4: GRANDMASTER (Level 45-60)
# -----------------------------------------------------------------------------

CHAOS_STORM = {
    'id': 'chaos_storm', 'display_name': 'Chaos Storm',
    'description': 'Calls down a storm of chaotic energy over a huge area. The storm deals damage and leaves behind patches of unstable ground that have random effects.',
    'level_req': 48, 'mana_cost': 200, 'cooldown': 90.0, 'casting_time': 3.0, 'target_type': 'aoe_ground', 'range': 35,
    'effects': [{'type': 'dot_with_unstable_ground', 'damage_type': 'Chaos', 'tick_damage': 50, 'duration': 8.0, 'interval': 1.0, 'radius': 15}]
}

DIMENSIONAL_SHIFT = {
    'id': 'dimensional_shift', 'display_name': 'Dimensional Shift',
    'description': 'You and your target are both shunted into a chaotic dimension for 10 seconds. In this realm, you deal 50% more damage to the target, but you also take continuous damage.',
    'level_req': 52, 'mana_cost': 150, 'cooldown': 180.0, 'casting_time': 1.0, 'target_type': 'single', 'range': 20,
    'effects': [{'type': 'dueling_realm', 'damage_bonus': 0.50, 'self_dot_damage': 30, 'duration': 10.0}]
}

SOUL_BURN = {
    'id': 'soul_burn', 'display_name': 'Soul Burn',
    'description': 'Deals massive Chaos damage to a target based on their missing health. The ultimate execute.',
    'level_req': 56, 'mana_cost': 100, 'cooldown': 25.0, 'casting_time': 2.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'execute_damage', 'damage_type': 'Chaos', 'base_damage': 100, 'missing_health_multiplier': 1.5}] # Deals 1.5x damage based on % missing health
}

METAMORPHOSIS = {
    'id': 'metamorphosis', 'display_name': 'Metamorphosis',
    'description': 'The ultimate expression of chaos. You transform into a powerful demon for 30 seconds, empowering your spells and granting you new abilities, but constantly draining your health.',
    'level_req': 60, 'mana_cost': 250, 'cooldown': 300.0, 'casting_time': 1.5, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'empowerment_transformation', 'form': 'demon', 'duration': 30.0, 'health_drain_percent': 0.02}] # Drains 2% max health per second
}

# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------
CHAOS_ABILITIES = {
    'chaos_bolt': CHAOS_BOLT, 'blood_rush': BLOOD_RUSH, 'warp': WARP, 'unstable_rift': UNSTABLE_RIFT,
    'life_tap': LIFE_TAP, 'chaos_aura': CHAOS_AURA, 'hellfire': HELLFIRE, 'edge_of_insanity': EDGE_OF_INSANITY,
    'pandemonium': PANDEMONIUM, 'shattered_soul': SHATTERED_SOUL, 'summon_imp': SUMMON_IMP, 'recklessness': RECKLESSNESS,
    'chaos_storm': CHAOS_STORM, 'dimensional_shift': DIMENSIONAL_SHIFT, 'soul_burn': SOUL_BURN, 'metamorphosis': METAMORPHOSIS,
}