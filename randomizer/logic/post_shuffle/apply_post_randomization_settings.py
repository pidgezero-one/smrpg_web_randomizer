"""Settings applied after enemy/character randomization, before cosmetics.

These four steps ran back-to-back in GameWorld.__init__ after the shuffle retry
loop and all the _randomize_* passes. Order is load-bearing:

* debug max stats first, so it overrides everything randomization produced;
* the EXP multiplier next, since it scales the randomized XP values;
* zero-XP settings AFTER all XP manipulation, so the 0-XP flags win;
* minigame settings last.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from randomizer.logic.post_shuffle.steps.debug_max_stats import apply_debug_max_stats
from randomizer.logic.post_shuffle.steps.experience_zero import (
    apply_experience_zero_settings,
)
from randomizer.logic.post_shuffle.steps.minigames_setup import apply_minigame_settings
from randomizer.logic.shufflers.enemies import apply_exp_multiplier

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld


def apply_post_randomization_settings(world: GameWorld) -> None:
    # Debug mode max stats, applied after all character randomization so debug
    # stats override everything.
    apply_debug_max_stats(world)

    apply_exp_multiplier(world)

    # AFTER all XP manipulation, so the 0 XP flags take precedence over
    # randomization.
    apply_experience_zero_settings(world)

    apply_minigame_settings(world)


__all__ = ["apply_post_randomization_settings"]
