"""Build a randomized GameWorld: the top-level pipeline.

Extracted from types/gameworld.py.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
import hashlib
import json
import re
from randomizer.logic.post_shuffle.apply_shuffler_results import (
    apply_shuffler_results_to_game_data,
)
from randomizer.logic.post_shuffle.steps.debug_max_stats import (apply_debug_max_stats)
from randomizer.logic.pre_shuffle.prize_locations import (set_locations)
from randomizer.logic.shufflers.items import (post_shuffle_cleanup, shuffle_prizes)
from randomizer.logic.solvability import (SettingsRelaxed, assert_solvable, relax_deadlocked_gates)
import random
from copy import (deepcopy)
from randomizer.data.items.definitions.able_juice_item import (AbleJuiceItem)
from randomizer.data.items.definitions.bad_mushroom_item import (BadMushroomItem)
from randomizer.data.items.definitions.bracer_item import (BracerItem)
from randomizer.data.items.definitions.crystalline_item import (CrystallineItem)
from randomizer.data.items.definitions.elixir_item import (ElixirItem)
from randomizer.data.items.definitions.energizer_item import (EnergizerItem)
from randomizer.data.items.definitions.fire_bomb_item import (FireBombItem)
from randomizer.data.items.definitions.flower_box_item import (FlowerBoxItem)
from randomizer.data.items.definitions.flower_jar_item import (FlowerJarItem)
from randomizer.data.items.definitions.flower_tab_item import (FlowerTabItem)
from randomizer.data.items.definitions.freshen_up_item import (FreshenUpItem)
from randomizer.data.items.definitions.fright_bomb_item import (FrightBombItem)
from randomizer.data.items.definitions.froggie_drink_item import (FroggieDrinkItem)
from randomizer.data.items.definitions.honey_syrup_item import (HoneySyrupItem)
from randomizer.data.items.definitions.ice_bomb_item import (IceBombItem)
from randomizer.data.items.definitions.kerokero_cola_item import (KerokeroColaItem)
from randomizer.data.items.definitions.maple_syrup_item import (MapleSyrupItem)
from randomizer.data.items.definitions.max_mushroom_item import (MaxMushroomItem)
from randomizer.data.items.definitions.megalixir_item import (MegalixirItem)
from randomizer.data.items.definitions.mid_mushroom_item import (MidMushroomItem)
from randomizer.data.items.definitions.moldy_mush_item import (MoldyMushItem)
from randomizer.data.items.definitions.muku_cookie_item import (MukuCookieItem)
from randomizer.data.items.definitions.mushroom_item import (MushroomItem)
from randomizer.data.items.definitions.mushroom_item_2 import (MushroomItem2)
from randomizer.data.items.definitions.pick_me_up_item import (PickMeUpItem)
from randomizer.data.items.definitions.power_blast_item import (PowerBlastItem)
from randomizer.data.items.definitions.pure_water_item import (PureWaterItem)
from randomizer.data.items.definitions.red_essence_item import (RedEssenceItem)
from randomizer.data.items.definitions.rock_candy_item import (RockCandyItem)
from randomizer.data.items.definitions.rotten_mush_item import (RottenMushItem)
from randomizer.data.items.definitions.royal_syrup_item import (RoyalSyrupItem)
from randomizer.data.items.definitions.sleepy_bomb_item import (SleepyBombItem)
from randomizer.data.items.definitions.wilt_shroom_item import (WiltShroomItem)
from randomizer.data.items.definitions.yoshi_ade_item import (YoshiAdeItem)
from randomizer.data.items.definitions.yoshi_candy_item import (YoshiCandyItem)
from randomizer.data.items.definitions.yoshi_cookie_item import (YoshiCookieItem)
from randomizer.logic.placement import (PlacementException)
from randomizer.logic.post_shuffle.apply_post_randomization_settings import (
    apply_post_randomization_settings,
)
from randomizer.logic.post_shuffle.cosmetics import (apply_cosmetic_settings)
from randomizer.logic.post_shuffle.steps.enemy_hp_thresholds import (_update_enemy_hp_thresholds)
from randomizer.logic.pre_shuffle.apply_pre_shuffle_settings import (apply_pre_shuffle_settings)
from randomizer.logic.shufflers.characters import (
    randomize_character_spell_stats,
    randomize_character_stats,
    randomize_levelup_xps,
)
from randomizer.logic.shufflers.enemies import (
    randomize_enemy_attacks_and_spells,
    randomize_enemy_drops,
    randomize_enemy_formations,
    randomize_enemy_stats,
)
from randomizer.logic.shufflers.equipment import (
    build_item_impact_categories,
    build_item_to_prize_mapping,
)
from randomizer.logic.shufflers.shops import (exclude_seeya_from_frog_disciple, shuffle_shops)
from randomizer.logic.validation import (validate_settings)
from randomizer.types.flags import (
    CharacterSpellStats,
    CharacterStats,
    EnemyAttacks,
    EnemyDrops,
    EnemyFormations,
    SeeYa,
    ShuffleShops,
)
from randomizer.types.world_errors import WorldBuildingException
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    RunEventAsSubroutine,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (
    UsableEventScriptCommand,
)
from randomizer.logic.post_shuffle.finalize_world import finalize_world

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld


def _rebuild_hash(world: GameWorld):
    """Build hash value for choosing file select character and file name hash.
    Use the same version, seed, mode, and flags used for the database hash.
    """
    final_seed = bytearray()
    final_seed += world.version.encode("utf-8")
    if isinstance(world.seed, int):
        final_seed += world.seed.to_bytes(4, "big")
    else:
        final_seed += str(world.seed).encode("utf-8")
    final_seed += world.settings.flag_string.encode("utf-8")
    world.hash = hashlib.md5(final_seed).hexdigest()

    # Possible names we can use for the hash values on the file select screen.  Needs to be 6 characters or less.
    file_entry_names = {
        "MARIO",
        "MALLOW",
        "GENO",
        "BOWSER",
        "PEACH",
    }
    # Also use enemy names, if they're 6 characters or less.
    e_choices = set(
        [
            re.sub(r"[^A-Za-z9]", "", e.name.upper())
            for e in world.enemies.enemies
            if len(re.sub(r"[^A-Za-z9]", "", e.name.upper())) <= 6
        ]
    )
    file_entry_names = sorted(e_choices)

    # Replace file select names with "hash" values for seed verification.
    world.file_select_names = [
        file_entry_names[int(world.hash[0:8], 16) % len(file_entry_names)],
        file_entry_names[int(world.hash[8:16], 16) % len(file_entry_names)],
        file_entry_names[int(world.hash[16:24], 16) % len(file_entry_names)],
        file_entry_names[int(world.hash[24:32], 16) % len(file_entry_names)],
    ]


def _shuffle_items(world: GameWorld):

    world._report_progress("Shuffling checks...", 10)

    # determine which checks exist in this seed
    # this doesn't mean which ones are shuffled, it means which ones can be accessed at all
    # exclusions would be things like remake checks, surplus invisible item checks, super jump prizes when super jump not usable
    set_locations(world)

    # Offsets override every other placement setting, but the gate flags
    # still evaluate against the bosses the offset pinned — so a gate can
    # demand a boss the offset locked inside the region that gate guards.
    # Open only the gates that actually deadlock, then bail out: the gates
    # were already turned into ROM state by apply_shuffler_independent_settings,
    # so the world has to be rebuilt for the change to reach the game and not
    # just the placer. create() catches this and rebuilds once.
    changes = relax_deadlocked_gates(world)
    if changes:
        for message in changes:
            world.settings.force_override(message)
        raise SettingsRelaxed(changes)

    # If a gate cycle still seals part of the world, no seed can win. Say so
    # now instead of burning retries and then blaming "excluded locations".
    assert_solvable(world)

    # shuffle according to settings
    shuffle_prizes(world)

    # replace bad items with coins, supplant YouMissed, fill empty locations, etc

    # Write spoiler to JSON file
    with open("spoiler.json", "w") as f:
        json.dump(world.spoiler, f, indent=2, default=str)

    post_shuffle_cleanup(world)


def _apply_shuffle_results(world: GameWorld):
    """Apply shuffle results to game data. Called after successful shuffle."""
    apply_shuffler_results_to_game_data(world)

    # Apply debug mode overrides (must be after apply_shuffler_results_to_game_data)

    apply_debug_max_stats(world)


__all__ = ['_rebuild_hash', '_shuffle_items', '_apply_shuffle_results']


def build_world(world: GameWorld) -> None:
    """Run the full randomization pipeline against a freshly constructed world."""
    # Validate settings combinations before doing anything else
    # This catches invalid combinations early with clear error messages
    validate_settings(world.settings)

    random.seed(world.seed)
    if world.settings.debug_mode:
        print(world.seed)

    world.event_2496_startup: list[UsableEventScriptCommand] = []

    # Apply any settings that might impact the progression shuffler, or that are independent of it.
    apply_pre_shuffle_settings(world)

    # Categorize items by impact.
    # This takes randomized equipment stats into account.
    build_item_impact_categories(world)

    # Build item to prize mapping (used to choose which items will be used in "completely random" item pool)
    build_item_to_prize_mapping(world)
    world.substitute_draw_counts = {}

    # Track placement failure counts to detect likely-unsolvable settings
    # Key = number of unplaced items, Value = count of times this failure occurred
    failure_counts: dict[int, int] = dict()
    MAX_FAILURES_PER_COUNT = 5

    # Save a snapshot of rooms before shuffling so we can restore on retry
    # (shuffle adds invisible items to rooms which would accumulate on retries)
    rooms_snapshot = deepcopy(world.rooms)

    success = False
    while not success:
        try:
            _shuffle_items(world)
            success = True
        except PlacementException as e:
            # Restore rooms to pre-shuffle state before retrying
            world.rooms = deepcopy(rooms_snapshot)
            # Reset dummy indices so _pre_allocate_dummy_npcs reruns with fresh rooms.
            # Also reset _invisible_item_locations so set_locations re-runs the
            # flag-NPC swap loop — otherwise the freshly re-added dummies stay at
            # (0, 0, 0) and the chosen flag NPCs never get written to room data.
            world._slot_dummy_indices = None
            world._flag_dummy_index = None
            world._invisible_item_locations = None
            if world.settings.debug_mode:
                print(f"[DEBUG] Placement failed with {e.unplaced_count} unplaced items, retrying...")

            # Track this failure count
            count = e.unplaced_count
            failure_counts[count] = failure_counts.get(count, 0) + 1

            # Check if any failure count has reached the threshold
            if failure_counts and all(
                v >= MAX_FAILURES_PER_COUNT for v in failure_counts.values()
            ):
                raise WorldBuildingException(
                    f"Item placement appears unsolvable. "
                    f"Repeated failures with the same unplaced item counts: {failure_counts}. "
                    f"The chosen settings with excluded locations may be impossible to solve. "
                    f"Unplaced items on last attempt: {e.unplaced_items}"
                )
        except Exception:
            # Re-raise unexpected exceptions
            raise

    # Do shop shuffling next. Placement can depend on how item/equip impact was judged
    if world.settings.isflag_enabled(ShuffleShops):
        shuffle_shops(world)
    elif world.settings.isflag_enabled(SeeYa):
        exclude_seeya_from_frog_disciple(world)

    if world.settings.isflag_enabled(EnemyAttacks):
        randomize_enemy_attacks_and_spells(world)

    # Modify the game to reflect the placement results
    _apply_shuffle_results(world)

    # Set enemy stats and Psychopath messages
    randomize_enemy_stats(world)

    # Update HP-based AI thresholds proportionately after all stat mutations are complete
    # (i.e. how much HP damage to advance past the Dodo phase in the Valentina fight)
    _update_enemy_hp_thresholds(world)


    if world.settings.isflag_enabled(EnemyDrops):
        randomize_enemy_drops(world)

    if world.settings.isflag_enabled(EnemyFormations):
        randomize_enemy_formations(world)

    # Randomize character stats
    if world.settings.isflag_enabled(CharacterStats):
        randomize_character_stats(world)
        randomize_levelup_xps(world)

    # Randomize character spell stats
    if world.settings.isflag_enabled(CharacterSpellStats):
        randomize_character_spell_stats(world)
    apply_post_randomization_settings(world)

    _rebuild_hash(world)
    world._report_progress("Applying cosmetics...", 40)

    # Apply cosmetic settings (re-seeded for variation between generations)
    apply_cosmetic_settings(world)

    with open("spoiler_after_replacements.json", "w") as f:
        json.dump(world.spoiler, f, indent=2, default=str)

    finalize_world(world)
