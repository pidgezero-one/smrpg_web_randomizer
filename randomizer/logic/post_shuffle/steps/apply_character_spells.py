"""Assign character spells and their learn levels.

Extracted from the apply_shuffler_results orchestrator.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
import random
from randomizer.logic.progression.prizelocations import (
    BowserSpell1,
    BowserSpell2,
    BowserSpell3,
    BowserSpell4,
    BowserSpell5,
    BowserSpell6,
    GenoSpell1,
    GenoSpell2,
    GenoSpell3,
    GenoSpell4,
    GenoSpell5,
    GenoSpell6,
    MallowSpell1,
    MallowSpell2,
    MallowSpell3,
    MallowSpell4,
    MallowSpell5,
    MallowSpell6,
    MarioSpell1,
    MarioSpell2,
    MarioSpell3,
    MarioSpell4,
    MarioSpell5,
    MarioSpell6,
    ToadstoolSpell1,
    ToadstoolSpell2,
    ToadstoolSpell3,
    ToadstoolSpell4,
    ToadstoolSpell5,
    ToadstoolSpell6,
)
from randomizer.types.flags import (
    BossScaleOptions,
    BossShuffleScaleStats,
    CharacterStats,
    SpellsAnywhere,
)
from randomizer.types.prize import (SpellPrize)
from typing import (cast)

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld



def apply_character_spells(world: GameWorld) -> None:
    # This takes the results of the shuffler and uses them to write the event scripts that grant prizes and launch boss fights, scale boss fight stats, put allies and enemies in the overworld where they've been shuffled to, etc

    # set spells and the levels at which they are learned
    for a in world.allies._allies:
        for l in a.levels:
            l.spell_learned = None
    if world.settings.isflag_enabled(CharacterStats):
        mario_spell_levels = sorted([1, *random.sample(range(2, 21), 5)])
        mallow_spell_levels = sorted([1, *random.sample(range(2, 21), 5)])
        geno_spell_levels = sorted([1, *random.sample(range(2, 21), 5)])
        bowser_spell_levels = sorted([1, *random.sample(range(2, 21), 5)])
        toadstool_spell_levels = sorted([1, *random.sample(range(2, 21), 5)])
    else:
        mario_spell_levels = [1, 3, 6, 10, 14, 18]
        mallow_spell_levels = [1, 3, 6, 10, 14, 18]
        geno_spell_levels = [1, 8, 11, 14, 17, None]
        bowser_spell_levels = [1, 12, 15, 18, None, None]
        toadstool_spell_levels = [1, 6, 11, 13, 15, 18]
    for char_id, levels, locations in zip(
        range(0, 5),
        [
            mario_spell_levels,
            toadstool_spell_levels,
            bowser_spell_levels,
            geno_spell_levels,
            mallow_spell_levels,
        ],
        [
            [
                MarioSpell1,
                MarioSpell2,
                MarioSpell3,
                MarioSpell4,
                MarioSpell5,
                MarioSpell6,
            ],
            [
                ToadstoolSpell1,
                ToadstoolSpell2,
                ToadstoolSpell3,
                ToadstoolSpell4,
                ToadstoolSpell5,
                ToadstoolSpell6,
            ],
            [
                BowserSpell1,
                BowserSpell2,
                BowserSpell3,
                BowserSpell4,
                BowserSpell5,
                BowserSpell6,
            ],
            [GenoSpell1, GenoSpell2, GenoSpell3, GenoSpell4, GenoSpell5, GenoSpell6],
            [
                MallowSpell1,
                MallowSpell2,
                MallowSpell3,
                MallowSpell4,
                MallowSpell5,
                MallowSpell6,
            ],
        ],
    ):
        ally = world.allies._allies[char_id]
        assert ally is not None
        # Skip spell assignment if SpellsAnywhere is enabled
        # (spells will be found as items in the world instead of learned at level-up)
        if world.settings.isflag_enabled(SpellsAnywhere):
            continue
        for level_num, spell_location in zip(levels, locations):
            if level_num is None:
                continue
            # Spell locations are only added when character spells are shuffled
            if spell_location not in world.locations:
                continue
            level = ally.levels[level_num - 2]
            assert level is not None
            spell_loc = world.get_location(spell_location)
            assert spell_loc is not None
            if spell_loc.prize is not None:
                level.spell_learned = cast(SpellPrize, spell_loc.prize)._spell
                


def apply_godmode_spells(world: GameWorld) -> None:
    # Godmode: grant all spell-slot spells to each character's starting_magic
    # (only when SpellsAnywhere is disabled, since spells are in the world otherwise)
    if (
        world.settings.is_flag_value(BossShuffleScaleStats, BossScaleOptions.GODMODE)
        and not world.settings.isflag_enabled(SpellsAnywhere)
    ):
        all_spell_locations_by_char: list[tuple[int, list[type]]] = [
            (0, [MarioSpell1, MarioSpell2, MarioSpell3, MarioSpell4, MarioSpell5, MarioSpell6]),
            (1, [ToadstoolSpell1, ToadstoolSpell2, ToadstoolSpell3, ToadstoolSpell4, ToadstoolSpell5, ToadstoolSpell6]),
            (2, [BowserSpell1, BowserSpell2, BowserSpell3, BowserSpell4, BowserSpell5, BowserSpell6]),
            (3, [GenoSpell1, GenoSpell2, GenoSpell3, GenoSpell4, GenoSpell5, GenoSpell6]),
            (4, [MallowSpell1, MallowSpell2, MallowSpell3, MallowSpell4, MallowSpell5, MallowSpell6]),
        ]
        for char_id, spell_locs in all_spell_locations_by_char:
            char = world.allies._allies[char_id]
            for spell_loc_type in spell_locs:
                if spell_loc_type not in world.locations:
                    continue
                spell_loc = world.get_location(spell_loc_type)
                if spell_loc is not None and spell_loc.prize is not None:
                    spell = cast(SpellPrize, spell_loc.prize)._spell
                    if spell not in char.starting_magic:
                        char.starting_magic.append(spell)


__all__ = ['apply_character_spells', 'apply_godmode_spells']
