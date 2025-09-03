"""
This file contains all data for Magical Foci abilities. These are not tied to a
specific element but represent a caster's fundamental skill in wielding magic.

As per your design, these abilities are unlocked by increasing a new
"Magical Foci" skill through the use of staves, wands, orbs, etc.

Philosophy: High Mana Manipulation, High Spellcasting Utility, Mid Magical Defense,
and Low Direct Damage. This tree makes your other magic schools better.
"""

# -----------------------------------------------------------------------------
# TIER 1: APPRENTICE (Level 1-14)
# -----------------------------------------------------------------------------

CHANNEL_MANA = {
    'id': 'channel_mana', 'display_name': 'Channel Mana',
    'description': 'Enter a meditative state to channel raw magic, restoring a portion of your mana over a few seconds. Cannot move while channeling.',
    'level_req': 1, 'skill_req': 1, 'mana_cost': 0, 'cooldown': 45.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'channeled_resource_gain', 'resource': 'mana', 'percent_per_tick': 0.10, 'duration': 4.0, 'interval': 1.0}] # Restores 40% mana over 4s
}

FOCUS_MAGIC = {
    'id': 'focus_magic', 'display_name': 'Focus Magic',
    'description': 'Focus your will through your implement, increasing the damage of your next spell by 20%.',
    'level_req': 4, 'skill_req': 5, 'mana_cost': 15, 'cooldown': 20.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'empower_next_spell', 'damage_multiplier': 1.20, 'charges': 1, 'duration': 10.0}]
}

DISRUPTING_ORB = {
    'id': 'disrupting_orb', 'display_name': 'Disrupting Orb',
    'description': 'Launch a slow-moving orb of pure magic that silences the first enemy it touches for 2 seconds.',
    'level_req': 8, 'skill_req': 10, 'mana_cost': 25, 'cooldown': 18.0, 'casting_time': 1.0, 'target_type': 'projectile', 'range': 25,
    'effects': [{'type': 'debuff', 'effect': 'silence', 'duration': 2.0}]
}

ARCANE_WARD = {
    'id': 'arcane_ward', 'display_name': 'Arcane Ward',
    'description': 'Create a personal ward that absorbs a small amount of incoming magic damage. Lasts until the shield is broken.',
    'level_req': 12, 'skill_req': 15, 'mana_cost': 30, 'cooldown': 40.0, 'casting_time': 0.5, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'magic_damage_shield', 'shield_amount': 150}]
}

# -----------------------------------------------------------------------------
# TIER 2: ADEPT (Level 15-29)
# -----------------------------------------------------------------------------

MANA_SURGE = {
    'id': 'mana_surge', 'display_name': 'Mana Surge',
    'description': 'Instantly restore a large amount of your mana, but reduces your magic damage dealt by 50% for 4 seconds.',
    'level_req': 16, 'skill_req': 20, 'mana_cost': 0, 'cooldown': 120.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [
        {'type': 'resource_gain', 'resource': 'mana', 'percent_gain': 0.50},
        {'type': 'debuff', 'stat': 'Magic_Damage_Dealt', 'amount': -0.50, 'duration': 4.0, 'target': 'self'}
    ]
}

RUNE_OF_POWER = {
    'id': 'rune_of_power', 'display_name': 'Rune of Power',
    'description': 'Inscribe a rune on the ground. While standing on the rune, your spell damage is increased by 15%.',
    'level_req': 20, 'skill_req': 25, 'mana_cost': 40, 'cooldown': 60.0, 'casting_time': 1.0, 'target_type': 'aoe_ground', 'range': 10,
    'effects': [{'type': 'ground_buff', 'stat': 'Magic_Damage_Dealt', 'amount': 0.15, 'duration': 15.0, 'radius': 5}]
}

SPELL_LOCK = {
    'id': 'spell_lock', 'display_name': 'Spell Lock',
    'description': 'A ranged interrupt that instantly silences an enemy for 3 seconds, preventing spellcasting.',
    'level_req': 24, 'skill_req': 30, 'mana_cost': 20, 'cooldown': 25.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'debuff', 'effect': 'silence', 'duration': 3.0}]
}

PRISMATIC_CLOAK = {
    'id': 'prismatic_cloak', 'display_name': 'Prismatic Cloak',
    'description': 'For 10 seconds, you have a 25% chance to reflect any single-target spell cast on you back at the attacker.',
    'level_req': 28, 'skill_req': 35, 'mana_cost': 50, 'cooldown': 90.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'effect': 'spell_reflection', 'proc_chance': 0.25, 'duration': 10.0}]
}

# -----------------------------------------------------------------------------
# TIER 3: MASTER (Level 30-44)
# -----------------------------------------------------------------------------

ARCANE_ATTUNEMENT = {
    'id': 'arcane_attunement', 'display_name': 'Arcane Attunement',
    'description': 'Your deep connection to magic is now permanent. You gain bonus spell damage equal to 10% of your maximum mana.',
    'level_req': 32, 'skill_req': 40, 'mana_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'effect': 'max_mana_to_spell_damage', 'conversion_rate': 0.10}]
}

GRAVITY_WELL = {
    'id': 'gravity_well', 'display_name': 'Gravity Well',
    'description': 'Create a sphere of immense gravity at a location that pulls all nearby enemies towards its center and slows them.',
    'level_req': 36, 'skill_req': 45, 'mana_cost': 80, 'cooldown': 45.0, 'casting_time': 1.5, 'target_type': 'aoe_ground', 'range': 30,
    'effects': [{'type': 'debuff', 'effect': 'pull_to_center', 'strength': 8, 'duration': 5.0, 'radius': 10}, {'type': 'debuff', 'effect': 'slow', 'amount': 0.50, 'duration': 5.0, 'radius': 10}]
}

FEEDBACK = {
    'id': 'feedback', 'display_name': 'Feedback',
    'description': 'Curse a target with magical feedback. For 12 seconds, whenever they cast a spell, they take Arcane damage.',
    'level_req': 40, 'skill_req': 50, 'mana_cost': 40, 'cooldown': 30.0, 'casting_time': 0.0, 'target_type': 'single', 'range': 30,
    'effects': [{'type': 'debuff', 'effect': 'damage_on_cast', 'damage_type': 'Arcane', 'min_damage': 40, 'max_damage': 50, 'duration': 12.0}]
}

TEMPORAL_FIELD = {
    'id': 'temporal_field', 'display_name': 'Temporal Field',
    'description': 'Create a field of distorted time. Enemies inside have their attack and casting speed slowed by 40%.',
    'level_req': 44, 'skill_req': 55, 'mana_cost': 70, 'cooldown': 60.0, 'casting_time': 1.0, 'target_type': 'aoe_ground', 'range': 25,
    'effects': [{'type': 'ground_debuff', 'stat': 'Haste_Percent', 'amount': -0.40, 'duration': 8.0, 'radius': 8}]
}

# -----------------------------------------------------------------------------
# TIER 4: GRANDMASTER (Level 45-60)
# -----------------------------------------------------------------------------

MANA_FONT = {
    'id': 'mana_font', 'display_name': 'Mana Font',
    'description': 'Your mastery over mana is absolute, greatly increasing your passive mana regeneration in and out of combat.',
    'level_req': 48, 'skill_req': 60, 'mana_cost': 0, 'cooldown': 0.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'passive_enhancement', 'stat': 'Mana_Regen_Multiplier', 'amount': 2.0}]
}

MIRROR_IMAGE = {
    'id': 'mirror_image', 'display_name': 'Mirror Image',
    'description': 'Create three illusory copies of yourself to confuse and distract enemies. The copies will cast non-damaging spells.',
    'level_req': 52, 'skill_req': 65, 'mana_cost': 60, 'cooldown': 120.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'summon_decoys', 'count': 3, 'duration': 20.0}]
}

OVERCHANNEL = {
    'id': 'overchannel', 'display_name': 'Overchannel',
    'description': 'The ultimate damage cooldown for a pure mage. For 10 seconds, all your spells deal 50% more damage, but you are silenced for 5 seconds when the effect ends.',
    'level_req': 56, 'skill_req': 70, 'mana_cost': 100, 'cooldown': 180.0, 'casting_time': 0.0, 'target_type': 'self', 'range': 0,
    'effects': [{'type': 'buff', 'stat': 'All_Damage_Dealt', 'amount': 0.50, 'duration': 10.0, 'penalty_debuff': 'silence', 'penalty_duration': 5.0}]
}

SINGULARITY = {
    'id': 'singularity', 'display_name': 'Singularity',
    'description': 'The ultimate expression of magical control. Create a singularity that pulls all enemies into its center, then explodes after 5 seconds, dealing massive Arcane damage.',
    'level_req': 60, 'skill_req': 75, 'mana_cost': 200, 'cooldown': 180.0, 'casting_time': 2.0, 'target_type': 'aoe_ground', 'range': 35,
    'effects': [
        {'type': 'debuff', 'effect': 'pull_to_center', 'strength': 10, 'duration': 5.0, 'radius': 15},
        {'type': 'delayed_aoe', 'trigger': 'on_expire', 'delay': 5.0, 'damage_type': 'Arcane', 'min_damage': 400, 'max_damage': 500, 'radius': 15}
    ]
}

# -----------------------------------------------------------------------------
# MAIN DATA DICTIONARY
# -----------------------------------------------------------------------------
MAGICAL_FOCI_ABILITIES = {
    'channel_mana': CHANNEL_MANA, 'focus_magic': FOCUS_MAGIC, 'disrupting_orb': DISRUPTING_ORB, 'arcane_ward': ARCANE_WARD,
    'mana_surge': MANA_SURGE, 'rune_of_power': RUNE_OF_POWER, 'spell_lock': SPELL_LOCK, 'prismatic_cloak': PRISMATIC_CLOAK,
    'arcane_attunement': ARCANE_ATTUNEMENT, 'gravity_well': GRAVITY_WELL, 'feedback': FEEDBACK, 'temporal_field': TEMPORAL_FIELD,
    'mana_font': MANA_FONT, 'mirror_image': MIRROR_IMAGE, 'overchannel': OVERCHANNEL, 'singularity': SINGULARITY,
}