"""place() must not give up on a stall a single swap can undo.

place() is first-fit with no backtracking: it picks a location for each item and
never reconsiders. So a perfectly legal assignment can be unreachable purely
because an earlier pick took the only location a later item could have used --
the classic trap being a permissive location consumed by an item that had
alternatives, stranding the item that had none.

_try_repair runs only where place() would otherwise raise, and only on the
last-resort attempt build_world spends after the ordinary retry budget is gone.
That gate is what keeps existing seeds intact: without it, any seed that today
succeeds on retry #2 would instead be rescued on attempt #1 and produce a
different game. (Measured, not assumed -- seed 7 with ShuffleItems changed
placement digest 8a068448 -> 21ddfeff when the repair ran ungated.)

These tests pin the properties that make the repair safe:
  * it un-sticks the trap above,
  * it leaves the world untouched when no swap helps,
  * it consumes no randomness, so a failed repair leaves the random stream --
    and therefore every downstream retry -- exactly where it was,
  * place() does not touch it unless the last-resort switch is armed.

The locations here override can_access/can_accept outright, so the heavyweight
PrizeLocation base (and the real GameWorld it needs) never runs.
"""
import os
import random

import django
import pytest

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smrpg_web_randomizer.settings")
django.setup()

from randomizer.logic import placement  # noqa: E402
from randomizer.logic.placement import PlacementException, _try_repair, place  # noqa: E402
from randomizer.types.logic import Inventory  # noqa: E402
from randomizer.types.prize import Prize  # noqa: E402
from randomizer.types.prizelocation import PrizeLocation  # noqa: E402


class RedPrize(Prize):
    pass


class BluePrize(Prize):
    pass


class GreenPrize(Prize):
    pass


class FakeLocation(PrizeLocation):
    """A location that accepts a fixed set of prize types and is always reachable."""

    def __init__(self, accepts: tuple[type[Prize], ...]) -> None:
        self._prize = None
        self._accepts = accepts

    def can_access(self, inventory: Inventory, world: "FakeWorld") -> bool:
        return True

    def can_accept(
        self, prize: Prize, inventory: Inventory, world: "FakeWorld"
    ) -> bool:
        return isinstance(prize, self._accepts)


class FakeSettings:
    """place() only asks settings whether to print its failure diagnostics."""

    debug_mode: bool = False


class FakeWorld:
    """The repair only reaches world.locations; place() also reads the switch."""

    def __init__(self, locations: list[FakeLocation]) -> None:
        self.locations = {i: loc for i, loc in enumerate(locations)}
        self.settings = FakeSettings()
        self.allow_placement_repair = False


def _trap() -> tuple[FakeLocation, FakeLocation, BluePrize, FakeWorld]:
    """The first-fit trap: the only Blue-capable location already holds Blue."""
    permissive = FakeLocation((RedPrize, BluePrize))
    blue_only = FakeLocation((BluePrize,))
    blue = BluePrize()
    permissive.set_prize(blue)
    return permissive, blue_only, blue, FakeWorld([permissive, blue_only])


def test_repair_frees_a_taken_location_for_a_stalled_item():
    permissive, blue_only, blue, world = _trap()
    pending: list[Prize] = [RedPrize()]

    assert _try_repair(world, pending, [permissive, blue_only], None) is True

    assert pending == []
    assert isinstance(permissive.prize, RedPrize)
    assert blue_only.prize is blue


def test_repair_leaves_the_world_untouched_when_no_swap_helps():
    permissive, blue_only, blue, world = _trap()
    # Nothing accepts Green, so no swap can help.
    pending: list[Prize] = [GreenPrize()]

    assert _try_repair(world, pending, [permissive, blue_only], None) is False

    assert len(pending) == 1
    assert permissive.prize is blue
    assert blue_only.prize is None


def test_repair_consumes_no_randomness():
    """A failed repair must not shift the random stream the retry loop depends on."""
    permissive, blue_only, _, world = _trap()
    random.seed(20260803)
    before = random.getstate()

    assert _try_repair(world, [GreenPrize()], [permissive, blue_only], None) is False

    assert random.getstate() == before


def test_repair_reports_the_move_through_on_placed():
    """Both halves of the swap must be reported, or bookkeeping goes stale."""
    permissive, blue_only, blue, world = _trap()
    red = RedPrize()
    seen: list[tuple[Prize, PrizeLocation]] = []

    assert (
        _try_repair(world, [red], [permissive, blue_only], lambda p, l: seen.append((p, l)))
        is True
    )

    assert (red, permissive) in seen
    assert (blue, blue_only) in seen


def test_repair_is_bounded():
    """The caps exist so unsolvable input still terminates."""
    assert placement._MAX_REPAIR_STALLS > 0
    assert placement._MAX_REPAIR_VALIDATIONS > 0


def test_place_still_raises_when_the_last_resort_switch_is_off():
    """The seed-compatibility guard: ordinary attempts must behave as before.

    Drop this gate and every seed that currently succeeds on a retry gets
    rescued on an earlier attempt instead, silently changing its game.
    """
    permissive, blue_only, blue, world = _trap()
    world.allow_placement_repair = False

    with pytest.raises(PlacementException):
        place(world, [RedPrize()])

    assert permissive.prize is blue
    assert blue_only.prize is None


def test_place_repairs_once_the_last_resort_switch_is_armed():
    permissive, blue_only, blue, world = _trap()
    world.allow_placement_repair = True

    place(world, [RedPrize()])

    assert isinstance(permissive.prize, RedPrize)
    assert blue_only.prize is blue
