# Spell randomization logic.

import random

from . import flags, utils

from randomizer.data import enemies
from randomizer.data import spells
from randomizer.data.spells import SpellElement


def _randomize_spell(world, spell):
    """Perform randomization for this spell.

    Args:
        spell(randomizer.data.spells.Spell):
    """
    if world.settings.is_flag_enabled(flags.CharacterSpellStats):
        spell.fp = utils.mutate_normal(spell.fp, minimum=1, maximum=99)

        # If this is an enemy spell with status effects, shuffle them.
        if isinstance(spell, spells.EnemySpell) and spell.status_effects:
            effects = [0, 1, 2, 3, 5, 6]
            # Chance to include berserk as an option if safety checks are disabled.
            if spell.world.settings.is_flag_enabled(flags.EnemyNoSafetyChecks) and utils.coin_flip(1 / 5):
                effects.append(4)

            spell.status_effects = random.sample(
                effects, len(spell.status_effects))

        # Don't shuffle power for certain spells that cause problems if they deal damage.
        if not isinstance(spell, (spells.GenoBoost, spells.Shredder, spells.SleepyTime, spells.Mute, spells.Psychopath)):
            spell.power = utils.mutate_normal(spell.power)

        # Don't shuffle hit rate for certain spells or Geno Boost.  We don't want those to ever be able to miss.
        if not isinstance(spell, (spells.GenoBoost, spells.Therapy, spells.GroupHug, spells.HPRain, spells.Recover,
                                  spells.MegaRecover, spells.Shredder, spells.Psychopath)):
            # If the spell is instant death, cap hit rate at 99% so items that protect from this actually work.
            # Protection forces the attack to miss, but 100% hit rate can't "miss" so it hits anyway.
            if spell.instant_ko:
                max_hit_rate = 99
            else:
                max_hit_rate = 100
            spell.hit_rate = utils.mutate_normal(
                spell.hit_rate, minimum=1, maximum=max_hit_rate)

    if world.settings.is_flag_enabled(flags.CharacterSpellElements) and spell.index in [0, 1, 2, 3, 4, 5, 21, 24, 25]:
        spell.element = random.choice(
            [Element.ICE, Element.THUNDER, Element.FIRE, Element.JUMP])

        new_name = spell.base_title
        if spell.index == 0 and spell.element != Element.JUMP:
            if spell.element == Element.ICE:
                new_name = "Ice Jump"
            elif spell.element == Element.THUNDER:
                new_name = "Thunder Jump"
            elif spell.element == Element.FIRE:
                new_name = "Fire Jump"
        elif spell.index == 2 and spell.element != Element.JUMP:
            if spell.element == Element.ICE:
                new_name = "Ice S.Jump"
            elif spell.element == Element.THUNDER:
                new_name = "Thndr S.Jump"
            elif spell.element == Element.FIRE:
                new_name = "Fire S.Jump"
        elif spell.index == 4 and spell.element != Element.JUMP:
            if spell.element == Element.ICE:
                new_name = "Ice U.Jump"
            elif spell.element == Element.THUNDER:
                new_name = "Thndr U.Jump"
            elif spell.element == Element.FIRE:
                new_name = "Fire U.Jump"
        if spell.index == 1 and spell.element != Element.FIRE:
            if spell.element == Element.ICE:
                new_name = "Ice Orb"
            elif spell.element == Element.THUNDER:
                new_name = "Thunder Orb"
            elif spell.element == Element.JUMP:
                new_name = "Earth Orb"
        elif spell.index == 3 and spell.element != Element.FIRE:
            if spell.element == Element.ICE:
                new_name = "Super Ice"
            elif spell.element == Element.THUNDER:
                new_name = "SuperThunder"
            elif spell.element == Element.JUMP:
                new_name = "Super Earth"
        elif spell.index == 5 and spell.element != Element.FIRE:
            if spell.element == Element.ICE:
                new_name = "Ultra Ice"
            elif spell.element == Element.THUNDER:
                new_name = "UltraThunder"
            elif spell.element == Element.JUMP:
                new_name = "Ultra Earth"
        elif spell.index == 21 and spell.element != Element.THUNDER:
            if spell.element == Element.ICE:
                new_name = "Icebolt"
            elif spell.element == Element.FIRE:
                new_name = "Firebolt"
            elif spell.element == Element.JUMP:
                new_name = "Earthbolt"
        elif spell.index == 24 and spell.element != Element.THUNDER:
            if spell.element == Element.ICE:
                new_name = "Ice Shocker"
            elif spell.element == Element.FIRE:
                new_name = "Fire Shocker"
            elif spell.element == Element.JUMP:
                new_name = "EarthShocker"
        elif spell.index == 25 and spell.element != Element.ICE:
            if spell.element == Element.THUNDER:
                new_name = "Thundery"
            elif spell.element == Element.FIRE:
                new_name = "Firey"
            elif spell.element == Element.JUMP:
                new_name = "Earthy"
        spell.title = new_name


def _randomize_spell_casting(world):
    for enemy in world.enemies:
        script = enemy.script
        for i in range(len(script)):
            command, args = script[i]
            if command != 'cast_spell':
                continue
            new_args = []
            for arg in args:
                possible_spells = [spell for spell in spells.SpellsToTargets[getattr(
                    arg, 'index', arg)] if spell.fp <= enemy.fp]
                # This should probably never happen...probably.
                if not possible_spells:
                    possible_spells = [arg]
                new_args.append(random.choice(possible_spells).index)
            script[i] = command, new_args


def randomize_all(world):
    """Randomize everything for spells for a single seed.

    :type world: randomizer.logic.main.GameWorld
    """
    # Randomize spell stats.
    for spell in world.spells:
        if isinstance(spell, spells.CharacterSpell):
            _randomize_spell(world, spell)

    if world.settings.is_flag_enabled(flags.CharacterSpellStats):
        # Randomize starting FP if we're randomizing spell stats.
        world.starting_fp = utils.mutate_normal(
            world.starting_fp, minimum=1, maximum=99)

    # Randomize enemy spells.
    if world.settings.is_flag_enabled(flags.EnemyAttacks):
        for spell in world.spells:
            if isinstance(spell, spells.EnemySpell):
                _randomize_spell(world, spell)

    if world.settings.is_flag_enabled(flags.EnemySpells):
        _randomize_spell_casting(world)

    # If we're generating a debug mode seed for testing, set max FP to start.
    if world.debug_mode:
        world.starting_fp = 99

    # Attack Scarf threshold
    value = world.settings.get_flag(flags.SuperJump1Threshold).value
    world.eventscripts[3393][0]["args"] = [value]
    world.search_replace_dialog('`SUPER_JUMP_PRIZE_1_CAP`', '%i' % value)

    # Super Suit threshold
    value = world.settings.get_flag(flags.SuperJump2Threshold).value
    if value <= world.settings.get_flag(flags.SuperJump1Threshold).value:
        raise Exception("2nd super jump threshold must be higher than 1st")
    world.eventscripts[3394][0]["args"] = [value]
    world.search_replace_dialog('`SUPER_JUMP_PRIZE_2_CAP`', '%i' % value)
