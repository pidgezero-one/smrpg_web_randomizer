"""rstars OFF: the hint builder must still emit hints for the vanilla star piece
holders (the locations that hold a star piece in the unshuffled game), even though
should_shuffle() drops every StarPieceLocation when ShuffleStarPieces is off.

Carve-outs (both exercised below):
  * The factory piece (StarPiece7 / FinalBossFightStarPiece) is excluded when the
    factory boss is the win condition (WinConditions.FACTORY, the default), since it
    is only collected as the game ends.
  * Non-vanilla star piece slots (originally_held is None, e.g. LandsEndCloudStarPiece)
    are never hinted when rstars is off.

Regression for apply_hint_text's sp_vanilla_holder exemption at the should_shuffle
gate (randomizer/logic/apply.py). Default Settings() is exactly the rstars-off +
FACTORY-win case, so no flag tweaking is needed.

Each hint block leads with `JmpIfBitSet(<collected-flag>, ["next"])`; a location's
hint is present iff that flag appears as a JmpIfBitSet in one of the three hint
scripts. Only classes whose leading flag is globally unique are used as fingerprints
(ForestMaze/InnerMines lead with a shared area gate, so they are omitted here -- the
gate is uniform across vanilla holders, so four representatives cover it).
"""

import pytest

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    JmpIfBitSet,
)
import randomizer.main as main
from randomizer.data.variables.event_script_names import (
    E0947_HINT_SYSTEM,
    E1536_HINT_SYSTEM,
    E3088_HINT_SYSTEM,
)
from randomizer.logic.progression.prizelocations import (
    MushroomKingdomStarPiece,
    StarHillStarPiece,
    SeasideBeachStarPiece,
    VolcanoExitStarPiece,
    FinalBossFightStarPiece,
    LandsEndCloudStarPiece,
)
from randomizer.types.settings import Settings

# Vanilla holders with a globally-unique leading flag -> must be hinted (rstars off).
VANILLA_HINTED = [
    MushroomKingdomStarPiece,
    StarHillStarPiece,
    SeasideBeachStarPiece,
    VolcanoExitStarPiece,
]
# Must NOT be hinted under default (rstars off, FACTORY win).
NOT_HINTED = [
    FinalBossFightStarPiece,  # StarPiece7, excluded when factory is the win condition
    LandsEndCloudStarPiece,   # originally_held is None (non-vanilla slot)
]


def _lead_flag(cls):
    """(byte, bit) of the collected-flag a location's hint block leads with."""
    cmd = next(c for c in cls._hint if isinstance(c, JmpIfBitSet))
    return (cmd.bit.byte, cmd.bit.bit)


@pytest.fixture(scope="module")
def emitted_flags():
    # Default Settings(): ShuffleStarPieces OFF, WinCondition FACTORY.
    world = main.create(20260714, Settings())
    flags = set()
    for sid in (E0947_HINT_SYSTEM, E1536_HINT_SYSTEM, E3088_HINT_SYSTEM):
        for cmd in world.event_scripts.get_script_by_id(sid).contents:
            if isinstance(cmd, JmpIfBitSet):
                flags.add((cmd.bit.byte, cmd.bit.bit))
    return flags


@pytest.mark.parametrize("cls", VANILLA_HINTED, ids=lambda c: c.__name__)
def test_vanilla_star_piece_holder_is_hinted(emitted_flags, cls):
    assert _lead_flag(cls) in emitted_flags, (
        f"{cls.__name__} star piece hint missing with rstars off"
    )


@pytest.mark.parametrize("cls", NOT_HINTED, ids=lambda c: c.__name__)
def test_excluded_star_piece_is_not_hinted(emitted_flags, cls):
    assert _lead_flag(cls) not in emitted_flags, (
        f"{cls.__name__} should not be hinted (rstars off, FACTORY win)"
    )
