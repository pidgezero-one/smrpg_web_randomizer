"""Progress location definitions for recruited characters."""

from typing import Optional, Type, List

from randomizer.entities.characters import (
    Bowser,
    Geno,
    Mallow,
    Mario,
    Toadstool,
)
from randomizer.entities.characters.characters import (
    BowserSpotted,
    GenoSpotted,
    MallowSpotted,
    MarioSpotted,
    ToadstoolSpotted,
)

from randomizer.types.characters import Character
from randomizer.types.items.classes import (
    IllegalItemPropertyException,
    SpottedCharacter,
)
from randomizer.types.overworld_scripts.ids import (
    R054_BOOSTER_HILL_____DUMMY,
    R088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION,
    R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
    R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM,
    R203_MUSHROOM_WAY_AREA_01,
    R204_MUSHROOM_WAY_AREA_02,
    R205_MUSHROOM_WAY_AREA_03,
    R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09,
    R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
    R269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW,
    R284_MOLEVILLE_MINES_AREA_18_MINECART_ROOM,
    R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY,
    R435_ENDING_CREDITS_BOWSERS_KEEP_BOWSER__TROOPS_REPAIR,
    R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE,
)
from randomizer.types.overworld_scripts.action_scripts.ids import (
    A0488_FOREST_MAZE_AREA_RECRUITABLE_CHARACTER,
    A0969_ENDING_CREDITS_CASTLE_DIRECTOR,
)
from randomizer.types.overworld_scripts.event_scripts.ids import (
    E0186_PARTY_JOIN_LOGIC,
    E0192_GATING_AND_PARTY_JOIN_LOGIC,
    E2448_FOREST_BOSS_FIGHT,
    E3499_BOOSTER_HILL_1ST_PASS_LOADER,
    E3502_BOOSTER_HILL_END,
    E3506_BOOSTER_HILL_GET_FLOWER,
    E3804_ENDING_CREDITS_CORONATION_NPCS,
    E3809_MARRYMORE_SANCTUARY_BEGIN_WEDDING_GEAR_SEQUENCE,
    E3885_END_GAME,
    E3930_MARRYMORE_GEAR_PRELOADER,
    E3950_POST_FINAL_BOSS_INIT,
    E3951_STAR_PIECE_CREDITS_INIT,
)
from randomizer.types.progress_locations import (
    CharacterRecruitLocation,
    CharacterReplacementFill,
    CharacterSpottedLocation,
    Inventory,
)
from randomizer.types.world import GameWorld
from randomizer.types.world.flags import StartingCharacters


from .characters_spotted import (
    ChapelCharacterSpotted,
    ForestMazeCharacterSpotted,
    MinesCharacterSpotted,
    MushroomWayCharacterSpotted,
    StartingCharacterSpotted1,
    StartingCharacterSpotted2,
    StartingCharacterSpotted3,
    StartingCharacterSpotted4,
    StartingCharacterSpotted5,
)
from .helpers.area_access import (
    can_defeat_chapel_boss,
    can_defeat_forest_boss,
    can_defeat_mushroom_way_boss,
    can_defeat_second_moleville_boss,
)


def permit_placing_character(world: GameWorld):
    """If true, a character may be placed here (depends on number of starting characters)."""
    starters: List[Type[CharacterRecruitLocation]] = [
        StartingCharacter1,
        StartingCharacter2,
        StartingCharacter3,
        StartingCharacter4,
        StartingCharacter5,
    ]
    starting_chars = world.settings.get_flag(StartingCharacters).value
    permitted = True
    for index, loc in enumerate(starters):
        inst = world.get_location_instance(loc)
        if inst.contents is None:
            return False
        if index + 1 >= starting_chars:
            break
    return permitted


def _equivalent_spotted_character(char_class: Character) -> Type[SpottedCharacter]:
    if isinstance(char_class, Mario):
        return MarioSpotted
    if isinstance(char_class, Mallow):
        return MallowSpotted
    if isinstance(char_class, Geno):
        return GenoSpotted
    if isinstance(char_class, Bowser):
        return BowserSpotted
    if isinstance(char_class, Toadstool):
        return ToadstoolSpotted
    raise IllegalItemPropertyException("what did you try to put in this location?")


def _set_equivalent(
    world: GameWorld,
    contents: Optional[Character],
    related: Type[CharacterSpottedLocation],
) -> None:
    equivalent_spotted_location = world.get_location_instance(related)
    if contents is not None:
        spotted_char = _equivalent_spotted_character(contents)
        spotted_char_instance = world.get_spotted_character_instance(spotted_char)
    else:
        spotted_char = None
        spotted_char_instance = None
    equivalent_spotted_location.set_contents(spotted_char_instance)


class MushroomWayCharacter(CharacterRecruitLocation):
    """MushroomWayCharacter progress location class"""

    _associated_spotted_location: Type[
        CharacterSpottedLocation
    ] = MushroomWayCharacterSpotted
    _original_item: Type[Character] = Mallow
    _room_ids: List[int] = [R205_MUSHROOM_WAY_AREA_03]
    _container_event: int = E0186_PARTY_JOIN_LOGIC

    def set_contents(self, contents: Optional[Character]) -> None:
        _set_equivalent(self.world, contents, MushroomWayCharacterSpotted)

        if contents is not None:
            contents.set_main_character(False)

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_mushroom_way_boss(
            self.world, inventory
        ) and permit_placing_character(self.world)

    _fills: List[CharacterReplacementFill] = [
        CharacterReplacementFill(R203_MUSHROOM_WAY_AREA_01, 8),
        CharacterReplacementFill(R204_MUSHROOM_WAY_AREA_02, 7),
        CharacterReplacementFill(R205_MUSHROOM_WAY_AREA_03, 5),
    ]
    _credits_fills: List[CharacterReplacementFill] = [
        CharacterReplacementFill(
            R269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW,
            0,
            [E3804_ENDING_CREDITS_CORONATION_NPCS],
        ),
        CharacterReplacementFill(
            R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE, 20, [E3885_END_GAME]
        ),
        CharacterReplacementFill(
            R088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION,
            2,
            [E3950_POST_FINAL_BOSS_INIT],
        ),
        CharacterReplacementFill(
            R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY,
            1,
            [E3951_STAR_PIECE_CREDITS_INIT],
        ),
    ]


class ForestMazeCharacter(CharacterRecruitLocation):
    """ForestMazeCharacter progress location class"""

    _associated_spotted_location: Type[
        CharacterSpottedLocation
    ] = ForestMazeCharacterSpotted
    _original_item: Type[Character] = Geno
    _room_ids: List[int] = [R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    _container_event: int = E0186_PARTY_JOIN_LOGIC

    def set_contents(self, contents: Optional[Character]) -> None:
        _set_equivalent(self.world, contents, ForestMazeCharacterSpotted)

        if contents is not None:
            contents.set_main_character(False)

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_forest_boss(
            self.world, inventory
        ) and permit_placing_character(self.world)

    _fills: List[CharacterReplacementFill] = [
        CharacterReplacementFill(
            R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09,
            11,
            action_scripts=[A0488_FOREST_MAZE_AREA_RECRUITABLE_CHARACTER],
        ),
        CharacterReplacementFill(
            R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
            10,
            [E2448_FOREST_BOSS_FIGHT],
        ),
    ]
    _credits_fills: List[CharacterReplacementFill] = [
        CharacterReplacementFill(
            R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE, 21, [E3885_END_GAME]
        )
    ]
    _doll_fills: List[CharacterReplacementFill] = [
        CharacterReplacementFill(
            R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE, 22
        ),
        CharacterReplacementFill(
            R088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION,
            3,
            [E3950_POST_FINAL_BOSS_INIT],
        ),
        CharacterReplacementFill(
            R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY,
            2,
            [E3951_STAR_PIECE_CREDITS_INIT],
        ),
    ]


class MinesCharacter(CharacterRecruitLocation):
    """MinesCharacter progress location class"""

    _associated_spotted_location: Type[CharacterSpottedLocation] = MinesCharacterSpotted
    _original_item: Type[Character] = Bowser
    _room_ids: List[int] = [R284_MOLEVILLE_MINES_AREA_18_MINECART_ROOM]
    _container_event: int = E0186_PARTY_JOIN_LOGIC

    def set_contents(self, contents: Optional[Character]) -> None:
        _set_equivalent(self.world, contents, MinesCharacterSpotted)

        if contents is not None:
            contents.set_main_character(False)

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_second_moleville_boss(
            self.world, inventory
        ) and permit_placing_character(self.world)

    _fills: List[CharacterReplacementFill] = [
        CharacterReplacementFill(R284_MOLEVILLE_MINES_AREA_18_MINECART_ROOM, 1),
    ]
    _credits_fills: List[CharacterReplacementFill] = [
        CharacterReplacementFill(
            R435_ENDING_CREDITS_BOWSERS_KEEP_BOWSER__TROOPS_REPAIR,
            7,
            action_scripts=[A0969_ENDING_CREDITS_CASTLE_DIRECTOR],
        ),
        CharacterReplacementFill(
            R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE, 23, [E3885_END_GAME]
        ),
        CharacterReplacementFill(
            R088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION,
            4,
            [E3950_POST_FINAL_BOSS_INIT],
        ),
        CharacterReplacementFill(
            R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY,
            4,
            [E3951_STAR_PIECE_CREDITS_INIT],
        ),
    ]


class ChapelCharacter(CharacterRecruitLocation):
    """ChapelCharacter progress location class"""

    _associated_spotted_location: Type[
        CharacterSpottedLocation
    ] = ChapelCharacterSpotted
    _original_item: Type[Character] = Toadstool
    _room_ids: List[int] = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _container_event: int = E0186_PARTY_JOIN_LOGIC

    def set_contents(self, contents: Optional[Character]) -> None:
        _set_equivalent(self.world, contents, ChapelCharacterSpotted)

        if contents is not None:
            contents.set_main_character(False)

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_chapel_boss(
            self.world, inventory
        ) and permit_placing_character(self.world)

    _fills: List[CharacterReplacementFill] = [
        CharacterReplacementFill(
            R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            8,
            [
                E3809_MARRYMORE_SANCTUARY_BEGIN_WEDDING_GEAR_SEQUENCE,
                E3930_MARRYMORE_GEAR_PRELOADER,
            ],
        ),
        CharacterReplacementFill(
            R054_BOOSTER_HILL_____DUMMY,
            8,
            [
                E3499_BOOSTER_HILL_1ST_PASS_LOADER,
                E3502_BOOSTER_HILL_END,
                E3506_BOOSTER_HILL_GET_FLOWER,
            ],
        ),
    ]
    _credits_fills: List[CharacterReplacementFill] = [
        CharacterReplacementFill(
            R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE, 19, [E3885_END_GAME]
        ),
        CharacterReplacementFill(
            R088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION,
            0,
            [E3950_POST_FINAL_BOSS_INIT],
        ),
        CharacterReplacementFill(
            R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY,
            0,
            [E3951_STAR_PIECE_CREDITS_INIT],
        ),
    ]


class ExtraStartingCharacterLocation(CharacterRecruitLocation):
    """ExtraStartingCharacterLocation progress location class"""

    _fill_priority: int = 0

    @property
    def credits_fills(self) -> List[CharacterReplacementFill]:
        counter = 0
        match = 1
        locs: List[Type[CharacterRecruitLocation]] = [
            MushroomWayCharacter,
            ForestMazeCharacter,
            MinesCharacter,
            ChapelCharacter,
        ]
        for loc in locs:
            inst = self.world.get_location_instance(loc)
            if inst.contents is None:
                counter += 1
            if counter == match:
                return inst.credits_fills
        return []


class StartingCharacter1(CharacterRecruitLocation):
    """StartingCharacter1 progress location class"""

    _associated_spotted_location: Type[
        CharacterSpottedLocation
    ] = StartingCharacterSpotted1
    _original_item: Type[Character] = Mario
    _fills: List[CharacterReplacementFill] = [
        CharacterReplacementFill(R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM, 0)
    ]
    _container_event: int = E0192_GATING_AND_PARTY_JOIN_LOGIC

    def set_contents(self, contents: Optional[Character]) -> None:
        _set_equivalent(self.world, contents, StartingCharacterSpotted1)

        if contents is not None:
            contents.set_main_character(True)


class StartingCharacter2(ExtraStartingCharacterLocation):
    """StartingCharacter2 progress location class"""

    _fill_priority: int = 1
    _associated_spotted_location: Type[
        CharacterSpottedLocation
    ] = StartingCharacterSpotted2
    _original_item = None
    _container_event: int = E0192_GATING_AND_PARTY_JOIN_LOGIC

    def can_access(self, inventory: Inventory) -> bool:
        starting_chars = self.world.settings.get_flag(StartingCharacters).value
        return starting_chars >= 2

    def set_contents(self, contents: Optional[Character]) -> None:
        _set_equivalent(self.world, contents, StartingCharacterSpotted2)

        if contents is not None:
            contents.set_main_character(False)


class StartingCharacter3(ExtraStartingCharacterLocation):
    """StartingCharacter3 progress location class"""

    _fill_priority: int = 2
    _associated_spotted_location: Type[
        CharacterSpottedLocation
    ] = StartingCharacterSpotted3
    _original_item = None
    _container_event: int = E0192_GATING_AND_PARTY_JOIN_LOGIC

    def can_access(self, inventory: Inventory) -> bool:
        starting_chars = self.world.settings.get_flag(StartingCharacters).value
        return starting_chars >= 3

    def set_contents(self, contents: Optional[Character]) -> None:
        _set_equivalent(self.world, contents, StartingCharacterSpotted3)

        if contents is not None:
            contents.set_main_character(False)


class StartingCharacter4(ExtraStartingCharacterLocation):
    """StartingCharacter4 progress location class"""

    _fill_priority: int = 3
    _associated_spotted_location: Type[
        CharacterSpottedLocation
    ] = StartingCharacterSpotted4
    _original_item = None
    _container_event: int = E0192_GATING_AND_PARTY_JOIN_LOGIC

    def can_access(self, inventory: Inventory) -> bool:
        starting_chars = self.world.settings.get_flag(StartingCharacters).value
        return starting_chars >= 4

    def set_contents(self, contents: Optional[Character]) -> None:
        _set_equivalent(self.world, contents, StartingCharacterSpotted4)

        if contents is not None:
            contents.set_main_character(False)


class StartingCharacter5(ExtraStartingCharacterLocation):
    """StartingCharacter5 progress location class"""

    _fill_priority: int = 4
    _associated_spotted_location: Type[
        CharacterSpottedLocation
    ] = StartingCharacterSpotted5
    _original_item = None
    _container_event: int = E0192_GATING_AND_PARTY_JOIN_LOGIC

    def set_contents(self, contents: Optional[Character]) -> None:
        _set_equivalent(self.world, contents, StartingCharacterSpotted5)

        if contents is not None:
            contents.set_main_character(False)

    def can_access(self, inventory: Inventory) -> bool:
        starting_chars = self.world.settings.get_flag(StartingCharacters).value
        return starting_chars >= 5
