"""When the win condition is "Beat Smithy", the SmithyBossFight must be the last
accessibility-relevant prize placed.

Beating Smithy ends the game instantly (WinConditions.SMITHY), so nothing is ever
gated behind him. shuffle_prizes() therefore pulls his fight out of the tier pool
and places it in a dedicated pass that runs after PROGRESSION, RESTRICTED and
MANDATORY -- just before the LOW_PRIORITY filler pass, which unlocks nothing. Every
other location is thus filled and proven reachable without beating Smithy, so his
slot can block nothing. If an attempt leaves only a stranding slot for him, the pass
raises PlacementException and _shuffle_items re-rolls.

Only fires when Smithy is actually in the boss pool (BossShuffle on); otherwise he
keeps his vanilla location and the deferral is a no-op.
"""

import pytest

import randomizer.main as main
import randomizer.logic.shufflers.items as items_mod
from randomizer.logic.progression.prizes import SmithyBossFight
from randomizer.types.flags import BossShuffle, WinCondition, WinConditions
from randomizer.types.prizelocation import BossFightLocation
from randomizer.types.settings import Settings

SEED = 3097306894


def test_smithy_is_placed_in_a_dedicated_final_pass(monkeypatch):
    # Spy on place(): the deferral is the ONLY thing that ever calls place() with a
    # to_place list of exactly one SmithyBossFight. Without it, Smithy rides along in
    # pool[PROGRESSION_PRIZES] and this call never happens -- so this assertion fails
    # if the deferral is removed (non-vacuous guard).
    real_place = items_mod.place
    dedicated_smithy_passes: list[list] = []

    def spy(world, to_place, **kwargs):
        if len(to_place) == 1 and isinstance(to_place[0], SmithyBossFight):
            dedicated_smithy_passes.append(list(to_place))
        return real_place(world, to_place, **kwargs)

    monkeypatch.setattr(items_mod, "place", spy)

    settings = Settings()
    settings.get_flag(BossShuffle).enable()
    settings.get_flag(WinCondition).select(WinConditions.SMITHY)
    world = main.create(SEED, settings)

    assert dedicated_smithy_passes, (
        "SmithyBossFight was not placed by its own trailing pass -- the "
        "WinConditions.SMITHY deferral did not run"
    )

    # 1:1 boss-prize -> boss-location is preserved: Smithy placed exactly once...
    smithy_locations = [
        type(loc).__name__
        for loc in world.locations.values()
        if isinstance(loc.prize, SmithyBossFight)
    ]
    assert len(smithy_locations) == 1, f"Smithy placements: {smithy_locations}"

    # ...and deferring him stranded no boss slot.
    empty_boss_slots = [
        type(loc).__name__
        for loc in world.locations.values()
        if isinstance(loc, BossFightLocation) and not loc.has_item
    ]
    assert not empty_boss_slots, f"boss slots left empty: {empty_boss_slots}"
