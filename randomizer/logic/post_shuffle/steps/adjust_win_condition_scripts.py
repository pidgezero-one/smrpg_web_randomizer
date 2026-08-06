"""Adjust ending scripts for the selected win condition.

Extracted from the apply_shuffler_results orchestrator.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from randomizer.logic.progression.prizelocations import (FinalBossFight, MonstroSealedDoorBossFight)
from randomizer.logic.progression.prizes import (SmithyBossFight)
from randomizer.types.flags import (WinCondition, WinConditions)
from smrpgpatchbuilder.datatypes.battle_animation_scripts.commands import (
    UseObjectQueueAtOffsetWithAMEM60Index,
)

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld



def adjust_win_condition_scripts(world: GameWorld) -> None:
    if not world.settings.is_flag_value(
        WinCondition, WinConditions.SMITHY
    ):
        if world.settings.is_flag_value(WinCondition, WinConditions.SEALED) and isinstance(world.get_location(MonstroSealedDoorBossFight).prize, SmithyBossFight):
            world.battle_animations[0x3A].delete_command_by_name("smithy_defeated_ending_effect_amem")
        elif world.settings.is_flag_value(WinCondition, WinConditions.FACTORY) and isinstance(world.get_location(FinalBossFight).prize, SmithyBossFight):
            world.battle_animations[0x3A].delete_command_by_name("smithy_defeated_ending_effect_amem")
        else:
            world.battle_animations[0x3A].replace_command_by_name(
                "smithy_defeated_ending_effect",
                UseObjectQueueAtOffsetWithAMEM60Index(destinations=["smithy_non_ending_oq_outer"], identifier="smithy_defeated_ending_effect"),
            )
    else:
        world.battle_animations[0x3A].delete_command_by_name("smithy_defeated_ending_effect_amem")


__all__ = ['adjust_win_condition_scripts']
