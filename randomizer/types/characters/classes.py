from randomizer.entities.progress_locations.characters_recruited import (
    StartingCharacter1,
)
from randomizer.types.characters.constants import (
    CHARACTER_BASE_ADDRESS,
    CHARACTER_BASE_LEARNED_SPELLS_ADDRESS,
    CHARACTER_BASE_STAT_BONUS_ADDRESS,
    CHARACTER_BASE_STAT_GROWTH_ADDRESS,
    LEVEL_CURVE,
    LEVELUP_BASE_ADDRESS,
)
from randomizer.types.numbers.classes import UInt4, UInt8, UInt16
from randomizer.types.spells.classes import CharacterSpell
from randomizer.types.palettes.classes import CharacterPaletteSet


from randomizer.logic import utils, flags
from randomizer.types.patch.classes import Patch

from randomizer.types.items.classes import RecruitedCharacter

import copy

from typing import Dict, List, Optional, Union

from randomizer.types.world.classes import GameWorld
from randomizer.types.world.flags.flags import ChangeNames, PlayAsStarter


class StatGrowth:
    _max_hp: UInt8 = UInt8(0)
    _attack: UInt4 = UInt4(0)
    _defense: UInt4 = UInt4(0)
    _magic_attack: UInt4 = UInt4(0)
    _magic_defense: UInt4 = UInt4(0)
    """Container class for a stat growth/bonus for a certain level + character."""

    @property
    def max_hp(self) -> UInt8:
        return self._max_hp

    def set_max_hp(self, max_hp: int) -> None:
        self._max_hp = UInt8(max_hp)

    @property
    def attack(self) -> UInt4:
        return self._attack

    def set_attack(self, attack: int) -> None:
        self._attack = UInt4(attack)

    @property
    def defense(self) -> UInt4:
        return self._defense

    def set_defense(self, defense: int) -> None:
        self._defense = UInt4(defense)

    @property
    def magic_attack(self) -> UInt4:
        return self._magic_attack

    def set_magic_attack(self, magic_attack: int) -> None:
        self._magic_attack = UInt4(magic_attack)

    @property
    def magic_defense(self) -> UInt4:
        return self._magic_defense

    def set_magic_defense(self, magic_defense: int) -> None:
        self._magic_defense = UInt4(magic_defense)

    def __init__(
        self,
        max_hp: int,
        attack: int,
        defense: int,
        magic_attack: int,
        magic_defense: int,
    ):
        self.set_max_hp(max_hp)
        self.set_attack(attack)
        self.set_defense(defense)
        self.set_magic_attack(magic_attack)
        self.set_magic_defense(magic_defense)

    @property
    def best_choices(self) -> "tuple[str]":
        """Best choice of attributes for a levelup bonus based on the numbers.  For HP, it must be twice the total of
        the attack + defense options to be considered "better".  This is arbitrary, but HP is less useful.

        :return: Tuple of attributes to select for best choice.
        """
        options = [
            (self.max_hp / 2, ("max_hp",)),
            (self.attack + self.defense, ("attack", "defense")),
            (self.magic_attack + self.magic_defense, ("magic_attack", "magic_defense")),
        ]
        a, b = max(options)
        options = [(c, d) for (c, d) in options if c == a]
        a, b = options[0]
        return b

    def as_bytes(self) -> bytearray:
        """Return byte representation of this stat growth object for the patch."""
        data = bytearray()

        # HP is one byte on its own.  Attack/defense stats are 4 bits each combined into a single byte together.
        data += utils.ByteField(self.max_hp).as_bytes()

        physical = self.attack << 4
        physical |= self.defense
        data += utils.ByteField(physical).as_bytes()

        magical = self.magic_attack << 4
        magical |= self.magic_defense
        data += utils.ByteField(magical).as_bytes()

        return data


class LevelUpExps:
    """Class for amounts of exp required for each levelup."""

    _levels: List[int] = []

    @property
    def levels(self) -> List[UInt16]:
        return [UInt16(l) for l in self._levels]

    def _set_levels(self, levels: List[int]) -> None:
        self._levels = levels

    def set_exp_for_level(self, exp: int, level: int):
        assert 1 <= level <= 30
        self._levels[level] = UInt16(exp)

    def __init__(self):
        self._set_levels(copy.deepcopy(LEVEL_CURVE))

    def get_xp_for_level(self, level: int) -> int:
        """
        :return: XP required to reach this level.
        """
        assert 1 <= level <= 30
        return self.levels[level - 1]

    def get_patch(self) -> Patch:
        """Get patch for exp required for each level up.

        :return: Patch data.
        """
        # Data is 29 blocks (starting at level 2), 2 bytes each block.
        data = bytearray()
        for level in range(2, 31):
            data += utils.ByteField(self.get_xp_for_level(level)).as_bytes()

        patch = Patch()
        patch.add_data(LEVELUP_BASE_ADDRESS, data)
        return patch


class Character(RecruitedCharacter):
    """Class for handling a character."""

    # Base stats.
    _original_name: str = ""
    _character_id: int = 0
    _starting_level: int = 1
    _max_hp: UInt16 = UInt16(1)
    _speed: UInt8 = UInt8(1)
    _attack: UInt8 = UInt8(1)
    _defense: UInt8 = UInt8(1)
    _magic_attack: UInt8 = UInt8(1)
    _magic_defense: UInt8 = UInt8(1)
    _xp: UInt16 = UInt16(0)
    _learned_spells: Dict[int, CharacterSpell] = {}
    _palette: CharacterPaletteSet

    # Placeholders for vanilla starting levelup growth and bonus numbers.
    _starting_growths: List[StatGrowth] = []
    _starting_bonuses: List[StatGrowth] = []
    _levelup_growths: List[StatGrowth] = []
    _levelup_bonuses: List[StatGrowth] = []

    _ending_palettes: List[int] = []

    _standard_sprite_addresses: List[int] = []
    _original_weapon_sprite_ids: List[Union[int, None]] = []
    _sprite_ids_as_main_character: List[int] = []
    _sprite_addresses: List[Union[list[int], None]] = [
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

    @property
    def original_name(self) -> str:
        return self._original_name

    @property
    def character_id(self) -> int:
        return self._character_id

    @property
    def starting_level(self) -> int:
        return self._starting_level

    @property
    def max_hp(self) -> UInt16:
        return self._max_hp

    @property
    def speed(self) -> UInt8:
        return self._speed

    @property
    def attack(self) -> UInt8:
        return self._attack

    @property
    def defense(self) -> UInt8:
        return self._defense

    @property
    def magic_attack(self) -> UInt8:
        return self._magic_attack

    @property
    def magic_defense(self) -> UInt8:
        return self._magic_defense

    @property
    def xp(self) -> UInt16:
        return self._xp

    @property
    def learned_spells(self) -> Dict[int, CharacterSpell]:
        return self._learned_spells

    @property
    def palette(self) -> CharacterPaletteSet:
        return self._palette

    @property
    def starting_growths(self) -> List[StatGrowth]:
        return self._starting_growths

    @property
    def starting_bonuses(self) -> List[StatGrowth]:
        return self._starting_bonuses

    @property
    def levelup_growths(self) -> List[StatGrowth]:
        return self._levelup_growths

    @property
    def levelup_bonuses(self) -> List[StatGrowth]:
        return self._levelup_bonuses

    @property
    def ending_palettes(self) -> List[int]:
        return self._ending_palettes

    @property
    def standard_sprite_addresses(self) -> List[int]:
        return self._standard_sprite_addresses

    @property
    def original_weapon_sprite_ids(self) -> List[Union[int, None]]:
        return self._original_weapon_sprite_ids

    @property
    def sprite_ids_as_main_character(self) -> List[int]:
        return self._sprite_ids_as_main_character

    @property
    def sprite_addresses(self) -> List[Union[list[int], None]]:
        return self._sprite_addresses

    @property
    def battle_sprite_offset(self) -> int:
        return self._battle_sprite_offset

    @property
    def battle_sprite_id(self) -> int:
        return self._battle_sprite_id

    @property
    def menu_sprite_offset(self) -> int:
        return self._menu_sprite_offset

    @property
    def menu_sprite_id(self) -> int:
        return self._menu_sprite_id

    @property
    def abxy_coord_offset(self) -> int:
        return self._abxy_coord_offset

    @property
    def abxy_coord(self) -> int:
        return self._abxy_coord

    @property
    def cursor_coord_offset(self) -> int:
        return self._cursor_coord_offset

    @property
    def cursor_coord(self) -> int:
        return self._cursor_coord

    @property
    def portrait_sprite_offset(self) -> int:
        return self._portrait_sprite_offset

    @property
    def portrait_id(self) -> int:
        return self._portrait_id

    @property
    def item_use_offset(self) -> int:
        return self._item_use_offset

    @property
    def item_use_bytes(self) -> bytearray:
        return self._item_use_bytes

    @property
    def runaway_offset(self) -> int:
        return self._runaway_offset

    @property
    def runaway_bytes(self) -> bytearray:
        return self._runaway_bytes

    def __init__(self, world: Optional[GameWorld] = None):
        super().__init__(world)
        self.starting_spells: "set[CharacterSpell]" = set()

        # Level-up stat growth and bonuses.
        self._levelup_growths = []
        for growth in self.starting_growths:
            self._levelup_growths.append(
                StatGrowth(
                    growth.max_hp,
                    growth.attack,
                    growth.defense,
                    growth.magic_attack,
                    growth.magic_defense,
                )
            )

        self._levelup_bonuses = []
        for growth in self.starting_bonuses:
            self._levelup_bonuses.append(
                StatGrowth(
                    growth.max_hp,
                    growth.attack,
                    growth.defense,
                    growth.magic_attack,
                    growth.magic_defense,
                )
            )

    def __str__(self):
        return "<{}>".format(self.name)

    def __repr__(self):
        return str(self)

    @property
    def name(self):
        return self.__class__.__name__

    def get_stat_at_level(self, attr, level):
        """Get natural value of the given stat at the given level using just the levelup growths.

        :type attr: str
        :type level: int
        :rtype: int
        """
        if level < 1 or level > 30:
            raise ValueError("Level must be between 1 and 30")

        value = getattr(self, attr)
        for g in self.levelup_growths[: level - 1]:
            value += getattr(g, attr)
        return value

    def get_optimal_stat_at_level(self, attr, level):
        """Get optimal value of the given stat at the given level using the levelup growths and best choice bonuses.

        :type attr: str
        :type level: int
        :rtype: int
        """
        if level < 1 or level > 30:
            raise ValueError("Level must be between 1 and 30")

        value = self.get_stat_at_level(attr, level)
        for b in self.levelup_bonuses[: level - 1]:
            if attr in b.best_choices:
                value += getattr(b, attr)
        return value

    def get_max_stat_at_level(self, attr, level):
        """Get max value of the given stat at the given level using the levelup growths and bonuses.

        :type attr: str
        :type level: int
        :rtype: int
        """
        if level < 1 or level > 30:
            raise ValueError("Level must be between 1 and 30")

        value = self.get_stat_at_level(attr, level)
        for b in self.levelup_bonuses[: level - 1]:
            value += getattr(b, attr)
        return value

    def get_patch(self):
        """Build patch data for this character.

        :return: Patch data for this character.
        :rtype: randomizer.logic.patch.Patch
        """
        patch = Patch()

        # Build character patch data.
        char_data = bytearray()
        char_data += utils.ByteField(self.starting_level).as_bytes()
        char_data += utils.ByteField(self.max_hp).as_bytes()  # Current HP
        char_data += utils.ByteField(self.max_hp).as_bytes()  # Max HP
        char_data += utils.ByteField(self.speed).as_bytes()
        char_data += utils.ByteField(self.attack).as_bytes()
        char_data += utils.ByteField(self.defense).as_bytes()
        char_data += utils.ByteField(self.magic_attack).as_bytes()
        char_data += utils.ByteField(self.magic_defense).as_bytes()
        char_data += utils.ByteField(self.xp).as_bytes()
        # Set starting weapon/armor/accessory as blank for all characters.
        char_data += utils.ByteField(0xFF).as_bytes()
        char_data += utils.ByteField(0xFF).as_bytes()
        char_data += utils.ByteField(0xFF).as_bytes()
        char_data.append(0x00)  # Unused byte
        char_data += utils.BitMapSet(
            4, [spell.index for spell in self.starting_spells]
        ).as_bytes()

        # Base address plus offset based on character index.
        addr = CHARACTER_BASE_ADDRESS + (self.character_id * 20)
        patch.add_data(addr, char_data)

        # Add levelup stat growth and bonuses to the patch data for this character.  Offset is 15 bytes for each stat
        # object, 3 bytes per character.
        for i, stat in enumerate(self.levelup_growths):
            addr = (
                CHARACTER_BASE_STAT_GROWTH_ADDRESS + (i * 15) + (self.character_id * 3)
            )
            patch.add_data(addr, stat.as_bytes())

        for i, stat in enumerate(self.levelup_bonuses):
            addr = (
                CHARACTER_BASE_STAT_BONUS_ADDRESS + (i * 15) + (self.character_id * 3)
            )
            patch.add_data(addr, stat.as_bytes())

        # Add learned spells data.
        # Data is 29 blocks (starting at level 2), 5 bytes each block (1 byte per character in order)
        base_addr = CHARACTER_BASE_LEARNED_SPELLS_ADDRESS + self.character_id
        for level in range(2, 31):
            level_addr = base_addr + ((level - 2) * 5)
            # If we have a spell for this level, add the index.  Otherwise it should be 0xff for no spell learned.
            if self.learned_spells.get(level):
                patch.add_data(
                    level_addr,
                    utils.ByteField(self.learned_spells[level].index).as_bytes(),
                )
            else:
                patch.add_data(level_addr, utils.ByteField(0xFF).as_bytes())

        starting_char = self.world.get_location_instance(StartingCharacter1).contents
        is_main_character = isinstance(
            starting_char, type(self)
        ) and self.world.settings.is_boolean_flag_enabled(PlayAsStarter)
        rename_character = self.world.settings.is_boolean_flag_enabled(ChangeNames)

        patch += self.palette.get_patch(rename_character, is_main_character)

        return patch
