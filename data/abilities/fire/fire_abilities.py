"""
This file contains all data for Fire school abilities. (Critically Enhanced Version)

The structure for each ability dictionary is as follows:
    - 'id': A unique, lowercase string for code identification.
    - 'display_name': The name shown to the player in the UI.
    - 'description': A tooltip explaining what the ability does.
    - ... and other relevant keys for game logic.

Philosophy: Mid single-target damage, high AoE, mid DoT, and mid critical damage.
Fire mages can specialize in overwhelming areas with fire or focus on landing
critical strikes to trigger explosive chain reactions.
"""

# -----------------------------------------------------------------------------
# TIER 1: APPRENTICE (Level 1-14)
# -----------------------------------------------------------------------------

FIRE_BOLT = {
    'id': 'fire_bolt', 'display_name': 'Fire Bolt',
    'description': 'Hurls a small bolt of fire at a single target. Your fundamental fire damage spell.',
    'level_req': 1, 'mana_cost': 10, 'cooldown': 0.0, 'casting_time': 1.0, 'target_type': 'single', 'range': 25,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Fire', 'min_damage': 8, 'max_damage': 12}]
}

IGNITE = {
    'id': 'ignite', 'display_name': 'Ignite',
    'description': 'Sets a target on fire, causing them to burn for a short duration.',
    'level_req': 4, 'mana_cost': 15, 'cooldown': 8.0, 'casting_time': 0.5, 'target_type': 'single', 'range': 20,
    'effects': [{'type': 'dot', 'damage_type': 'Fire', 'tick_damage': 4, 'duration': 9.0, 'interval': 1.0}]
}

FLAME_BURST = {
    'id': 'flame_burst', 'display_name': 'Flame Burst',
    'description': 'An instant burst of flame, damaging all enemies in melee range. A key defensive tool.',
    'level_req': 8, 'mana_cost': 25, 'cooldown': 10.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Fire', 'min_damage': 15, 'max_damage': 20, 'radius': 5}]
}

FIRE_SHIELD = {
    'id': 'fire_shield', 'display_name': 'Fire Shield',
    'description': 'Surrounds you with a shield of flame that increases Fire resistance and damages melee attackers.',
    'level_req': 12, 'mana_cost': 40, 'cooldown': 30.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'buff', 'stat': 'Fire_Resistance', 'amount': 25, 'duration': 60.0},
        {'type': 'retaliation_damage', 'damage_type': 'Fire', 'min_damage': 5, 'max_damage': 8, 'duration': 60.0}
    ]
}

# -----------------------------------------------------------------------------
# TIER 2: ADEPT (Level 15-29)
# -----------------------------------------------------------------------------

FIREBALL = {
    'id': 'fireball', 'display_name': 'Fireball',
    'description': 'Launches an explosive ball of fire that damages enemies in a small area upon impact.',
    'level_req': 16, 'mana_cost': 40, 'cooldown': 2.0, 'casting_time': 1.8, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Fire', 'min_damage': 35, 'max_damage': 50, 'radius': 4}]
}

SCORCH = {
    'id': 'scorch', 'display_name': 'Scorch',
    'description': 'Blasts a target with intense heat, dealing moderate damage and reducing their Fire resistance for a time.',
    'level_req': 20, 'mana_cost': 35, 'cooldown': 6.0, 'casting_time': 1.2, 'target_type': 'single', 'range': 25,
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Fire', 'min_damage': 25, 'max_damage': 35},
        {'type': 'debuff', 'stat': 'Fire_Resistance', 'amount': -15, 'duration': 10.0}
    ]
}

FIREWALL = {
    'id': 'firewall', 'display_name': 'Firewall',
    'description': 'Erects a wall of searing flames at a location, burning any enemy that passes through it.',
    'level_req': 24, 'mana_cost': 60, 'cooldown': 15.0, 'casting_time': 1.5, 'target_type': 'aoe_ground', 'range': 20,
    'effects': [{'type': 'dot', 'damage_type': 'Fire', 'tick_damage': 15, 'duration': 8.0, 'interval': 1.0, 'area_length': 12, 'area_width': 2}]
}

COMBUSTION = { # REWORKED FOR CRIT SYNERGY
    'id': 'combustion', 'display_name': 'Combustion',
    'description': 'A major damage cooldown. For 10 seconds, all your direct damage critical strikes also apply your Ignite DoT to the target.',
    'level_req': 28, 'mana_cost': 50, 'cooldown': 120.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'crits_apply_dot', 'dot_id': 'ignite', 'duration': 10.0}]
}

# -----------------------------------------------------------------------------
# TIER 3: MASTER (Level 30-44)
# -----------------------------------------------------------------------------

INNER_FLAME = { # MODIFIED FOR CRIT
    'id': 'inner_flame', 'display_name': 'Inner Flame',
    'description': 'You awaken the fire within, increasing all Fire damage you deal and your critical strike chance for a significant duration.',
    'level_req': 32, 'mana_cost': 70, 'cooldown': 60.0, 'casting_time': 1.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'buff', 'stat': 'Fire_Damage_Percent', 'amount': 0.15, 'duration': 120.0},
        {'type': 'buff', 'stat': 'Crit_Chance', 'amount': 0.10, 'duration': 120.0} # Added 10% crit
    ]
}

METEOR = {
    'id': 'meteor', 'display_name': 'Meteor',
    'description': 'Calls a meteor from the sky to strike a target location, dealing massive damage and stunning enemies in a large area.',
    'level_req': 36, 'mana_cost': 120, 'cooldown': 45.0, 'casting_time': 3.0, 'target_type': 'aoe_ground', 'range': 35,
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Fire', 'min_damage': 150, 'max_damage': 200, 'radius': 8},
        {'type': 'debuff', 'effect': 'stun', 'duration': 2.0, 'radius': 8}
    ]
}

DRAGONS_BREATH = {
    'id': 'dragons_breath', 'display_name': "Dragon's Breath",
    'description': 'Unleashes a cone of fire from your hands, scorching all enemies in front of you.',
    'level_req': 40, 'mana_cost': 90, 'cooldown': 12.0, 'casting_time': 2.0, 'target_type': 'cone', 'range': 15,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Fire', 'min_damage': 100, 'max_damage': 130, 'cone_angle': 45}]
}

IMMOLATION_AURA = {
    'id': 'immolation_aura', 'display_name': 'Immolation Aura',
    'description': 'Wreathes the caster in flames, burning all nearby enemies for as long as the spell is active.',
    'level_req': 44, 'mana_cost': 30, 'mana_upkeep': 15, 'cooldown': 5.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'dot', 'damage_type': 'Fire', 'tick_damage': 25, 'duration': -1, 'interval': 1.0, 'radius': 6}]
}

# -----------------------------------------------------------------------------
# TIER 4: GRANDMASTER (Level 45-60)
# -----------------------------------------------------------------------------

CONFLAGRATION = {
    'id': 'conflagration', 'display_name': 'Conflagration',
    'description': 'Instantly consumes your active Ignite or Combustion effect on a target to deal massive damage. A spell for masters of synergy.',
    'level_req': 48, 'mana_cost': 50, 'cooldown': 8.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'synergy_damage', 'consumes': ['ignite', 'combustion'], 'damage_multiplier': 1.5}]
}

LIVING_BOMB = {
    'id': 'living_bomb', 'display_name': 'Living Bomb',
    'description': 'Places a fiery bomb on a target that ticks for minor damage, then explodes after 12 seconds, dealing massive damage to the target and all nearby enemies.',
    'level_req': 52, 'mana_cost': 100, 'cooldown': 25.0, 'casting_time': 1.5, 'target_type': 'single', 'range': 30,
    'effects': [
        {'type': 'dot', 'damage_type': 'Fire', 'tick_damage': 20, 'duration': 12.0, 'interval': 1.0},
        {'type': 'delayed_aoe', 'trigger': 'on_expire', 'delay': 12.0, 'damage_type': 'Fire', 'min_damage': 250, 'max_damage': 300, 'radius': 10}
    ]
}

FIRESTARTER = { # NEW CRIT SPELL
    'id': 'firestarter', 'display_name': 'Firestarter',
    'description': 'Your critical strikes with Fire Bolt and Fireball have a 50% chance to make your next Fireball instant cast and a guaranteed critical strike.',
    'level_req': 56, 'mana_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'enhances_spell': ['fire_bolt', 'fireball'], 'trigger': 'on_crit', 'proc_chance': 0.50, 'effect': 'instant_guaranteed_crit', 'spell_id': 'fireball'}]
}

KINDLING = { # NEW CRIT SPELL
    'id': 'kindling', 'display_name': 'Kindling',
    'description': 'Your critical strikes reduce the remaining cooldown of Combustion by 2 seconds.',
    'level_req': 58, 'mana_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'trigger': 'on_crit', 'effect': 'cooldown_reduction', 'spell_id': 'combustion', 'reduction_amount': 2.0}]
}

ARMAGEDDON = {
    'id': 'armageddon', 'display_name': 'Armageddon',
    'description': 'Calls down a devastating rain of fire over a huge area for 10 seconds. The ultimate AoE spell.',
    'level_req': 60, 'mana_cost': 250, 'cooldown': 180.0, 'casting_time': 4.0, 'target_type': 'aoe_ground', 'range': 40,
    'effects': [{'type': 'dot', 'damage_type': 'Fire', 'tick_damage': 75, 'duration': 10.0, 'interval': 1.0, 'radius': 15}]
}


# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------
FIRE_ABILITIES = {
    'fire_bolt': FIRE_BOLT, 'ignite': IGNITE, 'flame_burst': FLAME_BURST, 'fire_shield': FIRE_SHIELD,
    'fireball': FIREBALL, 'scorch': SCORCH, 'firewall': FIREWALL, 'combustion': COMBUSTION,
    'inner_flame': INNER_FLAME, 'meteor': METEOR, 'dragons_breath': DRAGONS_BREATH, 'immolation_aura': IMMOLATION_AURA,
    'conflagration': CONFLAGRATION, 'living_bomb': LIVING_BOMB, 'firestarter': FIRESTARTER,
    'kindling': KINDLING, 'armageddon': ARMAGEDDON,
}