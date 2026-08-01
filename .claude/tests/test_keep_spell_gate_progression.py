"""Bowser's Keep needs a damage spell, so its OWNER must be a PROGRESSION-tier
character.

Every Keep location gates on ``can_pass_obstacle_courses()``, which in vanilla
learned-spell mode is satisfied only by recruiting a character who learns a spell
that damages enemies.

But ``shuffle_rules()`` only promotes a character to the PROGRESSION tier when an
area gate is set to "recruit X". Set every gate to "always open" and none of them
qualifies, so all four land in MANDATORY_INCLUSIONS -- which is filled by a *later*
``place()`` call. For the whole progression pass the inventory therefore holds no
damage spell, the entire Keep is unreachable, and its four BossFightLocations
(ObstacleCourseFinalFight, KeepAfterObstaclesBossFight, KeepChandelierBossFight,
KeepFinalBossFight) can never be filled.

Boss prizes are 1:1 with boss locations and every boss fight is a progression prize,
so exactly four boss fights are stranded -- on every retry, in every seed.

Note: this fixture picks Mario as the sole explicit starter, which was the *worst*
case under the old non-elemental-only rule (all of Mario's spells are elemental).
Since any damaging spell now qualifies, Mario's Jump satisfies the gate on his own,
so this now mainly guards that every boss location still fills. The promotion path
itself is exercised when Mario is excluded or his damage spells are disabled.
See tests/test_damaging_spell_gate.py for the current rule.
"""

import pytest

import randomizer.main as main
from randomizer.logic.placement import collect_accessible_items
from randomizer.logic.progression.prizelocations import (
    can_access_keep,
    can_damage_enemies_with_spells,
)
from randomizer.types.flags import (
    BanditsWayGate,
    BanditsWayGating,
    BoosterTowerGate,
    BoosterTowerGating,
    BossShuffle,
    BowsersKeepGate,
    BowsersKeepGating,
    KeroSewersGate,
    KeroSewersGating,
    Moleville1Gate,
    Moleville1Gating,
    PipeVaultGate,
    PipeVaultGating,
    SeaGate,
    SeaGating,
    ShuffleCharacters,
    StartingCharacterEnum,
    StartingCharacters,
)
from randomizer.types.prizelocation import BossFightLocation
from randomizer.types.settings import Settings

# Every gate that *can* be set to "recruit X". With all of them open, no character is
# gate-required -- exactly the configuration that strands the bosses.
OPEN_GATES = [
    (BanditsWayGate, BanditsWayGating.OPEN),
    (KeroSewersGate, KeroSewersGating.OPEN),
    (PipeVaultGate, PipeVaultGating.OPEN),
    (Moleville1Gate, Moleville1Gating.OPEN),
    (BoosterTowerGate, BoosterTowerGating.OPEN),
    (SeaGate, SeaGating.OPEN),
    (BowsersKeepGate, BowsersKeepGating.OPEN),
]


@pytest.fixture(scope="module")
def world():
    settings = Settings()
    settings.get_flag(ShuffleCharacters).enable()
    settings.get_flag(BossShuffle).enable()

    # Mario as the sole explicit starter: all his spells are elemental, which made
    # him the one character who could never satisfy the old non-elemental-only gate.
    starters = settings.get_flag(StartingCharacters)
    for option in list(starters.enabled):
        starters.disable(option)
    starters.enable(StartingCharacterEnum.Mario)

    for gate, option in OPEN_GATES:
        settings.get_flag(gate).select(option)

    # Raises WorldBuildingException before the fix: four boss fights never place.
    return main.create(3097306894, settings)


def test_bowsers_keep_is_reachable(world):
    inventory = collect_accessible_items(world)
    assert can_access_keep(world, inventory)
    assert can_damage_enemies_with_spells(world, inventory), (
        "no damage spell is ever reachable, so can_pass_obstacle_courses() "
        "is False and every Bowser's Keep location is unfillable"
    )


def test_every_boss_location_is_filled(world):
    empty = [
        type(loc).__name__
        for loc in world.locations.values()
        if isinstance(loc, BossFightLocation) and not loc.has_item
    ]
    assert not empty, f"boss locations left unfilled: {empty}"
