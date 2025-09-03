"""
This file is a grand bestiary of all summonable creatures in the game.

These abilities are unlocked by increasing a new "Summoning" skill. The design
is to provide a vast array of options that can synergize with any class or
form the foundation of a dedicated Summoner build.

The 'summon_creature' effect structure is as follows:
    - 'creature_name': The name of the summoned unit.
    - 'duration': How long it lasts in seconds (-1 for permanent until death).
    - 'health': The base health of the summon.
    - 'attack_damage_min'/'max': Base damage of its standard attack.
    - 'attack_speed': Time in seconds between its attacks.
    - 'attack_range': 'melee' or a number for ranged.
    - 'abilities': A list of unique powers the summon possesses.
        - 'name': The name of the ability.
        - 'type': 'passive_aura', 'on_hit_proc', 'active_ability', etc.
        - ... plus other keys specific to the ability's function.
"""

# =============================================================================
#
#                               ELEMENTAL SUMMONS
#
# =============================================================================

# --- TIER 1 ---
SUMMON_FIRE_SPRITE = {
    'id': 'summon_fire_sprite', 'display_name': 'Summon Fire Sprite',
    'description': 'Summons a mischievous Fire Sprite that hurls small fireballs at your enemies.',
    'level_req': 8, 'skill_req': 10, 'mana_cost': 50, 'cooldown': 45.0, 'casting_time': 1.5, 'target_type': 'aoe_ground', 'range': 20,
    'effects': [{'type': 'summon_creature', 'creature_name': 'Fire Sprite', 'duration': 45.0, 'health': 150,
                 'attack_damage_min': 10, 'attack_damage_max': 14, 'attack_speed': 1.8, 'attack_range': 25,
                 'abilities': [{'name': 'Kindle', 'type': 'on_hit_proc', 'proc_chance': 0.20, 'effect': 'dot', 'damage_type': 'Fire', 'tick_damage': 3, 'duration': 6.0}]
    }]
}

# --- TIER 2 ---
SUMMON_ROCK_GOLEM = {
    'id': 'summon_rock_golem', 'display_name': 'Summon Rock Golem',
    'description': 'Summons a sturdy Rock Golem to taunt enemies and protect you with its rocky hide.',
    'level_req': 20, 'skill_req': 25, 'mana_cost': 120, 'cooldown': 120.0, 'casting_time': 2.5, 'target_type': 'aoe_ground', 'range': 15,
    'effects': [{'type': 'summon_creature', 'creature_name': 'Rock Golem', 'duration': 60.0, 'health': 800,
                 'attack_damage_min': 25, 'attack_damage_max': 30, 'attack_speed': 2.5, 'attack_range': 'melee',
                 'abilities': [{'name': 'Taunt', 'type': 'active_ability', 'cooldown': 8.0, 'effect': 'taunt', 'radius': 10},
                               {'name': 'Stone Skin', 'type': 'passive_aura', 'effect': 'buff', 'stat': 'Toughness', 'amount': 25, 'radius': 15}]
    }]
}

# --- TIER 3 ---
SUMMON_FROST_ELEMENTAL = {
    'id': 'summon_frost_elemental', 'display_name': 'Summon Frost Elemental',
    'description': 'Summons a Frost Elemental that chills nearby enemies and can freeze them solid with its Frost Nova.',
    'level_req': 35, 'skill_req': 40, 'mana_cost': 180, 'cooldown': 180.0, 'casting_time': 3.0, 'target_type': 'aoe_ground', 'range': 20,
    'effects': [{'type': 'summon_creature', 'creature_name': 'Frost Elemental', 'duration': 60.0, 'health': 600,
                 'attack_damage_min': 40, 'attack_damage_max': 50, 'attack_speed': 2.0, 'attack_range': 'melee',
                 'abilities': [{'name': 'Chilling Aura', 'type': 'passive_aura', 'effect': 'debuff', 'debuff_type': 'slow', 'amount': 0.20, 'radius': 10},
                               {'name': 'Frost Nova', 'type': 'active_ability', 'cooldown': 15.0, 'effect': 'root', 'duration': 4.0, 'radius': 10}]
    }]
}

# --- TIER 4 ---
SUMMON_GREATER_FIRE_ELEMENTAL = {
    'id': 'summon_greater_fire_elemental', 'display_name': 'Summon Greater Fire Elemental',
    'description': 'The ultimate fire summon. Summons a towering Fire Elemental that burns nearby enemies and leaves patches of fire on the ground.',
    'level_req': 60, 'skill_req': 75, 'mana_cost': 300, 'cooldown': 300.0, 'casting_time': 4.0, 'target_type': 'aoe_ground', 'range': 25,
    'effects': [{'type': 'summon_creature', 'creature_name': 'Greater Fire Elemental', 'duration': 60.0, 'health': 1500,
                 'attack_damage_min': 80, 'attack_damage_max': 100, 'attack_speed': 2.2, 'attack_range': 'melee',
                 'abilities': [{'name': 'Immolation', 'type': 'passive_aura', 'effect': 'dot', 'damage_type': 'Fire', 'tick_damage': 25, 'radius': 8},
                               {'name': 'Scorched Earth', 'type': 'on_hit_proc', 'proc_chance': 0.30, 'effect': 'ground_dot', 'damage_type': 'Fire', 'tick_damage': 15, 'duration': 6.0, 'radius': 4}]
    }]
}

# =============================================================================
#
#                               NATURE SUMMONS
#
# =============================================================================

# --- TIER 1 ---
SUMMON_DIRE_WOLF = {
    'id': 'summon_dire_wolf', 'display_name': 'Summon Dire Wolf',
    'description': 'Summons a loyal Dire Wolf to fight by your side. Its attacks cause the enemy to bleed.',
    'level_req': 10, 'skill_req': 12, 'mana_cost': 60, 'cooldown': 60.0, 'casting_time': 2.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'summon_creature', 'creature_name': 'Dire Wolf', 'duration': 60.0, 'health': 200,
                 'attack_damage_min': 15, 'attack_damage_max': 18, 'attack_speed': 1.5, 'attack_range': 'melee',
                 'abilities': [{'name': 'Vicious Bite', 'type': 'on_hit_proc', 'proc_chance': 0.25, 'effect': 'dot', 'damage_type': 'Bleed', 'tick_damage': 4, 'duration': 8.0}]
    }]
}

# --- TIER 2 ---
SUMMON_POISON_WYRMLING = {
    'id': 'summon_poison_wyrmling', 'display_name': 'Summon Poison Wyrmling',
    'description': 'Summons a small dragon that spits poison from a distance, dealing damage over time.',
    'level_req': 22, 'skill_req': 28, 'mana_cost': 130, 'cooldown': 120.0, 'casting_time': 2.0, 'target_type': 'aoe_ground', 'range': 20,
    'effects': [{'type': 'summon_creature', 'creature_name': 'Poison Wyrmling', 'duration': 45.0, 'health': 300,
                 'attack_damage_min': 20, 'attack_damage_max': 25, 'attack_speed': 2.0, 'attack_range': 30,
                 'abilities': [{'name': 'Poison Spit', 'type': 'on_hit_proc', 'proc_chance': 1.0, 'effect': 'dot', 'damage_type': 'Poison', 'tick_damage': 10, 'duration': 10.0}]
    }]
}

# --- TIER 3 ---
SUMMON_GRIZZLY_BEAR = {
    'id': 'summon_grizzly_bear', 'display_name': 'Summon Grizzly Bear',
    'description': 'Summons a massive Grizzly Bear that can stun its target with a mighty swipe.',
    'level_req': 38, 'skill_req': 45, 'mana_cost': 200, 'cooldown': 180.0, 'casting_time': 3.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'summon_creature', 'creature_name': 'Grizzly Bear', 'duration': 60.0, 'health': 1200,
                 'attack_damage_min': 50, 'attack_damage_max': 60, 'attack_speed': 2.4, 'attack_range': 'melee',
                 'abilities': [{'name': 'Bash', 'type': 'on_hit_proc', 'proc_chance': 0.15, 'effect': 'debuff', 'debuff_type': 'stun', 'duration': 2.0}]
    }]
}

# --- TIER 4 ---
SUMMON_SPIRIT_BEAST = {
    'id': 'summon_spirit_beast', 'display_name': 'Summon Spirit Beast',
    'description': 'The ultimate nature summon. Calls forth a mystical Spirit Beast that heals all nearby allies with every attack.',
    'level_req': 58, 'skill_req': 70, 'mana_cost': 280, 'cooldown': 300.0, 'casting_time': 3.5, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'summon_creature', 'creature_name': 'Spirit Beast', 'duration': 45.0, 'health': 1000,
                 'attack_damage_min': 70, 'attack_damage_max': 85, 'attack_speed': 1.8, 'attack_range': 'melee',
                 'abilities': [{'name': 'Spirit Mend', 'type': 'on_hit_proc', 'proc_chance': 1.0, 'effect': 'hot', 'tick_healing': 20, 'duration': 5.0, 'radius': 20}]
    }]
}

# =============================================================================
#
#                               UNDEAD / DARK SUMMONS
#
# =============================================================================

# --- TIER 1 ---
RAISE_SKELETON = {
    'id': 'raise_skeleton', 'display_name': 'Raise Skeleton',
    'description': 'Raises a fragile Skeleton Warrior from a corpse to fight for you. Requires a nearby corpse.',
    'level_req': 12, 'skill_req': 15, 'mana_cost': 40, 'cooldown': 10.0, 'casting_time': 1.5, 'target_type': 'corpse', 'range': 20,
    'effects': [{'type': 'summon_creature', 'creature_name': 'Skeleton Warrior', 'duration': -1, 'health': 120,
                 'attack_damage_min': 12, 'attack_damage_max': 16, 'attack_speed': 2.0, 'attack_range': 'melee',
                 'abilities': []
    }]
}

# --- TIER 2 ---
SUMMON_SHADE = {
    'id': 'summon_shade', 'display_name': 'Summon Shade',
    'description': 'Summons a terrifying Shade that reduces the attack speed of enemies it strikes.',
    'level_req': 25, 'skill_req': 30, 'mana_cost': 140, 'cooldown': 120.0, 'casting_time': 2.0, 'target_type': 'aoe_ground', 'range': 20,
    'effects': [{'type': 'summon_creature', 'creature_name': 'Sorrowful Shade', 'duration': 60.0, 'health': 400,
                 'attack_damage_min': 30, 'attack_damage_max': 35, 'attack_speed': 1.9, 'attack_range': 'melee',
                 'abilities': [{'name': 'Withering Touch', 'type': 'on_hit_proc', 'proc_chance': 1.0, 'effect': 'debuff', 'stat': 'Haste_Percent', 'amount': -0.15, 'duration': 5.0}]
    }]
}

# --- TIER 3 ---
SUMMON_BONE_GOLEM = {
    'id': 'summon_bone_golem', 'display_name': 'Summon Bone Golem',
    'description': 'Constructs a massive Bone Golem from multiple corpses. The golem\'s armor reduces all damage it takes.',
    'level_req': 42, 'skill_req': 50, 'mana_cost': 220, 'cooldown': 180.0, 'casting_time': 3.5, 'target_type': 'corpse', 'range': 20, 'corpse_cost': 3,
    'effects': [{'type': 'summon_creature', 'creature_name': 'Bone Golem', 'duration': -1, 'health': 1500,
                 'attack_damage_min': 60, 'attack_damage_max': 70, 'attack_speed': 2.8, 'attack_range': 'melee',
                 'abilities': [{'name': 'Bone Armor', 'type': 'passive_buff', 'stat': 'Damage_Reduction', 'amount': 0.20}]
    }]
}

# --- TIER 4 ---
SUMMON_LICH = {
    'id': 'summon_lich', 'display_name': 'Summon Lich',
    'description': 'The ultimate necromantic summon. Summons a powerful Lich that casts Frostbolts and periodically raises lesser Skeletons.',
    'level_req': 60, 'skill_req': 75, 'mana_cost': 350, 'cooldown': 600.0, 'casting_time': 5.0, 'target_type': 'aoe_ground', 'range': 20,
    'effects': [{'type': 'summon_creature', 'creature_name': 'Ancient Lich', 'duration': 120.0, 'health': 1200,
                 'attack_damage_min': 70, 'attack_damage_max': 90, 'attack_speed': 2.5, 'attack_range': 30,
                 'abilities': [{'name': 'Raise Servant', 'type': 'active_ability', 'cooldown': 10.0, 'effect': 'summon_minion', 'minion_id': 'raise_skeleton'}]
    }]
}

# =============================================================================
#
#                               ARCANE / HOLY SUMMONS
#
# =============================================================================

# --- TIER 2 ---
SUMMON_MANA_WYRM = {
    'id': 'summon_mana_wyrm', 'display_name': 'Summon Mana Wyrm',
    'description': 'Summons a being of pure magic that restores a small amount of your mana with each attack.',
    'level_req': 28, 'skill_req': 35, 'mana_cost': 150, 'cooldown': 180.0, 'casting_time': 2.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'summon_creature', 'creature_name': 'Mana Wyrm', 'duration': 30.0, 'health': 350,
                 'attack_damage_min': 20, 'attack_damage_max': 25, 'attack_speed': 2.0, 'attack_range': 'melee',
                 'abilities': [{'name': 'Mana Feed', 'type': 'on_hit_proc', 'proc_chance': 1.0, 'effect': 'resource_gain', 'resource': 'mana', 'amount': 15}]
    }]
}

# --- TIER 3 ---
SUMMON_GUARDIAN_ANGEL = {
    'id': 'summon_guardian_angel', 'display_name': 'Summon Guardian Angel',
    'description': 'Summons an Angel to protect you. The Angel does not attack, but periodically heals you.',
    'level_req': 45, 'skill_req': 55, 'mana_cost': 250, 'cooldown': 300.0, 'casting_time': 2.5, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'summon_creature', 'creature_name': 'Guardian Angel', 'duration': 60.0, 'health': 1000,
                 'attack_damage_min': 0, 'attack_damage_max': 0, 'attack_speed': 999, 'attack_range': 0,
                 'abilities': [{'name': 'Holy Light', 'type': 'active_ability', 'cooldown': 5.0, 'effect': 'hot', 'tick_healing': 40, 'duration': 5.0, 'target': 'self'}]
    }]
}

# --- TIER 4 ---
SUMMON_ANIMATED_ARMOR = {
    'id': 'summon_animated_armor', 'display_name': 'Summon Animated Armor',
    'description': 'Animates a suit of heavy plate armor to serve as your bodyguard. It redirects a portion of the damage you take to itself.',
    'level_req': 55, 'skill_req': 65, 'mana_cost': 200, 'cooldown': 180.0, 'casting_time': 3.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'summon_creature', 'creature_name': 'Animated Armor', 'duration': -1, 'health': 2000,
                 'attack_damage_min': 50, 'attack_damage_max': 60, 'attack_speed': 2.2, 'attack_range': 'melee',
                 'abilities': [{'name': 'Bodyguard', 'type': 'passive_aura', 'effect': 'damage_redirect', 'percent': 0.20, 'radius': 10}]
    }]
}

# =============================================================================
#
#                               CHAOS SUMMONS
#
# =============================================================================

# --- TIER 2 ---
SUMMON_CHAOS_IMP = {
    'id': 'summon_chaos_imp', 'display_name': 'Summon Chaos Imp',
    'description': 'Summons a volatile Chaos Imp that casts random, weak elemental spells.',
    'level_req': 30, 'skill_req': 38, 'mana_cost': 160, 'cooldown': 150.0, 'casting_time': 2.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'summon_creature', 'creature_name': 'Chaos Imp', 'duration': 60.0, 'health': 450,
                 'attack_damage_min': 10, 'attack_damage_max': 10, 'attack_speed': 1.5, 'attack_range': 25,
                 'abilities': [{'name': 'Wild Magic', 'type': 'active_ability', 'cooldown': 4.0, 'effect': 'random_elemental_bolt'}]
    }]
}

# --- TIER 4 ---
SUMMON_VOID_TERROR = {
    'id': 'summon_void_terror', 'display_name': 'Summon Void Terror',
    'description': 'Summons a horrifying Void Terror from the space between worlds. Its attacks drain the target\'s life, healing itself.',
    'level_req': 59, 'skill_req': 72, 'mana_cost': 320, 'cooldown': 300.0, 'casting_time': 4.0, 'target_type': 'aoe_ground', 'range': 20,
    'effects': [{'type': 'summon_creature', 'creature_name': 'Void Terror', 'duration': 60.0, 'health': 1800,
                 'attack_damage_min': 90, 'attack_damage_max': 110, 'attack_speed': 2.0, 'attack_range': 'melee',
                 'abilities': [{'name': 'Void Leech', 'type': 'on_hit_proc', 'proc_chance': 1.0, 'effect': 'lifesteal', 'percent': 0.50}]
    }]
}


# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------
SUMMONING_ABILITIES = {
    'summon_fire_sprite': SUMMON_FIRE_SPRITE, 'summon_rock_golem': SUMMON_ROCK_GOLEM, 'summon_frost_elemental': SUMMON_FROST_ELEMENTAL,
    'summon_greater_fire_elemental': SUMMON_GREATER_FIRE_ELEMENTAL, 'summon_dire_wolf': SUMMON_DIRE_WOLF,
    'summon_poison_wyrmling': SUMMON_POISON_WYRMLING, 'summon_grizzly_bear': SUMMON_GRIZZLY_BEAR, 'summon_spirit_beast': SUMMON_SPIRIT_BEAST,
    'raise_skeleton': RAISE_SKELETON, 'summon_shade': SUMMON_SHADE, 'summon_bone_golem': SUMMON_BONE_GOLEM, 'summon_lich': SUMMON_LICH,
    'summon_mana_wyrm': SUMMON_MANA_WYRM, 'summon_guardian_angel': SUMMON_GUARDIAN_ANGEL, 'summon_animated_armor': SUMMON_ANIMATED_ARMOR,
    'summon_chaos_imp': SUMMON_CHAOS_IMP, 'summon_void_terror': SUMMON_VOID_TERROR,
}