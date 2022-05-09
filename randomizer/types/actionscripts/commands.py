from ..variables import variables
from classes import ActionScriptCommand, ActionScriptCommandNoArgs
from constants import command_names as cmdnm
from constants.classes import ActionScriptCommandName
from constants.misc import TOTAL_SCRIPTS
from ..numbers.classes import UInt16, UInt8
from ..variables.classes import Flag


# script operations

class JmpToScript(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.JMP_TO_SCRIPT
    destination: int

    def __init__(self, destination: int, identifier: str = None) -> None:
        assert 0 <= destination <= TOTAL_SCRIPTS
        super().__init__(identifier)
        self.destination = destination


class Jmp(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.JMP
    destination: str

    def __init__(self, destination: str, identifier: str = None) -> None:
        assert destination is not None and len(destination) > 0
        super().__init__(identifier)
        self.destination = destination


class JmpToSubroutine(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.JMP_TO_SUBROUTINE
    destination: str

    def __init__(self, destination: str, identifier: str = None) -> None:
        assert destination is not None and len(destination) > 0
        super().__init__(identifier)
        self.destination = destination


class StartLoopNFrames(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.START_LOOP_N_FRAMES
    length: int

    def __init__(self, length: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.length = UInt16(length)


class StartLoopNTimes(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.START_LOOP_N_TIMES
    count: int

    def __init__(self, count: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.count = UInt16(count)


class EndLoop(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.END_LOOP


class Pause(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.PAUSE
    length: int

    def __init__(self, length: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.length = UInt16(length)


class JmpToStartOfThisScript(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.JMP_TO_START_OF_THIS_SCRIPT


class JmpToStartOfThisScriptFA(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.JMP_TO_START_OF_THIS_SCRIPT_FA


class Ret(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.RET


class EndAll(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.END_ALL


class Db(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.DB
    contents: bytearray()

    def __init__(self, contents: bytearray, identifier: str = None) -> None:
        super().__init__(identifier)
        self.contents = contents

# visibility & collision


class VisibilityOn(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.VISIBILITY_ON


class VisibilityOff(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.VISIBILITY_OFF


class ResetProperties(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.RESET_PROPERTIES


class OverwriteSolidity(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.OVERWRITE_SOLIDITY
    bit_0: bool = False
    cant_walk_under: bool = False
    cant_pass_walls: bool = False
    cant_jump_through: bool = False
    bit_4: bool = False
    cant_pass_npcs: bool = False
    cant_walk_through: bool = False
    bit_7: bool = False

    def __init__(self, bit_0: bool = False, cant_walk_under: bool = False, cant_pass_walls: bool = False, cant_jump_through: bool = False, bit_4: bool = False, cant_pass_npcs: bool = False, cant_walk_through: bool = False, bit_7: bool = False, identifier: str = None) -> None:
        super().__init__(identifier)
        self.bit_0 = bit_0
        self.cant_walk_under = cant_walk_under
        self.cant_pass_walls = cant_pass_walls
        self.cant_jump_through = cant_jump_through
        self.bit_4 = bit_4
        self.cant_pass_npcs = cant_pass_npcs
        self.cant_walk_through = cant_walk_through
        self.bit_7 = bit_7


class SetSolidityBits(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.SET_SOLIDITY_BITS
    bit_0: bool = False
    cant_walk_under: bool = False
    cant_pass_walls: bool = False
    cant_jump_through: bool = False
    bit_4: bool = False
    cant_pass_npcs: bool = False
    cant_walk_through: bool = False
    bit_7: bool = False

    def __init__(self, bit_0: bool = False, cant_walk_under: bool = False, cant_pass_walls: bool = False, cant_jump_through: bool = False, bit_4: bool = False, cant_pass_npcs: bool = False, cant_walk_through: bool = False, bit_7: bool = False, identifier: str = None) -> None:
        super().__init__(identifier)
        self.bit_0 = bit_0
        self.cant_walk_under = cant_walk_under
        self.cant_pass_walls = cant_pass_walls
        self.cant_jump_through = cant_jump_through
        self.bit_4 = bit_4
        self.cant_pass_npcs = cant_pass_npcs
        self.cant_walk_through = cant_walk_through
        self.bit_7 = bit_7


class ClearSolidityBits(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.CLEAR_SOLIDITY_BITS
    bit_0: bool = False
    cant_walk_under: bool = False
    cant_pass_walls: bool = False
    cant_jump_through: bool = False
    bit_4: bool = False
    cant_pass_npcs: bool = False
    cant_walk_through: bool = False
    bit_7: bool = False

    def __init__(self, bit_0: bool = False, cant_walk_under: bool = False, cant_pass_walls: bool = False, cant_jump_through: bool = False, bit_4: bool = False, cant_pass_npcs: bool = False, cant_walk_through: bool = False, bit_7: bool = False, identifier: str = None) -> None:
        super().__init__(identifier)
        self.bit_0 = bit_0
        self.cant_walk_under = cant_walk_under
        self.cant_pass_walls = cant_pass_walls
        self.cant_jump_through = cant_jump_through
        self.bit_4 = bit_4
        self.cant_pass_npcs = cant_pass_npcs
        self.cant_walk_through = cant_walk_through
        self.bit_7 = bit_7


class SetMovementsBits(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.SET_MOVEMENT_BITS
    bit_0: bool = False
    cant_walk_under: bool = False
    cant_pass_walls: bool = False
    cant_jump_through: bool = False
    bit_4: bool = False
    cant_pass_npcs: bool = False
    cant_walk_through: bool = False
    bit_7: bool = False

    def __init__(self, bit_0: bool = False, cant_walk_under: bool = False, cant_pass_walls: bool = False, cant_jump_through: bool = False, bit_4: bool = False, cant_pass_npcs: bool = False, cant_walk_through: bool = False, bit_7: bool = False, identifier: str = None) -> None:
        super().__init__(identifier)
        self.bit_0 = bit_0
        self.cant_walk_under = cant_walk_under
        self.cant_pass_walls = cant_pass_walls
        self.cant_jump_through = cant_jump_through
        self.bit_4 = bit_4
        self.cant_pass_npcs = cant_pass_npcs
        self.cant_walk_through = cant_walk_through
        self.bit_7 = bit_7


class SetVRAMPriority(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.SET_VRAM_PRIORITY
    priority: int

    def __init__(self, priority: int, identifier: str = None) -> None:
        super().__init__(identifier)
        assert 0 <= priority <= 3
        self.priority = priority


class SetPriority(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.SET_PRIORITY
    priority: int

    def __init__(self, priority: int, identifier: str = None) -> None:
        super().__init__(identifier)
        assert 0 <= priority <= 3
        self.priority = priority


class ShadowOn(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.SHADOW_ON


class ShadowOff(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.SHADOW_OFF


class FloatingOn(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.FLOATING_ON


class FloatingOff(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.FLOATING_OFF

# memory


class SetObjectMemoryBits(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.SET_OBJECT_MEMORY_BITS
    arg_1: int
    bits: set[int]

    def __init__(self, arg_1: int, bits: set[int], identifier: str = None) -> None:
        super().__init__(identifier)
        assert 0 <= arg_1 <= 0xFF
        for bit in bits:
            assert 0 <= bit <= 7
        self.arg_1 = arg_1
        self.bits = bits


class ObjectMemorySetBit(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.OBJECT_MEMORY_SET_BIT
    arg_1: int
    bits: set[int]

    def __init__(self, arg_1: int, bits: set[int], identifier: str = None) -> None:
        super().__init__(identifier)
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
            (0x3C, [6])
        ]
        self.arg_1 = arg_1
        self.bits = bits


class ObjectMemoryClearBit(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.OBJECT_MEMORY_SET_BIT
    arg_1: int
    bits: set[int]

    def __init__(self, arg_1: int, bits: set[int], identifier: str = None) -> None:
        super().__init__(identifier)
        input = (arg_1, bits)
        assert input in [
            (0x08, [3, 4]),
            (0x09, [7]),
            (0x0B, [3]),
            (0x0C, [3, 4, 5]),
            (0x0E, [4]),
            (0x0E, [5]),
            (0x12, [5]),
            (0x30, [4])
        ]
        self.arg_1 = arg_1
        self.bits = bits


class ObjectMemoryModifyBits(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.OBJECT_MEMORY_SET_BIT
    arg_1: int
    set_bits: set[int]
    clear_bits: set[int]

    def __init__(self, arg_1: int, set_bits: set[int] = [], clear_bits: set[int] = [], identifier: str = None) -> None:
        super().__init__(identifier)
        input = (arg_1, set_bits, clear_bits)
        assert input in [
            (0x09, [5], [4, 6]),
            (0x0C, [4], [3, 5]),
        ]
        self.arg_1 = arg_1
        self.set_bits = set_bits
        self.clear_bits = clear_bits


class SetBit(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.SET_BIT
    bit: Flag

    def __init__(self, bit: Flag, identifier: str = None) -> None:
        super().__init__(identifier)
        self.bit = bit

