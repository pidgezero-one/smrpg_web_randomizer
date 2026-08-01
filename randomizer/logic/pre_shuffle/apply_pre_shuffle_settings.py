"""Settings applied to game data before any shuffling happens.

These five steps run back-to-back and depend only on `world.settings`, so they
are grouped here rather than inlined in GameWorld.__init__. The remaining
pre_shuffle entry points (apply_debug_max_stats, apply_experience_zero_settings,
apply_minigame_settings, set_locations) are NOT called from here -- each is
interleaved with GameWorld instance methods that constrain its position.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from randomizer.data.items.items import SeeYaItem
from randomizer.data.variables.variable_names import (
    FROG_DISCIPLE_ITEM_5_PURCHASED,
    MARIO_DOLL_SHUFFLE_ENABLED,
    PROGRESSIVE_FIREWORKS_ENABLED,
    SHOGUN_1_CLEARED,
    SHOGUN_2_CLEARED,
    SHOGUN_3_CLEARED,
    SHOGUN_4_CLEARED,
    SHOGUN_5_CLEARED,
    SHUFFLE_ONE_FIREWORKS_ENABLED,
    SKIP_MANDATORY_MINECART,
)
from randomizer.logic.pre_shuffle.enemy_tweaks import apply_enemy_tweaks
from randomizer.logic.pre_shuffle.equipment_setup import apply_equipment_settings
from randomizer.logic.pre_shuffle.item_protection import apply_item_protection
from randomizer.logic.pre_shuffle.pre_shuffler_settings import (
    apply_shuffler_independent_settings,
)
from randomizer.logic.pre_shuffle.thresholds import apply_threshold_settings
from randomizer.logic.progression.prizelocations import (E0091_INVISIBLE_ITEM_SUMMONER, E2496_START_GAME)
from randomizer.types.flags import (
    FireworksOptions,
    FireworksSetting,
    SeeYa,
    ShuffleItems,
    ShuffleMarioDoll,
    ShuffleShops,
    SkipAnts,
    SkipMinecart,
    SkipMustyFearsSequence,
)
from randomizer.utils.event_script_snippets.tower_access_scripts import AddToInventory
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    RunEventAsSubroutine,
    SetBit,
)

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld


def _set_startup_event_flags(world: GameWorld) -> None:
    """Settings-driven bits prepended to the E2496 game-start event script.

    Must run FIRST: event_2496_startup is an ordered accumulator, and in
    GameWorld.__init__ these bits were appended before
    apply_shuffler_independent_settings added its own.
    """
    if world.settings.isflag_enabled(SkipMustyFearsSequence):
        world.event_scripts.get_script_by_id(E2496_START_GAME).insert_after_identifier("EVENT_2496_flag_setup", RunEventAsSubroutine(E0091_INVISIBLE_ITEM_SUMMONER))

    if world.settings.isflag_enabled(SkipMinecart):
        world.event_2496_startup += [
            SetBit(SKIP_MANDATORY_MINECART),
        ]
    if world.settings.is_flag_value(FireworksSetting, FireworksOptions.PROGRESSIVE):
        world.event_2496_startup += [
            SetBit(PROGRESSIVE_FIREWORKS_ENABLED),
        ]
    elif world.settings.is_flag_value(FireworksSetting, FireworksOptions.SHUFFLE_ONE):
        world.event_2496_startup += [
            SetBit(SHUFFLE_ONE_FIREWORKS_ENABLED),
        ]
    if world.settings.isflag_enabled(SeeYa):
        world.event_2496_startup += [
            AddToInventory(SeeYaItem),
        ]
        # Pre-set the 5th Frog Disciple sale bit whenever SeeYa shrinks the
        # shop to 4 items — i.e. any time it is NOT fully shuffled (shops off
        # OR items off). If both are shuffled the shop keeps 5 items and the
        # bit must stay clear. This MUST match the FrogDiscipleLocation1
        # removal predicate in prize_locations.py; a 4-item shop with the bit
        # unset leaves an empty 5th slot that opens a glitched menu.
        if not (
            world.settings.isflag_enabled(ShuffleShops)
            and world.settings.isflag_enabled(ShuffleItems)
        ):
            world.event_2496_startup += [
                SetBit(FROG_DISCIPLE_ITEM_5_PURCHASED),
            ]
    if world.settings.isflag_enabled(SkipAnts):
        world.event_2496_startup += [
            SetBit(SHOGUN_1_CLEARED),
            SetBit(SHOGUN_2_CLEARED),
            SetBit(SHOGUN_3_CLEARED),
            SetBit(SHOGUN_4_CLEARED),
            SetBit(SHOGUN_5_CLEARED),
        ]
    if world.settings.isflag_enabled(ShuffleMarioDoll):
        world.event_2496_startup += [
            SetBit(MARIO_DOLL_SHUFFLE_ENABLED),
        ]


def apply_pre_shuffle_settings(world: GameWorld) -> None:
    # Startup event flags -- must precede apply_shuffler_independent_settings,
    # which appends to the same ordered accumulator.
    _set_startup_event_flags(world)

    # Apply progression gating settings (win conditions, area gates, travel)
    apply_shuffler_independent_settings(world)

    # Apply threshold adjustments
    apply_threshold_settings(world)

    # Apply enemy and combat tweaks
    apply_enemy_tweaks(world)

    # Apply equipment and spell element settings
    apply_equipment_settings(world)

    # Mark player-chosen items as unsellable
    apply_item_protection(world)


__all__ = ["apply_pre_shuffle_settings"]
