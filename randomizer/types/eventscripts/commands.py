from typing import Optional, Union, cast

from randomizer.types.eventscripts.classes import (
    ActionQueuePrototype,
    EventScriptCommand,
    EventScriptCommandNoArgs,
    EventScriptCommandAnySizeMem,
    EventScriptCommandBasicShortOperation,
    EventScriptCommandShortAddrAndValueOnly,
    EventScriptCommandWithJmps,
    EventScriptCommandShortMem,
    NonEmbeddedActionQueuePrototype,
    StartEmbeddedActionScriptPrototype,
)
from randomizer.types.eventscripts.constants.misc import TOTAL_SCRIPTS

from randomizer.types.actionscripts.constants.misc import (
    TOTAL_SCRIPTS as TOTAL_ACTION_SCRIPTS,
)

from randomizer.types.characters.classes import Character
from randomizer.types.constants.classes import (
    AreaObject,
    Battlefield,
    Colour,
    Coord,
    ControllerInput,
    Direction,
    IntroTitleText,
    PaletteType,
    Layer,
    Scene,
    Tutorial,
)
from randomizer.types.constants.misc import (
    TOTAL_DIALOGS,
    TOTAL_MUSIC,
    TOTAL_ROOMS,
    TOTAL_SHOPS,
    TOTAL_SOUNDS,
    TOTAL_WORLD_MAP_AREAS,
)
from randomizer.types.constants import coords

from randomizer.types.items.classes import Equipment, Item, Weapon, Armor, Accessory

from randomizer.types.numbers.classes import UInt16, UInt8
from randomizer.types.packets.classes import Packet
from randomizer.types.variables import variables
from randomizer.types.variables.classes import ByteVar, Flag, ShortVar
from randomizer.utils.memsize import cast_address
from randomizer.utils.number import bits_to_int, bools_to_int

# script operations


class StartLoopNFrames(EventScriptCommand):
    _opcode: int = 0xD5
    _size: int = 3
    _length: UInt16

    @property
    def length(self) -> UInt16:
        return self._length

    def set_length(self, length: int) -> None:
        self._length = UInt16(length)

    def __init__(self, length: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_length(length)

    def render(self) -> bytearray:
        return super().render(self.length)


class StartLoopNTimes(EventScriptCommand):
    _opcode: int = 0xD4
    _size: int = 2
    _count: UInt8

    @property
    def count(self) -> UInt8:
        return self._count

    def set_count(self, count: int) -> None:
        self._count = UInt8(count)

    def __init__(self, count: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_count(count)

    def render(self) -> bytearray:
        return super().render(self.count)


class EndLoop(EventScriptCommandNoArgs):
    _opcode: int = 0xD7


class Jmp(EventScriptCommandWithJmps):
    _opcode: int = 0xD2
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpToEvent(EventScriptCommand):
    _opcode: int = 0xD0
    _size: int = 3
    _destination: UInt16

    @property
    def destination(self) -> UInt16:
        return self._destination

    def set_destination(self, destination: int) -> None:
        assert 0 <= destination < TOTAL_SCRIPTS
        self._destination = UInt16(destination)

    def __init__(self, destination: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_destination(destination)

    def render(self) -> bytearray:
        return super().render(self.destination)


class JmpToStartOfThisScript(EventScriptCommandNoArgs):
    _opcode: int = 0xF9


class JmpToStartOfThisScriptFA(EventScriptCommandNoArgs):
    _opcode: int = 0xFA


class JmpToSubroutine(EventScriptCommandWithJmps):
    _opcode: int = 0xD3
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class MoveScriptToMainThread(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x40])


class MoveScriptToBackgroundThread1(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x41])


class MoveScriptToBackgroundThread2(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x42])


class Pause(EventScriptCommand):
    _length: Union[UInt8, UInt16]

    @property
    def length(self) -> Union[UInt8, UInt16]:
        return self._length

    def set_length(self, length: int) -> None:
        if 1 <= length <= 0x100:
            self._length = UInt8(length)
        elif 1 <= length <= 0x10000:
            self._length = UInt16(length)
        else:
            raise Exception(
                "illegal pause duration in %s: %i" % (self.identifier, length)
            )

    def __init__(self, length: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_length(length)
        if isinstance(self.length, UInt8):
            self._size: int = 2
        else:
            self._size: int = 3

    def render(self) -> bytearray:
        frames = self.length - 1
        if isinstance(frames, UInt8):
            return super().render(0xF0, frames)
        else:
            return super().render(0xF1, frames)


class RememberLastObject(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x32])


class ResumeBackgroundEvent(EventScriptCommand):
    _opcode: int = 0x47
    _size: int = 2
    _timer_var: int

    @property
    def timer_var(self) -> int:
        return self._timer_var

    def set_timer_var(self, timer_var: int) -> None:
        assert timer_var in [0x701C, 0x701E, 0x7020, 0x7022]
        self._timer_var = timer_var

    def __init__(self, timer_var: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_timer_var(timer_var)

    def render(self) -> bytearray:
        timer_byte: int = (self.timer_var - 0x701C) // 2
        return super().render(timer_byte)


class RunBackgroundEvent(EventScriptCommand):
    _opcode: 0x40
    _size: int = 3
    _event_id: UInt16
    _return_on_level_exit: bool
    _bit_6: bool
    _bit_7: bool

    @property
    def event_id(self) -> UInt16:
        return self._event_id

    def set_event_id(self, event_id: int) -> None:
        assert 0 <= event_id < TOTAL_SCRIPTS
        self._event_id = UInt16(event_id)

    @property
    def return_on_level_exit(self) -> bool:
        return self._return_on_level_exit

    def set_return_on_level_exit(self, return_on_level_exit: bool) -> None:
        self._return_on_level_exit = return_on_level_exit

    @property
    def bit_6(self) -> bool:
        return self._bit_6

    def set_bit_6(self, bit_6: bool) -> None:
        self._bit_6 = bit_6

    @property
    def bit_7(self) -> bool:
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        self._bit_7 = bit_7

    def __init__(
        self,
        event_id: int,
        return_on_level_exit: bool = False,
        bit_6: bool = False,
        bit_7: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_event_id(event_id)
        self.return_on_level_exit(return_on_level_exit)
        self.set_bit_6(bit_6)
        self.set_bit_7(bit_7)

    def render(self) -> bytearray:
        flags: int = bools_to_int(self._return_on_level_exit, self.bit_6, self.bit_7)
        flags = flags << 13
        arg_byte: UInt16(self.event_id + flags)
        return super().render(arg_byte)


class RunBackgroundEventWithPause(EventScriptCommand):
    _opcode: 0x44
    _size: int = 4
    _event_id: UInt16
    _timer_var: int
    _bit_4: bool
    _bit_5: bool

    @property
    def event_id(self) -> UInt16:
        return self._event_id

    def set_event_id(self, event_id: int) -> None:
        assert 0 <= event_id < TOTAL_SCRIPTS
        self._event_id = UInt16(event_id)

    @property
    def timer_var(self) -> int:
        return self._timer_var

    def set_timer_var(self, timer_var: int) -> None:
        assert timer_var in [0x701C, 0x701E, 0x7020, 0x7022]
        self._timer_var = timer_var

    @property
    def bit_4(self) -> bool:
        return self._bit_4

    def set_bit_4(self, bit_4: bool) -> None:
        self._bit_4 = bit_4

    @property
    def bit_5(self) -> bool:
        return self._bit_5

    def set_bit_5(self, bit_5: bool) -> None:
        self._bit_5 = bit_5

    def __init__(
        self,
        event_id: int,
        timer_var: int,
        bit_4: bool = False,
        bit_5: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_event_id(event_id)
        self.set_timer_var(timer_var)
        self.set_bit_4(bit_4)
        self.set_bit_5(bit_5)

    def render(self) -> bytearray:
        flags: int = bools_to_int(self.bit_4, self.bit_5)
        flags = flags << 12
        timer: self.timer_var << 14
        arg_byte: UInt16(self.event_id + timer + flags)
        return super().render(arg_byte)


class RunBackgroundEventWithPauseReturnOnExit(EventScriptCommand):
    _opcode: 0x45
    _size: int = 4
    _event_id: UInt16
    _timer_var: int
    _bit_4: bool
    _bit_5: bool

    @property
    def event_id(self) -> UInt16:
        return self._event_id

    def set_event_id(self, event_id: int) -> None:
        assert 0 <= event_id < TOTAL_SCRIPTS
        self._event_id = UInt16(event_id)

    @property
    def timer_var(self) -> int:
        return self._timer_var

    def set_timer_var(self, timer_var: int) -> None:
        assert timer_var in [0x701C, 0x701E, 0x7020, 0x7022]
        self._timer_var = timer_var

    @property
    def bit_4(self) -> bool:
        return self._bit_4

    def set_bit_4(self, bit_4: bool) -> None:
        self._bit_4 = bit_4

    @property
    def bit_5(self) -> bool:
        return self._bit_5

    def set_bit_5(self, bit_5: bool) -> None:
        self._bit_5 = bit_5

    def __init__(
        self,
        event_id: int,
        timer_var: int,
        bit_4: bool = False,
        bit_5: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_event_id(event_id)
        self.set_timer_var(timer_var)
        self.set_bit_4(bit_4)
        self.set_bit_5(bit_5)

    def render(self) -> bytearray:
        flags: int = bools_to_int(self.bit_4, self.bit_5)
        flags = flags << 12
        timer: self.timer_var << 14
        arg_byte: UInt16(self.event_id + timer + flags)
        return super().render(arg_byte)


class RunEventAtReturn(EventScriptCommand):
    _opcode = bytearray([0xFD, 0x46])
    _size: int = 4
    _event_id: UInt16

    @property
    def event_id(self) -> UInt16:
        return self._event_id

    def set_event_id(self, event_id: int) -> None:
        assert 0 <= event_id < TOTAL_SCRIPTS
        self._event_id = UInt16(event_id)

    def __init__(self, event_id: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_event_id(event_id)


class RunEventAsSubroutine(EventScriptCommand):
    _opcode: int = 0xD1
    _size: int = 3
    _event_id: UInt16

    @property
    def event_id(self) -> UInt16:
        return self._event_id

    def set_event_id(self, event_id: int) -> None:
        assert 0 <= event_id < TOTAL_SCRIPTS
        self._event_id = UInt16(event_id)

    def __init__(self, event_id: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_event_id(event_id)


class RememberLastObject(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x43])


class StopBackgroundEvent(EventScriptCommand):
    _opcode: int = 0x46
    _size: int = 2
    _timer_var: int

    @property
    def timer_var(self) -> int:
        return self._timer_var

    def set_timer_var(self, timer_var: int) -> None:
        assert timer_var in [0x701C, 0x701E, 0x7020, 0x7022]
        self._timer_var = timer_var

    def __init__(self, timer_var: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_timer_var(timer_var)

    def render(self) -> bytearray:
        timer_byte: int = (self.timer_var - 0x701C) // 2
        return super().render(timer_byte)


class Return(EventScriptCommandNoArgs):
    _opcode: int = 0xFE


class EndAll(EventScriptCommandNoArgs):
    _opcode: int = 0xFF


class Return_FD(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0xFE])


class Db(EventScriptCommand):
    _contents: bytearray

    @property
    def contents(self) -> bytearray:
        return self._contents

    def set_contents(self, contents: "int[int]") -> None:
        for b in contents:
            assert 0 <= b <= 0xFF
        self._contents = bytearray(contents)

    @property
    def size(self) -> int:
        return len(self.contents)

    def __init__(self, contents: "int[int]", identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_contents(contents)

    def render(self) -> bytearray:
        return super().render(self.contents)


# memory operations


class If0210Bits012ClearDoNotJump(EventScriptCommandWithJmps):
    _opcode = bytearray([0xFD, 0x62])
    _size: int = 4

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class If0210Bits012ClearDoNotJump(EventScriptCommandWithJmps):
    _opcode: int = 0x41
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIf7000AllBitsClear(EventScriptCommandWithJmps):
    _opcode: int = 0xE6
    _size: int = 5
    _bits: "set[int]"

    @property
    def bits(self) -> "set[int]":
        return self._bits

    def set_bits(self, bits: "str[int]") -> None:
        for bit in bits:
            assert 0 <= bit <= 15
        self._bits = bits

    def __init__(
        self,
        bits: "set[int]",
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_bits(bits)

    def render(self) -> bytearray:
        flags: UInt16(bits_to_int(self.bits))
        return super().render(flags, *self.destinations)


class JmpIf7000AnyBitsSet(EventScriptCommandWithJmps):
    _opcode: int = 0xE7
    _size: int = 5
    _bits: "set[int]"

    @property
    def bits(self) -> "set[int]":
        return self._bits

    def set_bits(self, bits: "set[int]") -> None:
        for bit in bits:
            assert 0 <= bit <= 15
        self._bits = bits

    def __init__(
        self,
        bits: "set[int]",
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_bits(bits)

    def render(self) -> bytearray:
        flags: UInt16(bits_to_int(self.bits))
        return super().render(flags, *self.destinations)


class JmpIfBitSet(EventScriptCommandWithJmps):
    _size: int = 4
    _bit: Flag

    @property
    def bit(self) -> Flag:
        return self._bit

    def set_bit(self, bit: Flag) -> None:
        self._bit = bit

    def __init__(
        self, bit: Flag, destinations: "str[int]", identifier: Optional[str] = None
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_bit(bit)

    def render(self) -> bytearray:
        if self.bit.byte >= 0x7080:
            opcode = UInt8(0xDA)
            offset = ShortVar(0x7080)
        elif self.bit.byte >= 0x7060:
            opcode = UInt8(0xD9)
            offset = ShortVar(0x7060)
        else:
            opcode = UInt8(0xD8)
            offset = ShortVar(0x7040)
        arg = UInt8(((self.bit.byte - offset) << 3) + self.bit.bit)
        return super().render(opcode, arg, *self.destinations)


class JmpIfBitClear(EventScriptCommandWithJmps):
    _size: int = 4
    _bit: Flag

    @property
    def bit(self) -> Flag:
        return self._bit

    def set_bit(self, bit: Flag) -> None:
        self._bit = bit

    def __init__(
        self, bit: Flag, destinations: "str[int]", identifier: Optional[str] = None
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_bit(bit)

    def render(self) -> bytearray:
        if self.bit.byte >= 0x7080:
            opcode = UInt8(0xDE)
            offset = ShortVar(0x7080)
        elif self.bit.byte >= 0x7060:
            opcode = UInt8(0xDD)
            offset = ShortVar(0x7060)
        else:
            opcode = UInt8(0xDC)
            offset = ShortVar(0x7040)
        arg = UInt8(((self.bit.byte - offset) << 3) + self.bit.bit)
        return super().render(opcode, arg, *self.destinations)


class JmpIfLoadedMemoryIs0(EventScriptCommandWithJmps):
    _opcode: int = 0xEA
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfLoadedMemoryIsAboveOrEqual0(EventScriptCommandWithJmps):
    _opcode: int = 0xEF
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfLoadedMemoryIsBelow0(EventScriptCommandWithJmps):
    _opcode: int = 0xEE
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfLoadedMemoryIsNot0(EventScriptCommandWithJmps):
    _opcode: int = 0xEB
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfMem704XAt7000BitSet(EventScriptCommandWithJmps):
    _opcode: 0xDB
    _size: int = 3

    def __init__(
        self, destinations: "str[int]", identifier: Optional[str] = None
    ) -> None:
        super().__init__(destinations, identifier)

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfMem704XAt7000BitClear(EventScriptCommandWithJmps):
    _size: int = 3
    _opcode: 0xDF

    def __init__(
        self, destinations: "str[int]", identifier: Optional[str] = None
    ) -> None:
        super().__init__(destinations, identifier)

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class SetMem704XAt7000Bit(EventScriptCommandNoArgs):
    _opcode: int = 0xA3


class ClearMem704XAt7000Bit(EventScriptCommandNoArgs):
    _opcode: int = 0xA7


class Move70107015To7016701B(EventScriptCommandNoArgs):
    _opcode: int = 0xBE


class Move7016701BTo70107015(EventScriptCommandNoArgs):
    _opcode: int = 0xBF


class SetVarToConst(EventScriptCommand):
    _value: Union[UInt8, UInt16]
    _address: Union[ShortVar, ByteVar]

    @property
    def value(self) -> Union[UInt8, UInt16]:
        return self._value

    def set_value(self, value: int) -> None:
        try:
            self.value = UInt8(value)
        except:
            self.value = UInt16(value)

    @property
    def address(self) -> Union[ShortVar, ByteVar]:
        return self._address

    def set_address(self, address: Union[UInt8, UInt16]) -> None:
        self._address = address
        if self.address == variables.PRIMARY_TEMP_7000 or isinstance(
            self.address, ByteVar
        ):
            self._size = 3
        else:
            self._size = 4

    def __init__(
        self, address: int, value: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_value(value)
        if isinstance(self.value, UInt8):
            try:
                self.set_address(ByteVar(address))
            except:
                self.set_address(ShortVar(address))
        else:
            self.set_address(ShortVar(address))

    def render(self) -> bytearray:
        if isinstance(self.address, ByteVar) and isinstance(self.value, UInt8):
            return super().render(0xA8, self.address, self.value)
        elif self.address == variables.PRIMARY_TEMP_7000:
            return super().render(0xAC, UInt16(self.value))
        elif isinstance(self.address, ShortVar):
            return super().render(0xB0, self.address, UInt16(self.value))
        else:
            raise Exception(
                "illegal args for %s: 0x%02x %r:"
                % (self.identifier.name, self.address, self.value)
            )


class ReadFromAddress(EventScriptCommand):
    _opcode: int = 0x5C
    _size: int = 3
    _address = UInt16

    @property
    def address(self) -> UInt16:
        return self._address

    def set_address(self, address: int) -> None:
        self._address = UInt16(address)

    def __init__(self, address: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_address(address)

    def render(self) -> bytearray:
        super().render(self.address)


class Set7000To7FMemVar(EventScriptCommand):
    _opcode = bytearray([0xFD, 0xAC])
    _size: int = 4
    _address = UInt16

    @property
    def address(self) -> UInt16:
        return self._address

    def set_address(self, address: int) -> None:
        assert int >= 0xF800
        self._address = UInt16(address)

    def __init__(self, address: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_address(address)

    def render(self) -> bytearray:
        super().render(self.address - 0xF800)


class SetBit(EventScriptCommand):
    _size: int = 2
    _bit: Flag

    @property
    def bit(self) -> Flag:
        return self._bit

    def set_bit(self, bit: Flag) -> None:
        self._bit = bit

    def __init__(self, bit: Flag, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_bit(bit)

    def render(self) -> bytearray:
        if self.bit.byte >= 0x7080:
            opcode = UInt8(0xA2)
            offset = ShortVar(0x7080)
        elif self.bit.byte >= 0x7060:
            opcode = UInt8(0xA1)
            offset = ShortVar(0x7060)
        else:
            opcode = UInt8(0xA0)
            offset = ShortVar(0x7040)
        arg = UInt8(((self.bit.byte - offset) << 3) + self.bit.bit)
        return super().render(opcode, arg)


class ClearBit(EventScriptCommand):
    _size: int = 2
    _bit: Flag

    @property
    def bit(self) -> Flag:
        return self._bit

    def set_bit(self, bit: Flag) -> None:
        self._bit = bit

    def __init__(self, bit: Flag, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_bit(bit)

    def render(self) -> bytearray:
        if self.bit.byte >= 0x7080:
            opcode = UInt8(0xA6)
            offset = ShortVar(0x7080)
        elif self.bit.byte >= 0x7060:
            opcode = UInt8(0xA5)
            offset = ShortVar(0x7060)
        else:
            opcode = UInt8(0xA4)
            offset = ShortVar(0x7040)
        arg = UInt8(((self.bit.byte - offset) << 3) + self.bit.bit)
        return super().render(opcode, arg)


class Set01D8Bit3(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0xFA])


class Set0158Bit3Offset(EventScriptCommand):
    _opcode = bytearray([0xFD, 0x8B])
    _size: int = 3
    _address: UInt16

    @property
    def address(self) -> UInt16:
        return self._address

    def set_address(self, address: int) -> None:
        assert address % 2 == 0 and address >= 0x0158
        self._address = UInt16(address)

    def __init__(self, address: int, identifier: Optional[str] = None):
        super().__init__(identifier)
        self.set_address(address)

    def render(self) -> bytearray:
        address_byte = (self.address - 0x0158) // 2
        address_byte &= 0x7F
        return super().render(address_byte)


class Set0158Bit7Offset(EventScriptCommand):
    _opcode = bytearray([0xFD, 0x88])
    _size: int = 3
    _address: UInt16
    _bit_7: bool

    @property
    def address(self) -> UInt16:
        return self._address

    def set_address(self, address: int) -> None:
        assert address % 2 == 0 and address >= 0x0158
        self._address = UInt16(address)

    @property
    def bit_7(self) -> bool:
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        self._bit_7 = bit_7

    def __init__(
        self, address: int, bit_7: bool = False, identifier: Optional[str] = None
    ):
        super().__init__(identifier)
        self.set_address(address)
        self.set_bit_7(bit_7)

    def render(self) -> bytearray:
        address_byte = (self.address - 0x0158) // 2
        address_byte &= 0x7F
        address_byte += self.bit_7 << 7
        return super().render(address_byte)


class Clear0158Bit7Offset(EventScriptCommand):
    _opcode = bytearray([0xFD, 0x89])
    _size: int = 3
    _address: UInt16
    _bit_7: bool

    @property
    def address(self) -> UInt16:
        return self._address

    def set_address(self, address: int) -> None:
        assert address % 2 == 0 and address >= 0x0158
        self._address = UInt16(address)

    @property
    def bit_7(self) -> bool:
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        self._bit_7 = bit_7

    def __init__(
        self, address: int, bit_7: bool = False, identifier: Optional[str] = None
    ):
        super().__init__(identifier)
        self.set_address(address)
        self.set_bit_7(bit_7)

    def render(self) -> bytearray:
        address_byte = (self.address - 0x0158) // 2
        address_byte &= 0x7F
        address_byte += self.bit_7 << 7
        return super().render(address_byte)


class Clear7016To7018AndIsolate701AHighByteIf7018Bit0Set(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0xC6])


class CopyVarToVar(EventScriptCommand):
    _address_left: Union[ShortVar, ByteVar]
    _address_right: Union[ShortVar, ByteVar]

    def _set_size(self):
        if (
            self.address_left != variables.PRIMARY_TEMP_7000
            and self.address_right != variables.PRIMARY_TEMP_7000
        ):
            self._size = 3
        else:
            self._size = 2

    @property
    def address_left(self) -> Union[ShortVar, ByteVar]:
        return self._address_left

    def set_address_left(self, address_left: Union[ShortVar, ByteVar]) -> None:
        self._address_left = address_left
        self._set_size()

    def cast_address_left(self, address_left: int) -> None:
        self.set_address_left(cast_address(address_left))

    @property
    def address_right(self) -> Union[ShortVar, ByteVar]:
        return self._address_right

    def set_address_right(self, address_right: int) -> None:
        self._address_right = cast_address(address_right)
        self._set_size()

    def cast_address_right(self, address_right: int) -> None:
        self.set_address_right(cast_address(address_right))

    def __init__(
        self,
        address_left: int,
        address_right: int,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        if address_left == variables.PRIMARY_TEMP_7000:
            self.set_address_left(ShortVar(address_left))
            self.cast_address_right(address_right)
        elif address_right == variables.PRIMARY_TEMP_7000:
            self.cast_address_left(address_left)
            self.set_address_right(ShortVar(address_right))
        else:
            self.set_address_left(ShortVar(address_left))
            self.set_address_right(ShortVar(address_right))

    def render(self) -> bytearray:
        if self.address_right == variables.PRIMARY_TEMP_7000 and isinstance(
            self.address_left, ByteVar
        ):
            return super().render(0xB4, self.address_left)
        elif self.address_left == variables.PRIMARY_TEMP_7000 and isinstance(
            self.address_right, ByteVar
        ):
            return super().render(0xB5, self.address_right)
        elif self.address_right == variables.PRIMARY_TEMP_7000 and isinstance(
            self.address_left, ShortVar
        ):
            return super().render(0xBA, self.address_left)
        elif self.address_left == variables.PRIMARY_TEMP_7000 and isinstance(
            self.address_right, ShortVar
        ):
            return super().render(0xBB, self.address_right)
        elif isinstance(self.address_left, ShortVar) and isinstance(
            self.address_right, ShortVar
        ):
            return super().render(0xBC, self.address_left, self.address_right)
        else:
            raise Exception(
                "illegal args for %s: 0x%04x 0x%04x:"
                % (self.identifier.name, self.address_left, self.address_right)
            )


class StoreBytesTo0335And0556(EventScriptCommand):
    _opcode = bytearray([0xFD, 0x90])
    _size: int = 4
    _value_1: UInt8
    _value_2: UInt8

    @property
    def value_1(self) -> UInt8:
        return self._value_1

    def set_value_1(self, value_1: int) -> None:
        self._value_1 = UInt8(value_1)

    @property
    def value_2(self) -> UInt8:
        return self._value_2

    def set_value_2(self, value_2: int) -> None:
        self._value_2 = UInt8(value_2)

    def __init__(
        self, value_1: int, value_2: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_value_1(value_1)
        self.set_value_2(value_2)

    def render(self) -> bytearray:
        return super().render(self.value_1, self.value_2)


class Store00To0248(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0xFC])


class Store00To0334(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x93])


class Store01To0248(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0xFB])


class Store01To0335(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x92])


class Store02To0248(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0xFD])


class StoreFFTo0335(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x91])


class Set7000ToMinecartTimer(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0xB8])


class StoreSetBits(EventScriptCommand):
    _size: int = 3
    _bit: Flag

    @property
    def bit(self) -> Flag:
        return self._bit

    def set_bit(self, bit: Flag) -> None:
        self._bit = bit

    def __init__(self, bit: Flag, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_bit(bit)

    def render(self) -> bytearray:
        if self.bit.byte >= 0x7080:
            opcode = bytearray([0xFD, 0xAA])
            offset = ShortVar(0x7080)
        elif self.bit.byte >= 0x7060:
            opcode = bytearray([0xFD, 0xA9])
            offset = ShortVar(0x7060)
        else:
            opcode = bytearray([0xFD, 0xA8])
            offset = ShortVar(0x7040)
        arg = UInt8(((self.bit.byte - offset) << 3) + self.bit.bit)
        return super().render(opcode, arg)


class SwapVars(EventScriptCommand):
    _opcode: int = 0xBD
    _size: int = 3
    _address_left: ShortVar
    _address_right: ShortVar

    @property
    def address_left(self) -> ShortVar:
        return self._address_left

    def set_address_left(self, address_left: int) -> None:
        self._address_left = ShortVar(address_left)

    @property
    def address_right(self) -> ShortVar:
        return self._address_right

    def set_address_right(self, address_right: int) -> None:
        self._address_right = ShortVar(address_right)

    def __init__(
        self,
        address_left: int,
        address_right: int,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_address_left(address_left)
        self.set_address_right(address_right)

    def render(self) -> bytearray:
        return super().render(self.address_left, self.address_right)


# math operations


class AddConstToVar(EventScriptCommand):
    _value: Union[UInt8, UInt16]
    _address: Union[ShortVar, ByteVar]

    @property
    def value(self) -> Union[UInt8, UInt16]:
        return self._value

    def set_value(self, value: int) -> None:
        try:
            self.value = UInt8(value)
        except:
            self.value = UInt16(value)

    @property
    def address(self) -> Union[ShortVar, ByteVar]:
        return self._address

    def set_address(self, address: Union[UInt8, UInt16]) -> None:
        self._address = address
        if self.address == variables.PRIMARY_TEMP_7000 or isinstance(
            self.address, ByteVar
        ):
            self._size = 3
        else:
            self._size = 4

    def __init__(
        self, address: int, value: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_value(value)
        if isinstance(self.value, UInt8):
            try:
                self.set_address(ByteVar(address))
            except:
                self.set_address(ShortVar(address))
        else:
            self.set_address(ShortVar(address))

    def render(self) -> bytearray:
        if isinstance(self.address, ByteVar) and isinstance(self.value, UInt8):
            return super().render(0xA9, self.address, self.value)
        elif self.address == variables.PRIMARY_TEMP_7000:
            return super().render(0xAD, UInt16(self.value))
        elif isinstance(self.address, ShortVar):
            return super().render(0xB1, self.address, UInt16(self.value))
        else:
            raise Exception(
                "illegal args for %s: 0x%02x %r:"
                % (self.identifier.name, self.address, self.value)
            )


class Inc(EventScriptCommandAnySizeMem):
    def render(self) -> bytearray:
        if isinstance(self.address, ByteVar):
            return super().render(0xAA, self.address)
        elif self.address == variables.PRIMARY_TEMP_7000:
            return super().render(0xAE)
        elif isinstance(self.address, ShortVar):
            return super().render(0xB2, self.address)
        else:
            raise Exception(
                "illegal args for %s: 0x%02x:" % (self.identifier.name, self.address)
            )


class Dec(EventScriptCommandAnySizeMem):
    def render(self) -> bytearray:
        if isinstance(self.address, ByteVar):
            return super().render(0xAB, self.address)
        elif self.address == variables.PRIMARY_TEMP_7000:
            return super().render(0xAF)
        elif isinstance(self.address, ShortVar):
            return super().render(0xB3, self.address)
        else:
            raise Exception(
                "illegal args for %s: 0x%02x:" % (self.identifier.name, self.address)
            )


class AddVarTo7000(EventScriptCommandShortMem):
    _opcode: int = 0xB8
    _size: int = 2


class DecVarFrom7000(EventScriptCommandShortMem):
    _opcode: int = 0xB9
    _size: int = 2


class GenerateRandomNumFromRangeVar(EventScriptCommandShortMem):
    _opcode = bytearray(0xFD, 0x62)
    _size: int = 3


class JmpIfRandomAbove66(EventScriptCommandWithJmps):
    _opcode: int = 0xE9
    _size: int = 5

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfRandomAbove128(EventScriptCommandWithJmps):
    _opcode: int = 0xE8
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class SetVarToRandom(EventScriptCommandShortAddrAndValueOnly):
    def render(self) -> bytearray:
        if self.address == variables.PRIMARY_TEMP_7000:
            return super().render(0xB6, self.value)
        else:
            return super().render(0xB7, self.address, self.value)


class CompareVarToConst(EventScriptCommandShortAddrAndValueOnly):
    def render(self) -> bytearray:
        if self.address == variables.PRIMARY_TEMP_7000:
            return super().render(0xC0, self.value)
        else:
            return super().render(0xC2, self.address, self.value)


class Compare7000ToVar(EventScriptCommandShortMem):
    _opcode: int = 0xC1
    _size: int = 2

    def render(self) -> bytearray:
        return super().render(self.address)


class JmpIfComparisonResultIsGreaterOrEqual(EventScriptCommandWithJmps):
    _opcode: int = 0xEC
    _size = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfComparisonResultIsLesser(EventScriptCommandWithJmps):
    _opcode: int = 0xED
    _size = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfVarEqualsConst(EventScriptCommandWithJmps):
    _value: Union[UInt8, UInt16]
    _address: Union[ShortVar, ByteVar]

    @property
    def value(self) -> Union[UInt8, UInt16]:
        return self._value

    def set_value(self, value: int) -> None:
        try:
            self.value = UInt8(value)
        except:
            self.value = UInt16(value)

    @property
    def address(self) -> Union[ShortVar, ByteVar]:
        return self._address

    def set_address(self, address: Union[UInt8, UInt16]) -> None:
        self._address = address
        if self.address == variables.PRIMARY_TEMP_7000 or isinstance(
            self.address, ByteVar
        ):
            self._size = 5
        else:
            self._size = 6

    def __init__(
        self,
        address: int,
        value: int,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_value(value)
        if isinstance(self.value, UInt8):
            try:
                self.set_address(ByteVar(address))
            except:
                self.set_address(ShortVar(address))
        else:
            self.set_address(ShortVar(address))

    def render(self) -> bytearray:
        if isinstance(self.address, ByteVar) and isinstance(self.value, UInt8):
            return super().render(0xE0, self.address, self.value, *self.destinations)
        elif self.address == variables.PRIMARY_TEMP_7000:
            return super().render(0xE2, UInt16(self.value), *self.destinations)
        elif isinstance(self.address, ShortVar):
            return super().render(
                0xE4, self.address, UInt16(self.value), *self.destinations
            )
        else:
            raise Exception(
                "illegal args for %s: 0x%02x %r:"
                % (self.identifier.name, self.address, self.value)
            )


class JmpIfVarNotEqualsConst(EventScriptCommandWithJmps):
    _value: Union[UInt8, UInt16]
    _address: Union[ShortVar, ByteVar]

    @property
    def value(self) -> Union[UInt8, UInt16]:
        return self._value

    def set_value(self, value: int) -> None:
        try:
            self.value = UInt8(value)
        except:
            self.value = UInt16(value)

    @property
    def address(self) -> Union[ShortVar, ByteVar]:
        return self._address

    def set_address(self, address: Union[UInt8, UInt16]) -> None:
        self._address = address
        if self.address == variables.PRIMARY_TEMP_7000 or isinstance(
            self.address, ByteVar
        ):
            self._size = 5
        else:
            self._size = 6

    def __init__(
        self,
        address: int,
        value: int,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_value(value)
        if isinstance(self.value, UInt8):
            try:
                self.set_address(ByteVar(address))
            except:
                self.set_address(ShortVar(address))
        else:
            self.set_address(ShortVar(address))

    def render(self) -> bytearray:
        if isinstance(self.address, ByteVar) and isinstance(self.value, UInt8):
            return super().render(0xE1, self.address, self.value, *self.destinations)
        elif self.address == variables.PRIMARY_TEMP_7000:
            return super().render(0xE3, UInt16(self.value), *self.destinations)
        elif isinstance(self.address, ShortVar):
            return super().render(
                0xE5, self.address, UInt16(self.value), *self.destinations
            )
        else:
            raise Exception(
                "illegal args for %s: 0x%02x %r:"
                % (self.identifier.name, self.address, self.value)
            )


class Mem7000AndConst(EventScriptCommandBasicShortOperation):
    _opcode = bytearray([0xFD, 0xB0])


class Mem7000AndVar(EventScriptCommandShortMem):
    _opcode = bytearray([0xFD, 0xB3])
    _size: int = 3


class Mem7000OrConst(EventScriptCommandBasicShortOperation):
    _opcode = bytearray([0xFD, 0xB1])


class Mem7000OrVar(EventScriptCommandShortMem):
    _opcode = bytearray([0xFD, 0xB4])
    _size: int = 3


class Mem7000XorConst(EventScriptCommandBasicShortOperation):
    _opcode = bytearray([0xFD, 0xB2])


class Mem7000XorVar(EventScriptCommandShortMem):
    _opcode = bytearray([0xFD, 0xB5])
    _size: int = 3


class VarShiftLeft(EventScriptCommand):
    _opcode = bytearray([0xFD, 0xB6])
    _size: int = 4
    _address: ShortVar
    _shift: UInt8

    @property
    def address(self) -> ShortVar:
        return self._address

    def set_address(self, address: int) -> None:
        self._address = ShortVar(address)

    @property
    def shift(self) -> UInt8:
        return self._shift

    def set_shift(self, shift: int) -> None:
        self._shift = UInt8(shift)

    def __init__(
        self, address: int, shift: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_address(address)
        self.set_shift(shift)

    def render(self) -> bytearray:
        return super().render(self.address, self.shift)


class MultiplyAndAddMem3148StoreToOffsrt7fB000PlusOutputX2(EventScriptCommand):
    _opcode = bytearray([0xFD, 0xC8])
    _size: int = 4
    _adding: UInt8
    _multiplying: UInt8

    @property
    def adding(self) -> UInt8:
        return self._adding

    def set_adding(self, adding: int) -> None:
        self._adding = UInt8(adding)

    @property
    def multiplying(self) -> UInt8:
        return self._multiplying

    def set_multiplying(self, multiplying: int) -> None:
        self._multiplying = UInt8(multiplying)

    def __init__(
        self, adding: int, multiplying: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_adding(adding)
        self.set_multiplying(multiplying)

    def render(self) -> bytearray:
        return super().render(self.adding, self.multiplying)


class Xor3105With01(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0xFE])


# room objects & camera


class ActionQueue(ActionQueuePrototype):
    pass


class StartEmbeddedActionScript(StartEmbeddedActionScriptPrototype):
    pass


class NonEmbeddedActionQueue(NonEmbeddedActionQueuePrototype):
    pass


class SetActionScript(EventScriptCommand):
    _size: int = 4
    _target: AreaObject
    _sync: bool
    _action_script_id: UInt16

    @property
    def target(self) -> AreaObject:
        return self._target

    def set_target(self, target: AreaObject) -> None:
        self._target = target

    @property
    def sync(self) -> bool:
        return self._sync

    def set_sync(self, sync: bool) -> None:
        self._sync = sync

    @property
    def action_script_id(self) -> UInt16:
        return self._action_script_id

    def set_action_script_id(self, action_script_id: int) -> None:
        assert 0 <= action_script_id < TOTAL_ACTION_SCRIPTS
        self._action_script_id = UInt16(action_script_id)

    def __init__(
        self,
        target: AreaObject,
        action_script_id: int,
        sync: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_target(target)
        self.set_sync(sync)
        self.set_action_script_id(action_script_id)

    def render(self) -> bytearray:
        header_byte: int = (not self.sync) + 0xF2
        return super().render(self.target, header_byte, self.action_script_id)


class SetTempActionScript(EventScriptCommand):
    _size: int = 4
    _target: AreaObject
    _sync: bool
    _action_script_id: UInt16

    @property
    def target(self) -> AreaObject:
        return self._target

    def set_target(self, target: AreaObject) -> None:
        self._target = target

    @property
    def sync(self) -> bool:
        return self._sync

    def set_sync(self, sync: bool) -> None:
        self._sync = sync

    @property
    def action_script_id(self) -> UInt16:
        return self._action_script_id

    def set_action_script_id(self, action_script_id: int) -> None:
        assert 0 <= action_script_id < TOTAL_ACTION_SCRIPTS
        self._action_script_id = UInt16(action_script_id)

    def __init__(
        self,
        target: AreaObject,
        action_script_id: int,
        sync: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_target(target)
        self.set_sync(sync)
        self.set_action_script_id(action_script_id)

    def render(self) -> bytearray:
        header_byte: int = (not self.sync) + 0xF4
        return super().render(self.target, header_byte, self.action_script_id)


class UnsyncActionScript(EventScriptCommand):
    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        return self._target

    def set_target(self, target: AreaObject) -> None:
        self._target = target

    def __init__(self, target: AreaObject, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self) -> bytearray:
        return super().render(self.target, 0xF6)


class SummonObjectToSpecificLevel(EventScriptCommand):
    _opcode: int = 0xF2
    _size: int = 3
    _object: AreaObject
    _level_id: UInt16

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    @property
    def level_id(self) -> UInt16:
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self, object: AreaObject, level_id: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_object(object)
        self.set_level_id(level_id)

    def render(self) -> bytearray:
        arg: int = UInt16(self.level_id + (self.object << 9) + (1 << 15))
        return super().render(arg)


class SummonObjectToCurrentLevel(EventScriptCommand):
    _size: int = 2
    _object: AreaObject

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    def __init__(self, object: AreaObject, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_object(object)

    def render(self) -> bytearray:
        return super().render(self.object, 0xF8)


class SummonObjectToCurrentLevelAtMariosCoords(EventScriptCommand):
    _size: int = 2
    _object: AreaObject

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    def __init__(self, object: AreaObject, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_object(object)

    def render(self) -> bytearray:
        return super().render(self.object, 0xF7)


class SummonObjectAt70A8ToCurrentLevel(EventScriptCommandNoArgs):
    _opcode: int = 0xF4


class RemoveObjectFromSpecificLevel(EventScriptCommand):
    _opcode: int = 0xF2
    _size: int = 3
    _object: AreaObject
    _level_id: UInt16

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    @property
    def level_id(self) -> UInt16:
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self, object: AreaObject, level_id: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_object(object)
        self.set_level_id(level_id)

    def render(self) -> bytearray:
        arg_raw = self.level_id + (self.object << 9)
        assert 0 <= arg_raw <= 0x7FFF
        arg: int = UInt16(arg_raw)
        return super().render(arg)


class RemoveObjectFromCurrentLevel(EventScriptCommand):
    _size: int = 2
    _object: AreaObject

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    def __init__(self, object: AreaObject, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_object(object)

    def render(self) -> bytearray:
        return super().render(self.object, 0xF9)


class RemoveObjectAt70A8FromCurrentLevel(EventScriptCommandNoArgs):
    _opcode: int = 0xF5


class PauseActionScript(EventScriptCommand):
    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        return self._target

    def set_target(self, target: AreaObject) -> None:
        self._target = target

    def __init__(self, target: AreaObject, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self) -> bytearray:
        return super().render(self.target, 0xFA)


class ResumeActionScript(EventScriptCommand):
    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        return self._target

    def set_target(self, target: AreaObject) -> None:
        self._target = target

    def __init__(self, target: AreaObject, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_targe(target)

    def render(self) -> bytearray:
        return super().render(self.target, 0xFB)


class EnableObjectTrigger(EventScriptCommand):
    _size: int = 2
    _object: AreaObject

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    def __init__(self, object: AreaObject, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_object(object)

    def render(self) -> bytearray:
        return super().render(self.object, 0xFC)


class DisableObjectTrigger(EventScriptCommand):
    _size: int = 2
    _object: AreaObject

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    def __init__(self, object: AreaObject, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_object(object)

    def render(self) -> bytearray:
        return super().render(self.object, 0xFD)


class DisableObjectTriggerInSpecificLevel(EventScriptCommand):
    _opcode: int = 0xF3
    _size: int = 3
    _object: AreaObject
    _level_id: UInt16

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    @property
    def level_id(self) -> UInt16:
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self, object: AreaObject, level_id: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_object(object)
        self.set_level_id(level_id)

    def render(self) -> bytearray:
        arg_raw = self.level_id + (self.object << 9)
        assert 0 <= arg_raw <= 0x7FFF
        arg: int = UInt16(arg_raw)
        return super().render(arg)


class DisableTriggerOfObjectAt70A8InCurrentLevel(EventScriptCommandNoArgs):
    _opcode: int = 0xF7


class StopEmbeddedActionScript(EventScriptCommand):
    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        return self._target

    def set_target(self, target: AreaObject) -> None:
        self._target = target

    def __init__(self, target: AreaObject, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_targe(target)

    def render(self) -> bytearray:
        return super().render(self.target, 0xFE)


class ResetCoords(EventScriptCommand):
    _size: int = 2
    _object: AreaObject

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    def __init__(self, object: AreaObject, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_object(object)

    def render(self) -> bytearray:
        return super().render(self.object, 0xFF)


class CreatePacketAtNPCCoords(EventScriptCommandWithJmps):
    _opcode: int = 0x3E
    _size: int = 5
    _packet_id: int
    _object: AreaObject

    @property
    def packet_id(self) -> UInt8:
        return self._packet_id

    def set_packet_id(self, packet_id: int) -> None:
        self._packet_id = UInt8(packet_id)

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    def __init__(
        self,
        packet: Packet,
        object: AreaObject,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_packet_id(packet.id)
        self.set_object(object)

    def render(self) -> bytearray:
        return super().render(self.packet_id, self.object, *self.destinations)


class CreatePacketAt7010(EventScriptCommandWithJmps):
    _opcode: int = 0x3F
    _size: int = 4
    _packet_id: UInt8

    @property
    def packet_id(self) -> UInt8:
        return self._packet_id

    def set_packet_id(self, packet_id: int) -> None:
        self._packet_id = UInt8(packet_id)

    def __init__(
        self, packet: Packet, destinations: "str[int]", identifier: Optional[str] = None
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_packet_id(packet.id)

    def render(self) -> bytearray:
        return super().render(self.packet_id, *self.destinations)


class CreatePacketAt7010WithEvent(EventScriptCommandWithJmps):
    _opcode: bytearray([0xFD, 0x3E])
    _size: int = 7
    _packet_id: UInt8
    _event_id: UInt16

    @property
    def packet_id(self) -> UInt8:
        return self._packet_id

    def set_packet_id(self, packet_id: int) -> None:
        self._packet_id = UInt8(packet_id)

    @property
    def event_id(self) -> UInt16:
        return self._event_id

    def set_event_id(self, event_id: int) -> None:
        assert 0 <= event_id < TOTAL_SCRIPTS
        self._event_id = UInt16(event_id)

    def __init__(
        self,
        packet: Packet,
        event_id: int,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_packet_id(packet.id)
        self.set_event_id(event_id)

    def render(self) -> bytearray:
        return super().render(self.packet_id, self.event_id, *self.destinations)


class FreezeAllNPCsUntilReturn(EventScriptCommandNoArgs):
    _opcode: int = 0x30


class UnfreezeAllNPCs(EventScriptCommandNoArgs):
    _opcode: int = 0x31


class FreezeCamera(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x31])


class JmpIfMarioOnObject(EventScriptCommandWithJmps):
    _opcode: int = 0x39
    _size: int = 4
    _object: AreaObject

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    def __init__(
        self,
        object: AreaObject,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_object(object)

    def render(self) -> bytearray:
        return super().render(self._object, *self.destinations)


class JmpIfMarioOnAnObjectOrNot(EventScriptCommandWithJmps):
    _opcode: int = 0x42
    _size: int = 5

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfObjectInAir(EventScriptCommandWithJmps):
    _opcode: bytearray([0xFD, 0x3D])
    _size: int = 5
    _object: AreaObject

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    def __init__(
        self,
        object: AreaObject,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_object(object)

    def render(self) -> bytearray:
        return super().render(self._object, *self.destinations)


class JmpIfObjectInSpecificLevel(EventScriptCommandWithJmps):
    _opcode: int = 0xF8
    _size: int = 5
    _object: AreaObject
    _level_id: UInt16

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    @property
    def level_id(self) -> UInt16:
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self,
        object: AreaObject,
        level_id: int,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_object(object)
        self.set_level_id(level_id)

    def render(self) -> bytearray:
        arg = UInt16(0x8000 + (self.object << 9) + self.level_id)
        return super().render(arg, *self.destinations)


class JmpIfObjectInCurrentLevel(EventScriptCommandWithJmps):
    _opcode: int = 0x32
    _size: int = 4
    _object: AreaObject

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    def __init__(
        self,
        object: AreaObject,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_object(object)

    def render(self) -> bytearray:
        return super().render(self.object, *self.destinations)


class JmpIfObjectNotInSpecificLevel(EventScriptCommandWithJmps):
    _opcode: int = 0xF8
    _size: int = 5
    _object: AreaObject
    _level_id: UInt16

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    @property
    def level_id(self) -> UInt16:
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self,
        object: AreaObject,
        level_id: int,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_object(object)
        self.set_level_id(level_id)

    def render(self) -> bytearray:
        arg = UInt16((self.object << 9) + self.level_id)
        assert 0 <= arg <= 0x7FFF
        return super().render(arg, *self.destinations)


class JmpIfObjectTriggerEnabledInSpecificLevel(EventScriptCommandWithJmps):
    _opcode = bytearray([0xFD, 0xF0])
    _size: int = 6
    _object: AreaObject
    _level_id: UInt16

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    @property
    def level_id(self) -> UInt16:
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self,
        object: AreaObject,
        level_id: int,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_object(object)
        self.set_level_id(level_id)

    def render(self) -> bytearray:
        arg: int = UInt16(self.level_id + (self.object << 9) + (1 << 15))
        return super().render(arg, *self.destinations)


class JmpIfObjectTriggerDisabledInSpecificLevel(EventScriptCommandWithJmps):
    _opcode = bytearray([0xFD, 0xF0])
    _size: int = 6
    _object: AreaObject
    _level_id: UInt16

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    @property
    def level_id(self) -> UInt16:
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self,
        object: AreaObject,
        level_id: int,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_object(object)
        self.set_level_id(level_id)

    def render(self) -> bytearray:
        arg = UInt16((self.object << 9) + self.level_id)
        assert 0 <= arg <= 0x7FFF
        return super().render(arg, *self.destinations)


class JmpIfObjectIsUnderwater(EventScriptCommandWithJmps):
    _opcode = bytearray([0xFD, 0x34])
    _size: int = 5
    _object: AreaObject

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    def __init__(
        self,
        object: AreaObject,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_object(object)

    def render(self) -> bytearray:
        return super().render(self.object, *self.destinations)


class JmpIfObjectActionScriptIsRunning(EventScriptCommandWithJmps):
    _opcode = bytearray([0xFD, 0x33])
    _size: int = 5
    _object: AreaObject

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    def __init__(
        self,
        object: AreaObject,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_object(object)

    def render(self) -> bytearray:
        return super().render(self.object, *self.destinations)


class JmpIfObjectsAreLessThanXYStepsApart(EventScriptCommandWithJmps):
    _opcode: int = 0x3A
    _size: int = 7
    _object_1: AreaObject
    _object_2: AreaObject
    _x: UInt8
    _y: UInt8

    @property
    def object_1(self) -> AreaObject:
        return self._object_1

    def set_object_1(self, object_1: AreaObject) -> None:
        self._object_1 = object_1

    @property
    def object_2(self) -> AreaObject:
        return self._object_2

    @property
    def x(self) -> UInt8:
        return self._x

    def set_x(self, x: int) -> None:
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        return self._y

    def set_y(self, y: int) -> None:
        self._y = UInt8(y)

    def __init__(
        self,
        object_1: AreaObject,
        object_2: AreaObject,
        x: int,
        y: int,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_object_1(object_1)
        self.set_object_2(object_2)
        self.set_x(x)
        self.set_y(y)


class JmpIfObjectsAreLessThanXYStepsApartSameZCoord(EventScriptCommandWithJmps):
    _opcode: int = 0x3B
    _size: int = 7
    _object_1: AreaObject
    _object_2: AreaObject
    _x: UInt8
    _y: UInt8

    @property
    def object_1(self) -> AreaObject:
        return self._object_1

    def set_object_1(self, object_1: AreaObject) -> None:
        self._object_1 = object_1

    @property
    def object_2(self) -> AreaObject:
        return self._object_2

    @property
    def x(self) -> UInt8:
        return self._x

    def set_x(self, x: int) -> None:
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        return self._y

    def set_y(self, y: int) -> None:
        self._y = UInt8(y)

    def __init__(
        self,
        object_1: AreaObject,
        object_2: AreaObject,
        x: int,
        y: int,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_object_1(object_1)
        self.set_object_2(object_2)
        self.set_x(x)
        self.set_y(y)


class ReactivateObject70A8TriggerIfMarioOnTopOfIt(EventScriptCommandNoArgs):
    _opcode: int = 0x5D


class Set700CToObjectCoord(EventScriptCommand):
    _size: int = 2
    _object: AreaObject
    _coord: Coord
    _is_isometric_not_pixel: bool = False
    _bit_7: bool = False

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    @property
    def coord(self) -> Coord:
        return self._coord

    def set_coord(self, coord: Coord) -> None:
        assert coord != coords.F
        self._coord = coord

    @property
    def is_isometric_not_pixel(self) -> bool:
        return self._is_isometric_not_pixel

    def set_is_isometric_not_pixel(self, is_isometric_not_pixel: bool) -> None:
        self._is_isometric_not_pixel = is_isometric_not_pixel

    @property
    def bit_7(self) -> bool:
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        self._bit_7 = bit_7

    def __init__(
        self,
        object: AreaObject,
        coord: Coord,
        isometric: bool = False,
        pixel: bool = False,
        bit_7: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        assert isometric ^ pixel
        super().__init__(identifier)
        self.set_object(object)
        self.set_coord(coord)
        self.set_is_isometric_not_pixel(isometric)
        self.set_bit_7(bit_7)

    def render(self) -> bytearray:
        opcode = UInt8(0xC4 + self.coord)
        arg = UInt8(
            (self.bit_7 << 7) + (self.is_isometric_not_pixel << 6) + self.object
        )
        return super().render(opcode, arg)


class Set70107015ToObjectXYZ(EventScriptCommand):
    _opcode: int = 0xC7
    _size: int = 2
    _object: AreaObject

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    def __init__(
        self,
        object: AreaObject,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_object(object)

    def render(self) -> bytearray:
        return super().render(self.object)


class Set7016701BToObjectXYZ(EventScriptCommand):
    _opcode: int = 0xC8
    _size: int = 2
    _object: AreaObject

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    def __init__(
        self,
        object: AreaObject,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_object(object)

    def render(self) -> bytearray:
        return super().render(self.object)


class SetObjectMemoryToVar(EventScriptCommandShortMem):
    _opcode: int = 0xD6
    _size: int = 2


# controls


class EnableControls(EventScriptCommand):
    _opcode: int = 0x35
    _size: int = 2
    _enabled_buttons: "set[ControllerInput]"

    @property
    def enabled_buttons(self) -> "set[ControllerInput]":
        return self._enabled_buttons

    def set_enabled_buttons(self, enabled_buttons: "set[ControllerInput]") -> None:
        self._enabled_buttons = enabled_buttons

    def __init__(
        self,
        enabled_buttons: "set[ControllerInput]" = [],
        identifier: Optional[str] = None,
    ):
        super.__init__(identifier)
        self.set_enabled_buttons(enabled_buttons)

    def render(self) -> bytearray:
        buttons_as_ints: "set[int]" = cast(
            "int[int]", [int(b) for b in self.enabled_buttons]
        )
        arg: int = bits_to_int(buttons_as_ints)
        return super().render(arg)


class EnableControlsUntilReturn(EventScriptCommand):
    _opcode: int = 0x34
    _size: int = 2
    _enabled_buttons: "set[ControllerInput]"

    @property
    def enabled_buttons(self) -> "set[ControllerInput]":
        return self._enabled_buttons

    def set_enabled_buttons(self, enabled_buttons: "set[ControllerInput]") -> None:
        self._enabled_buttons = enabled_buttons

    def __init__(
        self,
        enabled_buttons: "set[ControllerInput]" = [],
        identifier: Optional[str] = None,
    ):
        super.__init__(identifier)
        self.set_enabled_buttons(enabled_buttons)

    def render(self) -> bytearray:
        buttons_as_ints: "set[int]" = cast(
            "int[int]", [int(b) for b in self.enabled_buttons]
        )
        arg: int = bits_to_int(buttons_as_ints)
        return super().render(arg)


class Set7000ToPressedButton(EventScriptCommandNoArgs):
    _opcode: int = 0xCA


class Set7000ToTappedButton(EventScriptCommandNoArgs):
    _opcode: int = 0xCB


# inventory / party


class AddCoins(EventScriptCommand):
    _size: int = 2
    _amount: Union[ShortVar, UInt8]

    @property
    def amount(self) -> Union[ShortVar, UInt8]:
        return self._amount

    def set_amount(self, amount: int) -> None:
        if 0 <= amount <= 0xFF:
            self._amount = UInt8(amount)
        else:
            assert amount == 0x7000
            self._amount = amount

    def __init__(self, amount: int, identifier: Optional[str] = None) -> None:
        super.__init__(identifier)
        self.set_amount(amount)

    def render(self) -> bytearray:
        if isinstance(self.amount, ShortVar):
            return super().render(bytearray(0xFD, 0x52))
        else:
            return super().render(0x52, self.amount)


class Dec7000FromCoins(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x53])


class AddFrogCoins(EventScriptCommand):
    _size: int = 2
    _amount: Union[ShortVar, UInt8]

    @property
    def amount(self) -> Union[ShortVar, UInt8]:
        return self._amount

    def set_amount(self, amount: int) -> None:
        if 0 <= amount <= 0xFF:
            self._amount = UInt8(amount)
        else:
            assert amount == 0x7000
            self._amount = amount

    def __init__(self, amount: int, identifier: Optional[str] = None) -> None:
        super.__init__(identifier)
        self.set_amount(amount)

    def render(self) -> bytearray:
        if isinstance(self.amount, ShortVar):
            return super().render(bytearray(0xFD, 0x54))
        else:
            return super().render(0x53, self.amount)


class Dec7000FromFrogCoins(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x55])


class Add7000ToCurrentFP(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x56])


class Dec7000FromCurrentFP(EventScriptCommandNoArgs):
    _opcode: int = 0x57


class Add7000ToMaxFP(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x57])


class Dec7000FromCurrentHP(EventScriptCommand):
    _opcode: int = 0x57
    _size: int = 2
    _character_id: UInt8

    @property
    def character_id(self) -> UInt8:
        return self._character_id

    def set_character_id(self, character: Character) -> None:
        assert 0 <= character.id <= 4
        self._character_id = UInt8(character.id)

    def __init__(self, character: Character, identifier: Optional[str] = None) -> None:
        super.__init__(identifier)
        self.set_character_id(character)

    def render(self) -> bytearray:
        return super().render(self.character_id)


class EquipItemToCharacter(EventScriptCommand):
    _opcode: int = 0x54
    _size: int = 3
    _character_id: UInt8
    _item_id: UInt8

    @property
    def character_id(self) -> UInt8:
        return self._character_id

    def set_character_id(self, character: Character) -> None:
        assert 0 <= character.id <= 4
        self._character_id = UInt8(character.id)

    @property
    def item_id(self) -> UInt8:
        return self._item_id

    def set_item_id(self, item: Equipment) -> None:
        self._item_id = UInt8(item.id)

    def __init__(
        self, item: Equipment, character: Character, identifier: Optional[str] = None
    ) -> None:
        super.__init__(identifier)
        self.set_character_id(character)
        self.set_item_id(item)

    def render(self) -> bytearray:
        return super().render(self.character_id, self.item_id)


class IncEXPByPacket(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x48])


class CharacterJoinsParty(EventScriptCommand):
    _opcode: int = 0x36
    _size: int = 2
    _character_id: UInt8

    @property
    def character_id(self) -> UInt8:
        return self._character_id

    def set_character_id(self, character: Character) -> None:
        assert 0 <= character.id <= 4
        self._character_id = UInt8(character.id)

    def __init__(self, character: Character, identifier: Optional[str] = None) -> None:
        super.__init__(identifier)
        self.set_character_id(character)

    def render(self) -> bytearray:
        return super().render(self.character_id + (1 << 7))


class CharacterLeavesParty(EventScriptCommand):
    _opcode: int = 0x36
    _size: int = 2
    _character_id: UInt8

    @property
    def character_id(self) -> UInt8:
        return self._character_id

    def set_character_id(self, character: Character) -> None:
        assert 0 <= character.id <= 4
        self._character_id = UInt8(character.id)

    def __init__(self, character: Character, identifier: Optional[str] = None) -> None:
        super.__init__(identifier)
        self.set_character_id(character)

    def render(self) -> bytearray:
        return super().render(self.character_id & 0x7F)


class Store70A7ToEquipsInventory(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x51])


class AddToInventory(EventScriptCommand):
    _size: int = 2
    _item_id: Union[UInt8, ByteVar]

    @property
    def item_id(self) -> Union[UInt8, ByteVar]:
        return self._item_id

    def set_item_id(self, item: Union[Item, int]) -> None:
        if isinstance(item, int):
            assert item == 0x70A7
            self._item_id = ByteVar(item)
        elif isinstance(item, Item):
            self._item_id = UInt8(item.id)
        else:
            raise Exception(
                "illegal arg type for AddToInventory: %s %r" % type(item), item
            )

    def __init__(self, item: Equipment, identifier: Optional[str] = None) -> None:
        super.__init__(identifier)
        self.set_item_id(item)

    def render(self) -> bytearray:
        if isinstance(self.item_id, ByteVar):
            return super().render(bytearray([0xFD, 0x50]))
        else:
            return super().render(0x50, self.item_id)


class RemoveOneOfItemFromInventory(EventScriptCommand):
    _opcode: int = 0x51
    _size: int = 2
    _item_id: UInt8

    @property
    def item_id(self) -> UInt8:
        return self._item_id

    def set_item_id(self, item: Equipment) -> None:
        self._item_id = UInt8(item.id)

    def __init__(self, item: Equipment, identifier: Optional[str] = None) -> None:
        super.__init__(identifier)
        self.set_item_id(item)

    def render(self) -> bytearray:
        return super().render(self.item_id)


class RestoreAllFP(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x5C])


class RestoreAllHP(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x58])


class SetEXPPacketTo7000(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x64])


class Set7000ToIDOfMemberInSlot(EventScriptCommand):
    _opcode: int = 0x38
    _size: int = 2
    _slot: UInt8

    @property
    def slot(self) -> UInt8:
        return self._slot

    def set_slot(self, slot: int) -> None:
        assert 0 <= slot <= 4
        self._slot = UInt8(slot)

    def __init__(self, slot: int, identifier: Optional[str] = None) -> None:
        super.__init__(identifier)
        self.set_slot(slot)

    def render(self) -> bytearray:
        return super().render(0x08 + self.slot)


class Set7000ToPartySize(EventScriptCommandNoArgs):
    _opcode: int = 0x37


class StoreItemAt70A7QuantityAt7000(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x5E])


class StoreCharacterEquipmentTo7000(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x5D])
    _size: int = 4
    _character_id: UInt8
    _equip_slot: UInt8

    @property
    def character_id(self) -> UInt8:
        return self._character_id

    def set_character_id(self, character: Character) -> None:
        assert 0 <= character.id <= 4
        self._character_id = UInt8(character.id)

    @property
    def equip_slot(self) -> UInt8:
        return self._equip_slot

    def set_equip_slot(self, equip_slot: Equipment) -> None:
        assert (
            isinstance(equip_slot, Weapon)
            or isinstance(equip_slot, Armor)
            or isinstance(equip_slot, Accessory)
        )
        self._equip_slot = UInt8(equip_slot.id)

    def __init__(
        self,
        character: Character,
        equip_slot: Equipment,
        identifier: Optional[str] = None,
    ) -> None:
        super.__init__(identifier)
        self.set_character_id(character)
        self.set_equip_slot(equip_slot)

    def render(self) -> bytearray:
        return super().render(self.character_id, self.equip_slot)


class StoreCurrentFPTo7000(EventScriptCommandNoArgs):
    _opcode: int = 0x58


class StoreEmptyItemInventorySlotCountTo7000(EventScriptCommandNoArgs):
    _opcode: int = 0x55


class StoreCoinCountTo7000(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x59])


class StoreItemAmountTo7000(EventScriptCommand):
    _opcode = bytearray([0xFD, 0x58])
    _size: int = 3
    _item_id: UInt8

    @property
    def item_id(self) -> UInt8:
        return self._item_id

    def set_item_id(self, item: Item) -> None:
        self._item_id = UInt8(item.id)

    def __init__(self, item: Item, identifier: Optional[str] = None) -> None:
        super.__init__(identifier)
        self.set_item_id(item)

    def render(self) -> bytearray:
        return super().render(self.item_id)


class StoreFrogCoinCountTo7000(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x5A])


# yourself


class JmpIfMarioInAir(EventScriptCommandWithJmps):
    _opcode: 0x3D
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class MarioGlows(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0xF9])


# palettes & screen effects


class PaletteSet(EventScriptCommand):
    _opcode: int = 0xBA
    _size: int = 3
    _palette_set: UInt8
    _row: UInt8
    _bit_4: bool
    _bit_5: bool
    _bit_6: bool
    _bit_7: bool

    @property
    def palette_set(self) -> UInt8:
        return self._palette_set

    def set_palette_set(self, palette_set: int) -> None:
        self._palette_set = UInt8(palette_set)

    @property
    def row(self) -> UInt8:
        return self._row

    def set_row(self, row: int) -> None:
        assert 1 <= row <= 16
        self._row = UInt8(row)

    @property
    def bit_4(self) -> bool:
        return self._bit_4

    def set_bit_4(self, bit_4: bool) -> None:
        self._bit_4 = bit_4

    @property
    def bit_5(self) -> bool:
        return self._bit_5

    def set_bit_5(self, bit_5: bool) -> None:
        self._bit_5 = bit_5

    @property
    def bit_6(self) -> bool:
        return self._bit_6

    def set_bit_6(self, bit_6: bool) -> None:
        self._bit_6 = bit_6

    @property
    def bit_7(self) -> bool:
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        self._bit_7 = bit_7

    def __init__(
        self,
        palette_set: int,
        row: int,
        bit_4: bool = False,
        bit_5: bool = False,
        bit_6: bool = False,
        bit_7: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_palette_set(palette_set)
        self.set_row(row)
        self.set_bit_4(bit_4)
        self.set_bit_5(bit_5)
        self.set_bit_6(bit_6)
        self.set_bit_7(bit_7)

    def render(self) -> bytearray:
        flags: int = bools_to_int(self.bit_4, self.bit_5, self.bit_6, self.bit_7)
        flags = flags << 4
        arg_1 = UInt8(flags + (self.row - 1))
        return super().render(arg_1, self.palette_set)


class PaletteSetMorphs(EventScriptCommand):
    _opcode: int = 0xB9
    _size: int = 4
    _palette_type: PaletteType
    _palette_set: UInt8
    _duration: UInt8
    _row: UInt8

    @property
    def palette_type(self) -> PaletteType:
        return self._palette_type

    def set_palette_type(self, palette_type: PaletteType) -> None:
        self._palette_type = palette_type

    @property
    def palette_set(self) -> UInt8:
        return self._palette_set

    def set_palette_set(self, palette_set: int) -> None:
        self._palette_set = UInt8(palette_set)

    @property
    def duration(self) -> UInt8:
        return self._duration

    def set_duration(self, duration: int) -> None:
        assert 0 <= duration <= 15
        self._duration = UInt8(duration)

    @property
    def row(self) -> UInt8:
        return self._row

    def set_row(self, row: int) -> None:
        assert 1 <= row <= 16
        self._row = UInt8(row)

    def __init__(
        self,
        palette_type: PaletteType,
        palette_set: int,
        duration: int,
        row: int,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_palette_type(palette_type)
        self.set_palette_set(palette_set)
        self.set_duration(duration)
        self.set_row(row)

    def render(self) -> bytearray:
        arg_1 = UInt8(self.duration + (self.palette_type << 4))
        return super().render(arg_1, self.row, self.palette_set)


class PauseScriptUntilEffectDone(EventScriptCommandNoArgs):
    _opcode: int = 0x7F


class PixelateLayers(EventScriptCommand):
    _opcode: int = 0x84
    _size: int = 3
    _pixel_size: int
    _layers: "Layer[int]"
    _size: UInt8
    _duration: UInt8

    @property
    def layers(self) -> "Layer[int]":
        return self._layers

    def set_layers(self, layers: "Layer[int]") -> None:
        for layer in layers:
            assert 0 <= layer <= 3
        self._layers = layers

    @property
    def pixel_size(self) -> UInt8:
        return self._pixel_size

    def set_size(self, pixel_size: int) -> None:
        assert 0 <= pixel_size <= 15
        self._pixel_size = UInt8(pixel_size)

    @property
    def duration(self) -> UInt8:
        return self._duration

    def set_duration(self, duration: int) -> None:
        assert 0 <= duration <= 63
        self._duration = UInt8(duration)

    def __init__(
        self,
        layers: "Layer[int]",
        pixel_size: int,
        duration: int,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_layers(layers)
        self.set_pixel_size(pixel_size)
        self.set_duration(duration)

    def render(self) -> bytearray:
        layers: int = bits_to_int(self.layers)
        arg_1 = UInt8(layers + (self.pixel_size << 4))
        return super().render(arg_1, self.duration)


class PrioritySet(EventScriptCommand):
    _opcode: int = 0x81
    _size: int = 4
    _mainscreen: "Layer[int]"
    _subscreen: "Layer[int]"
    _colour_math: "Layer[int]"

    @property
    def mainscreen(self) -> "Layer[int]":
        return self._mainscreen

    def set_mainscreen(self, mainscreen: "Layer[int]") -> None:
        for layer in mainscreen:
            assert 0 <= layer <= 2 or layer == 4
        self._mainscreen = mainscreen

    @property
    def subscreen(self) -> "Layer[int]":
        return self._subscreen

    def set_subscreen(self, subscreen: "Layer[int]") -> None:
        for layer in subscreen:
            assert 0 <= layer <= 2 or layer == 4
        self._subscreen = subscreen

    @property
    def colour_math(self) -> "Layer[int]":
        return self._colour_math

    def set_colour_math(self, colour_math: "Layer[int]") -> None:
        for layer in colour_math:
            assert layer != 3
        self._colour_math = colour_math

    def __init__(
        self,
        mainscreen: "Layer[int]",
        subscreen: "Layer[int]",
        colour_math: "Layer[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_mainscreen(mainscreen)
        self.set_subscreen(subscreen)
        self.set_colour_math(colour_math)

    def render(self) -> bytearray:
        mainscreen: int = bits_to_int(self.mainscreen)
        subscreen: int = bits_to_int(self.subscreen)
        colour_math: int = bits_to_int(self.colour_math)
        return super().render(mainscreen, subscreen, colour_math)


class ResetPrioritySet(EventScriptCommandNoArgs):
    _opcode: int = 0x82


class ScreenFlashesWithColour(EventScriptCommand):
    _opcode: int = 0x83
    _size: int = 2
    _colour: Colour

    @property
    def colour(self) -> Colour:
        return self._colour

    def set_colour(self, colour: Colour) -> None:
        self._colour = colour

    def __init__(
        self,
        colour: Colour,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_colour(colour)

    def render(self) -> bytearray:
        return super().render(self.colour)


class TintLayers(EventScriptCommand):
    _opcode: int = 0x80
    _size: int = 5
    _layers: "Layer[int]"
    _red: UInt8
    _green: UInt8
    _blue: UInt8
    _speed: UInt8
    _bit_15: bool

    @property
    def layers(self) -> "Layer[int]":
        return self._layers

    def set_layers(self, layers: "Layer[int]") -> None:
        self._layers = layers

    @property
    def red(self) -> UInt8:
        return self._red

    def set_red(self, red: int) -> None:
        assert 0 <= red <= 248 and red % 8 == 0
        self._red = UInt8(red)

    @property
    def green(self) -> UInt8:
        return self._green

    def set_green(self, green: int) -> None:
        assert 0 <= green <= 248 and green % 8 == 0
        self._green = UInt8(green)

    @property
    def blue(self) -> UInt8:
        return self._blue

    def set_blue(self, blue: int) -> None:
        assert 0 <= blue <= 248 and blue % 8 == 0
        self._blue = UInt8(blue)

    @property
    def speed(self) -> UInt8:
        return self._speed

    def set_speed(self, speed: int) -> None:
        self._speed = UInt8(speed)

    @property
    def bit_15(self) -> bool:
        return self._bit_15

    def set_bit_15(self, bit_15: bool) -> None:
        self._bit_15 = bit_15

    def __init__(
        self,
        layers: "Layer[int]",
        red: int,
        green: int,
        blue: int,
        speed: int,
        bit_15: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_layers(layers)
        self.set_red(red)
        self.set_green(green)
        self.set_blue(blue)
        self.set_speed(speed)
        self.set_bit_15(bit_15)

    def render(self) -> bytearray:
        assembled_raw: int = (
            self.red + (self.green << 5) + (self.blue << 10) + (self.bit_15 << 15)
        )
        assembled_short = UInt16(assembled_raw)
        assembled_layers_raw: int = bits_to_int(self.layers)
        assembled_layers: UInt8(assembled_layers_raw)
        return super().render(assembled_short, assembled_layers, self.speed)


# screen transitions


class CircleMaskExpandFromScreenCenter(EventScriptCommandNoArgs):
    _opcode: int = 0x82


class CircleMaskShrinkToScreenCenter(EventScriptCommandNoArgs):
    _opcode: int = 0x7D


class CircleMaskShrinkToObject(EventScriptCommand):
    _size: int = 4
    _static: bool
    _object: AreaObject
    _width: UInt8
    _speed: UInt8

    @property
    def static(self) -> bool:
        return self._static

    def set_static(self, static: bool) -> None:
        self._static = static

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    @property
    def width(self) -> UInt8:
        return self._width

    def set_width(self, width: int) -> None:
        self._width = UInt8(width)

    @property
    def speed(self) -> UInt8:
        return self._speed

    def set_speed(self, speed: int) -> None:
        self._speed = UInt8(speed)

    def __init__(
        self,
        object: AreaObject,
        width: int,
        speed: int,
        static: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_object(object)
        self.set_width(width)
        self.set_speed(speed)
        self.set_static(static)

    def render(self) -> bytearray:
        opcode: int = 0x8F if self.static else 0x87
        return super().render(opcode, self.object, self.width, self.speed)


class StarMaskExpandFromScreenCenter(EventScriptCommandNoArgs):
    _opcode: int = 0x7A


class StarMaskShrinkToScreenCenter(EventScriptCommandNoArgs):
    _opcode: int = 0x7B


class FadeInFromBlack(EventScriptCommand):
    _sync: bool
    _duration: Optional[UInt8]

    @property
    def sync(self) -> bool:
        return self._sync

    def set_sync(self, sync: bool) -> None:
        self._sync = sync

    @property
    def duration(self) -> Optional[UInt8]:
        try:
            return self._duration
        except:
            return None

    def set_duration(self, duration: Optional[int] = None) -> None:
        if duration is not None:
            self._duration = UInt8(duration)
        if self.duration is None:
            self._size = 1
        else:
            self._size = 2

    def __init__(
        self,
        sync: bool,
        duration: Optional[int] = None,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_sync(sync)
        self.set_duration(duration)

    def render(self) -> bytearray:
        opcode: int = 0x70 + (not self.sync)
        if self.duration is not None:
            opcode += 2
            return super().render(opcode, self.duration)
        return super().render(opcode)


class FadeInFromColour(EventScriptCommand):
    _opcode: int = 0x78
    _size: int = 3
    _duration: UInt8
    _colour: Colour

    @property
    def duration(self) -> UInt8:
        return self._duration

    def set_duration(self, duration: int) -> None:
        self._duration = UInt8(duration)

    @property
    def colour(self) -> Colour:
        return self._colour

    def set_colour(self, colour: Colour) -> None:
        self._colour = colour

    def __init__(
        self, duration: int, colour: Colour, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_duration(duration)
        self.set_colour(colour)

    def render(self) -> bytearray:
        return super().render()


class FadeOutToBlack(EventScriptCommand):
    _sync: bool
    _duration: Optional[UInt8]

    @property
    def sync(self) -> bool:
        return self._sync

    def set_sync(self, sync: bool) -> None:
        self._sync = sync

    @property
    def duration(self) -> Optional[UInt8]:
        try:
            return self._duration
        except:
            return None

    def set_duration(self, duration: Optional[int] = None) -> None:
        if duration is not None:
            self._duration = UInt8(duration)
        if self.duration is None:
            self._size = 1
        else:
            self._size = 2

    def __init__(
        self,
        sync: bool,
        duration: Optional[int] = None,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_sync(sync)
        self.set_duration(duration)

    def render(self) -> bytearray:
        opcode: int = 0x74 + (not self.sync)
        if self.duration is not None:
            opcode += 2
            return super().render(opcode, self.duration)
        return super().render(opcode)


class FadeOutToColour(EventScriptCommand):
    _opcode: int = 0x79
    _size: int = 3
    _duration: UInt8
    _colour: Colour

    @property
    def duration(self) -> UInt8:
        return self._duration

    def set_duration(self, duration: int) -> None:
        self._duration = UInt8(duration)

    @property
    def colour(self) -> Colour:
        return self._colour

    def set_colour(self, colour: Colour) -> None:
        self._colour = colour

    def __init__(
        self, duration: int, colour: Colour, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_duration(duration)
        self.set_colour(colour)

    def render(self) -> bytearray:
        return super().render()


class InitiateBattleMask(EventScriptCommandNoArgs):
    _opcode: int = 0x7E


# music


class SlowDownMusicTempoBy(EventScriptCommand):
    _opcode: int = 0x97
    _size: int = 3
    _duration: UInt8
    _change: UInt8

    @property
    def duration(self) -> UInt8:
        return self._duration

    def set_duration(self, duration: int) -> None:
        self._duration = UInt8(duration)

    @property
    def change(self) -> UInt8:
        return self._change

    def set_change(self, change: int) -> None:
        assert 0 <= change <= 127
        self._change = UInt8(change)

    def __init__(
        self, duration: int, change: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_duration(duration)
        self.set_change(change)

    def render(self) -> bytearray:
        return super().render(0x00, self.duration, self.change)


class SpeedUpMusicTempoBy(EventScriptCommand):
    _opcode: int = 0x97
    _size: int = 3
    _duration: UInt8
    _change: UInt8

    @property
    def duration(self) -> UInt8:
        return self._duration

    def set_duration(self, duration: int) -> None:
        self._duration = UInt8(duration)

    @property
    def change(self) -> UInt8:
        return self._change

    def set_change(self, change: int) -> None:
        assert 0 <= change <= 127
        self._change = UInt8(change)

    def __init__(
        self, duration: int, change: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_duration(duration)
        self.set_change(change)

    def render(self) -> bytearray:
        return super().render(0x01, self.duration, 256 - self.change)


class DeactivateSoundChannels(EventScriptCommand):
    _opcode = bytearray([0xFD, 0x94])
    _size: int = 3
    _bits: "set[int]"

    @property
    def bits(self) -> "set[int]":
        return self._bits

    def set_bits(self, bits: "set[int]") -> None:
        for bit in bits:
            assert 0 <= bit <= 7
        self._bits = bits

    def __init__(
        self,
        bits: "set[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_bits(bits)

    def render(self) -> bytearray:
        flags: UInt8(bits_to_int(self.bits))
        return super().render(flags)


class FadeInMusic(EventScriptCommand):
    _opcode: int = 0x92
    _size: int = 2
    _music_id: int

    @property
    def music(self) -> UInt8:
        return self._music_id

    def set_music_id(self, music: int) -> None:
        assert 0 <= music < TOTAL_MUSIC
        self._music_id = UInt8(music)

    def __init__(self, music: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_music_id(music)

    def render(self) -> bytearray:
        return super().render(self.music)


class FadeOutMusic(EventScriptCommandNoArgs):
    _opcode: int = 0x93


class FadeOutMusicFDA3(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0xA3])


class FadeOutMusicToVolume(EventScriptCommand):
    _opcode: 0x95
    _size: 3
    _duration: UInt8
    _volume: UInt8

    @property
    def duration(self) -> UInt8:
        return self._duration

    def set_duration(self, duration: int) -> None:
        self._duration = UInt8(duration)

    @property
    def volume(self) -> UInt8:
        return self._volume

    def set_volume(self, volume: int) -> None:
        self._volume = UInt8(volume)

    def __init__(
        self, duration: int, volume: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_duration(duration)
        self.set_volume(volume)

    def render(self) -> bytearray:
        return super().render(self.duration, self.volume)


class FadeOutSoundToVolume(EventScriptCommand):
    _opcode: 0x9E
    _size: 3
    _duration: UInt8
    _volume: UInt8

    @property
    def duration(self) -> UInt8:
        return self._duration

    def set_duration(self, duration: int) -> None:
        self._duration = UInt8(duration)

    @property
    def volume(self) -> UInt8:
        return self._volume

    def set_volume(self, volume: int) -> None:
        self._volume = UInt8(volume)

    def __init__(
        self, duration: int, volume: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_duration(duration)
        self.set_volume(volume)

    def render(self) -> bytearray:
        return super().render(self.duration, self.volume)


class JmpIfAudioMemoryIsAtLeast(EventScriptCommandWithJmps):
    _opcode = bytearray([0xFD, 0x96])
    _size: 5
    _threshold: UInt8

    @property
    def threshold(self) -> UInt8:
        return self._threshold

    def set_threshold(self, threshold: int) -> None:
        self._threshold = UInt8(threshold)

    def __init__(
        self, threshold: int, destinations: "str[int]", identifier: Optional[str] = None
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_threshold(threshold)

    def render(self) -> bytearray:
        return super().render(self.threshold, *self.destinations)


class JmpIfAudioMemoryEquals(EventScriptCommandWithJmps):
    _opcode = bytearray([0xFD, 0x97])
    _size: 5
    _threshold: UInt8

    @property
    def threshold(self) -> UInt8:
        return self._threshold

    def set_threshold(self, threshold: int) -> None:
        self._threshold = UInt8(threshold)

    def __init__(
        self, threshold: int, destinations: "str[int]", identifier: Optional[str] = None
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_threshold(threshold)

    def render(self) -> bytearray:
        return super().render(self.threshold, *self.destinations)


class PlayMusic(EventScriptCommand):
    _opcode = bytearray([0xFD, 0x9E])
    _size: int = 3
    _music_id: int

    @property
    def music(self) -> UInt8:
        return self._music_id

    def set_music_id(self, music: int) -> None:
        assert 0 <= music < TOTAL_MUSIC
        self._music_id = UInt8(music)

    def __init__(self, music: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_music_id(music)

    def render(self) -> bytearray:
        return super().render(self.music)


class PlayMusicAtCurrentVolume(EventScriptCommand):
    _opcode: int = 0x90
    _size: int = 2
    _music_id: int

    @property
    def music(self) -> UInt8:
        return self._music_id

    def set_music_id(self, music: int) -> None:
        assert 0 <= music < TOTAL_MUSIC
        self._music_id = UInt8(music)

    def __init__(self, music: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_music_id(music)

    def render(self) -> bytearray:
        return super().render(self.music)


class PlayMusicAtDefaultVolume(EventScriptCommand):
    _opcode: int = 0x91
    _size: int = 2
    _music_id: int

    @property
    def music(self) -> UInt8:
        return self._music_id

    def set_music_id(self, music: int) -> None:
        assert 0 <= music < TOTAL_MUSIC
        self._music_id = UInt8(music)

    def __init__(self, music: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_music_id(music)

    def render(self) -> bytearray:
        return super().render(self.music)


class PlaySound(EventScriptCommand):
    _sound: UInt8
    _channel: UInt8

    @property
    def sound(self) -> UInt8:
        return self._sound

    def set_sound(self, sound: int) -> None:
        assert 0 <= sound < TOTAL_SOUNDS
        self._sound = UInt8(sound)

    @property
    def channel(self) -> UInt8:
        return self._channel

    def set_channel(self, channel: int) -> None:
        assert channel in [4, 6]
        self._channel = UInt8(channel)
        if self.channel == 4:
            self._size = 3
            self._opcode = bytearray([0xFD, 0x9C])
        else:
            self._size = 2
            self._opcode = 0x9C

    def __init__(
        self, sound: int, channel: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_sound(sound)
        self.set_channel(channel)

    def render(self) -> bytearray:
        return super().render(self.sound)


class PlaySoundBalance(EventScriptCommand):
    _opcode: 0x9D
    _size: int = 3
    _sound: UInt8
    _balance: UInt8

    @property
    def sound(self) -> UInt8:
        return self._sound

    def set_sound(self, sound: int) -> None:
        assert 0 <= sound < TOTAL_SOUNDS
        self._sound = UInt8(sound)

    @property
    def balance(self) -> UInt8:
        return self._balance

    def set_balance(self, balance: int) -> None:
        self._balance = UInt8(balance)

    def __init__(
        self, sound: int, balance: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_sound(sound)
        self.set_balance(balance)

    def render(self) -> bytearray:
        return super().render(self.sound, self.balance)


class PlaySoundBalanceFD9D(EventScriptCommand):
    _opcode = bytearray([0xFD, 0x9D])
    _size: int = 4
    _sound: UInt8
    _balance: UInt8

    @property
    def sound(self) -> UInt8:
        return self._sound

    def set_sound(self, sound: int) -> None:
        assert 0 <= sound < TOTAL_SOUNDS
        self._sound = UInt8(sound)

    @property
    def balance(self) -> UInt8:
        return self._balance

    def set_balance(self, balance: int) -> None:
        self._balance = UInt8(balance)

    def __init__(
        self, sound: int, balance: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_sound(sound)
        self.set_balance(balance)

    def render(self) -> bytearray:
        return super().render(self.sound, self.balance)


class SlowDownMusic(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0xA4])


class SpeedUpMusicToDefault(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0xA5])


class StopMusic(EventScriptCommandNoArgs):
    _opcode: int = 0x94


class StopMusicFD9F(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x9F])


class StopMusicFDA0(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0xA0])


class StopMusicFDA1(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0xA1])


class StopMusicFDA2(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0xA2])


class StopMusicFDA6(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0xA6])


class StopSound(EventScriptCommandNoArgs):
    _opcode: int = 0x9B


# dialogs


class AppendDialogAt7000ToCurrentDialog(EventScriptCommand):
    _opcode: int = 0x63
    _size: int = 2
    _closable: bool
    _sync: bool

    @property
    def closable(self) -> bool:
        return self._closable

    def set_closable(self, closable: bool) -> None:
        self._closable = closable

    @property
    def sync(self) -> bool:
        return self._sync

    def set_sync(self, sync: bool) -> None:
        self._sync = sync

    def __init__(
        self, closable: bool, sync: bool, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_closable(closable)
        self.set_sync(sync)

    def render(self) -> bytearray:
        flags = (self.closable << 5) + ((not self.sync) << 7)
        return super().render(flags)


class CloseDialog(EventScriptCommandNoArgs):
    _opcode: int = 0x64


class JmpIfDialogOptionBSelected(EventScriptCommandWithJmps):
    _opcode: int = 0x66
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfDialogOptionBOrCSelected(EventScriptCommandWithJmps):
    _opcode: int = 0x67
    _size: int = 5

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class PauseScriptResumeOnNextDialogPageA(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x60])


class PauseScriptResumeOnNextDialogPageB(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x61])


class RunDialog(EventScriptCommand):
    _dialog_id: Union[UInt16, ShortVar]
    _above_object: AreaObject
    _closable: bool
    _bit_6: bool
    _sync: bool
    _multiline: bool
    _use_background: bool

    @property
    def dialog_id(self) -> Union[UInt16, ShortVar]:
        return self._dialog_id

    def set_dialog_id(self, dialog_id: int) -> None:
        if dialog_id == variables.PRIMARY_TEMP_7000:
            self._dialog_id = ShortVar(dialog_id)
        else:
            assert 0 <= dialog_id < TOTAL_DIALOGS
            self._dialog_id = UInt16(dialog_id)

        if isinstance(self.dialog_id, ShortVar):
            self._size = 3
            self._opcode = 0x61
        else:
            self._size = 4
            self._opcode = 0x60

    @property
    def above_object(self) -> AreaObject:
        return self._above_object

    def set_above_object(self, above_object: AreaObject) -> None:
        self._above_object = above_object

    @property
    def closable(self) -> bool:
        return self._closable

    def set_closable(self, closable: bool) -> None:
        self._closable = closable

    @property
    def bit_6(self) -> bool:
        return self._bit_6

    def set_bit_6(self, bit_6: bool) -> None:
        self._bit_6 = bit_6

    @property
    def sync(self) -> bool:
        return self._sync

    def set_sync(self, sync: bool) -> None:
        self._sync = sync

    @property
    def multiline(self) -> bool:
        return self._multiline

    def set_multiline(self, multiline: bool) -> None:
        self._multiline = multiline

    @property
    def use_background(self) -> bool:
        return self._use_background

    def set_use_background(self, use_background: bool) -> None:
        self._use_background = use_background

    def __init__(
        self,
        dialog_id: UInt16,
        above_object: AreaObject,
        closable: bool,
        sync: bool,
        multiline: bool,
        use_background: bool,
        bit_6: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_dialog_id(dialog_id)
        self.set_above_object(above_object)
        self.set_closable(closable)
        self.set_bit_6(bit_6)
        self.set_sync(sync)
        self.set_multiline(multiline)
        self.set_use_background(use_background)

    def render(self) -> bytearray:
        flags_lower: int = (
            (self.closable << 5) + (self.bit_6 << 6) + ((not self.sync) << 7)
        )
        flags_upper: int = (self.multiline << 6) + (self.use_background << 7)
        final_arg = UInt8(self.above_object + flags_upper)
        if isinstance(self.dialog_id, ShortVar):
            return super().render(flags_lower, final_arg)
        id_arg = UInt16((flags_lower << 8) + self.dialog_id)
        return super().render(id_arg, final_arg)


class RunDialogForDuration(EventScriptCommand):
    _opcode: int = 0x62
    _size: int = 3
    _dialog_id: UInt16
    _duration: UInt8
    _sync: bool

    @property
    def dialog_id(self) -> UInt16:
        return self._dialog_id

    def set_dialog_id(self, dialog_id: int) -> None:
        assert 0 <= dialog_id < TOTAL_DIALOGS
        self._dialog_id = UInt16(dialog_id)

    @property
    def duration(self) -> UInt8:
        return self._duration

    def set_duration(self, duration: int) -> None:
        assert 0 <= duration <= 3
        self._duration = UInt8(duration)

    @property
    def sync(self) -> bool:
        return self._sync

    def set_sync(self, sync: bool) -> None:
        self._sync = sync

    def __init__(
        self,
        dialog_id: UInt16,
        duration: int,
        sync: bool,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_dialog_id(dialog_id)
        self.set_duration(duration)
        self.set_sync(sync)

    def render(self) -> bytearray:
        arg = UInt16(self.dialog_id + (self.duration << 13) + ((not self.sync) << 15))
        return super().render(arg)


class UnsyncDialog(EventScriptCommandNoArgs):
    _opcode: int = 0x65


# levels


class EnterArea(EventScriptCommand):
    _opcode: int = 0x68
    _size: int = 6
    _room_id: UInt16
    _face_direction: Direction
    _x: UInt8
    _y: UInt8
    _z: UInt8
    _z_add_half_unit: bool
    _show_banner: bool
    _run_entrance_event: bool

    @property
    def room_id(self) -> UInt16:
        return self._room_id

    def set_room_id(self, room_id: int) -> None:
        assert 0 <= room_id < TOTAL_ROOMS
        self._room_id = UInt16(room_id)

    @property
    def face_direction(self) -> Direction:
        return self._face_direction

    def set_face_direction(self, face_direction: Direction) -> None:
        self._face_direction = face_direction

    @property
    def x(self) -> UInt8:
        return self._x

    def set_x(self, x: int) -> None:
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        return self._y

    def set_y(self, y: int) -> None:
        assert 0 <= y <= 127
        self._y = UInt8(y)

    @property
    def z(self) -> UInt8:
        return self._z

    def set_z(self, z: int) -> None:
        assert 0 <= z <= 31
        self._z = UInt8(z)

    @property
    def z_add_half_unit(self) -> bool:
        return self._z_add_half_unit

    def set_z_add_half_unit(self, z_add_half_unit: bool) -> None:
        self._z_add_half_unit = z_add_half_unit

    @property
    def show_banner(self) -> bool:
        return self._show_banner

    def set_show_banner(self, show_banner: bool) -> None:
        self._show_banner = show_banner

    @property
    def run_entrance_event(self) -> bool:
        return self._run_entrance_event

    def set_run_entrance_event(self, run_entrance_event: bool) -> None:
        self._run_entrance_event = run_entrance_event

    def __init__(
        self,
        room_id: UInt16,
        face_direction: Direction,
        x: int,
        y: int,
        z: int,
        z_add_half_unit: bool = False,
        show_banner: bool = False,
        run_entrance_event: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_room_id(room_id)
        self.set_face_direction(face_direction)
        self.set_x(x)
        self.set_y(y)
        self.set_z(z)
        self.set_z_add_half_unit(z_add_half_unit)
        self.set_show_banner(show_banner)
        self.set_run_entrance_event(run_entrance_event)

    def render(self) -> bytearray:
        room_short = UInt16(
            self.room_id + (self.show_banner << 11) + (self.run_entrance_event << 15)
        )
        y_z_arg = UInt8(self.y + (self.z_add_half_unit << 7))
        direction_z_arg = UInt8(self.z + (self.direction << 5))
        return super().render(room_short, self.x, y_z_arg, direction_z_arg)


class ApplyTileModToLevel(EventScriptCommand):
    _opcode: int = 0x6A
    _size: int = 3
    _room_id: UInt16
    _mod_id: UInt8
    _use_alternate: bool

    @property
    def room_id(self) -> UInt16:
        return self._room_id

    def set_room_id(self, room_id: int) -> None:
        assert 0 <= room_id < TOTAL_ROOMS
        self._room_id = UInt16(room_id)

    @property
    def mod_id(self) -> UInt8:
        return self._mod_id

    def set_mod_id(self, mod_id: int) -> None:
        assert 0 <= mod_id <= 63
        self._mod_id = UInt8(mod_id)

    @property
    def use_alternate(self) -> bool:
        return self._use_alternate

    def set_use_alternate(self, use_alternate: bool) -> None:
        self._use_alternate = use_alternate

    def __init__(
        self,
        room_id: UInt16,
        mod_id: int,
        use_alternate: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_room_id(room_id)
        self.set_mod_id(mod_id)
        self.set_use_alternate(use_alternate)

    def render(self) -> bytearray:
        assembled_raw: int = (
            self.room_id + (self.mod_id << 9) + (self.use_alternate << 15)
        )
        return super().render(UInt16(assembled_raw))


class ApplySolidityModToLevel(EventScriptCommand):
    _opcode: int = 0x6B
    _size: int = 3
    _room_id: UInt16
    _mod_id: UInt8
    _use_alternate: bool

    @property
    def room_id(self) -> UInt16:
        return self._room_id

    def set_room_id(self, room_id: int) -> None:
        assert 0 <= room_id < TOTAL_ROOMS
        self._room_id = UInt16(room_id)

    @property
    def mod_id(self) -> UInt8:
        return self._mod_id

    def set_mod_id(self, mod_id: int) -> None:
        assert 0 <= mod_id <= 63
        self._mod_id = UInt8(mod_id)

    @property
    def use_alternate(self) -> bool:
        return self._use_alternate

    def set_use_alternate(self, use_alternate: bool) -> None:
        self._use_alternate = use_alternate

    def __init__(
        self,
        room_id: UInt16,
        mod_id: int,
        use_alternate: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_room_id(room_id)
        self.set_mod_id(mod_id)
        self.set_use_alternate(use_alternate)

    def render(self) -> bytearray:
        assembled_raw: int = (
            self.room_id + (self.mod_id << 9) + (self.use_alternate << 15)
        )
        return super().render(UInt16(assembled_raw))


class ExitToWorldMap(EventScriptCommand):
    _opcode: int = 0x4B
    _size: int = 3
    _area: UInt8
    _bit_5: bool
    _bit_6: bool
    _bit_7: bool

    @property
    def area(self) -> UInt8:
        return self._area

    def set_area(self, area: int) -> None:
        assert 0 <= area < TOTAL_WORLD_MAP_AREAS
        self._area = UInt8(area)

    @property
    def bit_5(self) -> bool:
        return self._bit_5

    def set_bit_5(self, bit_5: bool) -> None:
        self._bit_5 = bit_5

    @property
    def bit_6(self) -> bool:
        return self._bit_6

    def set_bit_6(self, bit_6: bool) -> None:
        self._bit_6 = bit_6

    @property
    def bit_7(self) -> bool:
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        self._bit_7 = bit_7

    def __init__(
        self,
        area: int,
        bit_5: bool,
        bit_6: bool,
        bit_7: bool,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_area(area)
        self.set_bit_5(bit_5)
        self.set_bit_6(bit_6)
        self.set_bit_7(bit_7)

    def render(self) -> bytearray:
        flags: int = bools_to_int(self.bit_5, self.bit_6, self.bit_7)
        flags = flags << 5
        return super().render(self.area, flags)


class Set7000ToCurrentLevel(EventScriptCommandNoArgs):
    _opcode: int = 0xC3


# scenes


class DisplayIntroTitleText(EventScriptCommand):
    _opcode = bytearray([0xFD, 0x66])
    _size: int = 4
    _text: IntroTitleText
    _y: UInt8

    @property
    def text(self) -> IntroTitleText:
        return self._text

    def set_text(self, text: IntroTitleText) -> None:
        self._text = text

    @property
    def y(self) -> UInt8:
        return self._y

    def set_y(self, y: int) -> None:
        self._y = UInt8(y)

    def __init__(
        self, text: IntroTitleText, y: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_text(text)
        self.set_y(y)

    def render(self) -> bytearray:
        return super().render()


class ExorCrashesIntoKeep(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0xF8])


class RunMenuOrEventSequence(EventScriptCommand):
    _opcode: int = 0x4F
    _size: int = 2
    _scene: Scene

    @property
    def scene(self) -> Scene:
        return self._scene

    def set_scene(self, scene: Scene) -> None:
        self._scene = scene

    def __init__(self, scene: Scene, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_scene(scene)

    def render(self) -> bytearray:
        return super().render(self.scene)


class OpenSaveMenu(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x4A])


class OpenShop(EventScriptCommand):
    _opcode: int = 0x4C
    _size: int = 2
    _shop_id: UInt8

    @property
    def shop_id(self) -> UInt8:
        return self._shop_id

    def set_shop_id(self, shop_id: int) -> None:
        assert 0 <= shop_id < TOTAL_SHOPS
        self._shop_id = UInt8(shop_id)

    def __init__(self, shop_id: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_shop_id(shop_id)

    def render(self) -> bytearray:
        return super().render(self.shop_id)


class PauseScriptIfMenuOpen(EventScriptCommandNoArgs):
    _opcode: int = 0x5B


class ResetAndChooseGame(EventScriptCommandNoArgs):
    _opcode: int = 0xFB


class ResetGame(EventScriptCommandNoArgs):
    _opcode: int = 0xFC


class RunEndingCredits(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x67])


class RunEventSequence(EventScriptCommand):
    _opcode: int = 0x4E
    _size: int = 3
    _scene: Scene
    _value: UInt8

    @property
    def scene(self) -> Scene:
        return self._scene

    def set_scene(self, scene: Scene) -> None:
        self._scene = scene

    @property
    def value(self) -> UInt8:
        return self._value

    def set_value(self, value: int) -> None:
        self._value = UInt8(value)

    def __init__(
        self, scene: Scene, value: int = 0, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_scene(scene)
        self.set_value(value)

    def render(self) -> bytearray:
        return super().render(self.scene, self.value)


class RunLevelupBonusSequence(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x65])


class RunMenuTutorial(EventScriptCommand):
    _opcode = bytearray([0xFD, 0x4C])
    _size: int = 3
    _tutorial: Tutorial

    @property
    def tutorial(self) -> Tutorial:
        return self._tutorial

    def set_tutorial(self, tutorial: Tutorial) -> None:
        self._tutorial = tutorial

    def __init__(self, tutorial: Tutorial, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_tutorial(tutorial)

    def render(self) -> bytearray:
        return super().render(self.tutorial)


class RunMolevilleMountainIntroSequence(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x4F])


class RunMolevilleMountainSequence(EventScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x4E])


class RunStarPieceSequence(EventScriptCommand):
    _opcode = bytearray([0xFD, 0x4D])
    _size: int = 3
    _star: UInt8

    @property
    def star(self) -> UInt8:
        return self._star

    def set_star(self, star: int) -> None:
        assert 1 <= star <= 7
        self._star = UInt8(star)

    def __init__(self, star: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_star(star)

    def render(self) -> bytearray:
        return super().render(self.star)


class StartBattleAtBattlefield(EventScriptCommand):
    _opcode: int = 0x4A
    _pack_id: UInt8
    _battlefield: Battlefield

    @property
    def pack_id(self) -> UInt8:
        return self._pack_id

    def set_pack_id(self, pack_id: int) -> None:
        self._pack_id = UInt8(pack_id)

    @property
    def battlefield(self) -> Battlefield:
        return self._battlefield

    def set_battlefield(self, battlefield: Battlefield) -> None:
        assert (
            0 <= battlefield <= 7 or 9 <= battlefield <= 27 or 30 <= battlefield <= 51
        )
        self._battlefield = battlefield

    def __init__(
        self, pack_id: int, battlefield: Battlefield, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_pack_id(pack_id)
        self.set_battlefield(battlefield)

    def render(self) -> bytearray:
        return super().render(self.pack_id, self.battlefield)


class StartBattleWithPackAt700E(EventScriptCommandNoArgs):
    _opcode: int = 0x49
