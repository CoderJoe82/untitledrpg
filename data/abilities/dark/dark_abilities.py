"""
This file contains all data for Dark school abilities.

Philosophy: Mid single-target damage, high single-target cursing/debuffs, and
low AoE debuffs. The goal is to isolate and cripple a primary target with an
array of debilitating effects, while applying constant pressure with DoTs.
"""

# -----------------------------------------------------------------------------
# TIER 1: APPRENTICE (Level 1-14)
# -----------------------------------------------------------------------------

SHADOW_BOLT = {
    'id': 'shadow_bolt', 'display_name': 'Shadow Bolt',
    'description': 'Hurls a bolt of shadow at the enemy, dealing moderate Dark damage. Your fundamental attack.',
    'level_req': 1, 'mana_cost': 14, 'cooldown': 0.0, 'casting_time': 1.5, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Dark', 'min_damage': 12, 'max_damage': 16}]
}

CURSE_OF_WEAKNESS = {
    'id': 'curse_of_weakness', 'display_name': 'Curse of Weakness',
    'description': 'Curses the target, reducing all physical damage they deal for a long duration.',
    'level_req': 4, 'mana_cost': 20, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'debuff', 'stat': 'Physical_Damage_Dealt', 'amount': -0.15, 'duration': 120.0}] # -15% damage
}

CORRUPTION = {
    'id': 'corruption', 'display_name': 'Corruption',
    'description': 'Instantly afflicts the target with a disease of shadow, causing Dark damage over time.',
    'level_req': 8, 'mana_cost': 22, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'dot', 'damage_type': 'Dark', 'tick_damage': 6, 'duration': 18.0, 'interval': 1.0}]
}

FEAR = {
    'id': 'fear', 'display_name': 'Fear',
    'description': 'Strikes terror into the heart of an enemy, causing them to flee in panic for a short duration. Damage may break the effect.',
    'level_req': 12, 'mana_cost': 35, 'cooldown': 25.0, 'casting_time': 1.5, 'target_type': 'single', 'range': 25,
    'effects': [{'type': 'debuff', 'effect': 'fear', 'duration': 8.0, 'break_on_damage_threshold': 40}]
}

# -----------------------------------------------------------------------------
# TIER 2: ADEPT (Level 15-29)
# -----------------------------------------------------------------------------

DRAIN_LIFE = {
    'id': 'drain_life', 'display_name': 'Drain Life',
    'description': 'Drains the life force from an enemy, dealing Dark damage and healing you for the same amount.',
    'level_req': 16, 'mana_cost': 50, 'cooldown': 10.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 25,
    'effects': [{'type': 'channeled_drain', 'damage_type': 'Dark', 'tick_damage': 15, 'duration': 5.0, 'interval': 1.0}]
}

CURSE_OF_TONGUES = {
    'id': 'curse_of_tongues', 'display_name': 'Curse of Tongues',
    'description': 'Curses a spellcaster, increasing the time it takes them to cast their spells.',
    'level_req': 20, 'mana_cost': 20, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'debuff', 'stat': 'Haste_Percent', 'amount': -0.30, 'duration': 120.0}] # 30% slower casting
}

AGONY = {
    'id': 'agony', 'display_name': 'Agony',
    'description': 'Inflicts a curse of escalating pain, dealing damage over time. The damage increases the longer it remains on the target.',
    'level_req': 24, 'mana_cost': 30, 'cooldown': 0.0, 'casting_time': 1.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'ramping_dot', 'damage_type': 'Dark', 'start_tick_damage': 5, 'damage_increase_per_tick': 1, 'duration': 18.0, 'interval': 1.0}]
}

SEED_OF_CORRUPTION = {
    'id': 'seed_of_corruption', 'display_name': 'Seed of Corruption',
    'description': 'Embeds a seed of darkness in the target. When the target takes enough damage from your spells, the seed explodes, applying Corruption to all nearby enemies.',
    'level_req': 28, 'mana_cost': 60, 'cooldown': 15.0, 'casting_time': 1.8, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'conditional_aoe_dot', 'trigger': 'on_damage_taken', 'damage_threshold': 150, 'dot_id': 'corruption', 'radius': 10}]
}

# -----------------------------------------------------------------------------
# TIER 3: MASTER (Level 30-44)
# -----------------------------------------------------------------------------

DARK_PACT = {
    'id': 'dark_pact', 'display_name': 'Dark Pact',
    'description': 'A risky pact that sacrifices 20% of your maximum health to instantly restore 40% of your maximum mana.',
    'level_req': 32, 'mana_cost': 0, 'cooldown': 60.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'resource_trade', 'health_cost_percent': 0.20, 'mana_gain_percent': 0.40}]
}

AMPLIFY_CURSE = {
    'id': 'amplify_curse', 'display_name': 'Amplify Curse',
    'description': 'Your next single-target Curse spell is amplified, doubling its effect. Does not affect damage-over-time spells.',
    'level_req': 36, 'mana_cost': 50, 'cooldown': 90.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'empower_next_curse', 'multiplier': 2.0, 'duration': 15.0}]
}

HAUNT = {
    'id': 'haunt', 'display_name': 'Haunt',
    'description': 'Sends a tormented spirit to haunt the target, dealing damage over time. When the target dies or the effect expires, the spirit returns to you, restoring a small amount of mana.',
    'level_req': 40, 'mana_cost': 45, 'cooldown': 12.0, 'casting_time': 1.2, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'dot_with_return', 'damage_type': 'Dark', 'tick_damage': 25, 'duration': 12.0, 'interval': 1.0, 'mana_return': 50}]
}

HOWL_OF_TERROR = {
    'id': 'howl_of_terror', 'display_name': 'Howl of Terror',
    'description': 'An instant scream that causes all nearby enemies to flee in terror for a short duration.',
    'level_req': 44, 'mana_cost': 80, 'cooldown': 45.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'debuff', 'effect': 'fear', 'duration': 6.0, 'radius': 10}]
}

# -----------------------------------------------------------------------------
# TIER 4: GRANDMASTER (Level 45-60)
# -----------------------------------------------------------------------------

UNSTABLE_AFFLICTION = {
    'id': 'unstable_affliction', 'display_name': 'Unstable Affliction',
    'description': 'A powerful DoT that erupts if dispelled, dealing significant damage to and silencing the dispeller.',
    'level_req': 48, 'mana_cost': 60, 'cooldown': 0.0, 'casting_time': 1.5, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'dispellable_dot', 'damage_type': 'Dark', 'tick_damage': 40, 'duration': 15.0, 'interval': 1.0, 'dispel_damage': 200, 'dispel_silence_duration': 5.0}]
}

DOOM = {
    'id': 'doom', 'display_name': 'Doom',
    'description': 'Curses a target with impending doom. After a long delay, the target takes a massive amount of shadow damage.',
    'level_req': 52, 'mana_cost': 100, 'cooldown': 60.0, 'casting_time': 2.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'delayed_damage', 'delay': 20.0, 'damage_type': 'Dark', 'min_damage': 800, 'max_damage': 900}]
}

SUMMON_SHADOWFIEND = {
    'id': 'summon_shadowfiend', 'display_name': 'Summon Shadowfiend',
    'description': 'Summons a shadowy horror to attack your target. Each time the Shadowfiend attacks, you restore mana.',
    'level_req': 56, 'mana_cost': 120, 'cooldown': 180.0, 'casting_time': 0.5, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'summon_utility_pet', 'name': 'Shadowfiend', 'duration': 15.0, 'attack_speed': 1.5, 'mana_per_hit': 15}]
}

SOUL_LINK = {
    'id': 'soul_link', 'display_name': 'Soul Link',
    'description': 'Links your soul to an enemy. While linked, 20% of the damage you take is redirected to the linked target.',
    'level_req': 58, 'mana_cost': 75, 'cooldown': 90.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'buff', 'effect': 'damage_redirect', 'percent': 0.20, 'duration': 60.0}]
}

DEATH_COIL = {
    'id': 'death_coil', 'display_name': 'Death Coil',
    'description': 'The ultimate expression of dark magic. Blasts a target with necrotic energy, dealing high damage and causing them to flee in horror.',
    'level_req': 60, 'mana_cost': 200, 'cooldown': 120.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 25,
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Dark', 'min_damage': 300, 'max_damage': 350},
        {'type': 'debuff', 'effect': 'fear', 'duration': 4.0}
    ]
}

# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------
DARK_ABILITIES = {
    'shadow_bolt': SHADOW_BOLT, 'curse_of_weakness': CURSE_OF_WEAKNESS, 'corruption': CORRUPTION, 'fear': FEAR,
    'drain_life': DRAIN_LIFE, 'curse_of_tongues': CURSE_OF_TONGUES, 'agony': AGONY, 'seed_of_corruption': SEED_OF_CORRUPTION,
    'dark_pact': DARK_PACT, 'amplify_curse': AMPLIFY_CURSE, 'haunt': HAUNT, 'howl_of_terror': HOWL_OF_TERROR,
    'unstable_affliction': UNSTABLE_AFFLICTION, 'doom': DOOM, 'summon_shadowfiend': SUMMON_SHADOWFIEND,
    'soul_link': SOUL_LINK, 'death_coil': DEATH_COIL,
}