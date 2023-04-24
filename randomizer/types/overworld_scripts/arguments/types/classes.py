"""Helper classes defining constants used in overworld and
NPC action scripts"""

from typing import List, Optional, NamedTuple

from randomizer.types.numbers import UInt8, UInt16
from randomizer.types.sprites.ids import TOTAL_SPRITES, SPR0524_EMPTY

from randomizer.types.overworld_scripts.action_scripts.ids import (
    TOTAL_SCRIPTS,
    A0015_DO_NOTHING,
)


class AreaObject(int):
    """Base class representing field objects, such as party members and NPCs,
    that can be targeted by overworld and NPC action script commands."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 0x2F
        return super(AreaObject, cls).__new__(cls, num)


class PartyCharacter(AreaObject):
    """Base AreaObject subclass representing field objects that can be targeted
    by commands targeting a pary member, 0x00 to 0x0B, where 0x00-0x04 represent
    your usable party members."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 0x0B
        return super(PartyCharacter, cls).__new__(cls, num)


class Direction(int):
    """Base class representing directions in which an object can walk or face."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 7
        return super(Direction, cls).__new__(cls, num)


class Coord(int):
    """Base class representing coordinate axes for commands requiring a coordinate
    or coordinate set."""

    def __new__(cls, *args):
        num = args[0]
        assert num in [0x00, 0x01, 0x02, 0x05]
        return super(Coord, cls).__new__(cls, num)


class ControllerInput(int):
    """Base class representing an input from a specific controller button."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 7
        return super(ControllerInput, cls).__new__(cls, num)


class PaletteType(int):
    """Base class representing special effects that can be applied to a palette."""

    def __new__(cls, *args):
        num = args[0]
        assert num in [0x00, 0x06, 0x0C, 0x0E]
        return super(PaletteType, cls).__new__(cls, num)


class Layer(int):
    """Base class representing a graphical layer in a level."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 3
        return super(Layer, cls).__new__(cls, num)


class Colour(int):
    """Base class representing a colour to be used by certain graphics commands."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 7
        return super(Colour, cls).__new__(cls, num)


class IntroTitleText(int):
    """Base class representing predefined texts that are displayed in the game's intro."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 5
        return super(IntroTitleText, cls).__new__(cls, num)


class Scene(int):
    """Base class representing IDs for some predefined cutscenes and screen transitions."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 16
        return super(Scene, cls).__new__(cls, num)


class Tutorial(int):
    """Base class representing IDs for some predefined in-game tutorial modes."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 3
        return super(Tutorial, cls).__new__(cls, num)


class Battlefield(int):
    """Base class representing IDs for valid battlefields."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 63
        return super(Battlefield, cls).__new__(cls, num)


class Packet:
    """An object to be spawned on the field that does not exist in the room's
    list of NPCs.\n
    Packets are fairly limited in what they can do, they are not as complex
    as NPCs.\n
    They are usually meant to be temporary, such as collectable items or
    treasure chest contents.\n
    It is recommended to use packet ID, sprite ID, and action script ID constant names.
    """

    _packet_id: UInt8 = UInt8(8)
    _sprite_id: UInt16 = UInt16(0)
    _shadow: bool = False
    _action_script_id: UInt16 = UInt16(0)
    _unknown_bits: List[bool] = [False] * 3
    _unknown_bytes: bytearray = bytearray()

    @property
    def packet_id(self) -> UInt8:
        """The ID of the packet."""
        return self._packet_id

    @property
    def sprite_id(self) -> UInt16:
        """The sprite ID for the packet to use."""
        return self._sprite_id

    def _set_sprite_id(self, sprite_id: int) -> None:
        """Set the sprite ID for the packet to use.\n
        It is recommended to use sprite ID constant names for this."""
        assert sprite_id < TOTAL_SPRITES
        self._sprite_id = UInt16(sprite_id)

    @property
    def shadow(self) -> bool:
        """If true, the packet casts a shadow when above ground."""
        return self._shadow

    def _set_shadow(self, shadow: bool) -> None:
        """If true, the packet casts a shadow when above ground."""
        self._shadow = shadow

    @property
    def action_script_id(self) -> UInt16:
        """The action script for this packet to run when spawned."""
        return self._action_script_id

    def _set_action_script_id(self, action_script_id: int) -> None:
        """Set the action script for this packet to run when spawned.\n
        It is recommended to use action script ID constant names for this."""
        assert action_script_id < TOTAL_SCRIPTS
        self._action_script_id = UInt16(action_script_id)

    @property
    def unknown_bits(self) -> List[bool]:
        """(unknown)"""
        return self._unknown_bits

    def _set_unknown_bits(self, unknown_bits: List[bool]) -> None:
        """(unknown)"""
        for bit in unknown_bits:
            assert 0 <= bit <= 7
        self._unknown_bits = unknown_bits

    @property
    def unknown_bytes(self) -> bytearray:
        """(unknown)"""
        return self._unknown_bytes

    def _set_unknown_bytes(self, unknown_bytes: bytearray) -> None:
        """(unknown)"""
        self._unknown_bytes = unknown_bytes

    def __init__(
        self,
        packet_id: int,
        sprite_id: int = SPR0524_EMPTY,
        shadow: bool = False,
        action_script_id: int = A0015_DO_NOTHING,
        unknown_bits: Optional[List[bool]] = None,
        unknown_bytes: bytearray = bytearray(),
    ) -> None:
        if unknown_bits is None:
            unknown_bits = []
        self._packet_id = UInt8(packet_id)
        self._set_sprite_id(sprite_id)
        self._set_shadow(shadow)
        self._set_action_script_id(action_script_id)
        self._set_unknown_bits(unknown_bits)
        self._set_unknown_bytes(unknown_bytes)


class _Flag(NamedTuple):
    byte: int
    bit: int


class Flag(_Flag):
    """An in-game variable that is a single true/false bit,
    normally carrying meaning independent of the byte it belongs to.\n
    Bits for 8-bit addresses between 0x7040 and 0x709F can be used for this."""

    def __new__(cls, byte: int, bit: int):
        assert 0x7040 <= byte <= 0x709F
        assert 0 <= bit <= 7
        return super().__new__(cls, byte, bit)


class ShortVar(int):
    """An in-game variable that can store 16-bit short int values.\n
    Addresses between 0x7000 and 0x71FE can be used for this."""

    def __new__(cls, *args):
        address = args[0]
        assert 0x7000 <= address <= 0x71FE and address % 2 == 0
        return super(ShortVar, cls).__new__(cls, address)

    def to_byte(self) -> int:
        """Casts the variable address to a byte value to be used
        when writing the ROM patch, understood by the game."""
        byte = (self - 0x7000) // 2
        assert 0 <= byte <= 0xFF
        return byte


class ByteVar(int):
    """An in-game variable that can store 8-bit byte int values.\n
    Addresses between 0x7040 and 0x719F can be used for this."""

    def __new__(cls, *args):
        address = args[0]
        assert 0x7040 <= address <= 0x719F
        return super(ByteVar, cls).__new__(cls, address)

    def to_byte(self) -> int:
        """Casts the variable address to a byte value to be used
        when writing the ROM patch, understood by the game."""
        byte = self - 0x70A0
        assert 0 <= byte <= 0xFF
        return byte
