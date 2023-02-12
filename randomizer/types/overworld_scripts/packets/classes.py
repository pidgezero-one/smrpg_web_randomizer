from typing import List
from randomizer.types.overworld_scripts.action_scripts.constants.misc import (
    TOTAL_SCRIPTS,
)
from randomizer.types.numbers.classes import UInt16, UInt8
from randomizer.types.overworld_scripts.packets.constants.misc import TOTAL_PACKETS
from randomizer.types.sprites.constants.misc import TOTAL_SPRITES
from randomizer.types.overworld_scripts.action_scripts.constants.misc import (
    TOTAL_SCRIPTS,
)
from randomizer.types.sprites.constants.sprite_ids import SPR0524_EMPTY


class Packet:
    _packet_id: UInt8 = UInt8(8)
    _sprite_id: UInt16 = UInt16(0)
    _shadow: bool = False
    _action_script_id: UInt16 = UInt16(0)
    _unknown_bits: List[bool] = [False] * 3
    _unknown_bytes: bytearray = bytearray()

    @property
    def packet_id(self) -> UInt8:
        return self._packet_id

    def _set_packet_id(self, packet_id: int) -> None:
        assert packet_id < TOTAL_PACKETS
        self._packet_id = UInt8(packet_id)

    @property
    def sprite_id(self) -> UInt16:
        return self._sprite_id

    def _set_sprite_id(self, sprite_id: int) -> None:
        assert sprite_id < TOTAL_SPRITES
        self._sprite_id = UInt16(sprite_id)

    @property
    def shadow(self) -> bool:
        return self._shadow

    def _set_shadow(self, shadow: bool) -> None:
        self._shadow = shadow

    @property
    def action_script_id(self) -> UInt16:
        return self._action_script_id

    def _set_action_script_id(self, action_script_id: int) -> None:
        assert action_script_id < TOTAL_SCRIPTS
        self._action_script_id = UInt16(action_script_id)

    @property
    def unknown_bits(self) -> List[bool]:
        return self._unknown_bits

    def _set_unknown_bits(self, unknown_bits: List[bool]) -> None:
        for b in unknown_bits:
            assert 0 <= b <= 7
        self._unknown_bits = unknown_bits

    @property
    def unknown_bytes(self) -> bytearray:
        return self._unknown_bytes

    def _set_unknown_bytes(self, unknown_bytes: bytearray) -> None:
        self._unknown_bytes = unknown_bytes

    def __init__(
        self,
        packet_id: int,
        sprite_id: int = SPR0524_EMPTY,
        shadow: bool = False,
        action_script_id: int = 15,
        unknown_bits: List[bool] = [],
        unknown_bytes: bytearray = bytearray(),
    ) -> None:
        self._set_packet_id(packet_id)
        self._set_sprite_id(sprite_id)
        self._set_shadow(shadow)
        self._set_action_script_id(action_script_id)
        self._set_unknown_bits(unknown_bits)
        self._set_unknown_bytes(unknown_bytes)
