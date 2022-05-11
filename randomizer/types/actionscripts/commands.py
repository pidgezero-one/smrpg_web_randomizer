from asyncore import loop
from typing import Union
from randomizer.types.actionscripts.constants.classes import VRAMPriority
from randomizer.types.constants.misc import TOTAL_ROOMS, TOTAL_SOUNDS
from randomizer.types.packets.classes import Packet
from randomizer.utils.memsize import cast_address

from classes import (
    TransformableIdentifier,
    ActionScriptCommand,
    ActionScriptCommandNoArgs,
    ActionScriptCommandSingleJmp,
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

from ..numbers.classes import UInt16, UInt8
from ..variables import variables
from ..variables.classes import ByteVar, Flag, ShortVar


# script operations


class JmpToScript(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.JMP_TO_SCRIPT
    destination: int

    def __init__(self, destination: int, identifier: str = None) -> None:
        assert 0 <= destination < TOTAL_ACTION_SCRIPTS
        super().__init__(identifier)
        self.destination = destination


class Jmp(ActionScriptCommandSingleJmp):
    command_name: ActionScriptCommandName = cmdnm.JMP


class JmpToSubroutine(ActionScriptCommandSingleJmp):
    command_name: ActionScriptCommandName = cmdnm.JMP_TO_SUBROUTINE


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
    priority: VRAMPriority

    def __init__(self, priority: VRAMPriority, identifier: str = None) -> None:
        super().__init__(identifier)
        self.priority = priority


class SetPriority(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.SET_PRIORITY
    priority: int

    def __init__(self, priority: int, identifier: str = None) -> None:
        assert 0 <= priority <= 3
        super().__init__(identifier)
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
    bits: "set[int]"

    def __init__(self, arg_1: int, bits: "set[int]", identifier: str = None) -> None:
        assert 0 <= arg_1 <= 0xFF
        for bit in bits:
            assert 0 <= bit <= 7
        super().__init__(identifier)
        self.arg_1 = arg_1
        self.bits = bits


class ObjectMemorySetBit(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.OBJECT_MEMORY_SET_BIT
    arg_1: int
    bits: "set[int]"

    def __init__(self, arg_1: int, bits: "set[int]", identifier: str = None) -> None:
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
        super().__init__(identifier)
        self.arg_1 = arg_1
        self.bits = bits


class ObjectMemoryClearBit(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.OBJECT_MEMORY_SET_BIT
    arg_1: int
    bits: "set[int]"

    def __init__(self, arg_1: int, bits: "set[int]", identifier: str = None) -> None:
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
        super().__init__(identifier)
        self.arg_1 = arg_1
        self.bits = bits


class ObjectMemoryModifyBits(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.OBJECT_MEMORY_SET_BIT
    arg_1: int
    set_bits: "set[int]"
    clear_bits: "set[int]"

    def __init__(
        self,
        arg_1: int,
        set_bits: "set[int]" = [],
        clear_bits: "set[int]" = [],
        identifier: str = None,
    ) -> None:
        input = (arg_1, set_bits, clear_bits)
        assert input in [
            (0x09, [5], [4, 6]),
            (0x0C, [4], [3, 5]),
        ]
        super().__init__(identifier)
        self.arg_1 = arg_1
        self.set_bits = set_bits
        self.clear_bits = clear_bits


class SetBit(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.SET_BIT
    bit: Flag

    def __init__(self, bit: Flag, identifier: str = None) -> None:
        super().__init__(identifier)
        self.bit = bit


class ClearBit(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.CLEAR_BIT
    bit: Flag

    def __init__(self, bit: Flag, identifier: str = None) -> None:
        super().__init__(identifier)
        self.bit = bit


class SetMem704XAt700CBit(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.SET_MEM_704X_AT_700C_BIT


class ClearMem704XAt700CBit(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.CLEAR_MEM_704X_AT_700C_BIT


class SetVarToConst(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.SET_VAR_TO_CONST
    value: Union[UInt8, UInt16]
    address: Union[ShortVar, ByteVar]

    def __init__(self, address: int, value: int, identifier: str = None) -> None:
        super().__init__(identifier)
        try:
            self.value = UInt8(value)
            self.address = ByteVar(address)
        except:
            self.value = UInt16(value)
            self.address = ShortVar(address)


class AddConstToVar(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.ADD_CONST_TO_VAR
    value: Union[UInt8, UInt16]
    address: Union[ShortVar, ByteVar]

    def __init__(self, address: int, value: int, identifier: str = None) -> None:
        super().__init__(identifier)
        try:
            self.value = UInt8(value)
            self.address = ByteVar(address)
        except:
            self.value = UInt16(value)
            self.address = ShortVar(address)


class Inc(ActionScriptCommandAnySizeMem):
    command_name: ActionScriptCommandName = cmdnm.INC


class Dec(ActionScriptCommandAnySizeMem):
    command_name: ActionScriptCommandName = cmdnm.DEC


class CopyVarToVar(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.COPY_VAR_TO_VAR
    address_left: Union[ShortVar, ByteVar]
    address_right: Union[ShortVar, ByteVar]

    def __init__(
        self,
        address_left: int,
        address_right: int,
        identifier: str = None,
    ) -> None:
        super().__init__(identifier)
        if address_left == variables.PRIMARY_TEMP_700C:
            self.address_left = ShortVar(address_left)
            self.address_right = cast_address(address_right)
        elif address_right == variables.PRIMARY_TEMP_700C:
            self.address_left = cast_address(address_right)
            self.address_right = ShortVar(address_left)
        else:
            self.address_left = ShortVar(address_left)
            self.address_right = ShortVar(address_right)


class CompareVarToConst(ActionScriptCommandShortAddrAndValueOnly):
    command_name: ActionScriptCommandName = cmdnm.COMPARE_VAR_TO_CONST


class Compare700CToVar(ActionScriptCommandShortMem):
    command_name: ActionScriptCommandName = cmdnm.COMPARE_700C_TO_VAR


class JmpIfComparisonResultIsGreaterOrEqual(ActionScriptCommandSingleJmp):
    command_name = (
        ActionScriptCommandName
    ) = cmdnm.JMP_IF_COMPARISON_RESULT_IS_GREATER_OR_EQUAL


class JmpIfComparisonResultIsLesser(ActionScriptCommandSingleJmp):
    command_name: ActionScriptCommandName = cmdnm.JMP_IF_COMPARISON_RESULT_IS_LESSER


class SetVarToRandom(ActionScriptCommandShortAddrAndValueOnly):
    command_name: ActionScriptCommandName = cmdnm.SET_VAR_TO_RANDOM


class AddVarTo700C(ActionScriptCommandShortMem):
    command_name: ActionScriptCommandName = cmdnm.ADD_VAR_TO_700C


class DecVarFrom700C(ActionScriptCommandShortMem):
    command_name: ActionScriptCommandName = cmdnm.DEC_VAR_FROM_700C


class SwapVars(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.SWAP_VARS
    address_left: ShortVar
    address_right: ShortVar

    def __init__(
        self,
        address_left: int,
        address_right: int,
        identifier: str = None,
    ) -> None:
        super().__init__(identifier)
        self.address_left = ShortVar(address_left)
        self.address_right = ShortVar(address_right)


class Move70107015To7016701B(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.MOVE_7010_7015_TO_7016_701B


class Move7016701BTo70107015(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.MOVE_7016_701B_TO_7010_7015


class JmpIfVarEqualsConst(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.JMP_IF_VAR_EQUALS_CONST
    address: Union[ShortVar, ByteVar]
    value: UInt16
    destination: TransformableIdentifier

    def __init__(
        self,
        address: int,
        value: int,
        destination: str,
        identifier: str = None,
    ) -> None:
        super().__init__(identifier)
        self.address = cast_address(address)
        self.value = UInt16(value)
        self.destination = TransformableIdentifier(destination)


class JmpIfVarNotEqualsConst(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.JMP_IF_VAR_NOT_EQUALS_CONST
    address: Union[ShortVar, ByteVar]
    value: UInt16
    destination: str

    def __init__(
        self,
        address: int,
        value: int,
        destination: str,
        identifier: str = None,
    ) -> None:
        super().__init__(identifier)
        self.address = cast_address(address)
        self.value = UInt16(value)
        self.destination = TransformableIdentifier(destination)


class JmpIf700CAllBitsClear(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.JMP_IF_700C_ALL_BITS_CLEAR
    bits: "set[int]"
    destination: TransformableIdentifier

    def __init__(
        self,
        bits: "set[int]",
        destination: str,
        identifier: str = None,
    ) -> None:
        for bit in bits:
            assert 0 <= bit <= 7
        super().__init__(identifier)
        self.bits = bits
        self.destination = TransformableIdentifier(destination)


class JmpIf700CAnyBitsSet(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.JMP_IF_700C_ANY_BITS_SET
    bits: "set[int]"
    destination: TransformableIdentifier

    def __init__(
        self,
        bits: "set[int]",
        destination: str,
        identifier: str = None,
    ) -> None:
        for bit in bits:
            assert 0 <= bit <= 7
        super().__init__(identifier)
        self.bits = bits
        self.destination = TransformableIdentifier(destination)


class JmpIfRandomAbove66(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.JMP_IF_RANDOM_ABOVE_66

    destination: TransformableIdentifier
    destination_2: TransformableIdentifier

    def __init__(self, destination: str, destination_2: str, identifier: str) -> None:
        super().__init__(identifier)
        self.destination = TransformableIdentifier(destination)
        self.destination_2 = TransformableIdentifier(destination_2)


class JmpIfRandomAbove128(ActionScriptCommandSingleJmp):
    command_name: ActionScriptCommandName = cmdnm.JMP_IF_RANDOM_ABOVE_128


class JmpIfLoadedMemoryIs0(ActionScriptCommandSingleJmp):
    command_name: ActionScriptCommandName = cmdnm.JMP_IF_LOADED_MEMORY_IS_0


class JmpIfLoadedMemoryIsAboveOrEqual0(ActionScriptCommandSingleJmp):
    command_name = (
        ActionScriptCommandName
    ) = cmdnm.JMP_IF_LOADED_MEMORY_IS_ABOVE_OR_EQUAL_0


class JmpIfLoadedMemoryIsBelow0(ActionScriptCommandSingleJmp):
    command_name: ActionScriptCommandName = cmdnm.JMP_IF_LOADED_MEMORY_IS_BELOW_0


class JmpIfLoadedMemoryIsNot0(ActionScriptCommandSingleJmp):
    command_name: ActionScriptCommandName = cmdnm.JMP_IF_LOADED_MEMORY_IS_NOT_0


class Mem700CAndConst(ActionScriptCommandBasicShortOperation):
    command_name: ActionScriptCommandName = cmdnm.MEM_700C_AND_CONST


class Mem700CAndVar(ActionScriptCommandShortMem):
    command_name: ActionScriptCommandName = cmdnm.MEM_700C_AND_VAR


class Mem700COrConst(ActionScriptCommandBasicShortOperation):
    command_name: ActionScriptCommandName = cmdnm.MEM_700C_OR_CONST


class Mem700COrVar(ActionScriptCommandShortMem):
    command_name: ActionScriptCommandName = cmdnm.MEM_700C_OR_VAR


class Mem700CXorConst(ActionScriptCommandBasicShortOperation):
    command_name: ActionScriptCommandName = cmdnm.MEM_700C_XOR_CONST


class Mem700CXorVar(ActionScriptCommandShortMem):
    command_name: ActionScriptCommandName = cmdnm.MEM_700C_XOR_VAR


class Mem700CShiftLeft(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.MEM_700C_SHIFT_LEFT
    address: ShortVar
    shift: UInt8

    def __init__(self, address: int, shift: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.address = ShortVar(address)
        self.shift = UInt8(shift)


# sequencing


class SetSpriteSequence(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.SET_SPRITE_SEQUENCE
    sequence_or_mold_id: UInt8
    sprite_offset: UInt8
    is_mold: bool = False
    is_sequence: bool = False
    looping_off: bool = False
    mirror_sprite: bool = False

    def __init__(
        self,
        sequence_or_mold_id,
        sprite_offset,
        is_mold: bool = False,
        is_sequence: bool = False,
        looping_off: bool = False,
        mirror_sprite: bool = False,
        identifier: str = None,
    ) -> None:
        assert 0 <= sprite_offset <= 7
        if is_mold:
            assert 0 <= sequence_or_mold_id <= 31
        else:
            assert 0 <= sequence_or_mold_id <= 15
        super().__init__(identifier)
        self.sequence_or_mold_id = sequence_or_mold_id
        self.sprite_offset = sprite_offset
        self.is_mold = is_mold
        self.is_sequence = is_sequence
        self.looping_off = looping_off
        self.mirror_sprite = mirror_sprite


class SequencePlaybackOn(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.SEQUENCE_PLAYBACK_ON


class SequencePlaybackOff(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.SEQUENCE_PLAYBACK_OFF


class SequenceLoopingOn(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.SEQUENCE_LOOPING_ON


class SequenceLoopingOff(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.SEQUENCE_LOOPING_OFF


class SetAnimationSpeed(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.SET_ANIMATION_SPEED
    speed: SequenceSpeed
    sequence_not_walking: bool = False

    def __init__(
        self,
        speed: SequenceSpeed,
        sequence: bool = False,
        walking: bool = False,
        identifier: str = None,
    ) -> None:
        assert sequence ^ walking
        super().__init__(identifier)
        self.speed = speed
        self.sequence_not_walking = sequence


class EmbeddedAnimationRoutine(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.EMBEDDED_ANIMATION_ROUTINE
    args: bytearray

    def __init__(self, args: bytearray, identifier: str = None) -> None:
        assert len(args) == 16
        super().__init__(identifier)
        self.args = args


class MaximizeSequenceSpeed(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.MAXIMIZE_SEQUENCE_SPEED


class MaximizeSequenceSpeed86(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.MAXIMIZE_SEQUENCE_SPEED_86


# positioning


class FixedFCoordOn(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.FIXED_F_COORD_ON


class FixedFCoordOff(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.FIXED_F_COORD_OFF


class JmpIfObjectWithinRange(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.JMP_IF_OBJECT_WITHIN_RANGE
    object: AreaObject
    usually: UInt8
    tiles: UInt8
    destination: TransformableIdentifier

    def __init__(
        self,
        object: AreaObject,
        usually: int,
        tiles: int,
        destination: str,
        identifier: str = None,
    ) -> None:
        super().__init__(identifier)
        self.object = object
        self.usually = UInt8(usually)
        self.tiles = UInt8(tiles)
        self.destination = TransformableIdentifier(destination)


class JmpIfObjectWithinRangeSameZ(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.JMP_IF_OBJECT_WITHIN_RANGE_SAME_Z
    object: AreaObject
    usually: UInt8
    tiles: UInt8
    destination: TransformableIdentifier

    def __init__(
        self,
        object: AreaObject,
        usually: int,
        tiles: int,
        destination: str,
        identifier: str = None,
    ) -> None:
        super().__init__(identifier)
        self.object = object
        self.usually = UInt8(usually)
        self.tiles = UInt8(tiles)
        self.destination = TransformableIdentifier(destination)


class Walk1StepEast(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.WALK_1_STEP_EAST


class Walk1StepSoutheast(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.WALK_1_STEP_SOUTHEAST


class Walk1StepSouth(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.WALK_1_STEP_SOUTH


class Walk1StepSouthwest(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.WALK_1_STEP_SOUTHWEST


class Walk1StepWest(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.WALK_1_STEP_WEST


class Walk1StepNorthwest(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.WALK_1_STEP_NORTHWEST


class Walk1StepNorth(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.WALK_1_STEP_NORTH


class Walk1StepNortheast(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.WALK_1_STEP_NORTHEAST


class Walk1StepFDirection(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.WALK_1_STEP_F_DIRECTION


class AddZCoord1Step(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.ADD_Z_COORD_1_STEP


class DecZCoord1Step(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.DEC_Z_COORD_1_STEP


class ShiftEastSteps(ActionScriptCommandByteSteps):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_EAST_STEPS


class ShiftSoutheastSteps(ActionScriptCommandByteSteps):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_SOUTHEAST_STEPS


class ShiftSouthSteps(ActionScriptCommandByteSteps):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_SOUTH_STEPS


class ShiftSouthwestSteps(ActionScriptCommandByteSteps):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_SOUTHWEST_STEPS


class ShiftWestSteps(ActionScriptCommandByteSteps):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_WEST_STEPS


class ShiftNorthwestSteps(ActionScriptCommandByteSteps):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_NORTHWEST_STEPS


class ShiftNorthSteps(ActionScriptCommandByteSteps):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_NORTH_STEPS


class ShiftNortheastSteps(ActionScriptCommandByteSteps):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_NORTHEAST_STEPS


class ShiftFDirectionSteps(ActionScriptCommandByteSteps):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_F_DIRECTION_STEPS


class ShiftZ20Steps(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_Z_20_STEPS


class ShiftZUpSteps(ActionScriptCommandByteSteps):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_Z_UP_STEPS


class ShiftZDownSteps(ActionScriptCommandByteSteps):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_Z_DOWN_STEPS


class ShiftZUp20Steps(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_Z_UP_20_STEPS


class ShiftZDown20Steps(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_Z_DOWN_20_STEPS


class ShiftEastPixels(ActionScriptCommandBytePixels):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_EAST_PIXELS


class ShiftSoutheastPixels(ActionScriptCommandBytePixels):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_SOUTHEAST_PIXELS


class ShiftSouthPixels(ActionScriptCommandBytePixels):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_SOUTH_PIXELS


class ShiftSouthwestPixels(ActionScriptCommandBytePixels):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_SOUTHWEST_PIXELS


class ShiftWestPixels(ActionScriptCommandBytePixels):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_WEST_PIXELS


class ShiftNorthwestPixels(ActionScriptCommandBytePixels):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_NORTHWEST_PIXELS


class ShiftNorthPixels(ActionScriptCommandBytePixels):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_NORTH_PIXELS


class ShiftNortheastPixels(ActionScriptCommandBytePixels):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_NORTHEAST_PIXELS


class ShiftFDirectionPixels(ActionScriptCommandBytePixels):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_F_DIRECTION_PIXELS


class WalkFDirection16Pixels(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.WALK_F_DIRECTION_16_PIXELS


class ShiftZUpPixels(ActionScriptCommandBytePixels):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_Z_UP_PIXELS


class ShiftZDownPixels(ActionScriptCommandBytePixels):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_Z_DOWN_PIXELS


class FaceEast(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.FACE_EAST


class FaceSoutheast(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.FACE_SOUTHEAST


class FaceSouth(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.FACE_SOUTH


class FaceSouthwest(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.FACE_SOUTHWEST


class FaceWest(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.FACE_WEST


class FaceNorthwest(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.FACE_NORTHWEST


class FaceNorth(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.FACE_NORTH


class FaceNortheast(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.FACE_NORTHEAST


class FaceMario(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.FACE_MARIO


class TurnClockwise45Degrees(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.TURN_CLOCKWISE_45_DEGREES


class TurnClockwise45Degrees(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.TURN_CLOCKWISE_45_DEGREES


class TurnClockwise45DegreesNTimes(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.TURN_CLOCKWISE_45_DEGREES_N_TIMES
    count: UInt8

    def __init__(self, count: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.count = UInt8(count)


class JumpToHeightSilent(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.JUMP_TO_HEIGHT_SILENT
    height: UInt16

    def __init__(self, height: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.height = UInt16(height)


class JumpToHeight(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.JUMP_TO_HEIGHT
    height: UInt16

    def __init__(self, height: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.height = UInt16(height)


class WalkToXYCoords(ActionScriptCommandXYBytes):
    command_name: ActionScriptCommandName = cmdnm.WALK_TO_XY_COORDS


class WalkXYSteps(ActionScriptCommandXYBytes):
    command_name: ActionScriptCommandName = cmdnm.WALK_XY_STEPS


class ShiftToXYCoords(ActionScriptCommandXYBytes):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_TO_XY_COORDS


class ShiftXYSteps(ActionScriptCommandXYBytes):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_XY_STEPS


class ShiftXYPixels(ActionScriptCommandXYBytes):
    command_name: ActionScriptCommandName = cmdnm.SHIFT_XY_PIXELS


class TransferToObjectXY(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.TRANSFER_TO_OBJECT_XY
    object: AreaObject

    def __init__(
        self,
        object: AreaObject,
        identifier: str = None,
    ) -> None:
        super().__init__(identifier)
        self.object = object


class TransferToObjectXYZ(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.TRANSFER_TO_OBJECT_XYZ
    object: AreaObject

    def __init__(
        self,
        object: AreaObject,
        identifier: str = None,
    ) -> None:
        super().__init__(identifier)
        self.object = object


class RunAwayShift(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.RUN_AWAY_SHIFT


class TransferTo70167018(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.TRANSFER_TO_7016_7018


class TransferTo70167018701A(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.TRANSFER_TO_7016_7018_701A


class WalkTo70167018(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.WALK_TO_7016_7018


class WalkTo70167018701A(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.WALK_TO_7016_7018_701A


class BounceToXYWithHeight(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.BOUNCE_TO_XY_WITH_HEIGHT
    x: UInt8
    y: UInt8
    height: UInt8

    def __init__(self, x: int, y: int, height: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.x = UInt8(x)
        self.y = UInt8(y)
        self.height = UInt8(height)


class BounceXYStepsWithHeight(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.BOUNCE_TO_XY_WITH_HEIGHT
    x: UInt8
    y: UInt8
    height: UInt8

    def __init__(self, x: int, y: int, height: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.x = UInt8(x)
        self.y = UInt8(y)
        self.height = UInt8(height)


class TransferToXYZF(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.TRANSFER_TO_XYZF
    x: UInt8
    y: UInt8
    z: UInt8
    direction: UInt8

    def __init__(
        self, x: int, y: int, z: int, direction: Direction, identifier: str = None
    ) -> None:
        assert 0 <= z <= 31
        super().__init__(identifier)
        self.x = UInt8(x)
        self.y = UInt8(y)
        self.z = UInt8(z)
        self.direction = direction


class TransferXYZFSteps(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.TRANSFER_XYZF_STEPS
    x: UInt8
    y: UInt8
    z: UInt8
    direction: UInt8

    def __init__(
        self, x: int, y: int, z: int, direction: Direction, identifier: str = None
    ) -> None:
        assert 0 <= z <= 31
        super().__init__(identifier)
        self.x = UInt8(x)
        self.y = UInt8(y)
        self.z = UInt8(z)
        self.direction = direction


class TransferXYZFPixels(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.TRANSFER_XYZF_PIXELS
    x: UInt8
    y: UInt8
    z: UInt8
    direction: UInt8

    def __init__(
        self, x: int, y: int, z: int, direction: Direction, identifier: str = None
    ) -> None:
        assert 0 <= z <= 31
        super().__init__(identifier)
        self.x = UInt8(x)
        self.y = UInt8(y)
        self.z = UInt8(z)
        self.direction = direction


# room objects and camera


class Set700CToObjectCoord(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.SET_700C_TO_OBJECT_COORD
    object: AreaObject
    coord: Coord
    is_isometric_not_pixel: bool = False
    bit_7: bool = False

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
        self.object = object
        self.coord = coord
        self.is_isometric_not_pixel = isometric
        self.bit_7 = bit_7


class CreatePacketAtNPCCoords(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.CREATE_PACKET_AT_NPC_COORDS
    packet_id: int
    object: AreaObject
    destination: TransformableIdentifier

    def __init__(
        self,
        packet: Packet,
        object: AreaObject,
        destination: str,
        identifier: str = None,
    ) -> None:
        super().__init__(identifier)
        self.packet_id = packet.id
        self.object = object
        self.destination = TransformableIdentifier(destination)


class CreatePacketAt7010(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.CREATE_PACKET_AT_7010
    packet_id: int
    destination: TransformableIdentifier

    def __init__(
        self, packet: Packet, destination: str, identifier: str = None
    ) -> None:
        super().__init__(identifier)
        self.packet_id = packet.id
        self.destination = TransformableIdentifier(destination)


class CreatePacketAt7010WithEvent(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.CREATE_PACKET_AT_7010_WITH_EVENT
    packet_id: int
    event_id: int
    destination: TransformableIdentifier

    def __init__(
        self, packet: Packet, event_id: int, destination: str, identifier: str = None
    ) -> None:
        assert 0 <= event_id < TOTAL_EVENT_SCRIPTS
        super().__init__(identifier)
        self.packet_id = packet.id
        self.event_id = event_id
        self.destination = TransformableIdentifier(destination)


class SummonToLevel(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.SUMMON_TO_LEVEL
    object: AreaObject
    level_id: UInt16

    def __init__(
        self, object: AreaObject, level_id: int, identifier: str = None
    ) -> None:
        assert 0 <= level_id < TOTAL_ROOMS
        super().__init__(identifier)
        self.object = object
        self.level_id = UInt16(level_id)


class SummonObjectAt70A8ToCurrentLevel(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.SUMMON_OBJECT_AT_70A8_TO_CURRENT_LEVEL


class RemoveFromLevel(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.REMOVE_FROM_LEVEL
    object: AreaObject
    level_id: UInt16

    def __init__(
        self, object: AreaObject, level_id: int, identifier: str = None
    ) -> None:
        assert 0 <= level_id < TOTAL_ROOMS
        super().__init__(identifier)
        self.object = object
        self.level_id = UInt16(level_id)


class RemoveObjectAt70A8FromCurrentLevel(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = (
        cmdnm.REMOVE_OBJECT_AT_70A8_FROM_CURRENT_LEVEL
    )


class EnableTriggerInLevel(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.ENABLE_TRIGGER_IN_LEVEL
    object: AreaObject
    level_id: UInt16

    def __init__(
        self, object: AreaObject, level_id: int, identifier: str = None
    ) -> None:
        assert 0 <= level_id < TOTAL_ROOMS
        super().__init__(identifier)
        self.object = object
        self.level_id = UInt16(level_id)


class EnableTriggerAt70A8(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.ENABLE_TRIGGER_AT_70A8


class DisableTriggerInLevel(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.DISABLE_TRIGGER_IN_LEVEL
    object: AreaObject
    level_id: UInt16

    def __init__(
        self, object: AreaObject, level_id: int, identifier: str = None
    ) -> None:
        assert 0 <= level_id < TOTAL_ROOMS
        super().__init__(identifier)
        self.object = object
        self.level_id = UInt16(level_id)


class DisableTriggerAt70A8(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.DISABLE_TRIGGER_AT_70A8


class JmpIfObjectInLevel(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.JMP_IF_OBJECT_IN_LEVEL
    object: AreaObject
    level_id: UInt16
    destination: TransformableIdentifier

    def __init__(
        self,
        object: AreaObject,
        level_id: int,
        destination: str,
        identifier: str = None,
    ) -> None:
        assert 0 <= level_id < TOTAL_ROOMS
        super().__init__(identifier)
        self.object = object
        self.level_id = UInt16(level_id)
        self.destination = TransformableIdentifier(destination)


class JmpIfObjectNotInLevel(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.JMP_IF_OBJECT_NOT_IN_LEVEL
    object: AreaObject
    level_id: UInt16
    destination: TransformableIdentifier

    def __init__(
        self,
        object: AreaObject,
        level_id: int,
        destination: str,
        identifier: str = None,
    ) -> None:
        assert 0 <= level_id < TOTAL_ROOMS
        super().__init__(identifier)
        self.object = object
        self.level_id = UInt16(level_id)
        self.destination = TransformableIdentifier(destination)


class JmpIfObjectInAir(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.JMP_IF_OBJECT_IN_AIR
    object: AreaObject
    destination: TransformableIdentifier

    def __init__(
        self, object: AreaObject, destination: str, identifier: str = None
    ) -> None:
        super().__init__(identifier)
        self.object = object
        self.destination = TransformableIdentifier(destination)


# controls


class Set700CToPressedButton(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.SET_700C_TO_PRESSED_BUTTON


class Set700CToTappedButton(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.SET_700C_TO_TAPPED_BUTTON


# palettes


class SetPaletteRow(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.SET_PALETTE_ROW
    row: UInt8

    def __init__(self, row: int, identifier: str = None) -> None:
        assert 0 <= row <= 15
        super().__init__(identifier)
        self.row = UInt8(row)


class IncPaletteRowBy(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.INC_PALETTE_ROW_BY
    row: UInt8

    def __init__(self, row: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.row = UInt8(row)


# branching / jumps


class BPL262728(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.BPL_26_27_28


class BMI262728(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.BMI_26_27_28


class BPL2627(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.BPL_26_27


class UnknownJmp3C(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.UNKNOWN_JMP_3C
    arg1: UInt8
    arg2: UInt8
    destination: TransformableIdentifier

    def __init__(
        self, arg1: int, arg2: int, destination: str, identifier: str = None
    ) -> None:
        super().__init__(identifier)
        self.arg1 = UInt8(arg1)
        self.arg2 = UInt8(arg2)
        self.destination = TransformableIdentifier(destination)


class JmpIfMarioInAir(ActionScriptCommandSingleJmp):
    command_name: ActionScriptCommandName = cmdnm.JMP_IF_MARIO_IN_AIR


# music


class StopSound(ActionScriptCommandNoArgs):
    command_name: ActionScriptCommandName = cmdnm.STOP_SOUND


class PlaySound(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.PLAY_SOUND
    sound: UInt8
    channel: UInt8

    def __init__(self, sound: int, channel: int, identifier: str = None) -> None:
        assert channel in [4, 6]
        assert 0 <= sound < TOTAL_SOUNDS
        super().__init__(identifier)
        self.sound = UInt8(sound)
        self.channel = UInt8(channel)


class PlaySoundBalance(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.PLAY_SOUND_BALANCE
    sound: UInt8
    balance: UInt8

    def __init__(self, sound: int, balance: int, identifier: str = None) -> None:
        assert 0 <= sound < TOTAL_SOUNDS
        super().__init__(identifier)
        self.sound = UInt8(sound)
        self.balance = UInt8(balance)


class FadeOutSoundToVolume(ActionScriptCommand):
    command_name: ActionScriptCommandName = cmdnm.FADE_OUT_SOUND_TO_VOLUME
    duration: UInt8
    volume: UInt8

    def __init__(self, duration: int, volume: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.duration = UInt8(duration)
        self.volume = UInt8(volume)
