"""Base classes for playable characters."""

from randomizer.entities.progress_locations.characters_recruited import (
    StartingCharacter1)

from randomizer.types.items import RecruitedCharacter
from randomizer.types.palettes import CharacterPaletteSet
from randomizer.types.patch import Patch
from randomizer.types.world.flags.flags import ChangeNames, PlayAsStarter


class Character(TODOImportedCharacterClass, RecruitedCharacter):
    """Base class for a playable character."""

    _original_name: str = ""

    _ending_palettes: list[int] = []

    _standard_sprite_addresses: list[int] = []
    _original_weapon_sprite_ids: list[int | None] = []
    _sprite_ids_as_main_character: list[int] = []
    _sprite_addresses: list[list[int] | None] = [
        [],
        [],
        [],
    ]  # not building an assembler for this in this version

    _battle_sprite_offset: int = 0
    _battle_sprite_id: int = 0
    _menu_sprite_offset: int = 0
    _menu_sprite_id: int = 0
    _abxy_coord_offset: int = 0
    _abxy_coord: int = 0
    _cursor_coord_offset: int = 0
    _cursor_coord: int = 0
    _portrait_sprite_offset: int = 0
    _portrait_id: int = 0
    _item_use_offset: int = 0
    _item_use_bytes: bytearray = bytearray()
    _runaway_offset: int = 0
    _runaway_bytes: bytearray = bytearray()

    _main_character: bool = False

    @property
    def original_name(self) -> str:
        """The character's original name, in case this needs to be referenced
        after they have been renamed by the palette shuffler."""
        return self._original_name

    @property
    def palette(self) -> CharacterPaletteSet:
        """The palette applied to this character."""
        return self._palette

    @property
    def ending_palettes(self) -> list[int]:
        """The addresses where this character's palettes should be written during the credits."""
        return self._ending_palettes

    @property
    def standard_sprite_addresses(self) -> list[int]:
        """Other places where this character's palettes should be written during the credits."""
        return self._standard_sprite_addresses

    @property
    def original_weapon_sprite_ids(self) -> list[int | None]:
        """The IDs of weapons this character can use in the original game."""
        return self._original_weapon_sprite_ids

    @property
    def sprite_ids_as_main_character(self) -> list[int]:
        """(deprecated)"""
        return self._sprite_ids_as_main_character

    @property
    def sprite_addresses(self) -> list[list[int] | None]:
        """(deprecated)"""
        return self._sprite_addresses

    @property
    def battle_sprite_offset(self) -> int:
        """The offset pointing to which sprite to load for this character in battle."""
        return self._battle_sprite_offset

    @property
    def battle_sprite_id(self) -> int:
        """The sprite ID to load for this character in battle."""
        return self._battle_sprite_id

    @property
    def menu_sprite_offset(self) -> int:
        """The offset pointing to which sprite to load for this character in the menu."""
        return self._menu_sprite_offset

    @property
    def menu_sprite_id(self) -> int:
        """The sprite ID to load for this character in the menu."""
        return self._menu_sprite_id

    @property
    def abxy_coord_offset(self) -> int:
        """The offset where the value is stored for the height at which the ABXY interface
        in battle sits for this character."""
        return self._abxy_coord_offset

    @property
    def abxy_coord(self) -> int:
        """The height at which the ABXY interface in battle should sit for this character."""
        return self._abxy_coord

    @property
    def cursor_coord_offset(self) -> int:
        """The offset where the value is stored for the height at which the cursor
        in battle sits for this character."""
        return self._cursor_coord_offset

    @property
    def cursor_coord(self) -> int:
        """The height at which the cursor in battle should sit for this character."""
        return self._cursor_coord

    @property
    def portrait_sprite_offset(self) -> int:
        """The offset where the value is for the sprite ID of this character's battle portrait."""
        return self._portrait_sprite_offset

    @property
    def portrait_id(self) -> int:
        """The sprite ID of this character's battle portrait."""
        return self._portrait_id

    @property
    def item_use_offset(self) -> int:
        """(don't remember what this does)"""
        return self._item_use_offset

    @property
    def item_use_bytes(self) -> bytearray:
        """(don't remember what this does)"""
        return self._item_use_bytes

    @property
    def runaway_offset(self) -> int:
        """(don't remember what this does)"""
        return self._runaway_offset

    @property
    def runaway_bytes(self) -> bytearray:
        """(don't remember what this does)"""
        return self._runaway_bytes

    @property
    def is_main_character(self) -> bool:
        """Main character is your overworld protagonist"""
        return self._main_character

    def set_main_character(self, main: bool) -> None:
        """Main character is your overworld protagonist"""
        self._main_character = main

    def __str__(self):
        """String representation of current state"""
        return f"<{self.name}>"

    def __repr__(self):
        """String representation of current state"""
        return str(self)

    @property
    def name(self):
        """String representation of class name"""
        return self.__class__.__name__

    def get_stat_at_level(self, attr: str, level: int) -> int:
        """Get natural value of the given stat at the given level using just the levelup growths.

        :type attr: str
        :type level: int
        :rtype: int
        """
        if level < 1 or level > 30:
            raise ValueError("Level must be between 1 and 30")

        value = getattr(self, attr)
        for growth in self.starting_growths[: level - 1]:
            value += getattr(growth, attr)
        return value

    def get_optimal_stat_at_level(self, attr: str, level: int) -> int:
        """Get optimal value of the given stat at the given level using the levelup growths
        and best choice bonuses."""
        if level < 1 or level > 30:
            raise ValueError("Level must be between 1 and 30")

        value = self.get_stat_at_level(attr, level)
        for bonus in self.levelup_bonuses[: level - 1]:
            if attr in bonus.best_choices:
                value += getattr(bonus, attr)
        return value

    def get_max_stat_at_level(self, attr, level) -> int:
        """Get max value of the given stat at the given level using the levelup growths and bonuses.

        :type attr: str
        :type level: int
        :rtype: int
        """
        if level < 1 or level > 30:
            raise ValueError("Level must be between 1 and 30")

        value = self.get_stat_at_level(attr, level)
        for bonus in self.levelup_bonuses[: level - 1]:
            value += getattr(bonus, attr)
        return value

    def get_patch(self) -> Patch:
        """Get ROM patch for this item."""
        patch = super().get_patch()

        starting_char = self.world.get_location_instance(StartingCharacter1).contents
        is_main_character = isinstance(
            starting_char, type(self)
        ) and self.world.settings.is_boolean_flag_enabled(PlayAsStarter)
        rename_character = self.world.settings.is_boolean_flag_enabled(ChangeNames)

        patch += self.palette.get_patch(rename_character, is_main_character)

        return patch
