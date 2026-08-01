"""Godmode must scale bosses that stayed on their own location.

`apply_boss_stat_scaling` used to drop every location whose prize was still its
`_originally_held` boss (an unmoved boss) before any mode ran. For GODMODE that
was wrong: an unmoved boss kept vanilla stats instead of being buffed to
endgame level. The moved-only filter now lives per-mode — MATCH/RANDOM still
skip unmoved bosses, GODMODE scales them too.

The two heavy helpers are monkeypatched so the test needs no ROM/world:
- `_calculate_location_stats` -> a fixed valid (HP > 0) tuple
- `_apply_stats_to_prize`      -> records which prizes got scaled
"""

import randomizer.main  # noqa: F401  -- loads the package in an order that breaks a circular import
from randomizer.logic.post_shuffle.steps import calculate_boss_stats as apply
from randomizer.logic.progression.prizelocations import MushrooomWayBossFight
from randomizer.logic.progression.prizes import MackBossFight
from randomizer.types.flags import BossShuffleScaleStats, BossScaleOptions


class _StubSettings:
    def __init__(self, active: BossScaleOptions) -> None:
        self._active = active

    def is_flag_value(self, flag_cls, option) -> bool:
        assert flag_cls is BossShuffleScaleStats
        return option is self._active


class _StubWorld:
    def __init__(self, active: BossScaleOptions, locations) -> None:
        self.settings = _StubSettings(active)
        self.locations = {i: loc for i, loc in enumerate(locations)}


def _run(active: BossScaleOptions, monkeypatch):
    """Return the set of prize types scaled for the given mode.

    Two locations of the same class: one left on its own boss (unmoved) and one
    carrying a different boss (moved).
    """
    unmoved = MushrooomWayBossFight()  # default prize == HammerBrosFight (its own)
    moved = MushrooomWayBossFight()
    moved._prize = MackBossFight()  # different class -> counts as relocated

    assert isinstance(unmoved.prize, unmoved._originally_held)
    assert not isinstance(moved.prize, moved._originally_held)

    scaled: list[type] = []
    monkeypatch.setattr(
        apply, "_calculate_location_stats",
        lambda location, world: (1000, 10, 5, 50, 40, 30, 20, 0, 0),
    )
    monkeypatch.setattr(
        apply, "_apply_stats_to_prize",
        lambda prize, stats, world: scaled.append(type(prize)),
    )

    apply.apply_boss_stat_scaling(_StubWorld(active, [unmoved, moved]))
    return set(scaled)


def test_godmode_scales_unmoved_boss(monkeypatch):
    scaled = _run(BossScaleOptions.GODMODE, monkeypatch)
    # The fix: the unmoved boss (HammerBrosFight on its own spot) is scaled too.
    assert MushrooomWayBossFight._originally_held in scaled
    assert MackBossFight in scaled


def test_match_and_random_still_skip_unmoved(monkeypatch):
    for mode in (BossScaleOptions.MATCH, BossScaleOptions.RANDOM):
        scaled = _run(mode, monkeypatch)
        assert MushrooomWayBossFight._originally_held not in scaled, mode
        assert MackBossFight in scaled, mode


def test_vanilla_scales_nothing(monkeypatch):
    assert _run(BossScaleOptions.VANILLA, monkeypatch) == set()
