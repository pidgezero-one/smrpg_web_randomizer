"""Give each ally the EXP their starting level is worth.

Allies recruited above level 1 (Mushroom Way at 2, Forest Maze at 6, Inner Mines
at 8, Marrymore at 9, or anything at 30 under GODMODE) otherwise join holding 0
EXP, so the game shows them owing the whole climb from level 1 to their next
level instead of just the remainder.

Order is load-bearing. This must run AFTER:

* ``calibrate_character_base_stats``, which sets ``starting_level`` from the
  recruitment location the ally was shuffled into;
* ``randomize_character_stats`` / ``randomize_levelup_xps``, which re-roll both
  ``starting_level`` and the ``exp_needed`` curve when CharacterStats is on;
* ``apply_debug_max_stats``, which pins level 30.

Reading the final level against the final curve keeps the two consistent no
matter which of those ran.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld


def apply_starting_experience(world: GameWorld) -> None:
    """Set every ally's starting EXP to the threshold for their starting level."""
    for ally in world.allies._allies:
        # levels[] covers 2-30, so a level-1 ally matches nothing and keeps 0.
        ally.starting_experience = max(
            (
                level_up.exp_needed
                for level_up in ally.levels
                if level_up.level <= ally.starting_level
            ),
            default=0,
        )


__all__ = ["apply_starting_experience"]
