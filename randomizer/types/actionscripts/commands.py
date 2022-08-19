from typing import Optional, Union

from randomizer.types.actionscripts.classes import (
    ActionScriptCommand,
    ActionScriptCommandNoArgs,
    ActionScriptCommandWithJmps,
    ActionScriptCommandAnySizeMem,
    ActionScriptCommandShortMem,
    ActionScriptCommandShortAddrAndValueOnly,
    ActionScriptCommandBasicShortOperation,
    ActionScriptCommandByteSteps,
    ActionScriptCommandBytePixels,
    ActionScriptCommandXYBytes,
)
from randomizer.types.actionscripts.constants.classes import SequenceSpeed, VRAMPriority
from randomizer.types.actionscripts.constants.misc import (
    TOTAL_SCRIPTS as TOTAL_ACTION_SCRIPTS,
)

from randomizer.types.eventscripts.constants.misc import (
    TOTAL_SCRIPTS as TOTAL_EVENT_SCRIPTS,
)

from randomizer.types.constants.classes import AreaObject, Direction, Coord
from randomizer.types.constants.misc import TOTAL_ROOMS, TOTAL_SOUNDS
from randomizer.types.constants import coords
from randomizer.types.numbers.classes import UInt16, UInt8
from randomizer.types.packets.classes import Packet
from randomizer.types.variables import variables
from randomizer.types.variables.classes import ByteVar, Flag, ShortVar
from randomizer.utils.number import bits_to_int, bools_to_int
from randomizer.utils.memsize import cast_address

# script operations


class JmpToScript(ActionScriptCommand):
    _opcode: int = 0xD0
    _size: int = 3
    _destination: UInt16

    @property
    def destination(self) -> UInt16:
        return self._destination

    def set_destination(self, destination: int) -> None:
        assert 0 <= destination < TOTAL_ACTION_SCRIPTS
        self._destination = UInt16(destination)

    def __init__(self, destination: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_destination(destination)

    def render(self) -> bytearray:
        return super().render(self.destination)


class Jmp(ActionScriptCommandWithJmps):
    _opcode: int = 0xD2
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpToSubroutine(ActionScriptCommandWithJmps):
    _opcode: int = 0xD3
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class StartLoopNFrames(ActionScriptCommand):
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


class StartLoopNTimes(ActionScriptCommand):
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


class EndLoop(ActionScriptCommandNoArgs):
    _opcode: int = 0xD7


class Pause(ActionScriptCommand):
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


class JmpToStartOfThisScript(ActionScriptCommandNoArgs):
    _opcode: int = 0xF9


class JmpToStartOfThisScriptFA(ActionScriptCommandNoArgs):
    _opcode: int = 0xFA


class Return(ActionScriptCommandNoArgs):
    _opcode: int = 0xFE


class EndAll(ActionScriptCommandNoArgs):
    _opcode: int = 0xFF


class Db(ActionScriptCommand):
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


# visibility & collision


class VisibilityOn(ActionScriptCommandNoArgs):
    _opcode: int = 0x00


class VisibilityOff(ActionScriptCommandNoArgs):
    _opcode: int = 0x01


class ResetProperties(ActionScriptCommandNoArgs):
    _opcode: int = 0x09


class OverwriteSolidity(ActionScriptCommand):
    _opcode: int = 0x0A
    _size: int = 2
    _bit_0: bool = False
    _cant_walk_under: bool = False
    _cant_pass_walls: bool = False
    _cant_jump_through: bool = False
    _bit_4: bool = False
    _cant_pass_npcs: bool = False
    _cant_walk_through: bool = False
    _bit_7: bool = False

    @property
    def bit_0(self) -> bool:
        return self._bit_0

    def set_bit_0(self, bit_0: bool) -> None:
        self._bit_0 = bit_0

    @property
    def cant_walk_under(self) -> bool:
        return self._cant_walk_under

    def set_cant_walk_under(self, cant_walk_under: bool) -> None:
        self._cant_walk_under = cant_walk_under

    @property
    def cant_pass_walls(self) -> bool:
        return self._cant_pass_walls

    def set_cant_pass_walls(self, cant_pass_walls: bool) -> None:
        self._cant_pass_walls = cant_pass_walls

    @property
    def cant_jump_through(self) -> bool:
        return self._cant_jump_through

    def set_cant_jump_through(self, cant_jump_through: bool) -> None:
        self._cant_jump_through = cant_jump_through

    @property
    def bit_4(self) -> bool:
        return self._bit_4

    def set_bit_4(self, bit_4: bool) -> None:
        self._bit_4 = bit_4

    @property
    def cant_pass_npcs(self) -> bool:
        return self._cant_pass_npcs

    def set_cant_pass_npcs(self, cant_pass_npcs: bool) -> None:
        self._cant_pass_npcs = cant_pass_npcs

    @property
    def cant_walk_through(self) -> bool:
        return self._cant_walk_through

    def set_cant_walk_through(self, cant_walk_through: bool) -> None:
        self._cant_walk_through = cant_walk_through

    @property
    def bit_7(self) -> bool:
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        self._bit_7 = bit_7

    def __init__(
        self,
        bit_0: bool = False,
        cant_walk_under: bool = False,
        cant_pass_walls: bool = False,
        cant_jump_through: bool = False,
        bit_4: bool = False,
        cant_pass_npcs: bool = False,
        cant_walk_through: bool = False,
        bit_7: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_bit_0(bit_0)
        self.set_cant_walk_under(cant_walk_under)
        self.set_cant_pass_walls(cant_pass_walls)
        self.set_cant_jump_through(cant_jump_through)
        self.set_bit_4(bit_4)
        self.set_cant_pass_npcs(cant_pass_npcs)
        self.set_cant_walk_through(cant_walk_through)
        self.set_bit_7(bit_7)

    def render(self) -> bytearray:
        raw_flags = bools_to_int(
            self.bit_0,
            self.cant_walk_under,
            self.cant_pass_walls,
            self.cant_jump_through,
            self.bit_4,
            self.cant_pass_npcs,
            self.cant_walk_through,
            self.bit_7,
        )
        flags = UInt8(raw_flags)
        return super().render(flags)


class SetSolidityBits(ActionScriptCommand):
    _opcode: int = 0x0B
    _size: int = 2
    _bit_0: bool = False
    _cant_walk_under: bool = False
    _cant_pass_walls: bool = False
    _cant_jump_through: bool = False
    _bit_4: bool = False
    _cant_pass_npcs: bool = False
    _cant_walk_through: bool = False
    _bit_7: bool = False

    @property
    def bit_0(self) -> bool:
        return self._bit_0

    def set_bit_0(self, bit_0: bool) -> None:
        self._bit_0 = bit_0

    @property
    def cant_walk_under(self) -> bool:
        return self._cant_walk_under

    def set_cant_walk_under(self, cant_walk_under: bool) -> None:
        self._cant_walk_under = cant_walk_under

    @property
    def cant_pass_walls(self) -> bool:
        return self._cant_pass_walls

    def set_cant_pass_walls(self, cant_pass_walls: bool) -> None:
        self._cant_pass_walls = cant_pass_walls

    @property
    def cant_jump_through(self) -> bool:
        return self._cant_jump_through

    def set_cant_jump_through(self, cant_jump_through: bool) -> None:
        self._cant_jump_through = cant_jump_through

    @property
    def bit_4(self) -> bool:
        return self._bit_4

    def set_bit_4(self, bit_4: bool) -> None:
        self._bit_4 = bit_4

    @property
    def cant_pass_npcs(self) -> bool:
        return self._cant_pass_npcs

    def set_cant_pass_npcs(self, cant_pass_npcs: bool) -> None:
        self._cant_pass_npcs = cant_pass_npcs

    @property
    def cant_walk_through(self) -> bool:
        return self._cant_walk_through

    def set_cant_walk_through(self, cant_walk_through: bool) -> None:
        self._cant_walk_through = cant_walk_through

    @property
    def bit_7(self) -> bool:
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        self._bit_7 = bit_7

    def __init__(
        self,
        bit_0: bool = False,
        cant_walk_under: bool = False,
        cant_pass_walls: bool = False,
        cant_jump_through: bool = False,
        bit_4: bool = False,
        cant_pass_npcs: bool = False,
        cant_walk_through: bool = False,
        bit_7: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_bit_0(bit_0)
        self.set_cant_walk_under(cant_walk_under)
        self.set_cant_pass_walls(cant_pass_walls)
        self.set_cant_jump_through(cant_jump_through)
        self.set_bit_4(bit_4)
        self.set_cant_pass_npcs(cant_pass_npcs)
        self.set_cant_walk_through(cant_walk_through)
        self.set_bit_7(bit_7)

    def render(self) -> bytearray:
        raw_flags = bools_to_int(
            self.bit_0,
            self.cant_walk_under,
            self.cant_pass_walls,
            self.cant_jump_through,
            self.bit_4,
            self.cant_pass_npcs,
            self.cant_walk_through,
            self.bit_7,
        )
        flags = UInt8(raw_flags)
        return super().render(flags)


class ClearSolidityBits(ActionScriptCommand):
    _opcode: int = 0x0C
    _size: int = 2
    _bit_0: bool = False
    _cant_walk_under: bool = False
    _cant_pass_walls: bool = False
    _cant_jump_through: bool = False
    _bit_4: bool = False
    _cant_pass_npcs: bool = False
    _cant_walk_through: bool = False
    _bit_7: bool = False

    @property
    def bit_0(self) -> bool:
        return self._bit_0

    def set_bit_0(self, bit_0: bool) -> None:
        self._bit_0 = bit_0

    @property
    def cant_walk_under(self) -> bool:
        return self._cant_walk_under

    def set_cant_walk_under(self, cant_walk_under: bool) -> None:
        self._cant_walk_under = cant_walk_under

    @property
    def cant_pass_walls(self) -> bool:
        return self._cant_pass_walls

    def set_cant_pass_walls(self, cant_pass_walls: bool) -> None:
        self._cant_pass_walls = cant_pass_walls

    @property
    def cant_jump_through(self) -> bool:
        return self._cant_jump_through

    def set_cant_jump_through(self, cant_jump_through: bool) -> None:
        self._cant_jump_through = cant_jump_through

    @property
    def bit_4(self) -> bool:
        return self._bit_4

    def set_bit_4(self, bit_4: bool) -> None:
        self._bit_4 = bit_4

    @property
    def cant_pass_npcs(self) -> bool:
        return self._cant_pass_npcs

    def set_cant_pass_npcs(self, cant_pass_npcs: bool) -> None:
        self._cant_pass_npcs = cant_pass_npcs

    @property
    def cant_walk_through(self) -> bool:
        return self._cant_walk_through

    def set_cant_walk_through(self, cant_walk_through: bool) -> None:
        self._cant_walk_through = cant_walk_through

    @property
    def bit_7(self) -> bool:
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        self._bit_7 = bit_7

    def __init__(
        self,
        bit_0: bool = False,
        cant_walk_under: bool = False,
        cant_pass_walls: bool = False,
        cant_jump_through: bool = False,
        bit_4: bool = False,
        cant_pass_npcs: bool = False,
        cant_walk_through: bool = False,
        bit_7: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_bit_0(bit_0)
        self.set_cant_walk_under(cant_walk_under)
        self.set_cant_pass_walls(cant_pass_walls)
        self.set_cant_jump_through(cant_jump_through)
        self.set_bit_4(bit_4)
        self.set_cant_pass_npcs(cant_pass_npcs)
        self.set_cant_walk_through(cant_walk_through)
        self.set_bit_7(bit_7)

    def render(self) -> bytearray:
        raw_flags = bools_to_int(
            self.bit_0,
            self.cant_walk_under,
            self.cant_pass_walls,
            self.cant_jump_through,
            self.bit_4,
            self.cant_pass_npcs,
            self.cant_walk_through,
            self.bit_7,
        )
        flags = UInt8(raw_flags)
        return super().render(flags)


class SetMovementsBits(ActionScriptCommand):
    _opcode: int = 0x15
    _size: int = 2
    _bit_0: bool = False
    _cant_walk_under: bool = False
    _cant_pass_walls: bool = False
    _cant_jump_through: bool = False
    _bit_4: bool = False
    _cant_pass_npcs: bool = False
    _cant_walk_through: bool = False
    _bit_7: bool = False

    @property
    def bit_0(self) -> bool:
        return self._bit_0

    def set_bit_0(self, bit_0: bool) -> None:
        self._bit_0 = bit_0

    @property
    def cant_walk_under(self) -> bool:
        return self._cant_walk_under

    def set_cant_walk_under(self, cant_walk_under: bool) -> None:
        self._cant_walk_under = cant_walk_under

    @property
    def cant_pass_walls(self) -> bool:
        return self._cant_pass_walls

    def set_cant_pass_walls(self, cant_pass_walls: bool) -> None:
        self._cant_pass_walls = cant_pass_walls

    @property
    def cant_jump_through(self) -> bool:
        return self._cant_jump_through

    def set_cant_jump_through(self, cant_jump_through: bool) -> None:
        self._cant_jump_through = cant_jump_through

    @property
    def bit_4(self) -> bool:
        return self._bit_4

    def set_bit_4(self, bit_4: bool) -> None:
        self._bit_4 = bit_4

    @property
    def cant_pass_npcs(self) -> bool:
        return self._cant_pass_npcs

    def set_cant_pass_npcs(self, cant_pass_npcs: bool) -> None:
        self._cant_pass_npcs = cant_pass_npcs

    @property
    def cant_walk_through(self) -> bool:
        return self._cant_walk_through

    def set_cant_walk_through(self, cant_walk_through: bool) -> None:
        self._cant_walk_through = cant_walk_through

    @property
    def bit_7(self) -> bool:
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        self._bit_7 = bit_7

    def __init__(
        self,
        bit_0: bool = False,
        cant_walk_under: bool = False,
        cant_pass_walls: bool = False,
        cant_jump_through: bool = False,
        bit_4: bool = False,
        cant_pass_npcs: bool = False,
        cant_walk_through: bool = False,
        bit_7: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_bit_0(bit_0)
        self.set_cant_walk_under(cant_walk_under)
        self.set_cant_pass_walls(cant_pass_walls)
        self.set_cant_jump_through(cant_jump_through)
        self.set_bit_4(bit_4)
        self.set_cant_pass_npcs(cant_pass_npcs)
        self.set_cant_walk_through(cant_walk_through)
        self.set_bit_7(bit_7)

    def render(self) -> bytearray:
        raw_flags = bools_to_int(
            self.bit_0,
            self.cant_walk_under,
            self.cant_pass_walls,
            self.cant_jump_through,
            self.bit_4,
            self.cant_pass_npcs,
            self.cant_walk_through,
            self.bit_7,
        )
        flags = UInt8(raw_flags)
        return super().render(flags)


class SetVRAMPriority(ActionScriptCommand):
    _opcode: int = 0x13
    _size: int = 2
    _priority: VRAMPriority

    @property
    def priority(self) -> VRAMPriority:
        return self._priority

    def set_priority(self, priority: VRAMPriority) -> None:
        self._priority = priority

    def __init__(
        self, priority: VRAMPriority, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_priority(priority)

    def render(self) -> bytearray:
        return super().render(self.priority)


class SetPriority(ActionScriptCommand):
    _opcode = bytearray([0xFD, 0x0F])
    _size: int = 3
    _priority: int

    @property
    def priority(self) -> int:
        return self._priority

    def set_priority(self, priority: int) -> None:
        assert 0 <= priority <= 3
        self._priority = priority

    def __init__(self, priority: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_priority(priority)

    def render(self) -> bytearray:
        return super().render(self.priority)


class ShadowOn(ActionScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x00])


class ShadowOff(ActionScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x01])


class FloatingOn(ActionScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x02])


class FloatingOff(ActionScriptCommandNoArgs):
    _opcode = bytearray([0xFD, 0x03])


# memory


class SetObjectMemoryBits(ActionScriptCommand):
    _size: int = 2
    _arg_1: int
    _bits: "set[int]"

    @property
    def arg_1(self) -> int:
        return self._arg_1

    def set_arg_1(self, arg_1: int) -> None:
        assert arg_1 in [0x0D, 0x0B, 0x0E]
        self._arg_1 = arg_1

    @property
    def bits(self) -> "set[int]":
        return self.bits

    def set_bits(self, bits: "set[int]") -> None:
        for bit in bits:
            assert 0 <= bit <= 7
        self._bits = bits

    def __init__(
        self, arg_1: int, bits: "set[int]", identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_arg_1(arg_1)
        self.set_bits(bits)

    def render(self) -> bytearray:
        flags: int = UInt8(bits_to_int(self.bits))
        if self.arg_1 == 0x0D:
            return super().render(0x11, flags)
        elif self.arg_1 == 0x0B:
            return super().render(0x12, flags)
        elif self.arg_1 == 0x0E:
            return super().render(0x14, flags)
        else:
            raise Exception("illegal args for %s: %r" % (self.identifier.name, flags))


class ObjectMemorySetBit(ActionScriptCommand):
    _size: int = 2
    _arg_1: int
    _bits: "set[int]"

    @property
    def arg_1(self) -> int:
        return self._arg_1

    @property
    def bits(self) -> "set[int]":
        return self._bits

    def set_props(self, arg_1: int, bits: "set[int]") -> None:
        input = (arg_1, bits)
        assert input in [
            (0x08, [4]),
            (0x09, [7]),
            (0x0B, [3]),
            (0x0C, [3, 4, 5]),
            (0x0D, [6]),
            (0x0E, [4]),
            (0x0E, [5]),
            (0x12, [5]),
            (0x30, [4]),
            (0x3C, [6]),
        ]
        self._arg_1 = arg_1
        self._bits = bits

    def __init__(
        self, arg_1: int, bits: "set[int]", identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_props(arg_1, bits)

    def render(self) -> bytearray:
        args = (self.arg_1, self.bits)
        if args == (0x08, [4]):
            opcode = bytearray([0xFD, 0x0A])
        elif args == (0x09, [7]):
            opcode = bytearray([0xFD, 0x08])
        elif args == (0x0B, [3]):
            opcode = bytearray([0xFD, 0x17])
        elif args == (0x0C, [3, 4, 5]):
            opcode = bytearray([0xFD, 0x14])
        elif args == (0x0D, [6]):
            opcode = bytearray([0xFD, 0x14])
        elif args == (0x0E, [4]):
            opcode = bytearray([0xFD, 0x04])
        elif args == (0x0E, [5]):
            opcode = bytearray([0xFD, 0x06])
        elif args == (0x12, [5]):
            opcode = bytearray([0xFD, 0x11])
        elif args == (0x30, [4]):
            opcode = bytearray([0xFD, 0x0D])
        elif args == (0x3C, [6]):
            opcode = bytearray([0xFD, 0x18])
        else:
            raise Exception("invalid args for %s: %r" % (self.identifier.name, args))
        return super().render(opcode)


class ObjectMemoryClearBit(ActionScriptCommand):
    _size: int = 2
    _arg_1: int
    _bits: "set[int]"

    @property
    def arg_1(self) -> int:
        return self._arg_1

    @property
    def bits(self) -> "set[int]":
        return self._bits

    def set_props(self, arg_1: int, bits: "set[int]") -> None:
        input = (arg_1, bits)
        assert input in [
            (0x08, [3, 4]),
            (0x09, [7]),
            (0x0B, [3]),
            (0x0C, [3, 4, 5]),
            (0x0E, [4]),
            (0x0E, [5]),
            (0x12, [5]),
            (0x30, [4]),
        ]
        self._arg_1 = arg_1
        self._bits = bits

    def __init__(
        self, arg_1: int, bits: "set[int]", identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_props(arg_1, bits)

    def render(self) -> bytearray:
        args = (self.arg_1, self.bits)
        if args == (0x08, [3, 4]):
            opcode = bytearray([0xFD, 0x0B])
        elif args == (0x09, [7]):
            opcode = bytearray([0xFD, 0x09])
        elif args == (0x0B, [3]):
            opcode = bytearray([0xFD, 0x16])
        elif args == (0x0C, [3, 4, 5]):
            opcode = bytearray([0xFD, 0x13])
        elif args == (0x0E, [4]):
            opcode = bytearray([0xFD, 0x05])
        elif args == (0x0E, [5]):
            opcode = bytearray([0xFD, 0x07])
        elif args == (0x12, [5]):
            opcode = bytearray([0xFD, 0x10])
        elif args == (0x30, [4]):
            opcode = bytearray([0xFD, 0x0C])
        else:
            raise Exception("invalid args for %s: %r" % (self.identifier.name, args))
        return super().render(opcode)


class ObjectMemoryModifyBits(ActionScriptCommand):
    _size: int = 2
    _arg_1: int
    _set_bits: "set[int]"
    _clear_bits: "set[int]"

    @property
    def arg_1(self) -> int:
        return self._arg_1

    @property
    def set_bits(self) -> "set[int]":
        return self._set_bits

    @property
    def clear_bits(self) -> "set[int]":
        return self._clear_bits

    def set_props(
        self, arg_1: int, set_bits: "set[int]", clear_bits: "set[int]"
    ) -> None:
        input = (arg_1, set_bits, clear_bits)
        assert input in [
            (0x09, [5], [4, 6]),
            (0x0C, [4], [3, 5]),
        ]
        self._arg_1 = arg_1
        self._set_bits = set_bits
        self._clear_bits = clear_bits

    def __init__(
        self,
        arg_1: int,
        set_bits: "set[int]" = [],
        clear_bits: "set[int]" = [],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_props(arg_1, set_bits, clear_bits)

    def render(self) -> bytearray:
        args = (self.arg_1, self.set_bits, self.clear_bits)
        if args == (0x09, [5], [4, 6]):
            return super().render(0xFD, 0x0E)
        elif args == (0x0C, [4], [3, 5]):
            return super().render(0xFD, 0x15)
        else:
            raise Exception("invalid args for %s: %r" % (self.identifier.name, args))


class SetBit(ActionScriptCommand):
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


class ClearBit(ActionScriptCommand):
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


class JmpIfBitSet(ActionScriptCommandWithJmps):
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


class JmpIfBitClear(ActionScriptCommandWithJmps):
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


class SetMem704XAt700CBit(ActionScriptCommandNoArgs):
    _opcode: int = 0xA3


class ClearMem704XAt700CBit(ActionScriptCommandNoArgs):
    _opcode: int = 0xA7


class JmpIfMem704XAt700CBitSet(ActionScriptCommandWithJmps):
    _opcode: 0xDB
    _size: int = 3

    def __init__(
        self, destinations: "str[int]", identifier: Optional[str] = None
    ) -> None:
        super().__init__(destinations, identifier)

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfMem704XAt700CBitClear(ActionScriptCommandWithJmps):
    _size: int = 3
    _opcode: 0xDF

    def __init__(
        self, destinations: "str[int]", identifier: Optional[str] = None
    ) -> None:
        super().__init__(destinations, identifier)

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfBitClear(ActionScriptCommandWithJmps):
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
        return super().render(opcode, arg, self.destinations)


class SetVarToConst(ActionScriptCommand):
    _value: Union[UInt8, UInt16]
    _address: Union[ShortVar, ByteVar]

    def set_value_and_address(self, value=None, address=None) -> None:
        if value is None:
            value = self.value
        try:
            value = UInt8(value)
        except:
            value = UInt16(value)
        if address is None:
            address = self.address
        if isinstance(value, UInt16) and isinstance(address, ByteVar):
            raise Exception(
                "illegal args for %s: 0x%02x %r:"
                % (self.identifier.name, self.address, self.value)
            )
        if address == variables.PRIMARY_TEMP_700C or isinstance(address, ByteVar):
            self._size = 3
        else:
            self._size = 4
        self._address = address
        self._value = value

    @property
    def value(self) -> Union[UInt8, UInt16]:
        return self._value

    @property
    def address(self) -> Union[ShortVar, ByteVar]:
        return self._address

    def __init__(
        self,
        address: Union[ShortVar, ByteVar],
        value: int,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_value_and_address(address, value)

    def render(self) -> bytearray:
        if isinstance(self.address, ByteVar) and isinstance(self.value, UInt8):
            return super().render(0xA8, self.address, self.value)
        elif self.address == variables.PRIMARY_TEMP_700C:
            return super().render(0xAC, UInt16(self.value))
        elif isinstance(self.address, ShortVar):
            return super().render(0xB0, self.address, UInt16(self.value))
        else:
            raise Exception(
                "illegal args for %s: 0x%02x %r:"
                % (self.identifier.name, self.address, self.value)
            )


class AddConstToVar(ActionScriptCommand):
    _value: Union[UInt8, UInt16]
    _address: Union[ShortVar, ByteVar]

    def set_value_and_address(self, value=None, address=None) -> None:
        if value is None:
            value = self.value
        try:
            value = UInt8(value)
        except:
            value = UInt16(value)
        if address is None:
            address = self.address
        if isinstance(value, UInt16) and isinstance(address, ByteVar):
            raise Exception(
                "illegal args for %s: 0x%02x %r:"
                % (self.identifier.name, self.address, self.value)
            )
        if address == variables.PRIMARY_TEMP_700C or isinstance(address, ByteVar):
            self._size = 3
        else:
            self._size = 4
        self._address = address
        self._value = value

    @property
    def value(self) -> Union[UInt8, UInt16]:
        return self._value

    @property
    def address(self) -> Union[ShortVar, ByteVar]:
        return self._address

    def __init__(
        self,
        address: Union[ShortVar, ByteVar],
        value: int,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_value_and_address(address, value)

    def render(self) -> bytearray:
        if isinstance(self.address, ByteVar) and isinstance(self.value, UInt8):
            return super().render(0xA9, self.address, self.value)
        elif self.address == variables.PRIMARY_TEMP_700C:
            return super().render(0xAD, UInt16(self.value))
        elif isinstance(self.address, ShortVar):
            return super().render(0xB1, self.address, UInt16(self.value))
        else:
            raise Exception(
                "illegal args for %s: 0x%02x %r:"
                % (self.identifier.name, self.address, self.value)
            )


class Inc(ActionScriptCommandAnySizeMem):
    def render(self) -> bytearray:
        if isinstance(self.address, ByteVar):
            return super().render(0xAA, self.address)
        elif self.address == variables.PRIMARY_TEMP_700C:
            return super().render(0xAE)
        elif isinstance(self.address, ShortVar):
            return super().render(0xB2, self.address)
        else:
            raise Exception(
                "illegal args for %s: 0x%02x:" % (self.identifier.name, self.address)
            )


class Dec(ActionScriptCommandAnySizeMem):
    def render(self) -> bytearray:
        if isinstance(self.address, ByteVar):
            return super().render(0xAB, self.address)
        elif self.address == variables.PRIMARY_TEMP_700C:
            return super().render(0xAF)
        elif isinstance(self.address, ShortVar):
            return super().render(0xB3, self.address)
        else:
            raise Exception(
                "illegal args for %s: 0x%02x:" % (self.identifier.name, self.address)
            )


class CopyVarToVar(ActionScriptCommand):
    _from_var: Union[ShortVar, ByteVar]
    _to_var: Union[ShortVar, ByteVar]

    def set_addresses(self, from_var=None, to_var=None):
        if from_var is None:
            from_var = self.from_var
        if to_var is None:
            to_var = self.to_var
        if isinstance(from_var, ByteVar) and isinstance(to_var, ByteVar):
            raise Exception(
                "illegal args for %s: 0x%04x 0x%04x:"
                % (self.identifier.name, from_var, to_var)
            )
        if (
            self.from_var != variables.PRIMARY_TEMP_700C
            and self.to_var != variables.PRIMARY_TEMP_700C
        ):
            self._size = 3
        else:
            self._size = 2

    @property
    def from_var(self) -> Union[ShortVar, ByteVar]:
        return self._from_var

    @property
    def to_var(self) -> Union[ShortVar, ByteVar]:
        return self._to_var

    def __init__(
        self,
        from_var: Union[ShortVar, ByteVar],
        to_var: Union[ShortVar, ByteVar],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_addresses(from_var, to_var)

    def render(self) -> bytearray:
        if self.to_var == variables.PRIMARY_TEMP_700C and isinstance(
            self.from_var, ByteVar
        ):
            return super().render(0xB4, self.from_var)
        elif self.from_var == variables.PRIMARY_TEMP_700C and isinstance(
            self.to_var, ByteVar
        ):
            return super().render(0xB5, self.to_var)
        elif self.to_var == variables.PRIMARY_TEMP_700C and isinstance(
            self.from_var, ShortVar
        ):
            return super().render(0xBA, self.from_var)
        elif self.from_var == variables.PRIMARY_TEMP_700C and isinstance(
            self.to_var, ShortVar
        ):
            return super().render(0xBB, self.to_var)
        elif isinstance(self.from_var, ShortVar) and isinstance(self.to_var, ShortVar):
            return super().render(0xBC, self.from_var, self.to_var)
        else:
            raise Exception(
                "illegal args for %s: 0x%04x 0x%04x:"
                % (self.identifier.name, self.from_var, self.to_var)
            )


class CompareVarToConst(ActionScriptCommandShortAddrAndValueOnly):
    def render(self) -> bytearray:
        if self.address == variables.PRIMARY_TEMP_700C:
            return super().render(0xC0, self.value)
        else:
            return super().render(0xC2, self.address, self.value)


class Compare700CToVar(ActionScriptCommandShortMem):
    _opcode: int = 0xC1
    _size: int = 2

    def render(self) -> bytearray:
        return super().render(self.address)


class JmpIfComparisonResultIsGreaterOrEqual(ActionScriptCommandWithJmps):
    _opcode: int = 0xEC
    _size = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfComparisonResultIsLesser(ActionScriptCommandWithJmps):
    _opcode: int = 0xED
    _size = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class SetVarToRandom(ActionScriptCommandShortAddrAndValueOnly):
    def render(self) -> bytearray:
        if self.address == variables.PRIMARY_TEMP_700C:
            return super().render(0xB6, self.value)
        else:
            return super().render(0xB7, self.address, self.value)


class AddVarTo700C(ActionScriptCommandShortMem):
    _opcode: int = 0xB8
    _size: int = 2


class DecVarFrom700C(ActionScriptCommandShortMem):
    _opcode: int = 0xB9
    _size: int = 2


class SwapVars(ActionScriptCommand):
    _opcode: int = 0xBD
    _size: int = 3
    _from_var: ShortVar
    _to_var: ShortVar

    @property
    def from_var(self) -> ShortVar:
        return self._from_var

    def set_from_var(self, from_var: ShortVar) -> None:
        self._from_var = from_var

    @property
    def to_var(self) -> ShortVar:
        return self._to_var

    def set_to_var(self, to_var: ShortVar) -> None:
        self._to_var = to_var

    def __init__(
        self,
        from_var: ShortVar,
        to_var: ShortVar,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_from_var(from_var)
        self.set_to_var(to_var)

    def render(self) -> bytearray:
        return super().render(self.from_var, self.to_var)


class Move70107015To7016701B(ActionScriptCommandNoArgs):
    _opcode: int = 0xBE


class Move7016701BTo70107015(ActionScriptCommandNoArgs):
    _opcode: int = 0xBF


class JmpIfVarEqualsConst(ActionScriptCommandWithJmps):
    _value: Union[UInt8, UInt16]
    _address: Union[ShortVar, ByteVar]

    def set_value_and_address(
        self, value: int = None, address: Union[ByteVar, ShortVar] = None
    ) -> None:
        if value is None:
            value = self.value
        try:
            value = UInt8(value)
        except:
            value = UInt16(value)
        if address is None:
            address = self.address
        if isinstance(value, UInt16) and isinstance(address, ByteVar):
            raise Exception(
                "illegal args for %s: 0x%02x %r:"
                % (self.identifier.name, self.address, self.value)
            )
        if address == variables.PRIMARY_TEMP_700C or isinstance(address, ByteVar):
            self._size = 5
        else:
            self._size = 6
        self._address = address
        self._value = value

    @property
    def value(self) -> Union[UInt8, UInt16]:
        return self._value

    @property
    def address(self) -> Union[ShortVar, ByteVar]:
        return self._address

    def __init__(
        self,
        address: Union[ByteVar, ShortVar],
        value: int,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_value_and_address(value, address)

    def render(self) -> bytearray:
        if isinstance(self.address, ByteVar) and isinstance(self.value, UInt8):
            return super().render(0xE0, self.address, self.value, *self.destinations)
        elif self.address == variables.PRIMARY_TEMP_700C:
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


class JmpIfVarNotEqualsConst(ActionScriptCommandWithJmps):
    _value: Union[UInt8, UInt16]
    _address: Union[ShortVar, ByteVar]

    def set_value_and_address(self, value=None, address=None) -> None:
        if value is None:
            value = self.value
        try:
            value = UInt8(value)
        except:
            value = UInt16(value)
        if address is None:
            address = self.address
        if isinstance(value, UInt16) and isinstance(address, ByteVar):
            raise Exception(
                "illegal args for %s: 0x%02x %r:"
                % (self.identifier.name, self.address, self.value)
            )
        if address == variables.PRIMARY_TEMP_700C or isinstance(address, ByteVar):
            self._size = 5
        else:
            self._size = 6
        self._address = address
        self._value = value

    @property
    def value(self) -> Union[UInt8, UInt16]:
        return self._value

    @property
    def address(self) -> Union[ShortVar, ByteVar]:
        return self._address

    def __init__(
        self,
        address: Union[ByteVar, ShortVar],
        value: int,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_value_and_address(address, value)

    def render(self) -> bytearray:
        if isinstance(self.address, ByteVar) and isinstance(self.value, UInt8):
            return super().render(0xE1, self.address, self.value, *self.destinations)
        elif self.address == variables.PRIMARY_TEMP_700C:
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


class JmpIf700CAllBitsClear(ActionScriptCommandWithJmps):
    _opcode: int = 0xE6
    _size = 5
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


class JmpIf700CAnyBitsSet(ActionScriptCommandWithJmps):
    _opcode: int = 0xE7
    _size = 5
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


class JmpIfRandom2of3(ActionScriptCommandWithJmps):
    _opcode: int = 0xE9
    _size: int = 5

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfRandom1of2(ActionScriptCommandWithJmps):
    _opcode: int = 0xE8
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfLoadedMemoryIs0(ActionScriptCommandWithJmps):
    _opcode: int = 0xEA
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfLoadedMemoryIsAboveOrEqual0(ActionScriptCommandWithJmps):
    _opcode: int = 0xEF
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfLoadedMemoryIsBelow0(ActionScriptCommandWithJmps):
    _opcode: int = 0xEE
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfLoadedMemoryIsNot0(ActionScriptCommandWithJmps):
    _opcode: int = 0xEB
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class Mem700CAndConst(ActionScriptCommandBasicShortOperation):
    _opcode = bytearray([0xFD, 0xB0])


class Mem700CAndVar(ActionScriptCommandShortMem):
    _opcode = bytearray([0xFD, 0xB3])
    _size: int = 3


class Mem700COrConst(ActionScriptCommandBasicShortOperation):
    _opcode = bytearray([0xFD, 0xB1])


class Mem700COrVar(ActionScriptCommandShortMem):
    _opcode = bytearray([0xFD, 0xB4])
    _size: int = 3


class Mem700CXorConst(ActionScriptCommandBasicShortOperation):
    _opcode = bytearray([0xFD, 0xB2])


class Mem700CXorVar(ActionScriptCommandShortMem):
    _opcode = bytearray([0xFD, 0xB5])
    _size: int = 3


class VarShiftLeft(ActionScriptCommand):
    _opcode = bytearray([0xFD, 0xB6])
    _size: int = 4
    _address: ShortVar
    _shift: UInt8

    @property
    def address(self) -> ShortVar:
        return self._address

    def set_address(self, address: ShortVar) -> None:
        self._address = address

    @property
    def shift(self) -> UInt8:
        return self._shift + 1

    def set_shift(self, shift: int) -> None:
        assert 1 <= shift <= 256
        self._shift = UInt8(shift - 1)

    def __init__(
        self, address: ShortVar, shift: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_address(address)
        self.set_shift(shift)

    def render(self) -> bytearray:
        return super().render(self.address, 0xFF - self.shift)


class LoadMemory(ActionScriptCommandShortMem):
    _opcode = 0xD6
    _size: int = 3


# sequencing


class SetSpriteSequence(ActionScriptCommand):
    _opcode: int = 0x08
    _size: int = 3
    _index: UInt8
    _sprite_offset: UInt8
    _is_mold: bool = False
    _is_sequence: bool = False
    _looping_off: bool = False
    _mirror_sprite: bool = False

    @property
    def index(self) -> UInt8:
        return self._index

    def set_index(self, index: int) -> None:
        self._index = UInt8(index)

    @property
    def sprite_offset(self) -> UInt8:
        return self._sprite_offset

    def set_sprite_offset(self, sprite_offset: int) -> None:
        assert 0 <= sprite_offset <= 7
        self._sprite_offset = UInt8(sprite_offset)

    @property
    def is_mold(self) -> bool:
        return self._is_mold

    def set_is_mold(self, is_mold: bool) -> None:
        self._is_mold = is_mold

    @property
    def is_sequence(self) -> bool:
        return self._is_sequence

    def set_is_sequence(self, is_sequence: bool) -> None:
        self._is_sequence = is_sequence

    @property
    def looping_off(self) -> bool:
        return self._looping_off

    def set_looping_off(self, looping_off: bool) -> None:
        self._looping_off = looping_off

    @property
    def mirror_sprite(self) -> bool:
        return self._mirror_sprite

    def set_mirror_sprite(self, mirror_sprite: bool) -> None:
        self._mirror_sprite = mirror_sprite

    def __init__(
        self,
        index: int,
        sprite_offset: int,
        is_mold: bool = False,
        is_sequence: bool = False,
        looping_off: bool = False,
        mirror_sprite: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        if is_mold:
            assert 0 <= index <= 31
        else:
            assert 0 <= index <= 15
        super().__init__(identifier)
        self.set_index(index)
        self.set_sprite_offset(sprite_offset)
        self.set_is_mold(is_mold)
        self.set_is_sequence(is_sequence)
        self.set_looping_off(looping_off)
        self.set_mirror_sprite(mirror_sprite)

    def render(self) -> bytearray:
        bit_array = [False] * 16
        bit_array[3] = self.is_mold
        bit_array[4] = self.looping_off
        bit_array[6] = self.is_sequence
        bit_array[15] = self.mirror_sprite
        flags: int = bools_to_int(*bit_array)
        arg = UInt16((self.index << 8) | self.sprite_offset | flags)
        return super().render(arg)


class SequencePlaybackOn(ActionScriptCommandNoArgs):
    _opcode: int = 0x02


class SequencePlaybackOff(ActionScriptCommandNoArgs):
    _opcode: int = 0x03


class SequenceLoopingOn(ActionScriptCommandNoArgs):
    _opcode: int = 0x04


class SequenceLoopingOff(ActionScriptCommandNoArgs):
    _opcode: int = 0x05


class _SetAnimationSpeed(ActionScriptCommand):
    _opcode: int = 0x10
    _size: int = 2
    _speed: SequenceSpeed
    _sequence: bool = False
    _walking: bool = False

    @property
    def speed(self) -> SequenceSpeed:
        return self._speed

    def set_speed(self, speed: SequenceSpeed) -> None:
        self._speed = speed
        assert self.speed or self.sequence

    @property
    def sequence(self) -> bool:
        return self._sequence

    def set_sequence(self, sequence: bool) -> None:
        self._sequence = sequence
        assert self.speed or self.sequence

    @property
    def walking(self) -> bool:
        return self._walking

    def set_walking(self, walking: bool) -> None:
        self._walking = walking

    def __init__(
        self,
        speed: SequenceSpeed,
        sequence: bool = False,
        walking: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_speed(speed)
        self.set_sequence(sequence)
        self.set_walking(walking)

    def render(self) -> bytearray:
        flags = bools_to_int(self.walking, self.sequence) << 6
        return super().render(UInt8(self.speed + flags))


class SetSequenceSpeed(_SetAnimationSpeed):
    def __init__(
        self,
        speed: SequenceSpeed,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(speed, sequence=True, walking=False, identifier=identifier)


class SetWalkingSpeed(_SetAnimationSpeed):
    def __init__(
        self,
        speed: SequenceSpeed,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(speed, sequence=False, walking=True, identifier=identifier)


class SetAllSpeeds(_SetAnimationSpeed):
    def __init__(
        self,
        speed: SequenceSpeed,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(speed, sequence=True, walking=True, identifier=identifier)


class EmbeddedAnimationRoutine(ActionScriptCommand):
    _args: bytearray
    _size: int = 16

    @property
    def args(self) -> bytearray:
        return self._args

    def set_args(self, args: bytearray) -> None:
        assert len(args) == 16
        assert args[0] in [0x26, 0x27, 0x28]
        self._args = args

    def __init__(self, args: bytearray, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_args(args)

    def render(self) -> bytearray:
        return super().render(self.args)


class MaximizeSequenceSpeed(ActionScriptCommandNoArgs):
    _opcode: int = 0x85


class MaximizeSequenceSpeed86(ActionScriptCommandNoArgs):
    _opcode: int = 0x86


# positioning


class FixedFCoordOn(ActionScriptCommandNoArgs):
    _opcode: int = 0x06


class FixedFCoordOff(ActionScriptCommandNoArgs):
    _opcode: int = 0x07


class JmpIfObjectWithinRange(ActionScriptCommandWithJmps):
    _opcode: int = 0x3A
    _size: int = 6
    _object: AreaObject
    _usually: UInt8
    _tiles: UInt8

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    @property
    def usually(self) -> UInt8:
        return self._usually

    def set_usually(self, usually: int) -> None:
        self._usually = UInt8(usually)

    @property
    def tiles(self) -> UInt8:
        return self._tiles

    def set_tiles(self, tiles: int) -> None:
        self._tiles = UInt8(tiles)

    def __init__(
        self,
        object: AreaObject,
        usually: int,
        tiles: int,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_object(object)
        self.set_usually(usually)
        self.set_tiles(tiles)

    def render(self) -> bytearray:
        return super().render(self.object, self.usually, self.tiles, *self.destinations)


class JmpIfObjectWithinRangeSameZ(ActionScriptCommandWithJmps):
    _opcode: int = 0x3B
    _size: int = 6
    _object: AreaObject
    _usually: UInt8
    _tiles: UInt8

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    @property
    def usually(self) -> UInt8:
        return self._usually

    def set_usually(self, usually: int) -> None:
        self._usually = UInt8(usually)

    @property
    def tiles(self) -> UInt8:
        return self._tiles

    def set_tiles(self, tiles: int) -> None:
        self._tiles = UInt8(tiles)

    def __init__(
        self,
        object: AreaObject,
        usually: int,
        tiles: int,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_object(object)
        self.set_usually(usually)
        self.set_tiles(tiles)

    def render(self) -> bytearray:
        return super().render(self.object, self.usually, self.tiles, *self.destinations)


class Walk1StepEast(ActionScriptCommandNoArgs):
    _opcode: int = 0x40


class Walk1StepSoutheast(ActionScriptCommandNoArgs):
    _opcode: int = 0x41


class Walk1StepSouth(ActionScriptCommandNoArgs):
    _opcode: int = 0x42


class Walk1StepSouthwest(ActionScriptCommandNoArgs):
    _opcode: int = 0x43


class Walk1StepWest(ActionScriptCommandNoArgs):
    _opcode: int = 0x44


class Walk1StepNorthwest(ActionScriptCommandNoArgs):
    _opcode: int = 0x45


class Walk1StepNorth(ActionScriptCommandNoArgs):
    _opcode: int = 0x46


class Walk1StepNortheast(ActionScriptCommandNoArgs):
    _opcode: int = 0x47


class Walk1StepFDirection(ActionScriptCommandNoArgs):
    _opcode: int = 0x48


class AddZCoord1Step(ActionScriptCommandNoArgs):
    _opcode: int = 0x4A


class DecZCoord1Step(ActionScriptCommandNoArgs):
    _opcode: int = 0x4B


class ShiftEastSteps(ActionScriptCommandByteSteps):
    _opcode: int = 0x50


class ShiftSoutheastSteps(ActionScriptCommandByteSteps):
    _opcode: int = 0x51


class ShiftSouthSteps(ActionScriptCommandByteSteps):
    _opcode: int = 0x52


class ShiftSouthwestSteps(ActionScriptCommandByteSteps):
    _opcode: int = 0x53


class ShiftWestSteps(ActionScriptCommandByteSteps):
    _opcode: int = 0x54


class ShiftNorthwestSteps(ActionScriptCommandByteSteps):
    _opcode: int = 0x55


class ShiftNorthSteps(ActionScriptCommandByteSteps):
    _opcode: int = 0x56


class ShiftNortheastSteps(ActionScriptCommandByteSteps):
    _opcode: int = 0x57


class ShiftFDirectionSteps(ActionScriptCommandByteSteps):
    _opcode: int = 0x58


class ShiftZ20Steps(ActionScriptCommandNoArgs):
    _opcode: int = 0x59


class ShiftZUpSteps(ActionScriptCommandByteSteps):
    _opcode: int = 0x5A


class ShiftZDownSteps(ActionScriptCommandByteSteps):
    _opcode: int = 0x5B


class ShiftZUp20Steps(ActionScriptCommandNoArgs):
    _opcode: int = 0x5C


class ShiftZDown20Steps(ActionScriptCommandNoArgs):
    _opcode: int = 0x5D


class ShiftEastPixels(ActionScriptCommandBytePixels):
    _opcode: int = 0x60


class ShiftSoutheastPixels(ActionScriptCommandBytePixels):
    _opcode: int = 0x61


class ShiftSouthPixels(ActionScriptCommandBytePixels):
    _opcode: int = 0x62


class ShiftSouthwestPixels(ActionScriptCommandBytePixels):
    _opcode: int = 0x63


class ShiftWestPixels(ActionScriptCommandBytePixels):
    _opcode: int = 0x64


class ShiftNorthwestPixels(ActionScriptCommandBytePixels):
    _opcode: int = 0x65


class ShiftNorthPixels(ActionScriptCommandBytePixels):
    _opcode: int = 0x66


class ShiftNortheastPixels(ActionScriptCommandBytePixels):
    _opcode: int = 0x67


class ShiftFDirectionPixels(ActionScriptCommandBytePixels):
    _opcode: int = 0x68


class WalkFDirection16Pixels(ActionScriptCommandNoArgs):
    _opcode: int = 0x69


class ShiftZUpPixels(ActionScriptCommandBytePixels):
    _opcode: int = 0x6A


class ShiftZDownPixels(ActionScriptCommandBytePixels):
    _opcode: int = 0x6B


class FaceEast(ActionScriptCommandNoArgs):
    _opcode: int = 0x70


class FaceEast7C(ActionScriptCommandNoArgs):
    _opcode: int = 0x7C


class FaceSoutheast(ActionScriptCommandNoArgs):
    _opcode: int = 0x71


class FaceSouth(ActionScriptCommandNoArgs):
    _opcode: int = 0x72


class FaceSouthwest(ActionScriptCommandNoArgs):
    _opcode: int = 0x73


class FaceSouthwest7D(ActionScriptCommandNoArgs):
    _opcode: int = 0x7D


class FaceWest(ActionScriptCommandNoArgs):
    _opcode: int = 0x74


class FaceNorthwest(ActionScriptCommandNoArgs):
    _opcode: int = 0x75


class FaceNorth(ActionScriptCommandNoArgs):
    _opcode: int = 0x76


class FaceNortheast(ActionScriptCommandNoArgs):
    _opcode: int = 0x77


class FaceMario(ActionScriptCommandNoArgs):
    _opcode: int = 0x78


class TurnClockwise45Degrees(ActionScriptCommandNoArgs):
    _opcode: int = 0x79


class TurnRandomDirection(ActionScriptCommandNoArgs):
    _opcode: int = 0x7A


class TurnClockwise45DegreesNTimes(ActionScriptCommand):
    _opcode: int = 0x7B
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


class JumpToHeight(ActionScriptCommand):
    _size: int = 3
    _height: UInt16
    _silent: bool

    def height(self) -> UInt16:
        return self._height

    def set_height(self, height: int) -> None:
        self._height = UInt16(height)

    def silent(self) -> bool:
        return self._silent

    def set_silent(self, silent: bool) -> None:
        self._silent = silent

    def __init__(
        self, height: int, silent: bool = False, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_height(height)
        self.set_silent(silent)

    def render(self) -> bytearray:
        if self.silent:
            return super().render(0x7E, self.height)
        else:
            return super().render(0x7F, self.height)


class WalkToXYCoords(ActionScriptCommandXYBytes):
    _opcode: int = 0x80


class WalkXYSteps(ActionScriptCommandXYBytes):
    _opcode: int = 0x81


class ShiftToXYCoords(ActionScriptCommandXYBytes):
    _opcode: int = 0x82


class ShiftXYSteps(ActionScriptCommandXYBytes):
    _opcode: int = 0x83


class ShiftXYPixels(ActionScriptCommandXYBytes):
    _opcode: int = 0x84


class TransferToObjectXY(ActionScriptCommand):
    _opcode: int = 0x87
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


class TransferToObjectXYZ(ActionScriptCommand):
    _opcode: int = 0x95
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


class RunAwayShift(ActionScriptCommandNoArgs):
    _opcode: int = 0x88


class TransferTo70167018(ActionScriptCommandNoArgs):
    _opcode: int = 0x89


class TransferTo70167018701A(ActionScriptCommandNoArgs):
    _opcode: int = 0x99


class WalkTo70167018(ActionScriptCommandNoArgs):
    _opcode: int = 0x8A


class WalkTo70167018701A(ActionScriptCommandNoArgs):
    _opcode: int = 0x98


class BounceToXYWithHeight(ActionScriptCommand):
    _opcode: int = 0x90
    _size: int = 4
    _x: UInt8
    _y: UInt8
    _height: UInt8

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

    @property
    def height(self) -> UInt8:
        return self._height

    def set_height(self, height: int) -> None:
        self._height = UInt8(height)

    def __init__(
        self, x: int, y: int, height: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_x(x)
        self.set_y(y)
        self.set_height(height)

    def render(self) -> bytearray:
        return super().render(self.x, self.y, self.height)


class BounceXYStepsWithHeight(ActionScriptCommand):
    _opcode: int = 0x91
    _size: int = 4
    _x: UInt8
    _y: UInt8
    _height: UInt8

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

    @property
    def height(self) -> UInt8:
        return self._height

    def set_height(self, height: int) -> None:
        self._height = UInt8(height)

    def __init__(
        self, x: int, y: int, height: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_x(x)
        self.set_y(y)
        self.set_height(height)

    def render(self) -> bytearray:
        return super().render(self.x, self.y, self.height)


class TransferToXYZF(ActionScriptCommand):
    _opcode: int = 0x92
    _size: int = 4
    _x: UInt8
    _y: UInt8
    _z: UInt8
    _direction: UInt8

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

    @property
    def z(self) -> UInt8:
        return self._z

    def set_z(self, z: int) -> None:
        assert 0 <= z <= 31
        self._z = UInt8(z)

    @property
    def direction(self) -> UInt8:
        return self._direction

    def set_direction(self, direction: int) -> None:
        self._direction = UInt8(direction)

    def __init__(
        self,
        x: int,
        y: int,
        z: int,
        direction: Direction,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_x(x)
        self.set_y(y)
        self.set_z(z)
        self.set_direction(direction)

    def render(self) -> bytearray:
        final_byte = UInt8(self.z + (self.direction << 5))
        return super().render(self.x, self.y, final_byte)


class TransferXYZFSteps(ActionScriptCommand):
    _opcode: int = 0x93
    _size: int = 4
    _x: UInt8
    _y: UInt8
    _z: UInt8
    _direction: UInt8

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

    @property
    def z(self) -> UInt8:
        return self._z

    def set_z(self, z: int) -> None:
        assert 0 <= z <= 31
        self._z = UInt8(z)

    @property
    def direction(self) -> UInt8:
        return self._direction

    def set_direction(self, direction: int) -> None:
        self._direction = UInt8(direction)

    def __init__(
        self,
        x: int,
        y: int,
        z: int,
        direction: Direction,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_x(x)
        self.set_y(y)
        self.set_z(z)
        self.set_direction(direction)

    def render(self) -> bytearray:
        final_byte = UInt8(self.z + (self.direction << 5))
        return super().render(self.x, self.y, final_byte)


class TransferXYZFPixels(ActionScriptCommand):
    _opcode: int = 0x94
    _size: int = 4
    _x: UInt8
    _y: UInt8
    _z: UInt8
    _direction: UInt8

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

    @property
    def z(self) -> UInt8:
        return self._z

    def set_z(self, z: int) -> None:
        assert 0 <= z <= 31
        self._z = UInt8(z)

    @property
    def direction(self) -> UInt8:
        return self._direction

    def set_direction(self, direction: int) -> None:
        self._direction = UInt8(direction)

    def __init__(
        self,
        x: int,
        y: int,
        z: int,
        direction: Direction,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_x(x)
        self.set_y(y)
        self.set_z(z)
        self.set_direction(direction)

    def render(self) -> bytearray:
        final_byte = UInt8(self.z + (self.direction << 5))
        return super().render(self.x, self.y, final_byte)


# room objects and camera


class Set700CToObjectCoord(ActionScriptCommand):
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
        arg_1 = UInt8(
            (self.bit_7 << 7) + (self.is_isometric_not_pixel << 6) + self.object
        )
        return super().render(opcode, arg_1)


class CreatePacketAtNPCCoords(ActionScriptCommandWithJmps):
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
        packet_id: int,
        object: AreaObject,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_packet_id(packet_id)
        self.set_object(object)

    def render(self) -> bytearray:
        return super().render(self.packet_id, self.object, *self.destinations)


class CreatePacketAt7010(ActionScriptCommandWithJmps):
    _opcode: int = 0x3F
    _size: int = 4
    _packet_id: UInt8

    @property
    def packet_id(self) -> UInt8:
        return self._packet_id

    def set_packet_id(self, packet_id: int) -> None:
        self._packet_id = UInt8(packet_id)

    def __init__(
        self, packet_id: int, destinations: "str[int]", identifier: Optional[str] = None
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_packet_id(packet_id)

    def render(self) -> bytearray:
        return super().render(self.packet_id, *self.destinations)


class CreatePacketAt7010WithEvent(ActionScriptCommandWithJmps):
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
        assert 0 <= event_id < TOTAL_EVENT_SCRIPTS
        self._event_id = UInt16(event_id)

    def __init__(
        self,
        packet_id: int,
        event_id: int,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_packet_id(packet_id)
        self.set_event_id(event_id)

    def render(self) -> bytearray:
        return super().render(self.packet_id, self.event_id, *self.destinations)


class SummonToLevel(ActionScriptCommand):
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
        arg_1 = UInt16(0x8000 + (self.object << 9) + self.level_id)
        return super().render(arg_1)


class SummonObjectAt70A8ToCurrentLevel(ActionScriptCommandNoArgs):
    _opcode: int = 0xF4


class RemoveFromLevel(ActionScriptCommand):
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
        arg_1 = UInt16((self.object << 9) + self.level_id)
        assert 0 <= arg_1 <= 0x7FFF
        return super().render(arg_1)


class RemoveObjectAt70A8FromCurrentLevel(ActionScriptCommandNoArgs):
    _opcode: int = 0xF5


class EnableTriggerInLevel(ActionScriptCommand):
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
        arg_1 = UInt16(0x8000 + (self.object << 9) + self.level_id)
        return super().render(arg_1)


class EnableTriggerAt70A8(ActionScriptCommandNoArgs):
    _opcode: int = 0xF6


class DisableTriggerInLevel(ActionScriptCommand):
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
        arg_1 = UInt16((self.object << 9) + self.level_id)
        assert 0 <= arg_1 <= 0x7FFF
        return super().render(arg_1)


class DisableTriggerAt70A8(ActionScriptCommandNoArgs):
    _opcode: int = 0xF7


class JmpIfObjectInSpecificLevel(ActionScriptCommandWithJmps):
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
        arg_1 = UInt16(0x8000 + (self.object << 9) + self.level_id)
        return super().render(arg_1, *self.destinations)


class JmpIfObjectNotInSpecificLevel(ActionScriptCommandWithJmps):
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
        arg_1 = UInt16((self.object << 9) + self.level_id)
        assert 0 <= arg_1 <= 0x7FFF
        return super().render(arg_1, *self.destinations)


class JmpIfObjectInAir(ActionScriptCommandWithJmps):
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


class Set700CToCurrentLevel(ActionScriptCommandNoArgs):
    _opcode: int = 0xC3


# controls


class Set700CToPressedButton(ActionScriptCommandNoArgs):
    _opcode: int = 0xCA


class Set700CToTappedButton(ActionScriptCommandNoArgs):
    _opcode: int = 0xCB


# palettes


class SetPaletteRow(ActionScriptCommand):
    _opcode: int = 0x0D
    _size: int = 2
    _row: UInt8

    @property
    def row(self) -> UInt8:
        return self._row

    def set_row(self, row: int) -> None:
        assert 0 <= row <= 15
        self._row = UInt8(row)

    def __init__(self, row: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_row(row)

    def render(self) -> bytearray:
        return super().render(self.row)


class IncPaletteRowBy(ActionScriptCommand):
    _rows: UInt8

    @property
    def rows(self) -> UInt8:
        return self._rows

    def set_rows(self, rows: int) -> None:
        self._rows = UInt8(rows)
        if self.rows == 1:
            self._size = 1
            self._opcode = 0x0F
        else:
            self._size = 2
            self._opcode = 0x0E

    def __init__(self, rows: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_rows(rows)

    def render(self) -> bytearray:
        if self.row == 1:
            return super().render()
        return super().render(UInt8(0xF0 + self.rows))


# branching / jumps


class BPL262728(ActionScriptCommandNoArgs):
    _opcode: int = 0x21


class BMI262728(ActionScriptCommandNoArgs):
    _opcode: int = 0x22


class BPL2627(ActionScriptCommandNoArgs):
    _opcode: int = 0x2A


class UnknownJmp3C(ActionScriptCommandWithJmps):
    _opcode: 0x3C
    _size: int = 5
    _arg1: UInt8
    _arg2: UInt8

    @property
    def arg1(self) -> UInt8:
        return self._arg1

    def set_arg1(self, arg1: int) -> None:
        self._arg1 = UInt8(arg1)

    @property
    def arg2(self) -> UInt8:
        return self._arg2

    def set_arg2(self, arg2: int) -> None:
        self._arg2 = UInt8(arg2)

    def __init__(
        self,
        arg1: int,
        arg2: int,
        destinations: "str[int]",
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_arg1(arg1)
        self.set_arg1(arg2)

    def render(self) -> bytearray:
        return super().render(self.arg1, self.arg2, *self.destinations)


class JmpIfMarioInAir(ActionScriptCommandWithJmps):
    _opcode: 0x3D
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


# music


class StopSound(ActionScriptCommandNoArgs):
    _opcode: 0x9B


class PlaySound(ActionScriptCommand):
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
            self._opcode = bytearray([0xFD, 0x9E])
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


class PlaySoundBalance(ActionScriptCommand):
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


class FadeOutSoundToVolume(ActionScriptCommand):
    _opcode: 0x9E
    _size: int = 3
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
