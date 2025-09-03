"""
This file contains all data for Crossbow abilities.

Philosophy: Mid single-target damage, mid-high AoE damage, low bleed damage,
and low CC. The crossbow user is a battlefield engineer, excelling at area
denial and AoE damage with explosive and specialized bolts.
"""

# -----------------------------------------------------------------------------
# TIER 1: APPRENTICE (Level 1-14)
# -----------------------------------------------------------------------------

POWER_SHOT = {
    'id': 'power_shot', 'display_name': 'Power Shot',
    'description': 'A heavy, powerful shot that deals solid physical damage to a single target.',
    'level_req': 1, 'stamina_cost': 20, 'cooldown': 0.0, 'casting_time': 2.0, 'target_type': 'single', 'range': 38,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 22, 'max_damage': 28}]
}

EXPLOSIVE_BOLT = {
    'id': 'explosive_bolt', 'display_name': 'Explosive Bolt',
    'description': 'Fire a bolt with an explosive tip that deals minor splash damage to enemies near the impact.',
    'level_req': 4, 'stamina_cost': 25, 'cooldown': 8.0, 'casting_time': 2.2, 'target_type': 'single', 'range': 38,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Fire', 'min_damage': 20, 'max_damage': 25, 'radius': 5}]
}

RELOAD_MECHANISM = {
    'id': 'reload_mechanism', 'display_name': 'Reload Mechanism',
    'description': 'Engage your crossbow\'s rapid reload mechanism, making your next shot with a cast time instant.',
    'level_req': 8, 'stamina_cost': 10, 'cooldown': 30.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'instant_cast', 'charges': 1, 'duration': 10.0}]
}

PINNING_SHOT = {
    'id': 'pinning_shot', 'display_name': 'Pinning Shot',
    'description': 'Fire a heavy bolt aimed at the target\'s feet, rooting them in place for 2 seconds.',
    'level_req': 12, 'stamina_cost': 20, 'cooldown': 20.0, 'casting_time': 1.0, 'target_type': 'single', 'range': 38,
    'effects': [{'type': 'debuff', 'effect': 'root', 'duration': 2.0}]
}

# -----------------------------------------------------------------------------
# TIER 2: ADEPT (Level 15-29)
# -----------------------------------------------------------------------------

BOLT_SPRAY = {
    'id': 'bolt_spray', 'display_name': 'Bolt Spray',
    'description': 'Load a special magazine to fire a wide spray of bolts in a cone, damaging all enemies hit.',
    'level_req': 16, 'stamina_cost': 45, 'cooldown': 12.0, 'casting_time': 1.5, 'target_type': 'cone', 'range': 15,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 35, 'max_damage': 40, 'cone_angle': 60}]
}

SERRATED_BOLT = {
    'id': 'serrated_bolt', 'display_name': 'Serrated Bolt',
    'description': 'Fire a bolt with a jagged head, causing a minor bleed effect on the target.',
    'level_req': 20, 'stamina_cost': 15, 'cooldown': 6.0, 'casting_time': 1.0, 'target_type': 'single', 'range': 38,
    'effects': [{'type': 'dot', 'damage_type': 'Bleed', 'tick_damage': 8, 'duration': 9.0, 'interval': 1.0}]
}

CALTROPS = {
    'id': 'caltrops', 'display_name': 'Caltrops',
    'description': 'Scatter sharp caltrops over a target area. Enemies that walk through the area take damage and are slowed.',
    'level_req': 24, 'stamina_cost': 30, 'cooldown': 25.0, 'casting_time': 0.0, 'target_type': 'aoe_ground', 'range': 20,
    'effects': [{'type': 'ground_dot', 'damage_type': 'Physical', 'tick_damage': 10, 'duration': 10.0, 'interval': 1.0, 'radius': 6, 'debuff': 'slow', 'debuff_amount': 0.30}]
}

HEAVY_REPEATER = {
    'id': 'heavy_repeater', 'display_name': 'Heavy Repeater',
    'description': 'Brace your crossbow and unload a rapid volley of 4 heavy bolts into a single target.',
    'level_req': 28, 'stamina_cost': 50, 'cooldown': 15.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 38,
    'effects': [{'type': 'channeled_damage', 'damage_type': 'Physical', 'tick_damage': 25, 'duration': 2.0, 'interval': 0.5}]
}

# -----------------------------------------------------------------------------
# TIER 3: MASTER (Level 30-44)
# -----------------------------------------------------------------------------

SHRAPNEL_BOMB = {
    'id': 'shrapnel_bomb', 'display_name': 'Shrapnel Bomb',
    'description': 'Hurl a bomb that explodes, dealing physical damage and applying a bleed to all enemies in a wide area.',
    'level_req': 32, 'stamina_cost': 40, 'cooldown': 30.0, 'casting_time': 0.5, 'target_type': 'aoe_ground', 'range': 25,
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 40, 'max_damage': 50, 'radius': 8},
        {'type': 'dot', 'damage_type': 'Bleed', 'tick_damage': 10, 'duration': 6.0, 'interval': 1.0, 'radius': 8}
    ]
}

DOUBLE_TAP = {
    'id': 'double_tap', 'display_name': 'Double Tap',
    'description': 'A special loading technique. Your next Power Shot or Serrated Bolt will fire a second time for free.',
    'level_req': 36, 'stamina_cost': 20, 'cooldown': 45.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'double_cast', 'enhances_spell': ['power_shot', 'serrated_bolt'], 'charges': 1, 'duration': 10.0}]
}

SNIPERS_NEST = {
    'id': 'snipers_nest', 'display_name': "Sniper's Nest",
    'description': 'Hunker down in a fixed position, increasing your range by 10 and critical damage by 25%. You cannot move while in this stance.',
    'level_req': 40, 'stamina_cost': 15, 'cooldown': 5.0, 'casting_time': 1.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'toggle_buff', 'buff_id': 'snipers_nest', 'range_increase': 10, 'crit_damage_increase': 0.25, 'prevents_movement': True}]
}

GRAPPLING_BOLT = {
    'id': 'grappling_bolt', 'display_name': 'Grappling Bolt',
    'description': 'Fire a grappling bolt that pulls you to the target location.',
    'level_req': 44, 'stamina_cost': 20, 'cooldown': 40.0, 'casting_time': 0.0, 'target_type': 'aoe_ground', 'range': 30,
    'effects': [{'type': 'movement', 'effect': 'pull_to_location'}]
}

# -----------------------------------------------------------------------------
# TIER 4: GRANDMASTER (Level 45-60)
# -----------------------------------------------------------------------------

CLUSTER_BOMB = {
    'id': 'cluster_bomb', 'display_name': 'Cluster Bomb',
    'description': 'Fire a heavy bomb that explodes on impact, releasing 3 smaller bomblets that explode a moment later.',
    'level_req': 48, 'stamina_cost': 80, 'cooldown': 60.0, 'casting_time': 2.5, 'target_type': 'aoe_ground', 'range': 35,
    'effects': [{'type': 'cascading_aoe', 'damage_type': 'Fire', 'main_min_damage': 100, 'main_max_damage': 120, 'main_radius': 6, 'sub_min_damage': 50, 'sub_max_damage': 60, 'sub_radius': 4, 'sub_count': 3}]
}

TINKERERS_INGENUITY = {
    'id': 'tinkerers_ingenuity', 'display_name': "Tinkerer's Ingenuity",
    'description': 'Your expertise with mechanical devices is legendary. Your Explosive Bolt and Bolt Spray abilities have a 20% chance to not trigger their cooldown.',
    'level_req': 52, 'stamina_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'enhances_spell': ['explosive_bolt', 'bolt_spray'], 'effect': 'cooldown_reset_chance', 'proc_chance': 0.20}]
}

THE_JUGGERNAUT = {
    'id': 'the_juggernaut', 'display_name': 'The Juggernaut',
    'description': 'Load a massive, heavy bolt. After a long cast, you fire a shot that deals massive damage and knocks the target down.',
    'level_req': 56, 'stamina_cost': 60, 'cooldown': 45.0, 'casting_time': 3.5, 'target_type': 'single', 'range': 45,
    'effects': [
        {'type': 'direct_damage', 'damage_type': 'Physical', 'min_damage': 300, 'max_damage': 350},
        {'type': 'debuff', 'effect': 'knockdown', 'duration': 2.5}
    ]
}

BALLISTA_TURRET = {
    'id': 'ballista_turret', 'display_name': 'Ballista Turret',
    'description': 'The ultimate siege weapon. Deploy a stationary, automated ballista turret that fires powerful bolts at your enemies for 20 seconds.',
    'level_req': 60, 'stamina_cost': 120, 'cooldown': 180.0, 'casting_time': 2.0, 'target_type': 'aoe_ground', 'range': 15,
    'effects': [{'type': 'summon_turret', 'name': 'Ballista Turret', 'duration': 20.0, 'attack_speed': 3.0, 'min_damage': 60, 'max_damage': 75, 'attack_range': 40}]
}

# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------
CROSSBOW_ABILITIES = {
    'power_shot': POWER_SHOT, 'explosive_bolt': EXPLOSIVE_BOLT, 'reload_mechanism': RELOAD_MECHANISM, 'pinning_shot': PINNING_SHOT,
    'bolt_spray': BOLT_SPRAY, 'serrated_bolt': SERRATED_BOLT, 'caltrops': CALTROPS, 'heavy_repeater': HEAVY_REPEATER,
    'shrapnel_bomb': SHRAPNEL_BOMB, 'double_tap': DOUBLE_TAP, 'snipers_nest': SNIPERS_NEST, 'grappling_bolt': GRAPPLING_BOLT,
    'cluster_bomb': CLUSTER_BOMB, 'tinkerers_ingenuity': TINKERERS_INGENUITY, 'the_juggernaut': THE_JUGGERNAUT, 'ballista_turret': BALLISTA_TURRET,
}