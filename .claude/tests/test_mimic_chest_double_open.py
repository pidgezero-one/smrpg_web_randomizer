"""A mimic host chest only stays hittable twice if the reload check holds a prize.

`TreasureChestLocation.grant()` prepends `JmpIfBitClear(MIMIC_n_CLEARED, ...)` to the
chest-disable block so the first open (mimic not yet beaten) skips the disable and the
chest can be hit again after a room reload. That second hit is
`Mimic1ReloadRewardLocation` / `Mimic2ReloadRewardLocation`. If those hold nothing, the
extra trip is a walk to an empty chest, so the guard must not be emitted and the chest
disables on the first open.
"""

import pytest
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    JmpIfBitClear,
)

from randomizer import main
from randomizer.logic.progression.prizelocations import (
    Mimic1ReloadRewardLocation,
    Mimic2ReloadRewardLocation,
)
from randomizer.logic.progression.prizes import (
    FirstMimicFightLauncher,
    SecondMimicFightLauncher,
)
from randomizer.types.gameworld import Settings
from randomizer.types.prizelocation import TreasureChestLocation


@pytest.fixture(scope="module")
def world():
    return main.create(seed=20260720, settings=Settings())


def _host_chest(world, launcher: type) -> TreasureChestLocation:
    host = next(
        (
            loc
            for loc in world.locations.values()
            if isinstance(loc, TreasureChestLocation) and isinstance(loc.prize, launcher)
        ),
        None,
    )
    assert host is not None, f"{launcher.__name__} is not in a chest this seed"
    return host


def _guards(world, host: TreasureChestLocation) -> int:
    return sum(1 for c in host.grant(world).contents if isinstance(c, JmpIfBitClear))


@pytest.mark.parametrize(
    "launcher,reload_location",
    [
        (FirstMimicFightLauncher, Mimic1ReloadRewardLocation),
        (SecondMimicFightLauncher, Mimic2ReloadRewardLocation),
    ],
)
def test_double_open_guard_tracks_reload_prize(world, launcher, reload_location):
    host = _host_chest(world, launcher)
    reload_loc = world.locations[reload_location]
    original = reload_loc.prize

    assert original is not None, "seed placed nothing in the reload check"
    assert _guards(world, host) == 1, "filled reload check lost its double-open guard"

    reload_loc.set_prize(None)
    try:
        assert _guards(world, host) == 0, "empty reload check still sends the player back"
    finally:
        reload_loc.set_prize(original)
