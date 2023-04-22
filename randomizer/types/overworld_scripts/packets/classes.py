"""Base classes supporting packet assembly."""

from typing import List, Optional
from randomizer.types.numbers.classes import UInt16, UInt8
from randomizer.types.overworld_scripts.action_scripts.constants.misc import (
    TOTAL_SCRIPTS,
)
from randomizer.types.overworld_scripts.action_scripts.constants.script_ids import (
    A0015_DO_NOTHING,
)
from randomizer.types.sprites.constants.misc import TOTAL_SPRITES
from randomizer.types.sprites.constants.sprite_ids import SPR0524_EMPTY


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
