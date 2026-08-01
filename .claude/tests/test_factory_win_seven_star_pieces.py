"""Under the FACTORY win condition, all TotalStarPieces star pieces must still exist.

FinalBossFightStarPiece is the only vanilla holder of StarPiece7, and the pool is
built by pulling vanilla holders. It used to be registered only when the win condition
was NOT FACTORY (defeating the factory final boss ends the game, so a star piece placed
THERE can't be collected). But dropping the location also dropped StarPiece7 from the
pool entirely, capping placeable star pieces at 6 even with TotalStarPieces=7.

Fix: always register it as a SOURCE (its StarPiece7 seeds the pool) but keep it
source-only under FACTORY (can_accept rejects everything), so StarPiece7 gets shuffled
to a collectible location and the final-boss spot stays empty.
"""

import pytest

import randomizer.main as main
from randomizer.logic.progression.prizelocations import FinalBossFightStarPiece
from randomizer.types.flags import (
    ShuffleStarPieces,
    StarPiecesRequired,
    TotalStarPieces,
    WinCondition,
    WinConditions,
)
from randomizer.types.prize import StarPiecePrize
from randomizer.types.settings import Settings


@pytest.fixture(scope="module")
def world():
    settings = Settings()
    settings.get_flag(ShuffleStarPieces).enable()
    settings.get_flag(TotalStarPieces).set_value(7)
    settings.get_flag(StarPiecesRequired).set_value(7)
    assert settings.is_flag_value(WinCondition, WinConditions.FACTORY), (
        "default win condition should be FACTORY for this regression"
    )
    return main.create(3097306894, settings)


def test_all_seven_star_pieces_placed_under_factory(world):
    placed = [
        type(loc.prize).__name__
        for loc in world.locations.values()
        if isinstance(loc.prize, StarPiecePrize)
    ]
    assert len(placed) == 7, (
        f"expected 7 star pieces placed under FACTORY win, got {len(placed)}: "
        f"{sorted(placed)}"
    )


def test_final_boss_star_piece_is_source_only_under_factory(world):
    # Registered (so StarPiece7 seeds the pool) but never a placement target under FACTORY.
    loc = world.locations[FinalBossFightStarPiece]
    assert loc.prize is None, (
        "FinalBossFightStarPiece must stay empty under FACTORY — a star piece there "
        "could never be collected"
    )
