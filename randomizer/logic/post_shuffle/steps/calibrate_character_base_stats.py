"""Calibrate character base stats to where they were recruited.

Extracted from the apply_shuffler_results orchestrator.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from randomizer.logic.progression.prizelocations import (
    ForestMazeCharacter,
    InnerMinesCharacter,
    MarrymoreCharacter,
    MushroomWayCharacter,
    StartingCharacter1,
    StartingCharacter2,
    StartingCharacter3,
    StartingCharacter4,
    StartingCharacter5,
)
from randomizer.types.flags import (
    BossScaleOptions,
    BossShuffleScaleStats,
    CharacterLearnedSpells,
    SpellsAnywhere,
)
from randomizer.types.prize import (CharacterPrize)
from randomizer.types.prizelocation import (CharacterRecruitmentLocation)
from typing import (cast)

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld



def calibrate_character_base_stats(world: GameWorld) -> None:
    # set starting stats based on where the character is recruited
    for l in [
        StartingCharacter1,
        StartingCharacter2,
        StartingCharacter3,
        StartingCharacter4,
        StartingCharacter5,
        MushroomWayCharacter,
        ForestMazeCharacter,
        InnerMinesCharacter,
        MarrymoreCharacter,
    ]:
        # StartingCharacter2-5 are only added when multiple starting characters are enabled
        if l not in world.locations:
            continue
        loc = cast(CharacterRecruitmentLocation, world.get_location(l))
        if loc.prize is not None:
            charp = cast(CharacterPrize, loc.prize)
            level = charp.starting_level
            if world.settings.is_flag_value(BossShuffleScaleStats, BossScaleOptions.GODMODE):
                level = 30
            ally = charp.ally
            id = ally.index
            char = world.allies._allies[id]
            char.starting_level = level
            # When SpellsAnywhere is enabled, characters don't start with or learn any spells
            # (spells are found as items in the world instead)
            if world.settings.isflag_enabled(SpellsAnywhere):
                char.starting_magic = []
            # When spell shuffling is enabled (but not SpellsAnywhere), rebuild from scratch
            elif world.settings.isflag_enabled(CharacterLearnedSpells):
                char.starting_magic = []
            else:
                # Keep original starting_magic (level-1 spells like Jump)
                char.starting_magic = list(char.starting_magic)
            # Apply stat bonuses from level-ups (and add spells if not SpellsAnywhere)
            for lv in range(0, level - 1):
                lvlup = char.levels[lv]
                # Only add spells from level-ups if SpellsAnywhere is disabled
                if not world.settings.isflag_enabled(SpellsAnywhere):
                    if lvlup.spell_learned is not None and lvlup.spell_learned not in char.starting_magic:
                        char.starting_magic.append(lvlup.spell_learned)
                char.starting_max_hp += lvlup.hp_plus
                char.starting_current_hp = char.starting_max_hp
                char.starting_attack += lvlup.attack_plus
                char.starting_defense += lvlup.defense_plus
                char.starting_mg_attack += lvlup.mg_attack_plus
                char.starting_mg_defense += lvlup.mg_defense_plus
                if (lv + 2) % 3 == 0:
                    char.starting_attack += lvlup.attack_plus_bonus
                    char.starting_defense += lvlup.defense_plus_bonus
                elif (lv + 2) % 3 == 1:
                    char.starting_max_hp += lvlup.hp_plus_bonus
                    char.starting_current_hp = char.starting_max_hp
                else:
                    char.starting_mg_attack += lvlup.mg_attack_plus_bonus
                    char.starting_mg_defense += lvlup.mg_defense_plus_bonus


__all__ = ['calibrate_character_base_stats']
