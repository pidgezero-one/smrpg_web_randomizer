from __future__ import annotations
from enum import Enum
from typing import TYPE_CHECKING, Any
from .base import ClassCategorizationOption
from .flags import (
    CategorizationFlag,
    ShuffleItems,
    ShuffleStarPieces,
    KeyItemsAnywhere,
    StarPieceAvailability,
    SpellsAnywhere,
    BossShuffle,
)
from randomizer.logic.progression import prizelocations
from .prizelocation import (
    PrizeLocation,
    BossFightLocation,
    StarPieceLocation,
    CharacterRecruitmentLocation,
    StandingLocation,
)
from .prize import CoinPrize, FrogCoinPrize
import re

if TYPE_CHECKING:
    ShuffledBossEnumType = Enum
else:
    ShuffledBossEnumType = Any


def _location_class_to_attr_name(cls: type[PrizeLocation]) -> str:
    """Convert a PrizeLocation class to an attribute name for the enum."""
    # Use the class name, converting CamelCase to Snake_Case

    name = cls.__name__
    name = re.sub(r"([a-z])([A-Z])", r"\1_\2", name)
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    return name


def _is_freestanding_coin_location(cls: type[PrizeLocation]) -> bool:
    """Check if a location is a freestanding item that originally held coins (not frog coins)."""
    if not issubclass(cls, StandingLocation):
        return False
    originally_held = getattr(cls, "_originally_held", None)
    if originally_held is None:
        return False
    # Check if it's a CoinPrize but not a FrogCoinPrize
    return issubclass(originally_held, CoinPrize) and not issubclass(
        originally_held, FrogCoinPrize
    )


# Build enum members dynamically from prizelocations
_item_check_members = {}
_boss_fight_check_members = {}
_star_piece_check_members = {}
for cls in vars(prizelocations).values():
    if isinstance(cls, type) and issubclass(cls, PrizeLocation) and hasattr(cls, "_id"):
        # Skip freestanding coin locations - they always get their original items
        if _is_freestanding_coin_location(cls):
            continue
        attr_name = _location_class_to_attr_name(cls)
        if issubclass(cls, StarPieceLocation) and cls is not StarPieceLocation:
            _star_piece_check_members[attr_name] = cls
        elif issubclass(cls, BossFightLocation) and cls is not BossFightLocation:
            _boss_fight_check_members[attr_name] = cls
        elif cls is not PrizeLocation and not issubclass(
            cls, (BossFightLocation, StarPieceLocation, CharacterRecruitmentLocation)
        ):
            _item_check_members[attr_name] = cls
# Create enums dynamically using functional API
ItemCheckEnum = ClassCategorizationOption("ItemCheckEnum", _item_check_members)
BossFightCheckEnum = ClassCategorizationOption(
    "BossFightCheckEnum", _boss_fight_check_members
)
StarPieceCheckEnum = ClassCategorizationOption(
    "StarPieceCheckEnum", _star_piece_check_members
)


# ✅
class EnabledRegularChecks(CategorizationFlag[ItemCheckEnum]):
    _name = "General item pool checks"
    _description = """If a check is highlighted (white text over blue), its contents can be shuffled.
<br>
<br>If a check is not highlighted, its contents will match the original game.
<br>
<br>Selecting a remake-specific check will do nothing if the remake flag is not enabled."""
    _id = "chests"
    _default = {o: True for o in ItemCheckEnum.__members__.values()}
    _requires_all = [(ShuffleItems(), True)]
    _requires_any = [
        (KeyItemsAnywhere(), True),
        (StarPieceAvailability(), True),
        (SpellsAnywhere(), True),
    ]


# ✅
class EnabledBossChecks(CategorizationFlag[StarPieceCheckEnum]):
    _name = "Boss location star pieces"
    _description = """If a check is highlighted (white text over blue), it can randomly contain a star piece.
<br>
<br>If a check is not highlighted, it will have a star piece if it had one in the original game, and it will not have a star piece otherwise.
<br>
<br>Selecting a remake-specific check will do nothing if the remake flag is not enabled."""
    _id = "bosses"
    _default = {o: True for o in StarPieceCheckEnum.__members__.values()}
    _requires_all = [(ShuffleStarPieces(), True)]


# ShuffledBossEnum is created lazily to avoid circular import with prizes module
# Using ShuffledBossEnumType for type checking (defined as Enum in TYPE_CHECKING block)
ShuffledBossEnum: type[ShuffledBossEnumType] | None = None
_shuffled_boss_enum_populated = False


def _ensure_shuffled_boss_enum_populated() -> None:
    """Create ShuffledBossEnum dynamically from BossFightLocation subclasses.

    Each enum member's value is a BossFightLocation subclass, but the display
    name (attr_name) is derived from the location's originally held boss fight prize.
    """
    global ShuffledBossEnum, _shuffled_boss_enum_populated
    if _shuffled_boss_enum_populated:
        return
    _shuffled_boss_enum_populated = True


    members = {}
    for cls in vars(prizelocations).values():
        if (
            isinstance(cls, type)
            and issubclass(cls, BossFightLocation)
            and cls is not BossFightLocation
            and hasattr(cls, "_originally_held")
            and cls._originally_held is not None
        ):
            # Use the originally held boss fight prize name for display
            attr_name = _boss_class_to_attr_name(cls._originally_held)
            members[attr_name] = cls

    ShuffledBossEnum = ClassCategorizationOption("ShuffledBossEnum", members)


# Helper function for boss class name conversion
def _boss_class_to_attr_name(boss_class: type) -> str:
    """Convert boss class name to an attribute name.

    Examples:
        Croco1BossFight -> Croco_1
        KnifeGuyGrateGuyBossFight -> Knife_Guy_Grate_Guy
        Culex3DBossFight -> Culex_3D
    """

    name = boss_class.__name__
    # Remove BossFight/Fight suffix
    name = re.sub(r"(BossFight|Fight|Dight)$", "", name)
    # Add spaces before capital letters and numbers
    name = re.sub(r"([a-z])([A-Z])", r"\1 \2", name)
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", name)
    name = re.sub(r"(\d+)", r" \1", name)
    # Clean up multiple spaces and convert to underscores
    name = re.sub(r"\s+", " ", name).strip()
    return name.replace(" ", "_").replace("-", "_")


# ✅
class ShuffledBosses(CategorizationFlag[ShuffledBossEnumType]):  # type: ignore[type-arg]
    _name = "Shuffled boss fights"
    _description = """Each boss fight location below states the enemy that originally inhabits it.
<br>
<br>If a location is highlighted (white text over blue), there will instead be a random different boss inhabiting that location.
<br>
<br>If a boss is not highlighted, the location's original boss fight will stay there.
<br>
<br>Selecting a remake-specific boss will do nothing if the remake flag is not enabled."""
    _id = "pool"
    _requires_all = [(BossShuffle(), True)]

    @property
    def default(self) -> dict:
        """Lazy default that ensures ShuffledBossEnum is populated first."""
        _ensure_shuffled_boss_enum_populated()
        return {o: True for o in ShuffledBossEnum.__members__.values()}  # type: ignore[union-attr]

    def __init__(self) -> None:
        _ensure_shuffled_boss_enum_populated()
        self._default = {o: True for o in ShuffledBossEnum.__members__.values()}  # type: ignore[union-attr]
        super().__init__()
