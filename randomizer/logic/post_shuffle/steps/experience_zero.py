"""Force zero-XP settings. Runs AFTER all XP manipulation."""

from __future__ import annotations
from typing import TYPE_CHECKING
from randomizer.data.variables.pack_names import *
from randomizer.data.enemies.enemies import (KINGBOMBEnemy)
from randomizer.types.flags import ExperienceNoBosses, ExperienceNoRegular
from randomizer.logic.pre_shuffle.enemy_tweaks import _get_enemy_lists
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


def apply_experience_zero_settings(world: GameWorld) -> None:
    """Apply experience zero settings for bosses and/or regular enemies.

    This must run AFTER all enemy stat randomization/scaling to ensure
    the 0 XP setting takes precedence over any randomization.
    """

    sidekicks, bosses = _get_enemy_lists()

    if world.settings.isflag_enabled(ExperienceNoBosses):
        for enemy_type in bosses + sidekicks:
            enemy = world.enemies.get_by_type(enemy_type)
            enemy.set_xp(0)

    if world.settings.isflag_enabled(ExperienceNoRegular):
        for enemy_type in [
            type(e)
            for e in world.enemies.enemies
            if type(e) not in bosses + sidekicks
        ]:
            world.enemies.get_by_type(enemy_type).set_xp(0)


__all__ = ["apply_experience_zero_settings"]
