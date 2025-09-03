"""
This file contains all data for Nature school abilities. (Expanded Healing Version)

The Nature school has two core identities a player can specialize in, or mix:
1.  DAMAGE/CONTROL: High DoT, mid single-target, mid CC, low direct AoE. Wears
    down and outlasts enemies.
2.  HEALING/SUPPORT: High HoT, high cleansing, high AoE healing, but low
    single-target burst healing. Keeps allies stable through continuous care.
"""

# -----------------------------------------------------------------------------
# TIER 1: APPRENTICE (Level 1-14)
# -----------------------------------------------------------------------------

THORN_LASH = {
    'id': 'thorn_lash', 'display_name': 'Thorn Lash',
    'description': 'Lashes a target with a thorny vine, dealing minor physical Nature damage.',
    'level_req': 1, 'mana_cost': 10, 'cooldown': 0.0, 'casting_time': 1.0, 'target_type': 'single', 'range': 28,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Nature', 'min_damage': 8, 'max_damage': 11}]
}

REJUVENATION = {
    'id': 'rejuvenation', 'display_name': 'Rejuvenation',
    'description': 'Blankets a friendly target with restorative energies, healing them over time. The cornerstone of a Nature healer.',
    'level_req': 3, 'mana_cost': 20, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'hot', 'tick_healing': 8, 'duration': 15.0, 'interval': 1.0}]
}

POISON_STING = {
    'id': 'poison_sting', 'display_name': 'Poison Sting',
    'description': 'Stings the target, injecting a venom that deals Nature damage over time.',
    'level_req': 5, 'mana_cost': 18, 'cooldown': 4.0, 'casting_time': 0.5, 'target_type': 'single', 'range': 25,
    'effects': [{'type': 'dot', 'damage_type': 'Poison', 'tick_damage': 5, 'duration': 12.0, 'interval': 1.0}]
}

HEALING_TOUCH = {
    'id': 'healing_touch', 'display_name': 'Healing Touch',
    'description': 'A slow but mana-efficient spell that heals a friendly target for a moderate amount.',
    'level_req': 7, 'mana_cost': 25, 'cooldown': 0.0, 'casting_time': 2.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'direct_heal', 'min_healing': 40, 'max_healing': 55}]
}

ENTANGLING_ROOTS = {
    'id': 'entangling_roots', 'display_name': 'Entangling Roots',
    'description': 'Causes roots to erupt from the ground, immobilizing the target. Damage taken may break the effect.',
    'level_req': 10, 'mana_cost': 25, 'cooldown': 15.0, 'casting_time': 1.5, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'debuff', 'effect': 'root', 'duration': 8.0, 'break_on_damage_threshold': 50}]
}

CURE_POISON = {
    'id': 'cure_poison', 'display_name': 'Cure Poison',
    'description': 'Cures a friendly target of one Poison effect.',
    'level_req': 14, 'mana_cost': 15, 'cooldown': 8.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'cleanse', 'cleanse_type': 'poison', 'count': 1}]
}

# -----------------------------------------------------------------------------
# TIER 2: ADEPT (Level 15-29)
# -----------------------------------------------------------------------------

INSECT_SWARM = {
    'id': 'insect_swarm', 'display_name': 'Insect Swarm',
    'description': 'Summons a swarm of insects to plague the target, dealing damage over time and causing their attacks to miss.',
    'level_req': 16, 'mana_cost': 45, 'cooldown': 10.0, 'casting_time': 1.0, 'target_type': 'single', 'range': 25,
    'effects': [
        {'type': 'dot', 'damage_type': 'Nature', 'tick_damage': 8, 'duration': 10.0, 'interval': 1.0},
        {'type': 'debuff', 'effect': 'miss_chance', 'amount': 0.15, 'duration': 10.0}
    ]
}

REGROWTH = {
    'id': 'regrowth', 'display_name': 'Regrowth',
    'description': 'Heals a target for a small initial amount, followed by a powerful heal-over-time effect.',
    'level_req': 20, 'mana_cost': 40, 'cooldown': 0.0, 'casting_time': 1.5, 'target_type': 'single', 'range': 30,
    'effects': [
        {'type': 'direct_heal', 'min_healing': 30, 'max_healing': 40},
        {'type': 'hot', 'tick_healing': 20, 'duration': 8.0, 'interval': 1.0}
    ]
}

BARKSKIN = {
    'id': 'barkskin', 'display_name': 'Barkskin',
    'description': 'Your skin becomes as tough as bark, increasing your Toughness and Nature resistance.',
    'level_req': 22, 'mana_cost': 40, 'cooldown': 5.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'buff', 'stat': 'Toughness', 'amount': 25, 'duration': 300.0},
        {'type': 'buff', 'stat': 'Nature_Resistance', 'amount': 20, 'duration': 300.0}
    ]
}

THORN_VOLLEY = {
    'id': 'thorn_volley', 'display_name': 'Thorn Volley',
    'description': 'Fires a spray of sharp thorns in a cone, damaging all enemies in front of you.',
    'level_req': 26, 'mana_cost': 60, 'cooldown': 8.0, 'casting_time': 1.2, 'target_type': 'cone', 'range': 12,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Nature', 'min_damage': 25, 'max_damage': 35, 'cone_angle': 45}]
}

NATURES_CURE = {
    'id': 'natures_cure', 'display_name': "Nature's Cure",
    'description': 'A powerful cleanse that removes all Poison and Disease effects from a friendly target.',
    'level_req': 30, 'mana_cost': 35, 'cooldown': 10.0, 'casting_time': 0.5, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'cleanse', 'cleanse_type': ['poison', 'disease'], 'count': 'all'}]
}

# -----------------------------------------------------------------------------
# TIER 3: MASTER (Level 30-44)
# -----------------------------------------------------------------------------

WILD_GROWTH = {
    'id': 'wild_growth', 'display_name': 'Wild Growth',
    'description': 'Heals the target and up to 4 other nearby allies with a potent heal-over-time effect.',
    'level_req': 34, 'mana_cost': 90, 'cooldown': 10.0, 'casting_time': 1.5, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'chain_hot', 'tick_healing': 18, 'duration': 9.0, 'interval': 1.0, 'max_jumps': 4, 'jump_range': 15}]
}

WRATH = {
    'id': 'wrath', 'display_name': 'Wrath',
    'description': 'Calls upon the sun\'s energy to smite a target, dealing significant Nature damage.',
    'level_req': 38, 'mana_cost': 80, 'cooldown': 2.0, 'casting_time': 2.0, 'target_type': 'single', 'range': 35,
    'effects': [{'type': 'direct_damage', 'damage_type': 'Nature', 'min_damage': 120, 'max_damage': 150}]
}

SUMMON_TREANT = {
    'id': 'summon_treant', 'display_name': 'Summon Treant',
    'description': 'Summons a sturdy Treant to fight for you. The Treant will taunt nearby enemies, protecting you.',
    'level_req': 42, 'mana_cost': 150, 'cooldown': 120.0, 'casting_time': 2.5, 'target_type': 'aoe_ground', 'range': 15,
    'effects': [{'type': 'summon_pet', 'name': 'Treant Protector', 'duration': 30.0, 'pet_abilities': ['taunt', 'slam']}]
}

EFFLORESCENCE = {
    'id': 'efflorescence', 'display_name': 'Efflorescence',
    'description': 'Grows a patch of healing flora at a location, restoring health every second to allies who stand within it.',
    'level_req': 45, 'mana_cost': 100, 'cooldown': 25.0, 'casting_time': 1.0, 'target_type': 'aoe_ground', 'range': 30,
    'effects': [{'type': 'ground_hot', 'tick_healing': 25, 'duration': 10.0, 'interval': 1.0, 'radius': 8}]
}

# -----------------------------------------------------------------------------
# TIER 4: GRANDMASTER (Level 45-60)
# -----------------------------------------------------------------------------

VENOMBLOOM = {
    'id': 'venombloom', 'display_name': 'Venombloom',
    'description': 'When an enemy dies while affected by your Poison Sting, they explode, poisoning all nearby enemies.',
    'level_req': 48, 'mana_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'conditional_aoe_dot', 'trigger': 'on_death_with_dot', 'dot_id': 'poison_sting', 'radius': 8}]
}

HURRICANE = {
    'id': 'hurricane', 'display_name': 'Hurricane',
    'description': 'Creates a hurricane around the caster, slowing and damaging all nearby enemies as long as it is channeled.',
    'level_req': 51, 'mana_cost': 60, 'mana_upkeep': 30, 'cooldown': 25.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'channeled_dot', 'damage_type': 'Nature', 'tick_damage': 30, 'duration': -1, 'interval': 1.0, 'radius': 10, 'debuff': 'slow', 'debuff_amount': 0.30}]
}

TRANQUILITY = {
    'id': 'tranquility', 'display_name': 'Tranquility',
    'description': 'The ultimate AoE heal. Heals all allies in a massive area over 8 seconds. Requires channeling.',
    'level_req': 54, 'mana_cost': 200, 'cooldown': 180.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'channeled_hot', 'tick_healing': 100, 'duration': 8.0, 'interval': 1.0, 'radius': 30}]
}

FORCE_OF_NATURE = {
    'id': 'force_of_nature', 'display_name': 'Force of Nature',
    'description': 'Summons three powerful Treants for a short duration that deal significant damage.',
    'level_req': 57, 'mana_cost': 180, 'cooldown': 150.0, 'casting_time': 1.5, 'target_type': 'aoe_ground', 'range': 20,
    'effects': [{'type': 'summon_multiple_pets', 'name': 'Treant Vindicator', 'duration': 20.0, 'count': 3}]
}

GIFT_OF_THE_EARTHMOTHER = {
    'id': 'gift_of_the_earthmother', 'display_name': 'Gift of the Earthmother',
    'description': 'Your Heal-over-Time effects now have a chance to critically heal, doubling the effect of that tick.',
    'level_req': 59, 'mana_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'enhances_spell': 'all_hots', 'proc_chance': 0.10, 'effect': 'critical_tick'}]
}

INFESTATION = {
    'id': 'infestation', 'display_name': 'Infestation',
    'description': 'The ultimate DoT. Infects the target with a plague that deals escalating damage. If the target dies, Infestation spreads to two nearby enemies.',
    'level_req': 60, 'mana_cost': 250, 'cooldown': 90.0, 'casting_time': 2.5, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'ramping_dot', 'damage_type': 'Poison', 'start_tick_damage': 20, 'damage_increase_per_tick': 5, 'duration': 20.0, 'interval': 1.0, 'spreads_on_death': 2}]
}

# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------
NATURE_ABILITIES = {
    'thorn_lash': THORN_LASH, 'rejuvenation': REJUVENATION, 'poison_sting': POISON_STING, 'healing_touch': HEALING_TOUCH,
    'entangling_roots': ENTANGLING_ROOTS, 'cure_poison': CURE_POISON, 'insect_swarm': INSECT_SWARM, 'regrowth': REGROWTH,
    'barkskin': BARKSKIN, 'thorn_volley': THORN_VOLLEY, 'natures_cure': NATURES_CURE, 'wild_growth': WILD_GROWTH,
    'wrath': WRATH, 'summon_treant': SUMMON_TREANT, 'efflorescence': EFFLORESCENCE, 'venombloom': VENOMBLOOM,
    'hurricane': HURRICANE, 'tranquility': TRANQUILITY, 'force_of_nature': FORCE_OF_NATURE,
    'gift_of_the_earthmother': GIFT_OF_THE_EARTHMOTHER, 'infestation': INFESTATION,
}