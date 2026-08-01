"""Factory conveyor lackeys must not turn northeast when the mook can't face north.

Action scripts 953-956 (Gun Yolk room, R470) drive the drill bits riding the conveyor.
Vanilla walks them northeast up the belt, and the scripts turn the sprite to face that
way first: `A_FaceNortheast(identifier="as_955_factory_lackey_faces_north")` in 955 and
`..._north_2` in the shared 953 loop tail.

FinalBossFight swaps those drill bits for whatever mook henchman the seed rolled. A
henchman whose sprite only has SW/SE sequences (VramStore.DIR2_SWSE, or south and north
sequences that resolve to identical molds — `is_swse_only`) has no north-facing molds to
show, so the turn either draws the south molds while the sprite walks away from the
camera or reads garbage. `render_final_boss_conveyor_lackeys` deletes both turns and
prepends `A_FixedFCoordOn()` to 955/956/954 so the sprite keeps its SE facing for the
whole loop instead. 953 is only ever reached by Jmp from those three, so it inherits the
pinned facing and needs no insert of its own.

The check is conditional: a 4-direction model must leave the scripts untouched.
"""

import pytest
from smrpgpatchbuilder.datatypes.levels.classes import VramStore
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import (
    A_FaceNortheast,
    A_FixedFCoordOn,
)

from randomizer import main
from randomizer.data.physical_objects import henchmen
from randomizer.logic.progression.prizelocations.inner_factory.final_boss_fight import (
    render_final_boss_conveyor_lackeys,
)
from randomizer.types.gameworld import Settings
from randomizer.types.physical_objects import HenchmanNPC
from randomizer.utils.npcs import is_swse_only

# The three scripts a conveyor lackey can be spawned into. 953 is the shared tail.
ENTRY_SCRIPTS = [954, 955, 956]
ALL_SCRIPTS = [953, 954, 955, 956]


@pytest.fixture(scope="module")
def world():
    return main.create(1, Settings())


def _models(world) -> tuple[type[HenchmanNPC], type[HenchmanNPC]]:
    """One henchman model that can only face SW/SE, and one that can face all four."""
    swse: type[HenchmanNPC] | None = None
    full: type[HenchmanNPC] | None = None
    for name in dir(henchmen):
        cls = getattr(henchmen, name)
        if not isinstance(cls, type) or not issubclass(cls, HenchmanNPC):
            continue
        if cls is HenchmanNPC:
            continue
        model = cls()
        sprite = world.sprites.sprites[model.base.sprite_id]
        limited = is_swse_only(sprite) or model.base.directions == VramStore.DIR2_SWSE
        if limited and swse is None:
            swse = cls
        elif not limited and full is None:
            full = cls
    assert swse is not None and full is not None
    return swse, full


def _northeast_turns(world) -> int:
    return sum(
        isinstance(command, A_FaceNortheast)
        for script_id in ALL_SCRIPTS
        for command in world.get_action_script(script_id).contents
    )


def _pinned_facings(world) -> int:
    return sum(
        isinstance(world.get_action_script(script_id).contents[0], A_FixedFCoordOn)
        for script_id in ENTRY_SCRIPTS
    )


def test_conveyor_lackey_turns_depend_on_mook_directions(world):
    """Both cases in one test: the fixture world is mutated in place, so the
    untouched-by-a-4-direction-model assertion has to come first."""
    swse, full = _models(world)

    render_final_boss_conveyor_lackeys(world, full)
    assert _northeast_turns(world) == 2
    assert _pinned_facings(world) == 0

    render_final_boss_conveyor_lackeys(world, swse)
    assert _northeast_turns(world) == 0
    assert _pinned_facings(world) == len(ENTRY_SCRIPTS)
    # Jump targets must still resolve after the deletes.
    world.action_scripts.render()
