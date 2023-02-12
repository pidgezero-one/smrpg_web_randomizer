from typing import Type
from randomizer.entities.characters.characters import (
    BowserSpotted,
    GenoSpotted,
    MallowSpotted,
    MarioSpotted,
    ToadstoolSpotted,
)
from randomizer.types.items.classes import SpottedCharacter
from randomizer.types.progress_locations.classes import CharacterSpottedLocation


class StartingCharacterSpotted1(CharacterSpottedLocation):
    _original_item: Type[SpottedCharacter] = MarioSpotted


class StartingCharacterSpotted2(CharacterSpottedLocation):
    _original_item = None


class StartingCharacterSpotted3(CharacterSpottedLocation):
    _original_item = None


class StartingCharacterSpotted4(CharacterSpottedLocation):
    _original_item = None


class StartingCharacterSpotted5(CharacterSpottedLocation):
    _original_item = None


class MushroomWayCharacterSpotted(CharacterSpottedLocation):
    _original_item: Type[SpottedCharacter] = MallowSpotted


class ForestMazeCharacterSpotted(CharacterSpottedLocation):
    _original_item: Type[SpottedCharacter] = GenoSpotted


class MinesCharacterSpotted(CharacterSpottedLocation):
    _original_item: Type[SpottedCharacter] = BowserSpotted


class ChapelCharacterSpotted(CharacterSpottedLocation):
    _original_item: Type[SpottedCharacter] = ToadstoolSpotted
