from typing import Union
from randomizer.management.disassembler_common import byte
from randomizer.types.actionscripts.constants.classes import VRAMPriority
from randomizer.types.constants.misc import TOTAL_ROOMS, TOTAL_SOUNDS
from randomizer.types.packets.classes import Packet
from randomizer.utils.number import bits_to_int, bools_to_int, set_bits_to_true
from randomizer.utils.memsize import cast_address

from classes import (
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

from constants import command_names as cmdnm
from constants.classes import (
    ActionScriptCommandName,
    SequenceSpeed,
)
from constants.misc import TOTAL_SCRIPTS as TOTAL_ACTION_SCRIPTS
from ..eventscripts.constants.misc import TOTAL_SCRIPTS as TOTAL_EVENT_SCRIPTS

from ..constants.classes import AreaObject, Direction, Coord
from ..constants import coords

from ..numbers.classes import UInt16, UInt8
from ..variables import variables
from ..variables.classes import ByteVar, Flag, ShortVar


# script operations


class JmpToScript(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.JMP_TO_SCRIPT
    _opcode: int = 0xD0
    _size: int = 3
    _destination: UInt16

    @property
    def destination(self) -> UInt16:
        return self._destination

    def set_destination(self, destination: int) -> None:
        assert 0 <= destination < TOTAL_ACTION_SCRIPTS
        self._destination = UInt16(destination)

    def __init__(self, destination: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_destination(destination)

    def render(self) -> bytearray:
        return super().render(self.destination)


class Jmp(ActionScriptCommandWithJmps):
    _command_name: ActionScriptCommandName = cmdnm.JMP
    _opcode: int = 0xD2
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpToSubroutine(ActionScriptCommandWithJmps):
    _command_name: ActionScriptCommandName = cmdnm.JMP_TO_SUBROUTINE
    _opcode: int = 0xD3
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class StartLoopNFrames(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.START_LOOP_N_FRAMES
    _opcode: int = 0xD5
    _size: int = 3
    _length: UInt16

    @property
    def length(self) -> UInt16:
        return self._length

    def set_length(self, length: int) -> None:
        self._length = UInt16(length)

    def __init__(self, length: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_length(length)

    def render(self) -> bytearray:
        return super().render(self.length)


class StartLoopNTimes(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.START_LOOP_N_TIMES
    _opcode: int = 0xD4
    _size: int = 2
    _count: UInt8

    @property
    def count(self) -> UInt8:
        return self._count

    def set_count(self, count: int) -> None:
        self._count = UInt8(count)

    def __init__(self, count: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_count(count)

    def render(self) -> bytearray:
        return super().render(self.count)


class EndLoop(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.END_LOOP
    _opcode: int = 0xD7


class Pause(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.PAUSE
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

    def __init__(self, length: int, identifier: str = None) -> None:
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
    _command_name: ActionScriptCommandName = cmdnm.JMP_TO_START_OF_THIS_SCRIPT
    _opcode: int = 0xF9


class JmpToStartOfThisScriptFA(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.JMP_TO_START_OF_THIS_SCRIPT_FA
    _opcode: int = 0xFA


class Ret(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.RET
    _opcode: int = 0xFE


class EndAll(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.END_ALL
    _opcode: int = 0xFF


class Db(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.DB
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

    def __init__(self, contents: "int[int]", identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_contents(contents)

    def render(self) -> bytearray:
        return super().render(self.contents)


# visibility & collision


class VisibilityOn(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.VISIBILITY_ON
    _opcode: int = 0x00


class VisibilityOff(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.VISIBILITY_OFF
    _opcode: int = 0x01


class ResetProperties(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.RESET_PROPERTIES
    _opcode: int = 0x09


class OverwriteSolidity(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.OVERWRITE_SOLIDITY
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
        identifier: str = None,
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
    _command_name: ActionScriptCommandName = cmdnm.SET_SOLIDITY_BITS
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
        identifier: str = None,
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
    _command_name: ActionScriptCommandName = cmdnm.CLEAR_SOLIDITY_BITS
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
        identifier: str = None,
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
    _command_name: ActionScriptCommandName = cmdnm.SET_MOVEMENT_BITS
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
        identifier: str = None,
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
    _command_name: ActionScriptCommandName = cmdnm.SET_VRAM_PRIORITY
    _opcode: int = 0x13
    _size: int = 2
    _priority: VRAMPriority

    @property
    def priority(self) -> VRAMPriority:
        return self._priority

    def set_priority(self, priority: VRAMPriority) -> None:
        self._priority = priority

    def __init__(self, priority: VRAMPriority, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_priority(priority)

    def render(self) -> bytearray:
        return super().render(self.priority)


class SetPriority(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.SET_PRIORITY
    _opcode = bytearray([0xFD, 0x0F])
    _size: int = 3
    _priority: int

    @property
    def priority(self) -> int:
        return self._priority

    def set_priority(self, priority: int) -> None:
        assert 0 <= priority <= 3
        self._priority = priority

    def __init__(self, priority: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_priority(priority)

    def render(self) -> bytearray:
        return super().render(self.priority)


class ShadowOn(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.SHADOW_ON
    _opcode = bytearray([0xFD, 0x00])


class ShadowOff(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.SHADOW_OFF
    _opcode = bytearray([0xFD, 0x01])


class FloatingOn(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.FLOATING_ON
    _opcode = bytearray([0xFD, 0x02])


class FloatingOff(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.FLOATING_OFF
    _opcode = bytearray([0xFD, 0x03])


# memory


class SetObjectMemoryBits(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.SET_OBJECT_MEMORY_BITS
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

    def __init__(self, arg_1: int, bits: "set[int]", identifier: str = None) -> None:
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
    _command_name: ActionScriptCommandName = cmdnm.OBJECT_MEMORY_SET_BIT
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

    def __init__(self, arg_1: int, bits: "set[int]", identifier: str = None) -> None:
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
    _command_name: ActionScriptCommandName = cmdnm.OBJECT_MEMORY_SET_BIT
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

    def __init__(self, arg_1: int, bits: "set[int]", identifier: str = None) -> None:
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
    _command_name: ActionScriptCommandName = cmdnm.OBJECT_MEMORY_MODIFY_BITS
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
        identifier: str = None,
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
    _command_name: ActionScriptCommandName = cmdnm.SET_BIT
    _size: int = 2
    _bit: Flag

    @property
    def bit(self) -> Flag:
        return self._bit

    def set_bit(self, bit: Flag) -> None:
        self._bit = bit

    def __init__(self, bit: Flag, identifier: str = None) -> None:
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
        arg = ((self.bit.byte - offset) << 3) + self.bit.bit
        return super().render(opcode, arg)


class ClearBit(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.CLEAR_BIT
    _size: int = 2
    _bit: Flag

    @property
    def bit(self) -> Flag:
        return self._bit

    def set_bit(self, bit: Flag) -> None:
        self._bit = bit

    def __init__(self, bit: Flag, identifier: str = None) -> None:
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
        arg = ((self.bit.byte - offset) << 3) + self.bit.bit
        return super().render(opcode, arg)


class SetMem704XAt700CBit(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.SET_MEM_704X_AT_700C_BIT
    _opcode: int = 0xA3


class ClearMem704XAt700CBit(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.CLEAR_MEM_704X_AT_700C_BIT
    _opcode: int = 0xA7


class SetVarToConst(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.SET_VAR_TO_CONST
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

    def __init__(self, address: int, value: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_value(value)
        if isinstance(self.value, UInt8):
            try:
                self.set_address(ByteVar(address))
            except:
                self.set_address(ShortVar(address))
        else:
            self.set_address(ShortVar(address))
        if self.address == variables.PRIMARY_TEMP_700C or isinstance(
            self.address, ByteVar
        ):
            self._size = 3
        else:
            self._size = 4

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
    _command_name: ActionScriptCommandName = cmdnm.ADD_CONST_TO_VAR
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

    def __init__(self, address: int, value: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_value(value)
        if isinstance(self.value, UInt8):
            try:
                self.set_address(ByteVar(address))
            except:
                self.set_address(ShortVar(address))
        else:
            self.set_address(ShortVar(address))
        if self.address == variables.PRIMARY_TEMP_700C or isinstance(
            self.address, ByteVar
        ):
            self._size = 3
        else:
            self._size = 4

    def render(self) -> bytearray:
        if isinstance(self.address, ByteVar) and isinstance(self.value, UInt8):
            return super().render(0xA0, self.address, self.value)
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
    _command_name: ActionScriptCommandName = cmdnm.INC

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
    _command_name: ActionScriptCommandName = cmdnm.DEC

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
    _command_name: ActionScriptCommandName = cmdnm.COPY_VAR_TO_VAR
    _address_left: Union[ShortVar, ByteVar]
    _address_right: Union[ShortVar, ByteVar]

    @property
    def address_left(self) -> Union[ShortVar, ByteVar]:
        return self._address_left

    def set_address_left(self, address_left: Union[ShortVar, ByteVar]) -> None:
        self._address_left = address_left

    def cast_address_left(self, address_left: int) -> None:
        self.set_address_left(cast_address(address_left))

    @property
    def address_right(self) -> Union[ShortVar, ByteVar]:
        return self._address_right

    def set_address_right(self, address_right: int) -> None:
        self._address_right = cast_address(address_right)

    def cast_address_right(self, address_right: int) -> None:
        self.set_address_right(cast_address(address_right))

    def __init__(
        self,
        address_left: int,
        address_right: int,
        identifier: str = None,
    ) -> None:
        super().__init__(identifier)
        if address_left == variables.PRIMARY_TEMP_700C:
            self.set_address_left(ShortVar(address_left))
            self.cast_address_right(address_right)
        elif address_right == variables.PRIMARY_TEMP_700C:
            self.cast_address_left(address_left)
            self.set_address_right(ShortVar(address_right))
        else:
            self.set_address_left(ShortVar(address_left))
            self.set_address_right(ShortVar(address_right))

        if (
            self.address_left != variables.PRIMARY_TEMP_700C
            and self.address_right != variables.PRIMARY_TEMP_700C
        ):
            self._size = 3
        else:
            self._size = 2

    def render(self) -> bytearray:
        if self.address_right == variables.PRIMARY_TEMP_700C and isinstance(
            self.address_left, ByteVar
        ):
            return super().render(0xB4, self.address_left)
        elif self.address_left == variables.PRIMARY_TEMP_700C and isinstance(
            self.address_right, ByteVar
        ):
            return super().render(0xB5, self.address_right)
        elif self.address_right == variables.PRIMARY_TEMP_700C and isinstance(
            self.address_left, ShortVar
        ):
            return super().render(0xBA, self.address_left)
        elif self.address_left == variables.PRIMARY_TEMP_700C and isinstance(
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


class CompareVarToConst(ActionScriptCommandShortAddrAndValueOnly):
    _command_name: ActionScriptCommandName = cmdnm.COMPARE_VAR_TO_CONST

    def render(self) -> bytearray:
        if self.address == variables.PRIMARY_TEMP_700C:
            return super().render(0xC0, self.value)
        else:
            return super().render(0xC2, self.address, self.value)


class Compare700CToVar(ActionScriptCommandShortMem):
    _command_name: ActionScriptCommandName = cmdnm.COMPARE_700C_TO_VAR
    _opcode: int = 0xC1
    _size: int = 2

    def render(self) -> bytearray:
        return super().render(self.address)


class JmpIfComparisonResultIsGreaterOrEqual(ActionScriptCommandWithJmps):
    _command_name = (
        ActionScriptCommandName
    ) = cmdnm.JMP_IF_COMPARISON_RESULT_IS_GREATER_OR_EQUAL
    _opcode: int = 0xEC
    _size = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfComparisonResultIsLesser(ActionScriptCommandWithJmps):
    _command_name: ActionScriptCommandName = cmdnm.JMP_IF_COMPARISON_RESULT_IS_LESSER
    _opcode: int = 0xED
    _size = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class SetVarToRandom(ActionScriptCommandShortAddrAndValueOnly):
    _command_name: ActionScriptCommandName = cmdnm.SET_VAR_TO_RANDOM

    def render(self) -> bytearray:
        if self.address == variables.PRIMARY_TEMP_700C:
            return super().render(0xB6, self.value)
        else:
            return super().render(0xB7, self.address, self.value)


class AddVarTo700C(ActionScriptCommandShortMem):
    _command_name: ActionScriptCommandName = cmdnm.ADD_VAR_TO_700C
    _opcode: int = 0xB8
    _size: int = 2


class DecVarFrom700C(ActionScriptCommandShortMem):
    _command_name: ActionScriptCommandName = cmdnm.DEC_VAR_FROM_700C
    _opcode: int = 0xB9
    _size: int = 2


class SwapVars(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.SWAP_VARS
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
        identifier: str = None,
    ) -> None:
        super().__init__(identifier)
        self.set_address_left(address_left)
        self.set_address_right(address_right)

    def render(self) -> bytearray:
        return super().render(self.address_left, self.address_right)


class Move70107015To7016701B(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.MOVE_7010_7015_TO_7016_701B
    _opcode: int = 0xBE


class Move7016701BTo70107015(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.MOVE_7016_701B_TO_7010_7015
    _opcode: int = 0xBF


class JmpIfVarEqualsConst(ActionScriptCommandWithJmps):
    _command_name: ActionScriptCommandName = cmdnm.JMP_IF_VAR_EQUALS_CONST
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

    def __init__(
        self, address: int, value: int, destinations: "str[int]", identifier: str = None
    ) -> None:
        super().__init__(identifier, destinations)
        self.set_value(value)
        if isinstance(self.value, UInt8):
            try:
                self.set_address(ByteVar(address))
            except:
                self.set_address(ShortVar(address))
        else:
            self.set_address(ShortVar(address))
        if self.address == variables.PRIMARY_TEMP_700C or isinstance(
            self.address, ByteVar
        ):
            self._size = 5
        else:
            self._size = 6

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
    _command_name: ActionScriptCommandName = cmdnm.JMP_IF_VAR_NOT_EQUALS_CONST
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

    def __init__(
        self, address: int, value: int, destinations: "str[int]", identifier: str = None
    ) -> None:
        super().__init__(identifier, destinations)
        self.set_value(value)
        if isinstance(self.value, UInt8):
            try:
                self.set_address(ByteVar(address))
            except:
                self.set_address(ShortVar(address))
        else:
            self.set_address(ShortVar(address))
        if self.address == variables.PRIMARY_TEMP_700C or isinstance(
            self.address, ByteVar
        ):
            self._size = 5
        else:
            self._size = 6

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
    _command_name: ActionScriptCommandName = cmdnm.JMP_IF_700C_ALL_BITS_CLEAR
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
        identifier: str = None,
    ) -> None:
        super().__init__(identifier, destinations)
        self.set_bits(bits)

    def render(self) -> bytearray:
        flags: UInt16(bits_to_int(self.bits))
        return super().render(flags, *self.destinations)


class JmpIf700CAnyBitsSet(ActionScriptCommandWithJmps):
    _command_name: ActionScriptCommandName = cmdnm.JMP_IF_700C_ANY_BITS_SET
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
        identifier: str = None,
    ) -> None:
        super().__init__(identifier, destinations)
        self.set_bits(bits)

    def render(self) -> bytearray:
        flags: UInt16(bits_to_int(self.bits))
        return super().render(flags, *self.destinations)


class JmpIfRandomAbove66(ActionScriptCommandWithJmps):
    _command_name: ActionScriptCommandName = cmdnm.JMP_IF_RANDOM_ABOVE_66
    _opcode: int = 0xE9
    _size: int = 5

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfRandomAbove128(ActionScriptCommandWithJmps):
    _command_name: ActionScriptCommandName = cmdnm.JMP_IF_RANDOM_ABOVE_128
    _opcode: int = 0xE8
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfLoadedMemoryIs0(ActionScriptCommandWithJmps):
    _command_name: ActionScriptCommandName = cmdnm.JMP_IF_LOADED_MEMORY_IS_0
    _opcode: int = 0xEA
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfLoadedMemoryIsAboveOrEqual0(ActionScriptCommandWithJmps):
    _command_name = (
        ActionScriptCommandName
    ) = cmdnm.JMP_IF_LOADED_MEMORY_IS_ABOVE_OR_EQUAL_0
    _opcode: int = 0xEF
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfLoadedMemoryIsBelow0(ActionScriptCommandWithJmps):
    _command_name: ActionScriptCommandName = cmdnm.JMP_IF_LOADED_MEMORY_IS_BELOW_0
    _opcode: int = 0xEE
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfLoadedMemoryIsNot0(ActionScriptCommandWithJmps):
    _command_name: ActionScriptCommandName = cmdnm.JMP_IF_LOADED_MEMORY_IS_NOT_0
    _opcode: int = 0xEB
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class Mem700CAndConst(ActionScriptCommandBasicShortOperation):
    _command_name: ActionScriptCommandName = cmdnm.MEM_700C_AND_CONST
    _opcode = bytearray([0xFD, 0xB0])


class Mem700CAndVar(ActionScriptCommandShortMem):
    _command_name: ActionScriptCommandName = cmdnm.MEM_700C_AND_VAR
    _opcode = bytearray([0xFD, 0xB3])
    _size: int = 3


class Mem700COrConst(ActionScriptCommandBasicShortOperation):
    _command_name: ActionScriptCommandName = cmdnm.MEM_700C_OR_CONST
    _opcode = bytearray([0xFD, 0xB1])


class Mem700COrVar(ActionScriptCommandShortMem):
    _command_name: ActionScriptCommandName = cmdnm.MEM_700C_OR_VAR
    _opcode = bytearray([0xFD, 0xB4])
    _size: int = 3


class Mem700CXorConst(ActionScriptCommandBasicShortOperation):
    _command_name: ActionScriptCommandName = cmdnm.MEM_700C_XOR_CONST
    _opcode = bytearray([0xFD, 0xB2])


class Mem700CXorVar(ActionScriptCommandShortMem):
    _command_name: ActionScriptCommandName = cmdnm.MEM_700C_XOR_VAR
    _opcode = bytearray([0xFD, 0xB5])
    _size: int = 3


class VarShiftLeft(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.MEM_SHIFT_LEFT
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

    def __init__(self, address: int, shift: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_address(address)
        self.set_shift(shift)

    def render(self) -> bytearray:
        return super().render(self.address, self.shift)


# sequencing


class SetSpriteSequence(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.SET_SPRITE_SEQUENCE
    _opcode: int = 0x08
    _size: int = 3
    _sequence_or_mold_id: UInt8
    _sprite_offset: UInt8
    _is_mold: bool = False
    _is_sequence: bool = False
    _looping_off: bool = False
    _mirror_sprite: bool = False

    @property
    def sequence_or_mold_id(self) -> UInt8:
        return self._sequence_or_mold_id

    def set_sequence_or_mold_id(self, sequence_or_mold_id: int) -> None:
        self._sequence_or_mold_id = UInt8(sequence_or_mold_id)

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
        sequence_or_mold_id: int,
        sprite_offset: int,
        is_mold: bool = False,
        is_sequence: bool = False,
        looping_off: bool = False,
        mirror_sprite: bool = False,
        identifier: str = None,
    ) -> None:
        if is_mold:
            assert 0 <= sequence_or_mold_id <= 31
        else:
            assert 0 <= sequence_or_mold_id <= 15
        super().__init__(identifier)
        self.set_sequence_or_mold_id(sequence_or_mold_id)
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
        arg = UInt16((self.sequence_or_mold_id << 8) | self.sprite_offset | flags)
        return super().render(arg)


class SequencePlaybackOn(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.SEQUENCE_PLAYBACK_ON
    _opcode: int = 0x02


class SequencePlaybackOff(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.SEQUENCE_PLAYBACK_OFF
    _opcode: int = 0x03


class SequenceLoopingOn(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.SEQUENCE_LOOPING_ON
    _opcode: int = 0x04


class SequenceLoopingOff(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.SEQUENCE_LOOPING_OFF
    _opcode: int = 0x05


class SetAnimationSpeed(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.SET_ANIMATION_SPEED
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

    @property
    def sequence(self) -> bool:
        return self._sequence

    def set_sequence(self, sequence: bool) -> None:
        self._sequence = sequence

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
        identifier: str = None,
    ) -> None:
        super().__init__(identifier)
        self.set_speed(speed)
        self.set_sequence(sequence)
        self.set_walking(walking)

    def render(self) -> bytearray:
        flags = bools_to_int(self.walking, self.sequence) << 6
        return super().render(UInt8(self.speed + flags))


class EmbeddedAnimationRoutine(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.EMBEDDED_ANIMATION_ROUTINE
    _args: bytearray
    _size: int = 16

    @property
    def args(self) -> bytearray:
        return self._args

    def set_args(self, args: bytearray) -> None:
        assert len(args) == 16
        assert args[0] in [0x26, 0x27, 0x28]
        self._args = args

    def __init__(self, args: bytearray, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_args(args)

    def render(self) -> bytearray:
        return super().render(self.args)


class MaximizeSequenceSpeed(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.MAXIMIZE_SEQUENCE_SPEED
    _opcode: int = 0x85


class MaximizeSequenceSpeed86(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.MAXIMIZE_SEQUENCE_SPEED_86
    _opcode: int = 0x86


# positioning


class FixedFCoordOn(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.FIXED_F_COORD_ON
    _opcode: int = 0x06


class FixedFCoordOff(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.FIXED_F_COORD_OFF
    _opcode: int = 0x07


class JmpIfObjectWithinRange(ActionScriptCommandWithJmps):
    _command_name: ActionScriptCommandName = cmdnm.JMP_IF_OBJECT_WITHIN_RANGE
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
        identifier: str = None,
    ) -> None:
        super().__init__(identifier, destinations)
        self.set_object(object)
        self.set_usually(usually)
        self.set_tiles(tiles)

    def render(self) -> bytearray:
        return super().render(self.object, self.usually, self.tiles, *self.destinations)


class JmpIfObjectWithinRangeSameZ(ActionScriptCommandWithJmps):
    _command_name: ActionScriptCommandName = cmdnm.JMP_IF_OBJECT_WITHIN_RANGE_SAME_Z
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
        identifier: str = None,
    ) -> None:
        super().__init__(identifier, destinations)
        self.set_object(object)
        self.set_usually(usually)
        self.set_tiles(tiles)

    def render(self) -> bytearray:
        return super().render(self.object, self.usually, self.tiles, *self.destinations)


class Walk1StepEast(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.WALK_1_STEP_EAST
    _opcode: int = 0x40


class Walk1StepSoutheast(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.WALK_1_STEP_SOUTHEAST
    _opcode: int = 0x41


class Walk1StepSouth(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.WALK_1_STEP_SOUTH
    _opcode: int = 0x42


class Walk1StepSouthwest(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.WALK_1_STEP_SOUTHWEST
    _opcode: int = 0x43


class Walk1StepWest(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.WALK_1_STEP_WEST
    _opcode: int = 0x44


class Walk1StepNorthwest(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.WALK_1_STEP_NORTHWEST
    _opcode: int = 0x45


class Walk1StepNorth(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.WALK_1_STEP_NORTH
    _opcode: int = 0x46


class Walk1StepNortheast(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.WALK_1_STEP_NORTHEAST
    _opcode: int = 0x47


class Walk1StepFDirection(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.WALK_1_STEP_F_DIRECTION
    _opcode: int = 0x48


class AddZCoord1Step(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.ADD_Z_COORD_1_STEP
    _opcode: int = 0x4A


class DecZCoord1Step(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.DEC_Z_COORD_1_STEP
    _opcode: int = 0x4B


class ShiftEastSteps(ActionScriptCommandByteSteps):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_EAST_STEPS
    _opcode: int = 0x50


class ShiftSoutheastSteps(ActionScriptCommandByteSteps):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_SOUTHEAST_STEPS
    _opcode: int = 0x51


class ShiftSouthSteps(ActionScriptCommandByteSteps):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_SOUTH_STEPS
    _opcode: int = 0x52


class ShiftSouthwestSteps(ActionScriptCommandByteSteps):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_SOUTHWEST_STEPS
    _opcode: int = 0x53


class ShiftWestSteps(ActionScriptCommandByteSteps):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_WEST_STEPS
    _opcode: int = 0x54


class ShiftNorthwestSteps(ActionScriptCommandByteSteps):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_NORTHWEST_STEPS
    _opcode: int = 0x55


class ShiftNorthSteps(ActionScriptCommandByteSteps):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_NORTH_STEPS
    _opcode: int = 0x56


class ShiftNortheastSteps(ActionScriptCommandByteSteps):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_NORTHEAST_STEPS
    _opcode: int = 0x57


class ShiftFDirectionSteps(ActionScriptCommandByteSteps):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_F_DIRECTION_STEPS
    _opcode: int = 0x58


class ShiftZ20Steps(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_Z_20_STEPS
    _opcode: int = 0x59


class ShiftZUpSteps(ActionScriptCommandByteSteps):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_Z_UP_STEPS
    _opcode: int = 0x5A


class ShiftZDownSteps(ActionScriptCommandByteSteps):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_Z_DOWN_STEPS
    _opcode: int = 0x5B


class ShiftZUp20Steps(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_Z_UP_20_STEPS
    _opcode: int = 0x5C


class ShiftZDown20Steps(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_Z_DOWN_20_STEPS
    _opcode: int = 0x5D


class ShiftEastPixels(ActionScriptCommandBytePixels):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_EAST_PIXELS
    _opcode: int = 0x60


class ShiftSoutheastPixels(ActionScriptCommandBytePixels):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_SOUTHEAST_PIXELS
    _opcode: int = 0x61


class ShiftSouthPixels(ActionScriptCommandBytePixels):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_SOUTH_PIXELS
    _opcode: int = 0x62


class ShiftSouthwestPixels(ActionScriptCommandBytePixels):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_SOUTHWEST_PIXELS
    _opcode: int = 0x63


class ShiftWestPixels(ActionScriptCommandBytePixels):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_WEST_PIXELS
    _opcode: int = 0x64


class ShiftNorthwestPixels(ActionScriptCommandBytePixels):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_NORTHWEST_PIXELS
    _opcode: int = 0x65


class ShiftNorthPixels(ActionScriptCommandBytePixels):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_NORTH_PIXELS
    _opcode: int = 0x66


class ShiftNortheastPixels(ActionScriptCommandBytePixels):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_NORTHEAST_PIXELS
    _opcode: int = 0x67


class ShiftFDirectionPixels(ActionScriptCommandBytePixels):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_F_DIRECTION_PIXELS
    _opcode: int = 0x68


class WalkFDirection16Pixels(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.WALK_F_DIRECTION_16_PIXELS
    _opcode: int = 0x69


class ShiftZUpPixels(ActionScriptCommandBytePixels):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_Z_UP_PIXELS
    _opcode: int = 0x6A


class ShiftZDownPixels(ActionScriptCommandBytePixels):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_Z_DOWN_PIXELS
    _opcode: int = 0x6B


class FaceEast(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.FACE_EAST
    _opcode: int = 0x70


class FaceEast7C(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.FACE_EAST_7C
    _opcode: int = 0x7C


class FaceSoutheast(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.FACE_SOUTHEAST
    _opcode: int = 0x71


class FaceSouth(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.FACE_SOUTH
    _opcode: int = 0x72


class FaceSouthwest(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.FACE_SOUTHWEST
    _opcode: int = 0x73


class FaceSouthwes0t7D(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.FACE_SOUTHWEST_7D
    _opcode: int = 0x7D


class FaceWest(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.FACE_WEST
    _opcode: int = 0x74


class FaceNorthwest(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.FACE_NORTHWEST
    _opcode: int = 0x75


class FaceNorth(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.FACE_NORTH
    _opcode: int = 0x76


class FaceNortheast(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.FACE_NORTHEAST
    _opcode: int = 0x77


class FaceMario(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.FACE_MARIO
    _opcode: int = 0x78


class TurnClockwise45Degrees(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.TURN_CLOCKWISE_45_DEGREES
    _opcode: int = 0x79


class TurnClockwise45DegreesNTimes(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.TURN_CLOCKWISE_45_DEGREES_N_TIMES
    _opcode: int = 0x7B
    _size: int = 2
    _count: UInt8

    @property
    def count(self) -> UInt8:
        return self._count

    def set_count(self, count: int) -> None:
        self._count = UInt8(count)

    def __init__(self, count: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_count(count)

    def render(self) -> bytearray:
        return super().render(self.count)


class JumpToHeightSilent(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.JUMP_TO_HEIGHT_SILENT
    _opcode: int = 0x7E
    _size: int = 3
    _height: UInt16

    def height(self) -> UInt16:
        return self._height

    def set_height(self, height: int) -> None:
        self._height = UInt16(height)

    def __init__(self, height: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_height(height)

    def render(self) -> bytearray:
        return super().render(self.height)


class JumpToHeight(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.JUMP_TO_HEIGHT
    _opcode: int = 0x7F
    _size: int = 3
    _height: UInt16

    def height(self) -> UInt16:
        return self._height

    def set_height(self, height: int) -> None:
        self._height = UInt16(height)

    def __init__(self, height: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_height(height)

    def render(self) -> bytearray:
        return super().render(self.height)


class WalkToXYCoords(ActionScriptCommandXYBytes):
    _command_name: ActionScriptCommandName = cmdnm.WALK_TO_XY_COORDS
    _opcode: int = 0x80


class WalkXYSteps(ActionScriptCommandXYBytes):
    _command_name: ActionScriptCommandName = cmdnm.WALK_XY_STEPS
    _opcode: int = 0x81


class ShiftToXYCoords(ActionScriptCommandXYBytes):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_TO_XY_COORDS
    _opcode: int = 0x82


class ShiftXYSteps(ActionScriptCommandXYBytes):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_XY_STEPS
    _opcode: int = 0x83


class ShiftXYPixels(ActionScriptCommandXYBytes):
    _command_name: ActionScriptCommandName = cmdnm.SHIFT_XY_PIXELS
    _opcode: int = 0x84


class TransferToObjectXY(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.TRANSFER_TO_OBJECT_XY
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
        identifier: str = None,
    ) -> None:
        super().__init__(identifier)
        self.set_object(object)

    def render(self) -> bytearray:
        return super().render(self.object)


class TransferToObjectXYZ(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.TRANSFER_TO_OBJECT_XYZ
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
        identifier: str = None,
    ) -> None:
        super().__init__(identifier)
        self.set_object(object)

    def render(self) -> bytearray:
        return super().render(self.object)


class RunAwayShift(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.RUN_AWAY_SHIFT
    _opcode: int = 0x88


class TransferTo70167018(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.TRANSFER_TO_7016_7018
    _opcode: int = 0x89


class TransferTo70167018701A(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.TRANSFER_TO_7016_7018_701A
    _opcode: int = 0x99


class WalkTo70167018(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.WALK_TO_7016_7018
    _opcode: int = 0x8A


class WalkTo70167018701A(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.WALK_TO_7016_7018_701A
    _opcode: int = 0x98


class BounceToXYWithHeight(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.BOUNCE_TO_XY_WITH_HEIGHT
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

    def __init__(self, x: int, y: int, height: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_x(x)
        self.set_y(y)
        self.set_height(height)

    def render(self) -> bytearray:
        return super().render(self.x, self.y, self.height)


class BounceXYStepsWithHeight(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.BOUNCE_TO_XY_WITH_HEIGHT
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

    def __init__(self, x: int, y: int, height: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_x(x)
        self.set_y(y)
        self.set_height(height)

    def render(self) -> bytearray:
        return super().render(self.x, self.y, self.height)


class TransferToXYZF(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.TRANSFER_TO_XYZF
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
        self, x: int, y: int, z: int, direction: Direction, identifier: str = None
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
    _command_name: ActionScriptCommandName = cmdnm.TRANSFER_XYZF_STEPS
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
        self, x: int, y: int, z: int, direction: Direction, identifier: str = None
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
    _command_name: ActionScriptCommandName = cmdnm.TRANSFER_XYZF_PIXELS
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
        self, x: int, y: int, z: int, direction: Direction, identifier: str = None
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
    _command_name: ActionScriptCommandName = cmdnm.SET_700C_TO_OBJECT_COORD
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
        identifier: str = None,
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
    _command_name: ActionScriptCommandName = cmdnm.CREATE_PACKET_AT_NPC_COORDS
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
        identifier: str = None,
    ) -> None:
        super().__init__(identifier, destinations)
        self.set_packet_id(packet.id)
        self.set_object(object)

    def render(self) -> bytearray:
        return super().render(self.packet_id, self.object, *self.destinations)


class CreatePacketAt7010(ActionScriptCommandWithJmps):
    _command_name: ActionScriptCommandName = cmdnm.CREATE_PACKET_AT_7010
    _opcode: int = 0x3F
    _size: int = 4
    _packet_id: UInt8

    @property
    def packet_id(self) -> UInt8:
        return self._packet_id

    def set_packet_id(self, packet_id: int) -> None:
        self._packet_id = UInt8(packet_id)

    def __init__(
        self, packet: Packet, destinations: "str[int]", identifier: str = None
    ) -> None:
        super().__init__(identifier, destinations)
        self.set_packet_id(packet.id)

    def render(self) -> bytearray:
        return super().render(self.packet_id, *self.destinations)


class CreatePacketAt7010WithEvent(ActionScriptCommandWithJmps):
    _command_name: ActionScriptCommandName = cmdnm.CREATE_PACKET_AT_7010_WITH_EVENT
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
        packet: Packet,
        event_id: int,
        destinations: "str[int]",
        identifier: str = None,
    ) -> None:
        super().__init__(identifier, destinations)
        self.set_packet_id(packet.id)
        self.set_event_id(event_id)

    def render(self) -> bytearray:
        return super().render(self.packet_id, self.event_id, *self.destinations)


class SummonToLevel(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.SUMMON_TO_LEVEL
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
        self, object: AreaObject, level_id: int, identifier: str = None
    ) -> None:
        super().__init__(identifier)
        self.set_object(object)
        self.set_level_id(level_id)

    def render(self) -> bytearray:
        arg_1 = UInt16(0x8000 + (self.object << 9) + self.level_id)
        return super().render(arg_1)


class SummonObjectAt70A8ToCurrentLevel(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = (
        cmdnm.SUMMON_OBJECT_AT_70A8_TO_CURRENT_LEVEL
    )
    _opcode: int = 0xF4


class RemoveFromLevel(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.REMOVE_FROM_LEVEL
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
        self, object: AreaObject, level_id: int, identifier: str = None
    ) -> None:
        super().__init__(identifier)
        self.set_object(object)
        self.set_level_id(level_id)

    def render(self) -> bytearray:
        arg_1 = UInt16((self.object << 9) + self.level_id)
        assert 0 <= arg_1 <= 0x7FFF
        return super().render(arg_1)


class RemoveObjectAt70A8FromCurrentLevel(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = (
        cmdnm.REMOVE_OBJECT_AT_70A8_FROM_CURRENT_LEVEL
    )
    _opcode: int = 0xF5


class EnableTriggerInLevel(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.ENABLE_TRIGGER_IN_LEVEL
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
        self, object: AreaObject, level_id: int, identifier: str = None
    ) -> None:
        super().__init__(identifier)
        self.set_object(object)
        self.set_level_id(level_id)

    def render(self) -> bytearray:
        arg_1 = UInt16(0x8000 + (self.object << 9) + self.level_id)
        return super().render(arg_1)


class EnableTriggerAt70A8(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.ENABLE_TRIGGER_AT_70A8
    _opcode: int = 0xF6


class DisableTriggerInLevel(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.DISABLE_TRIGGER_IN_LEVEL
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
        self, object: AreaObject, level_id: int, identifier: str = None
    ) -> None:
        super().__init__(identifier)
        self.set_object(object)
        self.set_level_id(level_id)

    def render(self) -> bytearray:
        arg_1 = UInt16((self.object << 9) + self.level_id)
        assert 0 <= arg_1 <= 0x7FFF
        return super().render(arg_1)


class DisableTriggerAt70A8(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.DISABLE_TRIGGER_AT_70A8
    _opcode: int = 0xF7


class JmpIfObjectInLevel(ActionScriptCommandWithJmps):
    _command_name: ActionScriptCommandName = cmdnm.JMP_IF_OBJECT_IN_LEVEL
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
        identifier: str = None,
    ) -> None:
        super().__init__(identifier, destinations)
        self.set_object(object)
        self.set_level_id(level_id)

    def render(self) -> bytearray:
        arg_1 = UInt16(0x8000 + (self.object << 9) + self.level_id)
        return super().render(arg_1, *self.destinations)


class JmpIfObjectNotInLevel(ActionScriptCommandWithJmps):
    _command_name: ActionScriptCommandName = cmdnm.JMP_IF_OBJECT_NOT_IN_LEVEL
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
        identifier: str = None,
    ) -> None:
        super().__init__(identifier, destinations)
        self.set_object(object)
        self.set_level_id(level_id)

    def render(self) -> bytearray:
        arg_1 = UInt16((self.object << 9) + self.level_id)
        assert 0 <= arg_1 <= 0x7FFF
        return super().render(arg_1, *self.destinations)


class JmpIfObjectInAir(ActionScriptCommandWithJmps):
    _command_name: ActionScriptCommandName = cmdnm.JMP_IF_OBJECT_IN_AIR
    _opcode: bytearray([0xFD, 0x3D])
    _size: int = 5
    _object: AreaObject

    @property
    def object(self) -> AreaObject:
        return self._object

    def set_object(self, object: AreaObject) -> None:
        self._object = object

    def __init__(
        self, object: AreaObject, destinations: "str[int]", identifier: str = None
    ) -> None:
        super().__init__(identifier, destinations)
        self.set_object(object)

    def render(self) -> bytearray:
        return super().render(self._object, *self.destinations)


# controls


class Set700CToPressedButton(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.SET_700C_TO_PRESSED_BUTTON
    _opcode: int = 0xCA


class Set700CToTappedButton(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.SET_700C_TO_TAPPED_BUTTON
    _opcode: int = 0xCB


# palettes


class SetPaletteRow(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.SET_PALETTE_ROW
    _opcode: int = 0x0D
    _size: int = 2
    _row: UInt8

    @property
    def row(self) -> UInt8:
        return self._row

    def set_row(self, row: int) -> None:
        assert 0 <= row <= 15
        self._row = UInt8(row)

    def __init__(self, row: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_row(row)

    def render(self) -> bytearray:
        return super().render(self.row)


class IncPaletteRowBy(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.INC_PALETTE_ROW_BY
    _row: UInt8

    @property
    def row(self) -> UInt8:
        return self._row

    def set_row(self, row: int) -> None:
        self._row = UInt8(row)

    def __init__(self, row: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_row(row)
        if self.row == 1:
            self._size = 1
        else:
            self._size = 2

    def render(self) -> bytearray:
        if self.row == 1:
            return super().render(0x0F)
        return super().render(0x0E, self.row)


# branching / jumps


class BPL262728(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.BPL_26_27_28
    _opcode: int = 0x21


class BMI262728(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.BMI_26_27_28
    _opcode: int = 0x22


class BPL2627(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.BPL_26_27
    _opcode: int = 0x2A


class UnknownJmp3C(ActionScriptCommandWithJmps):
    _command_name: ActionScriptCommandName = cmdnm.UNKNOWN_JMP_3C
    _opcode: 0x3C
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
        self, arg1: int, arg2: int, destinations: "str[int]", identifier: str = None
    ) -> None:
        super().__init__(identifier, destinations)
        self.set_arg1(arg1)
        self.set_arg1(arg2)

    def render(self) -> bytearray:
        return super().render(self.arg1, self.arg2, *self.destinations)


class JmpIfMarioInAir(ActionScriptCommandWithJmps):
    _command_name: ActionScriptCommandName = cmdnm.JMP_IF_MARIO_IN_AIR
    _opcode: 0x3D

    def render(self) -> bytearray:
        return super().render(*self.destinations)


# music


class StopSound(ActionScriptCommandNoArgs):
    _command_name: ActionScriptCommandName = cmdnm.STOP_SOUND
    _opcode: 0x9B


class PlaySound(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.PLAY_SOUND
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

    def __init__(self, sound: int, channel: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_sound(sound)
        self.set_channel(channel)
        if self.channel == 4:
            self._size = 3
        else:
            self._size = 2

    def render(self) -> bytearray:
        if self.channel == 4:
            opcode = bytearray([0xFD, 0x9E])
        else:
            opcode = 0x9C
        return super().render(opcode, self.sound)


class PlaySoundBalance(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.PLAY_SOUND_BALANCE
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

    def __init__(self, sound: int, balance: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_sound(sound)
        self.set_balance(balance)

    def render(self) -> bytearray:
        return super().render(self.sound, self.balance)


class FadeOutSoundToVolume(ActionScriptCommand):
    _command_name: ActionScriptCommandName = cmdnm.FADE_OUT_SOUND_TO_VOLUME
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

    def __init__(self, duration: int, volume: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_duration(duration)
        self.set_volume(volume)

    def render(self) -> bytearray:
        return super().render(self.duration, self.volume)
