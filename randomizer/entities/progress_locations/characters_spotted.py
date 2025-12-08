"""Progress location definitions for spotted (not necessarily recruited) characters."""

from randomizer.entities.characters import (
    BowserSpotted,
    GenoSpotted,
    MallowSpotted,
    MarioSpotted,
    ToadstoolSpotted)
from randomizer.types.items import SpottedCharacter
from randomizer.types.progress_locations import CharacterSpottedLocation


class StartingCharacterSpotted1(CharacterSpottedLocation):
    """StartingCharacterSpotted1 progress location class"""

    _original_item: type[SpottedCharacter] = MarioSpotted


class StartingCharacterSpotted2(CharacterSpottedLocation):
    """StartingCharacterSpotted2 progress location class"""

    _original_item = None


class StartingCharacterSpotted3(CharacterSpottedLocation):
    """StartingCharacterSpotted3 progress location class"""

    _original_item = None


class StartingCharacterSpotted4(CharacterSpottedLocation):
    """StartingCharacterSpotted4 progress location class"""

    _original_item = None


class StartingCharacterSpotted5(CharacterSpottedLocation):
    """StartingCharacterSpotted5 progress location class"""

    _original_item = None


class MushroomWayCharacterSpotted(CharacterSpottedLocation):
    """MushroomWayCharacterSpotted progress location class"""

    _original_item: type[SpottedCharacter] = MallowSpotted


class ForestMazeCharacterSpotted(CharacterSpottedLocation):
    """ForestMazeCharacterSpotted progress location class"""

    _original_item: type[SpottedCharacter] = GenoSpotted


class MinesCharacterSpotted(CharacterSpottedLocation):
    """MinesCharacterSpotted progress location class"""

    _original_item: type[SpottedCharacter] = BowserSpotted


class ChapelCharacterSpotted(CharacterSpottedLocation):
    """ChapelCharacterSpotted progress location class"""

    _original_item: type[SpottedCharacter] = ToadstoolSpotted
