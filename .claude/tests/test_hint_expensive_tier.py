"""The 'expensive' hint tier must stay well-formed.

apply_hint_text defers large-payment locations to their own hint tier (after
regular locations, before invisible-flag / postgame / super-jump). This guards
the two things that silently break that: a renamed/removed class, or a class
that also lives in one of the later tiers (which would shadow the expensive
branch, since that branch is checked last).
"""

from randomizer.logic.progression import prizelocations as pl
from randomizer.types.prizelocation import InvisibleFlagLocation

EXPENSIVE = [
    "MushroomKingdomInnPurchaseLocation",
    "MarrymoreFirstSuitePrizeLocation",
    "MarrymoreSecondSuitePrizeLocation",
    "MarrymoreThirdSuitePrizeLocation",
    "MarrymoreFourthSuitePrizeLocation",
    "MarrymoreFifthSuitePrizeLocation",
    "MarrymoreSixthSuitePrizeLocation",
    "MarrymoreBigTipLocation",
    "TreasureShopItem1",
    "TreasureShopItem2",
    "TreasureShopItem3",
    "FireworksShopItemLocation",
    "LandsEndFirstPurchasableChestLocation",
    "LandsEndSecondPurchasableChestLocation",
    "FrogDiscipleLocation1",
    "FrogDiscipleLocation2",
    "FrogDiscipleLocation3",
    "FrogDiscipleLocation4",
    "FrogDiscipleLocation5",
]

# Kept in sync with apply_hint_text's later tiers.
POSTGAME = [
    "InnerMinesPostgameStarPiece", "InnerMinesPostgameDrop",
    "BoosterTowerIndoorStarPieceRemake", "BoosterTowerRemakeBossFightPrizeLocation",
    "MarrymoreBossFightStarPieceRemake", "MarrymoreBossFightRemakeItemDrop",
    "ShipPostgameFightItemDrop", "ShipPostgameStarPiece",
    "TempleBossFightStarPiecePostgame", "TemplePostgameFightItemDrop",
    "DojoFifthFightStarPiece", "MonstroDojoPostgameClearRewardLocation",
    "MonstroSealedDoorStarPiecePostgame", "MonstroSealedDoorClearRewardLocationPostgame",
]
SUPER_JUMP = ["MonstroFirstSuperJumpRewardLocation", "MonstroSecondSuperJumpRewardLocation"]


def test_expensive_classes_all_exist():
    missing = [n for n in EXPENSIVE if not isinstance(getattr(pl, n, None), type)]
    assert not missing, f"expensive hint locations no longer exist: {missing}"


def test_expensive_disjoint_from_later_tiers():
    later = set(POSTGAME) | set(SUPER_JUMP)
    overlap = set(EXPENSIVE) & later
    assert not overlap, f"expensive locations also in a later tier (would be shadowed): {overlap}"

    invisible = [n for n in EXPENSIVE if issubclass(getattr(pl, n), InvisibleFlagLocation)]
    assert not invisible, f"expensive locations are also InvisibleFlagLocations: {invisible}"
