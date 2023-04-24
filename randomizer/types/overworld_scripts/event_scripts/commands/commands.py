"""Individual event script command classes.
These are the building blocks of logical progression in SMRPG."""

from typing import List, Optional, Set, Type, Union, cast
from randomizer.types.overworld_scripts.arguments import (
    LAYER_L1,
    LAYER_L2,
    LAYER_L3,
    LAYER_L4,
    NPC_SPRITES,
    COORD_F,
    ITEM_ID,
    PRIMARY_TEMP_7000,
    TIMER_701C,
    TIMER_701E,
    TIMER_7020,
    TIMER_7022,
)

from randomizer.types.overworld_scripts.event_scripts.commands.types import (
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
    UsableEventScriptCommand,
)
from randomizer.types.overworld_scripts.event_scripts.ids import (
    TOTAL_SCRIPTS,
)

from randomizer.types.overworld_scripts.action_scripts.commands.types import (
    UsableActionScriptCommand,
)
from randomizer.types.overworld_scripts.action_scripts.ids import (
    TOTAL_SCRIPTS as TOTAL_ACTION_SCRIPTS,
)

from randomizer.types.overworld_scripts.arguments.types import (
    AreaObject,
    PartyCharacter,
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
    Packet,
)
from randomizer.types.overworld_scripts.ids import (
    TOTAL_ROOMS,
    TOTAL_MUSIC,
    TOTAL_SOUNDS,
    TOTAL_SHOPS,
    TOTAL_WORLD_MAP_AREAS,
    TOTAL_DIALOGS,
)

from randomizer.types.items import Equipment, Item, Weapon, Armor, Accessory

from randomizer.types.numbers import UInt16, UInt8
from randomizer.types.overworld_scripts.arguments.types import ByteVar, Flag, ShortVar
from randomizer.types.scripts_common.classes import InvalidCommandArgumentException
from randomizer.utils.number import bits_to_int, bools_to_int

# script operations


class StartLoopNFrames(UsableEventScriptCommand, EventScriptCommand):
    """Loop all commands over N frames that are between this command
    and the next `EndLoop` command."""

    _opcode: int = 0xD5
    _size: int = 3
    _length: UInt16

    @property
    def length(self) -> UInt16:
        """The total duration of the loop, in frames"""
        return self._length

    def set_length(self, length: int) -> None:
        """Set the total duration of the loop, in frames"""
        self._length = UInt16(length)

    def __init__(self, length: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_length(length)

    def render(self) -> bytearray:
        return super().render(self.length)


class StartLoopNTimes(UsableEventScriptCommand, EventScriptCommand):
    """Loop all commands over N loop iterations that are between this command
    and the next `EndLoop` command."""

    _opcode: int = 0xD4
    _size: int = 2
    _count: UInt8

    @property
    def count(self) -> UInt8:
        """The total number of times this loop should iterate"""
        return self._count

    def set_count(self, count: int) -> None:
        """Set the total number of times this loop should iterate"""
        self._count = UInt8(count)

    def __init__(self, count: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_count(count)

    def render(self) -> bytearray:
        return super().render(self.count)


class EndLoop(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """If previous commands were part of a loop, this is where the loop ends."""

    _opcode: int = 0xD7


class Jmp(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Goto a specific command by command identifier."""

    _opcode: int = 0xD2
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpToEvent(UsableEventScriptCommand, EventScriptCommand):
    """Goto event script by ID.\n
    It is highly recommended to use contextual event script
    const names for this."""

    _opcode: int = 0xD0
    _size: int = 3
    _destination: UInt16

    @property
    def destination(self) -> UInt16:
        """The ID of the script to jump to."""
        return self._destination

    def set_destination(self, destination: int) -> None:
        """Set the ID of the script to jump to.\n
        It is highly recommended to use contextual event script
        const names for this."""
        assert 0 <= destination < TOTAL_SCRIPTS
        self._destination = UInt16(destination)

    def __init__(self, destination: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_destination(destination)

    def render(self) -> bytearray:
        return super().render(self.destination)


class JmpToStartOfThisScript(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Return to the beginning of the script containing this command"""

    _opcode: int = 0xF9


class JmpToStartOfThisScriptFA(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Return to the beginning of the script containing this command.\n
    (Unknown how this differs from `JmpToStartOfThisScript`.)"""

    _opcode: int = 0xFA


class JmpToSubroutine(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Run a specific event script as a subroutine, by command identifier."""

    _opcode: int = 0xD3
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class MoveScriptToMainThread(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Move this script from being a background process to being
    the main process."""

    _opcode = bytearray([0xFD, 0x40])


class MoveScriptToBackgroundThread1(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Move this script to run as the first of two background processes."""

    _opcode = bytearray([0xFD, 0x41])


class MoveScriptToBackgroundThread2(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Move this script to run as the second of two background processes."""

    _opcode = bytearray([0xFD, 0x42])


class Pause(UsableEventScriptCommand, EventScriptCommand):
    """Pause the active script for the given number of frames"""

    _length: Union[UInt8, UInt16]

    @property
    def length(self) -> Union[UInt8, UInt16]:
        """The length of the pause, in frames"""
        return self._length

    def set_length(self, length: int) -> None:
        """Set the length of the pause, in frames, from 1 to 0x10000"""
        if 1 <= length <= 0x100:
            self._length = UInt8(length)
        elif 1 <= length <= 0x10000:
            self._length = UInt16(length)
        else:
            raise InvalidCommandArgumentException(
                f"illegal pause duration in {self.identifier}: {length}"
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
        return super().render(0xF1, frames)


class RememberLastObject(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """(unknown)"""

    _opcode = bytearray([0xFD, 0x32])


class ResumeBackgroundEvent(UsableEventScriptCommand, EventScriptCommand):
    """If a background event is paused, resume it."""

    _opcode: int = 0x47
    _size: int = 2
    _timer_var: ShortVar

    @property
    def timer_var(self) -> ShortVar:
        """(unknown)"""
        return self._timer_var

    def set_timer_var(self, timer_var: ShortVar) -> None:
        """(unknown, but must be $701C, $701E, $7020, or $7022)"""
        assert timer_var in [TIMER_701C, TIMER_701E, TIMER_7020, TIMER_7022]
        self._timer_var = timer_var

    def __init__(self, timer_var: ShortVar, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_timer_var(timer_var)

    def render(self) -> bytearray:
        timer_byte: int = (self.timer_var - 0x701C) // 2
        return super().render(timer_byte)


class RunBackgroundEvent(UsableEventScriptCommand, EventScriptCommand):
    """Run an event (by ID) as a background event.\n
    It is recommended to use event script const names."""

    _opcode: int = 0x40
    _size: int = 3
    _event_id: UInt16
    _return_on_level_exit: bool
    _bit_6: bool
    _bit_7: bool

    @property
    def event_id(self) -> UInt16:
        """The ID of the event to run in the background."""
        return self._event_id

    def set_event_id(self, event_id: int) -> None:
        """The ID of the event to run in the background.\n
        It is recommended to use event script const names."""
        assert 0 <= event_id < TOTAL_SCRIPTS
        self._event_id = UInt16(event_id)

    @property
    def return_on_level_exit(self) -> bool:
        """IF true, exit this script when the player exits the level."""
        return self._return_on_level_exit

    def set_return_on_level_exit(self, return_on_level_exit: bool) -> None:
        """IF true, exit this script when the player exits the level."""
        self._return_on_level_exit = return_on_level_exit

    @property
    def bit_6(self) -> bool:
        """(unknown)"""
        return self._bit_6

    def set_bit_6(self, bit_6: bool) -> None:
        """(unknown)"""
        self._bit_6 = bit_6

    @property
    def bit_7(self) -> bool:
        """(unknown)"""
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        """(unknown)"""
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
        self.set_return_on_level_exit(return_on_level_exit)
        self.set_bit_6(bit_6)
        self.set_bit_7(bit_7)

    def render(self) -> bytearray:
        flags: int = bools_to_int(self._return_on_level_exit, self.bit_6, self.bit_7)
        flags = flags << 13
        arg_byte = UInt16(self.event_id + flags)
        return super().render(arg_byte)


class RunBackgroundEventWithPause(UsableEventScriptCommand, EventScriptCommand):
    """(unknown)"""

    _opcode: int = 0x44
    _size: int = 4
    _event_id: UInt16
    _timer_var: ShortVar
    _bit_4: bool
    _bit_5: bool

    @property
    def event_id(self) -> UInt16:
        """The ID of the event to run in the background."""
        return self._event_id

    def set_event_id(self, event_id: int) -> None:
        """The ID of the event to run in the background.\n
        It is recommended to use event script const names."""
        assert 0 <= event_id < TOTAL_SCRIPTS
        self._event_id = UInt16(event_id)

    @property
    def timer_var(self) -> ShortVar:
        """(unknown)"""
        return self._timer_var

    def set_timer_var(self, timer_var: ShortVar) -> None:
        """(unknown)"""
        assert timer_var in [TIMER_701C, TIMER_701E, TIMER_7020, TIMER_7022]
        self._timer_var = timer_var

    @property
    def bit_4(self) -> bool:
        """(unknown)"""
        return self._bit_4

    def set_bit_4(self, bit_4: bool) -> None:
        """(unknown)"""
        self._bit_4 = bit_4

    @property
    def bit_5(self) -> bool:
        """(unknown)"""
        return self._bit_5

    def set_bit_5(self, bit_5: bool) -> None:
        """(unknown)"""
        self._bit_5 = bit_5

    def __init__(
        self,
        event_id: int,
        timer_var: ShortVar,
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
        timer = self.timer_var << 14
        arg_byte = UInt16(self.event_id + timer + flags)
        return super().render(arg_byte)


class RunBackgroundEventWithPauseReturnOnExit(
    UsableEventScriptCommand, EventScriptCommand
):
    """(unknown)"""

    _opcode: int = 0x45
    _size: int = 4
    _event_id: UInt16
    _timer_var: ShortVar
    _bit_4: bool
    _bit_5: bool

    @property
    def event_id(self) -> UInt16:
        """The ID of the event to run in the background."""
        return self._event_id

    def set_event_id(self, event_id: int) -> None:
        """The ID of the event to run in the background.\n
        It is recommended to use event script const names."""
        assert 0 <= event_id < TOTAL_SCRIPTS
        self._event_id = UInt16(event_id)

    @property
    def timer_var(self) -> ShortVar:
        """(unknown)"""
        return self._timer_var

    def set_timer_var(self, timer_var: ShortVar) -> None:
        """(unknown)"""
        assert timer_var in [TIMER_701C, TIMER_701E, TIMER_7020, TIMER_7022]
        self._timer_var = timer_var

    @property
    def bit_4(self) -> bool:
        """(unknown)"""
        return self._bit_4

    def set_bit_4(self, bit_4: bool) -> None:
        """(unknown)"""
        self._bit_4 = bit_4

    @property
    def bit_5(self) -> bool:
        """(unknown)"""
        return self._bit_5

    def set_bit_5(self, bit_5: bool) -> None:
        """(unknown)"""
        self._bit_5 = bit_5

    def __init__(
        self,
        event_id: int,
        timer_var: ShortVar,
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
        timer = self.timer_var << 14
        arg_byte = UInt16(self.event_id + timer + flags)
        return super().render(arg_byte)


class RunEventAtReturn(UsableEventScriptCommand, EventScriptCommand):
    """When the current script ends, start running the script denoted by ID.\n
    It is recommended to use event script const names."""

    _opcode = bytearray([0xFD, 0x46])
    _size: int = 4
    _event_id: UInt16

    @property
    def event_id(self) -> UInt16:
        """The ID of the event to defer."""
        return self._event_id

    def set_event_id(self, event_id: int) -> None:
        """The ID of the event to defer.\n
        It is recommended to use event script const names."""
        assert 0 <= event_id < TOTAL_SCRIPTS
        self._event_id = UInt16(event_id)

    def __init__(self, event_id: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_event_id(event_id)


class RunEventAsSubroutine(UsableEventScriptCommand, EventScriptCommand):
    """Run aother event by IDas a subroutine (function).\n
    The game will crash if you call this method from code that is
    already itself being run as a subroutine, so be careful using it.\n
    It is recommended to use event script const names."""

    _opcode: int = 0xD1
    _size: int = 3
    _event_id: UInt16

    @property
    def event_id(self) -> UInt16:
        """The ID of the event to run as a subroutine."""
        return self._event_id

    def set_event_id(self, event_id: int) -> None:
        """The ID of the event to run as a subroutine.\n
        It is recommended to use event script const names."""
        assert 0 <= event_id < TOTAL_SCRIPTS
        self._event_id = UInt16(event_id)

    def __init__(self, event_id: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_event_id(event_id)


class StopAllBackgroundEvents(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Halt all background events on all threads."""

    _opcode = bytearray([0xFD, 0x43])


class StopBackgroundEvent(UsableEventScriptCommand, EventScriptCommand):
    """Stop a background event."""

    _opcode: int = 0x46
    _size: int = 2
    _timer_var: ShortVar

    @property
    def timer_var(self) -> ShortVar:
        """(unknown)"""
        return self._timer_var

    def set_timer_var(self, timer_var: ShortVar) -> None:
        """(unknown)"""
        assert timer_var in [TIMER_701C, TIMER_701E, TIMER_7020, TIMER_7022]
        self._timer_var = timer_var

    def __init__(self, timer_var: ShortVar, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_timer_var(timer_var)

    def render(self) -> bytearray:
        timer_byte: int = (self.timer_var - 0x701C) // 2
        return super().render(timer_byte)


class Return(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Exits the execution of the current script or subroutine."""

    _opcode: int = 0xFE


class EndAll(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Exits the execution of the current script or subroutine, as well as
    any events that may have called this script as a subroutine."""

    _opcode: int = 0xFF


class ReturnFD(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """(unknown)"""

    _opcode = bytearray([0xFD, 0xFE])


class Db(UsableEventScriptCommand, EventScriptCommand):
    """Catch-all command class representing any command not represented by other
    EventScriptCommand subclasses.
    Use this sparingly as there are no safety checks to make sure that
    the number of arguments in the command are correct."""

    _contents: bytearray

    @property
    def contents(self) -> bytearray:
        """The whole contents of the command as bytes, including the opcode."""
        return self._contents

    def set_contents(self, contents: bytearray) -> None:
        """Set the whole contents of the command as bytes, including the opcode."""
        self._contents = contents

    @property
    def size(self) -> int:
        return len(self.contents)

    def __init__(self, contents: bytearray, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_contents(contents)

    def render(self) -> bytearray:
        return super().render(self.contents)


# memory operations


class If0210Bits012ClearDoNotJump(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """(unknown)"""

    _opcode = bytearray([0xFD, 0x62])
    _size: int = 4

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIf316DIs3(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """(unknown)"""

    _opcode: int = 0x41
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIf7000AllBitsClear(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """If all of the stated bits are clear on $7000, jump to the script command
    indicated by the given identifier."""

    _opcode: int = 0xE6
    _size: int = 5
    _bits: Set[int]

    @property
    def bits(self) -> Set[int]:
        """All of the bit positions which should be clear in order to execute the goto."""
        return self._bits

    def set_bits(self, bits: List[int]) -> None:
        """Overwrite the list of the bit positions which should be clear
        in order to execute the goto."""
        for bit in bits:
            assert 0 <= bit <= 15
        self._bits = set(bits)

    def __init__(
        self,
        bits: List[int],
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_bits(bits)

    def render(self) -> bytearray:
        flags = UInt16(bits_to_int(list(self.bits)))
        return super().render(flags, *self.destinations)


class JmpIf7000AnyBitsSet(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """If any of the stated bits are set on $7000, go to to the script command
    indicated by the given identifier."""

    _opcode: int = 0xE7
    _size: int = 5
    _bits: Set[int]

    @property
    def bits(self) -> Set[int]:
        """The bit positions, of which any should be set in order to execute the goto."""
        return self._bits

    def set_bits(self, bits: List[int]) -> None:
        """Overwrite the list of the bit positions which, if any one is set,
        would execute the goto."""
        for bit in bits:
            assert 0 <= bit <= 15
        self._bits = set(bits)

    def __init__(
        self,
        bits: List[int],
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_bits(bits)

    def render(self) -> bytearray:
        flags = UInt16(bits_to_int(list(self.bits)))
        return super().render(flags, *self.destinations)


class JmpIfBitSet(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Jump to a point in script bank indicated by the provided identifier,
    but only if the given long-term memory bit is set.\n
    It is recommended to specify the bit using the const names defined for
    these particular bits."""

    _size: int = 4
    _bit: Flag

    @property
    def bit(self) -> Flag:
        """The exact bit which, if set, proceeds to go to the code section
        indicated by the provided identifier."""
        return self._bit

    def set_bit(self, bit: Flag) -> None:
        """Designate the exact bit which, if set, proceeds to go to the code section
        indicated by the provided identifier."""
        self._bit = bit

    def __init__(
        self, bit: Flag, destinations: List[str], identifier: Optional[str] = None
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


class JmpIfBitClear(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Jump to a point in script bank indicated by the provided identifier,
    but only if the given long-term memory bit is clear.\n
    It is recommended to specify the bit using the const names defined for
    these particular bits."""

    _size: int = 4
    _bit: Flag

    @property
    def bit(self) -> Flag:
        """The exact bit which, if clear, proceeds to go to the code section
        indicated by the provided identifier."""
        return self._bit

    def set_bit(self, bit: Flag) -> None:
        """Designate the exact bit which, if clear, proceeds to go to the code section
        indicated by the provided identifier."""
        self._bit = bit

    def clear_bit(self, bit: Flag) -> None:
        """Designate the exact bit which, if clear, proceeds to go to the code section
        indicated by the provided identifier."""
        self.set_bit(bit)

    def __init__(
        self, bit: Flag, destinations: List[str], identifier: Optional[str] = None
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


class JmpIfLoadedMemoryIs0(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """'Loaded Memory' in most cases refers to the result of a comparison command.
    Jump to the code indicated by the given identifier if the comparison result was zero
    (both values were equal)."""

    _opcode: int = 0xEA
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfLoadedMemoryIsAboveOrEqual0(
    UsableEventScriptCommand, EventScriptCommandWithJmps
):
    """'Loaded Memory' in most cases refers to the result of a comparison command.
    Jump to the code indicated by the given identifier if the comparison result indicated
    that the first value was less than or equal the second value."""

    _opcode: int = 0xEF
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfLoadedMemoryIsBelow0(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """'Loaded Memory' in most cases refers to the result of a comparison command.
    Jump to the code indicated by the given identifier if the comparison result indicated
    that the first value was greater than the second value."""

    _opcode: int = 0xEE
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfLoadedMemoryIsNot0(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """'Loaded Memory' in most cases refers to the result of a comparison command.
    Jump to the code indicated by the given identifier if the comparison result was not zero
    (values were not equal, irrespective of which was larger or smaller)."""

    _opcode: int = 0xEB
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfMem704XAt7000BitSet(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Jump to a point in script bank indicated by the provided identifier,
    but only if the bit corresponding to the index indicated by the value
    of $7000 is set.\n
    For example, if $7000 is set to 5, then this command will jump to the code
    beginning at the given identifier if $7040 bit 5 is set. If $7000 is set
    to 12, then the jump will occur if $7041 bit 4 is set."""

    _opcode: int = 0xDB
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfMem704XAt7000BitClear(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Jump to a point in script bank indicated by the provided identifier,
    but only if the bit corresponding to the index indicated by the value
    of $7000 is clear.\n
    For example, if $7000 is set to 5, then this command will jump to the code
    beginning at the given identifier if $7040 bit 5 is clear. If $7000 is set
    to 12, then the jump will occur if $7041 bit 4 is clear."""

    _size: int = 3
    _opcode: int = 0xDF

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class SetMem704XAt7000Bit(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """For the literal value currently stored at $7000, set the bit that
    corresponds to this index (starting from $7040 bit 0).\n
    For example, if $7000 is set to 5, then $7040 bit 5 will be set. If
    $700C is set to 12, then $7041 bit 4 will be set."""

    _opcode: int = 0xA3


class ClearMem704XAt7000Bit(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """For the literal value currently stored at $7000, clear the bit that
    corresponds to this index (starting from $7040 bit 0).\n
    For example, if $7000 is set to 5, then $7040 bit 5 will be cleared. If
    $700C is set to 12, then $7041 bit 4 will be cleared."""

    _opcode: int = 0xA7


class Move70107015To7016701B(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Copy the 16 bit values stored at $7010, $7012, and $7014
    to replace the 16 bit values stored at $7016, $7018, and $701A."""

    _opcode: int = 0xBE


class Move7016701BTo70107015(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Copy the 16 bit values stored at $7016, $7018, and $701A
    to replace the 16 bit values stored at $7010, $7012, and $7014."""

    _opcode: int = 0xBF


class SetVarToConst(UsableEventScriptCommand, EventScriptCommand):
    """Set the given long-term memory variable to the given numerical literal.\n
    It is recommended to use contextual const names for these variables."""

    _value: Union[UInt8, UInt16]
    _address: Union[ShortVar, ByteVar]

    def set_value_and_address(
        self,
        address: Optional[Union[ByteVar, ShortVar]] = None,
        value: Optional[Union[int, Type[Item]]] = None,
    ) -> None:
        """Set the literal value, the destination variable, or both,
        that will be used for this command. \n
        This validates if the given number is appropriate for the given
        variable size."""
        if value is None:
            value = self.value
        if not isinstance(value, int) and issubclass(value, Item):
            value = value().item_id
        try:
            value = UInt8(value)
        except AssertionError:
            value = UInt16(value)
        if address is None:
            address = self.address
        if isinstance(value, UInt16) and isinstance(address, ByteVar):
            raise InvalidCommandArgumentException(
                f"illegal args for {self.identifier.name}: 0x{address:04x}: {value}"
            )
        if address == PRIMARY_TEMP_7000 or isinstance(address, ByteVar):
            self._size = 3
        else:
            self._size = 4
        self._address = address
        self._value = value

    @property
    def value(self) -> Union[UInt8, UInt16]:
        """The literal value to set the variable to."""
        return self._value

    @property
    def address(self) -> Union[ShortVar, ByteVar]:
        """The variable to store the literal value to.\n
        It is recommended to use contextual const names for SMRPG variables."""
        return self._address

    def __init__(
        self,
        address: Union[ShortVar, ByteVar],
        value: Union[int, Type[Item]],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_value_and_address(address, value)

    def render(self) -> bytearray:
        if isinstance(self.address, ByteVar) and isinstance(self.value, UInt8):
            return super().render(0xA8, self.address, self.value)
        if self.address == PRIMARY_TEMP_7000:
            return super().render(0xAC, UInt16(self.value))
        if isinstance(self.address, ShortVar):
            return super().render(0xB0, self.address, UInt16(self.value))
        raise InvalidCommandArgumentException(
            f"illegal args for {self.identifier.name}: 0x{self.address:04x}: {self.value}"
        )


class ReadFromAddress(UsableEventScriptCommand, EventScriptCommand):
    """(unknown)"""

    _opcode: int = 0x5C
    _size: int = 3
    _address: UInt16

    @property
    def address(self) -> UInt16:
        """(unknown)"""
        return self._address

    def set_address(self, address: int) -> None:
        """(unknown)"""
        self._address = UInt16(address)

    def __init__(self, address: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_address(address)

    def render(self) -> bytearray:
        return super().render(self.address)


class Set7000To7FMemVar(UsableEventScriptCommand, EventScriptCommand):
    """Set the value of $7000 to the value of any address between
    $7FF800 and $7FFFFF."""

    _opcode = bytearray([0xFD, 0xAC])
    _size: int = 4
    _address: UInt16

    @property
    def address(self) -> UInt16:
        """The address to copy from."""
        return self._address

    def set_address(self, address: int) -> None:
        """Designate the address for this command to copy from.
        Must be from 0xF800 to 0xFFFF."""
        assert address >= 0xF800
        self._address = UInt16(address)

    def __init__(self, address: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_address(address)

    def render(self) -> bytearray:
        return super().render(self.address - 0xF800)


class SetBit(UsableEventScriptCommand, EventScriptCommand):
    """Set a bit in the range of long-term memory bits dedicated for use in
    event and action scripts.\n
    It is recommended to specify the bit using the const names defined for
    these particular bits."""

    _size: int = 2
    _bit: Flag

    @property
    def bit(self) -> Flag:
        """The exact bit to set."""
        return self._bit

    def set_bit(self, bit: Flag) -> None:
        """Designate the exact bit to set."""
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


class ClearBit(UsableEventScriptCommand, EventScriptCommand):
    """Clear a bit in the range of long-term memory bits dedicated for use in
    event and action scripts.\n
    It is recommended to specify the bit using the const names defined for
    these particular bits."""

    _size: int = 2
    _size: int = 2
    _bit: Flag

    @property
    def bit(self) -> Flag:
        """The exact bit to clear."""
        return self._bit

    def set_bit(self, bit: Flag) -> None:
        """Designate the exact bit to clear."""
        self._bit = bit

    def clear_bit(self, bit: Flag) -> None:
        """Designate the exact bit to clear."""
        self.set_bit(bit)

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


class Set01D8Bit3(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """(unknown)"""

    _opcode = bytearray([0xFD, 0xFA])


class Set0158Bit3Offset(UsableEventScriptCommand, EventScriptCommand):
    """(unknown)"""

    _opcode = bytearray([0xFD, 0x8B])
    _size: int = 3
    _address: UInt16

    @property
    def address(self) -> UInt16:
        """(unknown)"""
        return self._address

    def set_address(self, address: int) -> None:
        """(unknown)"""
        assert address % 2 == 0 and address >= 0x0158
        self._address = UInt16(address)

    def __init__(self, address: int, identifier: Optional[str] = None):
        super().__init__(identifier)
        self.set_address(address)

    def render(self) -> bytearray:
        address_byte = (self.address - 0x0158) // 2
        address_byte &= 0x7F
        return super().render(address_byte)


class Set0158Bit7Offset(UsableEventScriptCommand, EventScriptCommand):
    """(unknown)"""

    _opcode = bytearray([0xFD, 0x88])
    _size: int = 3
    _address: UInt16
    _bit_7: bool

    @property
    def address(self) -> UInt16:
        """(unknown)"""
        return self._address

    def set_address(self, address: int) -> None:
        """(unknown)"""
        assert address % 2 == 0 and address >= 0x0158
        self._address = UInt16(address)

    @property
    def bit_7(self) -> bool:
        """(unknown)"""
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        """(unknown)"""
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


class Clear0158Bit7Offset(UsableEventScriptCommand, EventScriptCommand):
    """(unknown)"""

    _opcode = bytearray([0xFD, 0x89])
    _size: int = 3
    _address: UInt16
    _bit_7: bool

    @property
    def address(self) -> UInt16:
        """(unknown)"""
        return self._address

    def set_address(self, address: int) -> None:
        """(unknown)"""
        assert address % 2 == 0 and address >= 0x0158
        self._address = UInt16(address)

    @property
    def bit_7(self) -> bool:
        """(unknown)"""
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        """(unknown)"""
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


class Clear7016To7018AndIsolate701AHighByteIf7018Bit0Set(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """(unknown)"""

    _opcode = bytearray([0xFD, 0xC6])


class CopyVarToVar(UsableEventScriptCommand, EventScriptCommand):
    """Copy the value from one variable to another variable."""

    _from_var: Union[ShortVar, ByteVar]
    _to_var: Union[ShortVar, ByteVar]

    def set_addresses(self, from_var=None, to_var=None):
        """Set the source variable, destination variable, or both.\n
        Can accept either two 16 bit ShortVars, or $7000 and one ByteVar or ShortVar.
        Cannot accept two ByteVars."""
        if from_var is None:
            from_var = self.from_var
        if to_var is None:
            to_var = self.to_var
        if isinstance(from_var, ByteVar) and isinstance(to_var, ByteVar):
            raise InvalidCommandArgumentException(
                f"illegal args for {self.identifier.name}: 0x{from_var:04x} 0x{to_var:04x}"
            )
        if PRIMARY_TEMP_7000 not in (self.from_var, self.to_var):
            self._size = 3
        else:
            self._size = 2

    @property
    def from_var(self) -> Union[ShortVar, ByteVar]:
        """The source variable, which the value is copied from."""
        return self._from_var

    @property
    def to_var(self) -> Union[ShortVar, ByteVar]:
        """The destination variable, where the value is written to."""
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
        if self.to_var == PRIMARY_TEMP_7000 and isinstance(self.from_var, ByteVar):
            return super().render(0xB4, self.from_var)
        if self.from_var == PRIMARY_TEMP_7000 and isinstance(self.to_var, ByteVar):
            return super().render(0xB5, self.to_var)
        if self.to_var == PRIMARY_TEMP_7000 and isinstance(self.from_var, ShortVar):
            return super().render(0xBA, self.from_var)
        if self.from_var == PRIMARY_TEMP_7000 and isinstance(self.to_var, ShortVar):
            return super().render(0xBB, self.to_var)
        if isinstance(self.from_var, ShortVar) and isinstance(self.to_var, ShortVar):
            return super().render(0xBC, self.from_var, self.to_var)
        raise InvalidCommandArgumentException(
            f"""illegal args for {self.identifier.name}: 
            0x{self.from_var:04x} 0x{self.to_var:04x}"""
        )


class StoreBytesTo0335And0556(UsableEventScriptCommand, EventScriptCommand):
    """(unknown)"""

    _opcode = bytearray([0xFD, 0x90])
    _size: int = 4
    _value_1: UInt8
    _value_2: UInt8

    @property
    def value_1(self) -> UInt8:
        """(unknown)"""
        return self._value_1

    def set_value_1(self, value_1: int) -> None:
        """(unknown)"""
        self._value_1 = UInt8(value_1)

    @property
    def value_2(self) -> UInt8:
        """(unknown)"""
        return self._value_2

    def set_value_2(self, value_2: int) -> None:
        """(unknown)"""
        self._value_2 = UInt8(value_2)

    def __init__(
        self, value_1: int, value_2: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_value_1(value_1)
        self.set_value_2(value_2)

    def render(self) -> bytearray:
        return super().render(self.value_1, self.value_2)


class Store00To0248(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """(unknown)"""

    _opcode = bytearray([0xFD, 0xFC])


class Store00To0334(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """(unknown)"""

    _opcode = bytearray([0xFD, 0x93])


class Store01To0248(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """(unknown)"""

    _opcode = bytearray([0xFD, 0xFB])


class Store01To0335(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """(unknown)"""

    _opcode = bytearray([0xFD, 0x92])


class Store02To0248(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """(unknown)"""

    _opcode = bytearray([0xFD, 0xFD])


class StoreFFTo0335(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """(unknown)"""

    _opcode = bytearray([0xFD, 0x91])


class Set7000ToMinecartTimer(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Set the value of $7000 to the latest value of the minecraft timer."""

    _opcode = bytearray([0xFD, 0xB8])


class StoreSetBits(UsableEventScriptCommand, EventScriptCommand):
    """(unknown)"""

    _size: int = 3
    _bit: Flag

    @property
    def bit(self) -> Flag:
        """(unknown)"""
        return self._bit

    def set_bit(self, bit: Flag) -> None:
        """(unknown)"""
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


class SwapVars(UsableEventScriptCommand, EventScriptCommand):
    """Switch the values stored at two variables between each other."""

    _opcode: int = 0xBD
    _size: int = 3
    _from_var: ShortVar
    _to_var: ShortVar

    @property
    def from_var(self) -> ShortVar:
        """The first variable whose value to swap."""
        return self._from_var

    def set_from_var(self, from_var: ShortVar) -> None:
        """Set the first variable whose value to swap."""
        self._from_var = from_var

    @property
    def to_var(self) -> ShortVar:
        """The second variable whose value to swap."""
        return self._to_var

    def set_to_var(self, to_var: ShortVar) -> None:
        """Set the second variable whose value to swap."""
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


# math operations


class AddConstToVar(UsableEventScriptCommand, EventScriptCommand):
    """Add the given numerical literal to the given long-term memory variable.\n
    It is recommended to use contextual const names for these variables."""

    _value: Union[UInt8, UInt16]
    _address: Union[ShortVar, ByteVar]

    def set_value_and_address(self, address=None, value=None) -> None:
        """Set the literal value, the destination variable, or both,
        that will be used for this command. \n
        This validates if the given number is appropriate for the given
        variable size."""
        if value is None:
            value = self.value
        try:
            value = UInt8(value)
        except AssertionError:
            value = UInt16(value)
        if address is None:
            address = self.address
        if isinstance(value, UInt16) and isinstance(address, ByteVar):
            raise InvalidCommandArgumentException(
                f"illegal args for {self.identifier.name}: 0x{address:04x}: {value}"
            )
        if address == PRIMARY_TEMP_7000 or isinstance(address, ByteVar):
            self._size = 3
        else:
            self._size = 4
        self._address = address
        self._value = value

    @property
    def value(self) -> Union[UInt8, UInt16]:
        """The literal value to set the variable to."""
        return self._value

    @property
    def address(self) -> Union[ShortVar, ByteVar]:
        """The variable to store the literal value to.\n
        It is recommended to use contextual const names for SMRPG variables."""
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
        if self.address == PRIMARY_TEMP_7000:
            return super().render(0xAD, UInt16(self.value))
        if isinstance(self.address, ShortVar):
            return super().render(0xB1, self.address, UInt16(self.value))
        raise InvalidCommandArgumentException(
            f"illegal args for {self.identifier.name}: 0x{self.address:04x}: {self.value}"
        )


class Inc(UsableEventScriptCommand, EventScriptCommandAnySizeMem):
    """Increase the given variable by 1."""

    def render(self) -> bytearray:
        if isinstance(self.address, ByteVar):
            return super().render(0xAA, self.address)
        if self.address == PRIMARY_TEMP_7000:
            return super().render(0xAE)
        if isinstance(self.address, ShortVar):
            return super().render(0xB2, self.address)
        raise InvalidCommandArgumentException(
            f"illegal args for {self.identifier.name}: 0x{self.address:04x}"
        )


class Dec(UsableEventScriptCommand, EventScriptCommandAnySizeMem):
    """Decrease the given variable by 1."""

    def render(self) -> bytearray:
        if isinstance(self.address, ByteVar):
            return super().render(0xAB, self.address)
        if self.address == PRIMARY_TEMP_7000:
            return super().render(0xAF)
        if isinstance(self.address, ShortVar):
            return super().render(0xB3, self.address)
        raise InvalidCommandArgumentException(
            f"illegal args for {self.identifier.name}: 0x{self.address:04x}"
        )


class AddVarTo7000(UsableEventScriptCommand, EventScriptCommandShortMem):
    """Add the value stored at the given variable to $7000."""

    _opcode: int = 0xB8
    _size: int = 2


class DecVarFrom7000(UsableEventScriptCommand, EventScriptCommandShortMem):
    """Subtract the value stored at the given variable to $7000."""

    _opcode: int = 0xB9
    _size: int = 2


class GenerateRandomNumFromRangeVar(
    UsableEventScriptCommand, EventScriptCommandShortMem
):
    """Use the value of the given variable as an upper range
    to generate a random number with between 0 and that value."""

    _opcode = bytearray([0xFD, 0xB7])
    _size: int = 3


class JmpIfRandom2of3(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """There is a 2/3 chance that, when this command is executed, a goto will be performed
    to the command indicated by the given identifier."""

    _opcode: int = 0xE9
    _size: int = 5

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfRandom1of2(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """There is a 50/50 chance that, when this command is executed, a goto will be performed
    to the command indicated by the given identifier."""

    _opcode: int = 0xE8
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class SetVarToRandom(UsableEventScriptCommand, EventScriptCommandShortAddrAndValueOnly):
    """Set the given variable to a random number between 0 and the
    given upper bound."""

    def render(self) -> bytearray:
        if self.address == PRIMARY_TEMP_7000:
            return super().render(0xB6, self.value)
        return super().render(0xB7, self.address, self.value)


class CompareVarToConst(
    UsableEventScriptCommand, EventScriptCommandShortAddrAndValueOnly
):
    """Compare the value stored at a given variable to a literal constant.
    The result of this comparison can be used in JmpIfComparisonResultIs... commands
    or JmpIfLoadedMemory... commands."""

    def render(self) -> bytearray:
        if self.address == PRIMARY_TEMP_7000:
            return super().render(0xC0, self.value)
        return super().render(0xC2, self.address, self.value)

    def __init__(
        self,
        address: ShortVar,
        value: Union[int, Type[Item]],
        identifier: Optional[str] = None,
    ) -> None:
        if not isinstance(value, int) and issubclass(value, Item):
            value = value().item_id
        super().__init__(address, value, identifier)


class Compare7000ToVar(UsableEventScriptCommand, EventScriptCommandShortMem):
    """Compare the value stored at $7000 to the value stored at a given variable.
    The result of this comparison can be used in JmpIfComparisonResultIs... commands
    or JmpIfLoadedMemory... commands."""

    _opcode: int = 0xC1
    _size: int = 2


class JmpIfComparisonResultIsGreaterOrEqual(
    UsableEventScriptCommand, EventScriptCommandWithJmps
):
    """Depending on the result of an earlier CompareVarToConst or Compare7000ToVar,
    jump to the code indicated by the given identifier if the comparison result
    returned greater or equal."""

    _opcode: int = 0xEC
    _size = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfComparisonResultIsLesser(
    UsableEventScriptCommand, EventScriptCommandWithJmps
):
    """Depending on the result of an earlier CompareVarToConst or Compare7000ToVar,
    jump to the code indicated by the given identifier if the comparison result
    returned lesser."""

    _opcode: int = 0xED
    _size = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfVarEqualsConst(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """If the given variable matches the given value, jump to the section of code
    beginning with the given identifier."""

    _value: Union[UInt8, UInt16]
    _address: Union[ShortVar, ByteVar]

    def set_value_and_address(
        self,
        address: Optional[Union[ByteVar, ShortVar]] = None,
        value: Optional[Union[int, Type[Item]]] = None,
    ) -> None:
        """Set the literal value, the comparison variable, or both,
        that will be used for this command. \n
        This validates if the given number is appropriate for the given
        variable size."""
        if value is None:
            value = self.value
        if not isinstance(value, int) and issubclass(value, Item):
            value = value().item_id
        try:
            value = UInt8(value)
        except AssertionError:
            value = UInt16(value)
        if address is None:
            address = self.address
        if isinstance(value, UInt16) and isinstance(address, ByteVar):
            raise InvalidCommandArgumentException(
                f"illegal args for {self.identifier.name}: 0x{address:04x}: {value}"
            )
        if address == PRIMARY_TEMP_7000 or isinstance(address, ByteVar):
            self._size = 5
        else:
            self._size = 6
        self._address = address
        self._value = value

    @property
    def value(self) -> Union[UInt8, UInt16]:
        """The literal value to set the variable to."""
        return self._value

    @property
    def address(self) -> Union[ShortVar, ByteVar]:
        """The variable to compare the literal value to.\n
        It is recommended to use contextual const names for SMRPG variables."""
        return self._address

    def __init__(
        self,
        address: Union[ByteVar, ShortVar],
        value: Union[int, Type[Item]],
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_value_and_address(address, value)

    def render(self) -> bytearray:
        if isinstance(self.address, ByteVar) and isinstance(self.value, UInt8):
            return super().render(0xE0, self.address, self.value, *self.destinations)
        if self.address == PRIMARY_TEMP_7000:
            return super().render(0xE2, UInt16(self.value), *self.destinations)
        if isinstance(self.address, ShortVar):
            return super().render(
                0xE4, self.address, UInt16(self.value), *self.destinations
            )
        raise InvalidCommandArgumentException(
            f"illegal args for {self.identifier.name}: 0x{self.address:04x}: {self.value}"
        )


class JmpIfVarNotEqualsConst(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """If the given variable does not match the given value, jump to the section of code
    beginning with the given identifier."""

    _value: Union[UInt8, UInt16]
    _address: Union[ShortVar, ByteVar]

    def set_value_and_address(
        self,
        address: Optional[Union[ByteVar, ShortVar]] = None,
        value: Optional[Union[int, Type[Item]]] = None,
    ) -> None:
        """Set the literal value, the comparison variable, or both,
        that will be used for this command. \n
        This validates if the given number is appropriate for the given
        variable size."""
        if value is None:
            value = self.value
        if not isinstance(value, int) and issubclass(value, Item):
            value = value().item_id
        try:
            value = UInt8(value)
        except AssertionError:
            value = UInt16(value)
        if address is None:
            address = self.address
        if isinstance(value, UInt16) and isinstance(address, ByteVar):
            raise InvalidCommandArgumentException(
                f"illegal args for {self.identifier.name}: 0x{address:04x}: {value}"
            )
        if address == PRIMARY_TEMP_7000 or isinstance(address, ByteVar):
            self._size = 5
        else:
            self._size = 6
        self._address = address
        self._value = value

    @property
    def value(self) -> Union[UInt8, UInt16]:
        """The literal value to set the variable to."""
        return self._value

    @property
    def address(self) -> Union[ShortVar, ByteVar]:
        """The variable to compare the literal value to.\n
        It is recommended to use contextual const names for SMRPG variables."""
        return self._address

    def __init__(
        self,
        address: Union[ByteVar, ShortVar],
        value: Union[int, Type[Item]],
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_value_and_address(address, value)

    def render(self) -> bytearray:
        if isinstance(self.address, ByteVar) and isinstance(self.value, UInt8):
            return super().render(0xE1, self.address, self.value, *self.destinations)
        if self.address == PRIMARY_TEMP_7000:
            return super().render(0xE3, UInt16(self.value), *self.destinations)
        if isinstance(self.address, ShortVar):
            return super().render(
                0xE5, self.address, UInt16(self.value), *self.destinations
            )
        raise InvalidCommandArgumentException(
            f"illegal args for {self.identifier.name}: 0x{self.address:04x}: {self.value}"
        )


class Mem7000AndConst(UsableEventScriptCommand, EventScriptCommandBasicShortOperation):
    """Perform an AND operation between the value of $7000 and a given literal number,
    save the result to $7000."""

    _opcode = bytearray([0xFD, 0xB0])


class Mem7000AndVar(UsableEventScriptCommand, EventScriptCommandShortMem):
    """Perform an AND operation between the value of $7000 and a given variable,
    save the result to $7000."""

    _opcode = bytearray([0xFD, 0xB3])
    _size: int = 3


class Mem7000OrConst(UsableEventScriptCommand, EventScriptCommandBasicShortOperation):
    """Perform an OR operation between the value of $7000 and a given literal number,
    save the result to $7000."""

    _opcode = bytearray([0xFD, 0xB1])


class Mem7000OrVar(UsableEventScriptCommand, EventScriptCommandShortMem):
    """Perform an OR operation between the value of $7000 and a given variable,
    save the result to $7000."""

    _opcode = bytearray([0xFD, 0xB4])
    _size: int = 3


class Mem7000XorConst(UsableEventScriptCommand, EventScriptCommandBasicShortOperation):
    """Perform a XOR operation between the value of $7000 and a given literal number,
    save the result to $7000."""

    _opcode = bytearray([0xFD, 0xB2])


class Mem7000XorVar(UsableEventScriptCommand, EventScriptCommandShortMem):
    """Perform a XOR operation between the value of $7000 and a given variable,
    save the result to $7000."""

    _opcode = bytearray([0xFD, 0xB5])
    _size: int = 3


class VarShiftLeft(UsableEventScriptCommand, EventScriptCommand):
    """Shift the specified variable to the left by the given amount of bits."""

    _opcode = bytearray([0xFD, 0xB6])
    _size: int = 4
    _address: ShortVar
    _shift: UInt8

    @property
    def address(self) -> ShortVar:
        """The variable to have its value shifted."""
        return self._address

    def set_address(self, address: ShortVar) -> None:
        """Designate te variable to have its value shifted."""
        self._address = address

    @property
    def shift(self) -> UInt8:
        """The amount of bits to shift the value left by."""
        return UInt8(self._shift + 1)

    def set_shift(self, shift: int) -> None:
        """Set the amount of bits to shift the value left by."""
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


class MultiplyAndAddMem3148StoreToOffsrt7fB000PlusOutputX2(
    UsableEventScriptCommand, EventScriptCommand
):
    """(unknown)"""

    _opcode = bytearray([0xFD, 0xC8])
    _size: int = 4
    _adding: UInt8
    _multiplying: UInt8

    @property
    def adding(self) -> UInt8:
        """(unknown)"""
        return self._adding

    def set_adding(self, adding: int) -> None:
        """(unknown)"""
        self._adding = UInt8(adding)

    @property
    def multiplying(self) -> UInt8:
        """(unknown)"""
        return self._multiplying

    def set_multiplying(self, multiplying: int) -> None:
        """(unknown)"""
        self._multiplying = UInt8(multiplying)

    def __init__(
        self, adding: int, multiplying: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_adding(adding)
        self.set_multiplying(multiplying)

    def render(self) -> bytearray:
        return super().render(self.adding, self.multiplying)


class Xor3105With01(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """(unknown)"""

    _opcode = bytearray([0xFD, 0xFE])


# room objects & camera


class ActionQueueAsync(UsableEventScriptCommand, ActionQueuePrototype):
    """The specified NPC performs the given set of action script commands.
    The included action script must complete before the parent event script
    is allowed to continue.\n
    Unlike `StartAcyncEmbeddedActionScript`, this cannot be forcibly stopped
    with `StopEmbeddedActionScript`."""

    def __init__(
        self,
        target: AreaObject,
        subscript: Optional[List[UsableActionScriptCommand]] = None,
        identifier: Optional[str] = None,
    ) -> None:
        if subscript is None:
            subscript = []
        super().__init__(target, False, subscript, identifier)


class ActionQueueSync(UsableEventScriptCommand, ActionQueuePrototype):
    """The specified NPC performs the given set of action script commands.
    The included action script does not need to achieve completion in order
    for the parent event script to continue.\n
    Unlike `StartSyncEmbeddedActionScript`, this cannot be forcibly stopped
    with `StopEmbeddedActionScript`."""

    def __init__(
        self,
        target: AreaObject,
        subscript: Optional[List[UsableActionScriptCommand]] = None,
        identifier: Optional[str] = None,
    ) -> None:
        if subscript is None:
            subscript = []
        super().__init__(target, True, subscript, identifier)


class StartAsyncEmbeddedActionScript(
    UsableEventScriptCommand, StartEmbeddedActionScriptPrototype
):
    """The specified NPC performs the given set of action script commands.
    The included action script must complete before the parent event script
    is allowed to continue.\n
    Unlike `ActionQueueAsync`, this can be forcibly stopped with `StopEmbeddedActionScript`.
    """

    def __init__(
        self,
        target: AreaObject,
        prefix: int,
        subscript: Optional[List[UsableActionScriptCommand]] = None,
        identifier: Optional[str] = None,
    ) -> None:
        if subscript is None:
            subscript = []
        super().__init__(target, prefix, False, subscript, identifier)


class StartSyncEmbeddedActionScript(
    UsableEventScriptCommand, StartEmbeddedActionScriptPrototype
):
    """The specified NPC performs the given set of action script commands.
    The included action script does not need to achieve completion in order
    for the parent event script to continue.\n
    Unlike `ActionQueueSync`, this can be forcibly stopped with `StopEmbeddedActionScript`.
    """

    def __init__(
        self,
        target: AreaObject,
        prefix: int,
        subscript: Optional[List[UsableActionScriptCommand]] = None,
        identifier: Optional[str] = None,
    ) -> None:
        if subscript is None:
            subscript = []
        super().__init__(target, prefix, True, subscript, identifier)


class NonEmbeddedActionQueue(UsableEventScriptCommand, NonEmbeddedActionQueuePrototype):
    """A section of unheadered code to be run as an action script instead of an event script.\n
    When assembled, these queues contain no header to indicate where they begin.
    The game understands  where these scripts are intended to begin via ASM that
    exists outside of the scope of the script bank.\n
    Do not change the relative starting index of non-embedded action queues.
    If there were 100 bytes in the event before a non-embedded action queue begins,
    there must always be 100 bytes in the event before the non-embedded action queue begins.
    """


class _SetActionScript(UsableEventScriptCommand, EventScriptCommand):
    """Force a given NPC to run an action script by ID.\n
    It is recommended to use contextual action script ID constant names for this."""

    _size: int = 4
    _target: AreaObject
    _sync: bool
    _action_script_id: UInt16

    @property
    def target(self) -> AreaObject:
        """The NPC to run the action script."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC to run the action script."""
        self._target = target

    @property
    def sync(self) -> bool:
        """If false, the action script must complete before any further commands in the
        event script can continue."""
        return self._sync

    def set_sync(self, sync: bool) -> None:
        """If false, the action script must complete before any further commands in the
        event script can continue."""
        self._sync = sync

    @property
    def action_script_id(self) -> UInt16:
        """The ID of the action script to run.\n
        It is recommended to use contextual action script ID constant names for this."""
        return self._action_script_id

    def set_action_script_id(self, action_script_id: int) -> None:
        """Set the ID of the action script to run.\n
        It is recommended to use contextual action script ID constant names for this."""
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


class SetAsyncActionScript(
    _SetActionScript,
    UsableEventScriptCommand,
):
    """Force a given NPC to run an action script by ID.\n
    It is recommended to use contextual action script ID constant names for this.
    The action script must complete before further commands in the event script can run.
    """

    def __init__(
        self,
        target: AreaObject,
        action_script_id: int,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(target, action_script_id, False, identifier)


class SetSyncActionScript(_SetActionScript, UsableEventScriptCommand):
    """Force a given NPC to run an action script by ID.\n
    It is recommended to use contextual action script ID constant names for this.
    The action script does not need to complete before
    further commands in the event script can run."""

    def __init__(
        self,
        target: AreaObject,
        action_script_id: int,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(target, action_script_id, True, identifier)


class _SetTempActionScript(EventScriptCommand):
    """Force a given NPC to run an action script by ID, where they will resume
    their original assigned action script upon completion.\n
    It is recommended to use contextual action script ID constant names for this."""

    _size: int = 4
    _target: AreaObject
    _sync: bool
    _action_script_id: UInt16

    @property
    def target(self) -> AreaObject:
        """The NPC to run the action script."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC to run the action script."""
        self._target = target

    @property
    def sync(self) -> bool:
        """If false, the action script must complete before any further commands in the
        event script can continue."""
        return self._sync

    def set_sync(self, sync: bool) -> None:
        """If false, the action script must complete before any further commands in the
        event script can continue."""
        self._sync = sync

    @property
    def action_script_id(self) -> UInt16:
        """The ID of the action script to run.\n
        It is recommended to use contextual action script ID constant names for this."""
        return self._action_script_id

    def set_action_script_id(self, action_script_id: int) -> None:
        """Set the ID of the action script to run.\n
        It is recommended to use contextual action script ID constant names for this."""
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


class SetTempAsyncActionScript(_SetTempActionScript, UsableEventScriptCommand):
    """The specified NPC performs the given set of action script commands.
    The NPC will resume their original assigned action script upon completion
    The included action script must complete before the parent event script
    is allowed to continue."""

    def __init__(
        self,
        target: AreaObject,
        action_script_id: int,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(target, action_script_id, False, identifier)


class SetTempSyncActionScript(_SetTempActionScript, UsableEventScriptCommand):
    """The specified NPC performs the given set of action script commands.
    The NPC will resume their original assigned action script upon completion
    The action script does not need to complete before
    further commands in the event script can run."""

    def __init__(
        self,
        target: AreaObject,
        action_script_id: int,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(target, action_script_id, True, identifier)


class UnsyncActionScript(UsableEventScriptCommand, EventScriptCommand):
    """Changes an async script (blocks the progression of the main thread until completion) to
    a sync script (runs simultaneously with other event script commands)."""

    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC to run the action script."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC to run the action script."""
        self._target = target

    def __init__(self, target: AreaObject, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self) -> bytearray:
        return super().render(self.target, 0xF6)


class SummonObjectToSpecificLevel(UsableEventScriptCommand, EventScriptCommand):
    """Summon the specified NPC to the given level.\n
    This will not really do anything if the NPC has not already been
    removed from the given level.\n
    It is recommended to use contextual room constant names for this."""

    _opcode: int = 0xF2
    _size: int = 3
    _target_npc: AreaObject
    _level_id: UInt16

    @property
    def target_npc(self) -> AreaObject:
        """The NPC to be summoned to the given level."""
        return self._target_npc

    def set_target_npc(self, target_npc: AreaObject) -> None:
        """Designate the NPC to be summoned to the given level."""
        self._target_npc = target_npc

    @property
    def level_id(self) -> UInt16:
        """The ID of the room in which the NPC is to be summoned."""
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        """Designate the ID of the room in which the NPC is to be summoned.\n
        It is recommended to use contextual room constant names for this."""
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self, target_npc: AreaObject, level_id: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_target_npc(target_npc)
        self.set_level_id(level_id)

    def render(self) -> bytearray:
        arg: int = UInt16(self.level_id + (self.target_npc << 9) + (1 << 15))
        return super().render(arg)


class SummonObjectToCurrentLevel(UsableEventScriptCommand, EventScriptCommand):
    """The specified NPC will become present in the level (`visible` set to true)."""

    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The target to become active with this command."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Specify the target to become active with this command."""
        self._target = target

    def __init__(self, target: AreaObject, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self) -> bytearray:
        return super().render(self.target, 0xF8)


class SummonObjectToCurrentLevelAtMariosCoords(
    UsableEventScriptCommand, EventScriptCommand
):
    """The specified NPC will become present in the level (`visible` set to true)
    and teleported to the player's current coordinates."""

    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The target to become active with this command."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Specify the target to become active with this command."""
        self._target = target

    def __init__(self, target: AreaObject, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self) -> bytearray:
        return super().render(self.target, 0xF7)


class SummonObjectAt70A8ToCurrentLevel(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """The NPC whose relative ID is stored at $70A8 (usually the most recent NPC the player
    interacted with) will be summoned to the current level.\n
    This provides no effect if the NPC in question has not already been removed from the level.
    """

    _opcode: int = 0xF4


class RemoveObjectFromSpecificLevel(UsableEventScriptCommand, EventScriptCommand):
    """The specified NPC will be removed from the given level
    (`visible` set to false)."""

    _opcode: int = 0xF2
    _size: int = 3
    _target_npc: AreaObject
    _level_id: UInt16

    @property
    def target_npc(self) -> AreaObject:
        """The NPC to be removed from the given level."""
        return self._target_npc

    def set_target_npc(self, target_npc: AreaObject) -> None:
        """Designate the NPC to be removed from the given level."""
        self._target_npc = target_npc

    @property
    def level_id(self) -> UInt16:
        """The ID of the room in which the NPC is to be removed."""
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        """Designate the ID of the room in which the NPC is to be removed.\n
        It is recommended to use contextual room constant names for this."""
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self, target_npc: AreaObject, level_id: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_target_npc(target_npc)
        self.set_level_id(level_id)

    def render(self) -> bytearray:
        arg_raw = self.level_id + (self.target_npc << 9)
        assert 0 <= arg_raw <= 0x7FFF
        arg: int = UInt16(arg_raw)
        return super().render(arg)


class RemoveObjectFromCurrentLevel(UsableEventScriptCommand, EventScriptCommand):
    """The specified NPC will no longer be present in the level (`visible` set to false)."""

    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC to be removed from the current level."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC to be removed from the current level."""
        self._target = target

    def __init__(self, target: AreaObject, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self) -> bytearray:
        return super().render(self.target, 0xF9)


class RemoveObjectAt70A8FromCurrentLevel(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """The NPC whose relative ID is stored at $70A8 (usually the most recent NPC the player
    interacted with) will be removed from the current level.\n
    This provides no effect if the NPC in question has already been removed from the level.
    """

    _opcode: int = 0xF5


class PauseActionScript(UsableEventScriptCommand, EventScriptCommand):
    """The given NPC's action script will pause until a `ResumeActionScript`
    command runs with the same NPC as the target."""

    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The target whose action script to pause with this command."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC whose action script should be paused."""
        self._target = target

    def __init__(self, target: AreaObject, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self) -> bytearray:
        return super().render(self.target, 0xFA)


class ResumeActionScript(UsableEventScriptCommand, EventScriptCommand):
    """Resumes a paused action script for the target NPC."""

    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The target whose paused action script to resume with this command."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC whose paused action script should be resumed."""
        self._target = target

    def __init__(self, target: AreaObject, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self) -> bytearray:
        return super().render(self.target, 0xFB)


class EnableObjectTrigger(UsableEventScriptCommand, EventScriptCommand):
    """The specified NPC will become interact-able."""

    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC that should become interact-able."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC that should become interact-able."""
        self._target = target

    def __init__(self, target: AreaObject, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self) -> bytearray:
        return super().render(self.target, 0xFC)


class DisableObjectTrigger(UsableEventScriptCommand, EventScriptCommand):
    """The specified NPC will enter a state in which it cannot be interacted with."""

    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC that should become un-interact-able."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC that should become un-interact-able."""
        self._target = target

    def __init__(self, target: AreaObject, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self) -> bytearray:
        return super().render(self.target, 0xFD)


class EnableObjectTriggerInSpecificLevel(UsableEventScriptCommand, EventScriptCommand):
    """Enable the object trigger of the NPC to the given level.\n
    This will not really do anything if the NPC's object trigger has not already been
    removed from the given level.\n
    It is recommended to use contextual room constant names for this."""

    _opcode: int = 0xF3
    _size: int = 3
    _target_npc: AreaObject
    _level_id: UInt16

    @property
    def target_npc(self) -> AreaObject:
        """The NPC whose object trigger to enable (belonging to the specified level)."""
        return self._target_npc

    def set_target_npc(self, target_npc: AreaObject) -> None:
        """Designate the NPC whose object trigger to enable
        (belonging to the specified level)."""
        self._target_npc = target_npc

    @property
    def level_id(self) -> UInt16:
        """The ID of the room in which the NPC whose object trigger is being enabled lives."""
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        """Designate the ID of the room in which the NPC
        whose object trigger is being enabled lives.\n
        It is recommended to use contextual room constant names for this."""
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self, target_npc: AreaObject, level_id: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_target_npc(target_npc)
        self.set_level_id(level_id)

    def render(self) -> bytearray:
        arg_raw = self.level_id + (self.target_npc << 9) + (1 << 15)
        arg: int = UInt16(arg_raw)
        return super().render(arg)


class DisableObjectTriggerInSpecificLevel(UsableEventScriptCommand, EventScriptCommand):
    """Disable the object trigger of the NPC to the given level.\n
    This will not really do anything if the NPC's object trigger has already been
    removed from the given level.\n
    It is recommended to use contextual room constant names for this."""

    _opcode: int = 0xF3
    _size: int = 3
    _target_npc: AreaObject
    _level_id: UInt16

    @property
    def target_npc(self) -> AreaObject:
        """The NPC whose object trigger to disable (belonging to the specified level)."""
        return self._target_npc

    def set_target_npc(self, target_npc: AreaObject) -> None:
        """Designate the NPC whose object trigger to disable
        (belonging to the specified level)."""
        self._target_npc = target_npc

    @property
    def level_id(self) -> UInt16:
        """The ID of the room in which the NPC whose object trigger is being disabled lives."""
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        """Designate the ID of the room in which the NPC
        whose object trigger is being disabled lives.\n
        It is recommended to use contextual room constant names for this."""
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self, target_npc: AreaObject, level_id: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_target_npc(target_npc)
        self.set_level_id(level_id)

    def render(self) -> bytearray:
        arg_raw = self.level_id + (self.target_npc << 9)
        assert 0 <= arg_raw <= 0x7FFF
        arg: int = UInt16(arg_raw)
        return super().render(arg)


class EnableTriggerOfObjectAt70A8InCurrentLevel(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """The NPC whose relative ID is stored at $70A8 (usually the most recent NPC the player
    interacted with) will have its object trigger enabled.\n
    Because you can't interact with a disabled NPC in order to automatically write it to
    $70A8 in the first place, this would require manually writing a value to $70A8 in order
    to use this command, and thus you won't see it very often as other similar commands
    are more useful.\n
    This provides no effect if the NPC in question has not already
    had its object trigger disabled."""

    _opcode: int = 0xF6


class DisableTriggerOfObjectAt70A8InCurrentLevel(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """The NPC whose relative ID is stored at $70A8 (usually the most recent NPC the player
    interacted with) will have its object trigger disabled.\n
    This provides no effect if the NPC in question has already
    had its object trigger disabled."""

    _opcode: int = 0xF7


class StopEmbeddedActionScript(UsableEventScriptCommand, EventScriptCommand):
    """If the NPC is running an action script that was applied to it
    via an `EmbeddedActionScript` (not an `ActionQueue`), this command
    will stop it regardless of how far along in its execution it is."""

    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC whose embedded action queue is to be stopped."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC whose embedded action queue is to be stopped."""
        self._target = target

    def __init__(self, target: AreaObject, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self) -> bytearray:
        return super().render(self.target, 0xFE)


class ResetCoords(UsableEventScriptCommand, EventScriptCommand):
    """The given NPC will return to the coordinates as set in the room definition."""

    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC whose coords should be reset to the original coords listed
        in the room definition."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC whose coords should be reset to the original coords listed
        in the room definition."""
        self._target = target

    def __init__(self, target: AreaObject, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self) -> bytearray:
        return super().render(self.target, 0xFF)


class CreatePacketAtObjectCoords(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Create a packet spawning at any NPC's current coordinates.\n
    It is recommended to use contextual packet name constants for this."""

    _opcode: int = 0x3E
    _size: int = 5
    _packet_id: UInt8
    _target_npc: AreaObject

    @property
    def packet_id(self) -> UInt8:
        """The ID of the packet to create."""
        return self._packet_id

    def set_packet_id(self, packet: Packet) -> None:
        """Designate the ID of the packet to create.\n
        It is recommended to use contextual packet name constants for this."""
        self._packet_id = packet.packet_id

    @property
    def target_npc(self) -> AreaObject:
        """The NPC at whose coordinates the packet should spawn."""
        return self._target_npc

    def set_target_npc(self, target_npc: AreaObject) -> None:
        """Designate the NPC at whose coordinates the packet should spawn."""
        self._target_npc = target_npc

    def __init__(
        self,
        packet: Packet,
        target_npc: AreaObject,
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_packet_id(packet)
        self.set_target_npc(target_npc)

    def render(self) -> bytearray:
        return super().render(self.packet_id, self.target_npc, *self.destinations)


class CreatePacketAt7010(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Create a packet at pixel coordinates determined by the current values of
    $7010, $7012, and $7014.\n
    It is recommended to use contextual packet name constants for this."""

    _opcode: int = 0x3F
    _size: int = 4
    _packet_id: UInt8

    @property
    def packet_id(self) -> UInt8:
        """The ID of the packet to create."""
        return self._packet_id

    def set_packet_id(self, packet: Packet) -> None:
        """Designate the ID of the packet to create.\n
        It is recommended to use contextual packet name constants for this."""
        self._packet_id = packet.packet_id

    def __init__(
        self,
        packet: Packet,
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_packet_id(packet)

    def render(self) -> bytearray:
        return super().render(self.packet_id, *self.destinations)


class CreatePacketAt7010WithEvent(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Create a packet at pixel coordinates determined by the current values of
    $7010, $7012, and $7014. When touched, the packet will run the event
    specified by the given ID.\n
    It is recommended to use contextual packet name constants and
    contextual event name contants for this."""

    _opcode = bytearray([0xFD, 0x3E])
    _size: int = 7
    _packet_id: UInt8
    _event_id: UInt16

    @property
    def packet_id(self) -> UInt8:
        """The ID of the packet to create."""
        return self._packet_id

    def set_packet_id(self, packet: Packet) -> None:
        """Designate the ID of the packet to create.\n
        It is recommended to use contextual packet name constants for this."""
        self._packet_id = packet.packet_id

    @property
    def event_id(self) -> UInt16:
        """The ID of the event to run when the packet is touched."""
        return self._event_id

    def set_event_id(self, event_id: int) -> None:
        """Set the ID of the event to run when the packet is touched.\n
        It is recommended to use contextual event ID constants for this."""
        assert 0 <= event_id < TOTAL_SCRIPTS
        self._event_id = UInt16(event_id)

    def __init__(
        self,
        packet: Packet,
        event_id: int,
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_packet_id(packet)
        self.set_event_id(event_id)

    def render(self) -> bytearray:
        return super().render(self.packet_id, self.event_id, *self.destinations)


class FreezeAllNPCsUntilReturn(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """All NPCs in the room will have their current actions frozen until the next
    `Return` command is run."""

    _opcode: int = 0x30


class UnfreezeAllNPCs(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Cancels any commands that have frozen NPCs in the room."""

    _opcode: int = 0x31


class FreezeCamera(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The camera will no longer adjust to the player's position."""

    _opcode = bytearray([0xFD, 0x31])


class UnfreezeCamera(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The camera will resume following the player's position."""

    _opcode = bytearray([0xFD, 0x30])


class JmpIfMarioOnObject(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """If the player is currently on top of the specific NPC,
    go to the section of code beginning with the specified identifier."""

    _opcode: int = 0x39
    _size: int = 4
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC whose positioning controls whether the goto executes or not."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC whose positioning controls whether the goto executes or not."""
        self._target = target

    def __init__(
        self,
        target: AreaObject,
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_target(target)

    def render(self) -> bytearray:
        return super().render(self._target, *self.destinations)


class JmpIfMarioOnAnObjectOrNot(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Accepts two identifiers for commands to go to:\n
    One in the case where Mario is on top of any object, and
    one in the case where Mario is not on top of any object."""

    _opcode: int = 0x42
    _size: int = 5

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfObjectInAir(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """If the specified NPC is currently airborne,
    jump to the code section beginning with the specified identifier."""

    _opcode = bytearray([0xFD, 0x3D])
    _size: int = 5
    _target_npc: AreaObject

    @property
    def target_npc(self) -> AreaObject:
        """The NPC whose airborne status to check."""
        return self._target_npc

    def set_target_npc(self, target_npc: AreaObject) -> None:
        """Specify the NPC whose airborne status to check."""
        self._target_npc = target_npc

    def __init__(
        self,
        target_npc: AreaObject,
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_target_npc(target_npc)

    def render(self) -> bytearray:
        return super().render(self._target_npc, *self.destinations)


class JmpIfObjectInSpecificLevel(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """If the specified NPC is not present in the specified level,
    jump to the code section beginning with the specified identifier.\n
    It is recommended to use contextual room constant names for this."""

    _opcode: int = 0xF8
    _size: int = 5
    _target_npc: AreaObject
    _level_id: UInt16

    @property
    def target_npc(self) -> AreaObject:
        """The NPC whose presence to check in the given room."""
        return self._target_npc

    def set_target_npc(self, target_npc: AreaObject) -> None:
        """Specify the NPC whose presence to check in the given room."""
        self._target_npc = target_npc

    @property
    def level_id(self) -> UInt16:
        """The room to check for the NPC's presence in."""
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        """The room to check for the NPC's presence in.\n
        It is recommended to use contextual room constant names for this."""
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self,
        target_npc: AreaObject,
        level_id: int,
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_target_npc(target_npc)
        self.set_level_id(level_id)

    def render(self) -> bytearray:
        arg = UInt16(0x8000 + (self.target_npc << 9) + self.level_id)
        return super().render(arg, *self.destinations)


class JmpIfObjectInCurrentLevel(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """If the specified NPC is not present in the current level,
    jump to the code section beginning with the specified identifier."""

    _opcode: int = 0x32
    _size: int = 4
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC whose presence to check in the current room."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Specify the NPC whose presence to check in the current room."""
        self._target = target

    def __init__(
        self,
        target: AreaObject,
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_target(target)

    def render(self) -> bytearray:
        return super().render(self.target, *self.destinations)


class JmpIfObjectNotInSpecificLevel(
    UsableEventScriptCommand, EventScriptCommandWithJmps
):
    """If the specified NPC is not present in the specified level,
    jump to the code section beginning with the specified identifier."""

    _opcode: int = 0xF8
    _size: int = 5
    _target_npc: AreaObject
    _level_id: UInt16

    @property
    def target_npc(self) -> AreaObject:
        """The NPC whose presence to check in the given room."""
        return self._target_npc

    def set_target_npc(self, target_npc: AreaObject) -> None:
        """Specify the NPC whose presence to check in the given room."""
        self._target_npc = target_npc

    @property
    def level_id(self) -> UInt16:
        """The room to check for the NPC's presence in."""
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        """The room to check for the NPC's presence in.\n
        It is recommended to use contextual room constant names for this."""
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self,
        target_npc: AreaObject,
        level_id: int,
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_target_npc(target_npc)
        self.set_level_id(level_id)

    def render(self) -> bytearray:
        arg = UInt16((self.target_npc << 9) + self.level_id)
        assert 0 <= arg <= 0x7FFF
        return super().render(arg, *self.destinations)


class JmpIfObjectTriggerEnabledInSpecificLevel(
    UsableEventScriptCommand, EventScriptCommandWithJmps
):
    """If the specified NPC is currently interact-able in the specified level,
    jump to the code section beginning with the specified identifier.\n
    It is recommended to use contextual room constant names for this."""

    _opcode = bytearray([0xFD, 0xF0])
    _size: int = 6
    _target: AreaObject
    _level_id: UInt16

    @property
    def target(self) -> AreaObject:
        """The NPC whose interactability state to check in the given room."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Specify the NPC whose interactability stage to check in the given room."""
        self._target = target

    @property
    def level_id(self) -> UInt16:
        """The room to check the NPC's interactability state in."""
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        """The room to check the NPC's interactability state in.\n
        It is recommended to use contextual room constant names for this."""
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self,
        target: AreaObject,
        level_id: int,
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_target(target)
        self.set_level_id(level_id)

    def render(self) -> bytearray:
        arg: int = UInt16(self.level_id + (self.target << 9) + (1 << 15))
        return super().render(arg, *self.destinations)


class JmpIfObjectTriggerDisabledInSpecificLevel(
    UsableEventScriptCommand, EventScriptCommandWithJmps
):
    """If the specified NPC is not currently interact-able in the specified level,
    jump to the code section beginning with the specified identifier.\n
    It is recommended to use contextual room constant names for this."""

    _opcode = bytearray([0xFD, 0xF0])
    _size: int = 6
    _target: AreaObject
    _level_id: UInt16

    @property
    def target(self) -> AreaObject:
        """The NPC whose interactability state to check in the given room."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Specify the NPC whose interactability stage to check in the given room."""
        self._target = target

    @property
    def level_id(self) -> UInt16:
        """The room to check the NPC's interactability state in."""
        return self._level_id

    def set_level_id(self, level_id: int) -> None:
        """The room to check the NPC's interactability state in.\n
        It is recommended to use contextual room constant names for this."""
        assert 0 <= level_id < TOTAL_ROOMS
        self._level_id = UInt16(level_id)

    def __init__(
        self,
        target: AreaObject,
        level_id: int,
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_target(target)
        self.set_level_id(level_id)

    def render(self) -> bytearray:
        arg = UInt16((self.target << 9) + self.level_id)
        assert 0 <= arg <= 0x7FFF
        return super().render(arg, *self.destinations)


class JmpIfObjectIsUnderwater(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """If the specified NPC is underwater in the current level,
    jump to the code section beginning with the specified identifier."""

    _opcode = bytearray([0xFD, 0x34])
    _size: int = 5
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC whose water submersion status to check."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC whose water submersion status to check."""
        self._target = target

    def __init__(
        self,
        target: AreaObject,
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_target(target)

    def render(self) -> bytearray:
        return super().render(self.target, *self.destinations)


class JmpIfObjectActionScriptIsRunning(
    UsableEventScriptCommand, EventScriptCommandWithJmps
):
    """If the specified NPC's action script is not paused or stopped',
    jump to the code section beginning with the specified identifier."""

    _opcode = bytearray([0xFD, 0x33])
    _size: int = 5
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC whose action script status to check."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC whose action script status to check."""
        self._target = target

    def __init__(
        self,
        target: AreaObject,
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_target(target)

    def render(self) -> bytearray:
        return super().render(self.target, *self.destinations)


class JmpIfObjectsAreLessThanXYStepsApart(
    UsableEventScriptCommand, EventScriptCommandWithJmps
):
    """If the two given NPCs are less than the given number of steps
    apart (ignoring Z axis), go to the section of code indicated by the identifier."""

    _opcode: int = 0x3A
    _size: int = 7
    _object_1: AreaObject
    _object_2: AreaObject
    _x: UInt8
    _y: UInt8

    @property
    def object_1(self) -> AreaObject:
        """The first NPC in the range check."""
        return self._object_1

    def set_object_1(self, object_1: AreaObject) -> None:
        """Designate the first object in the range check."""
        self._object_1 = object_1

    @property
    def object_2(self) -> AreaObject:
        """The second NPC in the range check."""
        return self._object_2

    def set_object_2(self, object_2: AreaObject) -> None:
        """Designate the second object in the range check."""
        self._object_2 = object_2

    @property
    def x(self) -> UInt8:
        """The max number of steps on the X axis separating the
        two NPCs for which the goto can be triggered."""
        return self._x

    def set_x(self, x: int) -> None:
        """Designate the max number of steps on the X axis separating the
        two NPCs for which the goto can be triggered."""
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        """The max number of steps on the Y axis separating the
        two NPCs for which the goto can be triggered."""
        return self._y

    def set_y(self, y: int) -> None:
        """Designate the max number of steps on the Y axis separating the
        two NPCs for which the goto can be triggered."""
        self._y = UInt8(y)

    def __init__(
        self,
        object_1: AreaObject,
        object_2: AreaObject,
        x: int,
        y: int,
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_object_1(object_1)
        self.set_object_2(object_2)
        self.set_x(x)
        self.set_y(y)


class JmpIfObjectsAreLessThanXYStepsApartSameZCoord(
    UsableEventScriptCommand, EventScriptCommandWithJmps
):
    """If the two given NPCs are less than the given number of steps
    apart (when on the same Z coord), go to the section of code indicated by the identifier.
    """

    _opcode: int = 0x3B
    _size: int = 7
    _object_1: AreaObject
    _object_2: AreaObject
    _x: UInt8
    _y: UInt8

    @property
    def object_1(self) -> AreaObject:
        """The first NPC in the range check."""
        return self._object_1

    def set_object_1(self, object_1: AreaObject) -> None:
        """Designate the first object in the range check."""
        self._object_1 = object_1

    @property
    def object_2(self) -> AreaObject:
        """The second NPC in the range check."""
        return self._object_2

    def set_object_2(self, object_2: AreaObject) -> None:
        """Designate the second object in the range check."""
        self._object_2 = object_2

    @property
    def x(self) -> UInt8:
        """The max number of steps on the X axis separating the
        two NPCs for which the goto can be triggered."""
        return self._x

    def set_x(self, x: int) -> None:
        """Designate the max number of steps on the X axis separating the
        two NPCs for which the goto can be triggered."""
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        """The max number of steps on the Y axis separating the
        two NPCs for which the goto can be triggered."""
        return self._y

    def set_y(self, y: int) -> None:
        """Designate the max number of steps on the Y axis separating the
        two NPCs for which the goto can be triggered."""
        self._y = UInt8(y)

    def __init__(
        self,
        object_1: AreaObject,
        object_2: AreaObject,
        x: int,
        y: int,
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_object_1(object_1)
        self.set_object_2(object_2)
        self.set_x(x)
        self.set_y(y)


class ReactivateObject70A8TriggerIfMarioOnTopOfIt(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """The NPC whose relative ID is stored at $70A8 (usually the most recent NPC the player
    interacted with) will re-enter a state of interactability, but only if
    the player is currently on top of it."""

    _opcode: int = 0x5D


class Set7000ToObjectCoord(UsableEventScriptCommand, EventScriptCommand):
    """Sets $7000 to the pixel or isometric coordinate value of one dimension
    from any NPC's current coordinates."""

    _size: int = 2
    _size: int = 2
    _target_npc: AreaObject
    _coord: Coord
    _is_isometric_not_pixel: bool = False
    _bit_7: bool = False

    @property
    def target_npc(self) -> AreaObject:
        """The NPC from whom this value comes from."""
        return self._target_npc

    def set_target_npc(self, target_npc: AreaObject) -> None:
        """Choose the NPC from whom this value comes from."""
        self._target_npc = target_npc

    @property
    def coord(self) -> Coord:
        """The specific coordinate whose value to store to $7000."""
        return self._coord

    def set_coord(self, coord: Coord) -> None:
        """Set the specific (not-F) coordinate whose value to store to $7000."""
        assert coord != COORD_F
        self._coord = coord

    @property
    def is_isometric_not_pixel(self) -> bool:
        """If true, stores the isometric coord value (i.e. tile coord)
        instead of the pixel value."""
        return self._is_isometric_not_pixel

    def set_is_isometric_not_pixel(self, is_isometric_not_pixel: bool) -> None:
        """If true, stores the isometric coord value (i.e. tile coord)
        instead of the pixel value."""
        self._is_isometric_not_pixel = is_isometric_not_pixel

    @property
    def bit_7(self) -> bool:
        """(unknown)"""
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        """(unknown)"""
        self._bit_7 = bit_7

    def __init__(
        self,
        target_npc: AreaObject,
        coord: Coord,
        isometric: bool = False,
        pixel: bool = False,
        bit_7: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        assert isometric ^ pixel
        super().__init__(identifier)
        self.set_target_npc(target_npc)
        self.set_coord(coord)
        self.set_is_isometric_not_pixel(isometric)
        self.set_bit_7(bit_7)

    def render(self) -> bytearray:
        opcode = UInt8(0xC4 + self.coord)
        arg = UInt8(
            (self.bit_7 << 7) + (self.is_isometric_not_pixel << 6) + self.target_npc
        )
        return super().render(opcode, arg)


class Set70107015ToObjectXYZ(UsableEventScriptCommand, EventScriptCommand):
    """Copy the X, Y, and Z pixel coordinates of the NPC to $7010, $7012, and $7014."""

    _opcode: int = 0xC7
    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC whose coordinates to store."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC whose coordinates to store."""
        self._target = target

    def __init__(
        self,
        target: AreaObject,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self) -> bytearray:
        return super().render(self.target)


class Set7016701BToObjectXYZ(UsableEventScriptCommand, EventScriptCommand):
    """Copy the X, Y, and Z pixel coordinates of the NPC to $7016, $7018, and $701A."""

    _opcode: int = 0xC8
    _size: int = 2
    _target: AreaObject

    @property
    def target(self) -> AreaObject:
        """The NPC whose coordinates to store."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the NPC whose coordinates to store."""
        self._target = target

    def __init__(
        self,
        target: AreaObject,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self) -> bytearray:
        return super().render(self.target)


class SetObjectMemoryToVar(UsableEventScriptCommand, EventScriptCommandShortMem):
    """(unknown)"""

    _opcode: int = 0xD6
    _size: int = 2


# controls


class EnableControls(UsableEventScriptCommand, EventScriptCommand):
    """Buttons included in this command will be enabled, and buttons excluded will be disabled.\n
    Dpad Left = 0\n
    Dpad Right = 1\n
    Dpad Down = 2\n
    Dpad Up = 3\n
    X = 4\n
    A = 5\n
    Y = 6\n
    B = 7"""

    _opcode: int = 0x35
    _size: int = 2
    _enabled_buttons: Set[ControllerInput]

    @property
    def enabled_buttons(self) -> Set[ControllerInput]:
        """The complete list of buttons that the player can use as of this command."""
        return self._enabled_buttons

    def set_enabled_buttons(
        self, enabled_buttons: Union[List[ControllerInput], Set[ControllerInput]]
    ) -> None:
        """Overwrite the complete list of buttons that the player can use as of this command."""
        self._enabled_buttons = set(enabled_buttons)

    def __init__(
        self,
        enabled_buttons: Union[List[ControllerInput], Set[ControllerInput]],
        identifier: Optional[str] = None,
    ):
        super().__init__(identifier)
        self.set_enabled_buttons(enabled_buttons)

    def render(self) -> bytearray:
        buttons_as_ints: List[int] = cast(
            List[int], [int(b) for b in self.enabled_buttons]
        )
        arg: int = bits_to_int(buttons_as_ints)
        return super().render(arg)


class EnableControlsUntilReturn(UsableEventScriptCommand, EventScriptCommand):
    """Buttons included in this command will be enabled, and buttons excluded will be disabled.\n
    When the next `Return` command is run, all controls will be re-enabled.\n
    Dpad Left = 0\n
    Dpad Right = 1\n
    Dpad Down = 2\n
    Dpad Up = 3\n
    X = 4\n
    A = 5\n
    Y = 6\n
    B = 7"""

    _opcode: int = 0x34
    _size: int = 2
    _enabled_buttons: Set[ControllerInput]

    @property
    def enabled_buttons(self) -> Set[ControllerInput]:
        """The complete list of buttons that the player can use as of this command."""
        return self._enabled_buttons

    def set_enabled_buttons(
        self, enabled_buttons: Union[Set[ControllerInput], List[ControllerInput]]
    ) -> None:
        """Overwrite the complete list of buttons that the player can use as of this command."""
        self._enabled_buttons = set(enabled_buttons)

    def __init__(
        self,
        enabled_buttons: Optional[List[ControllerInput]] = None,
        identifier: Optional[str] = None,
    ):
        super().__init__(identifier)
        if enabled_buttons is None:
            enabled_buttons = []
        self.set_enabled_buttons(enabled_buttons)

    def render(self) -> bytearray:
        buttons_as_ints: List[int] = cast(
            List[int], [int(b) for b in self.enabled_buttons]
        )
        arg: int = bits_to_int(buttons_as_ints)
        return super().render(arg)


class Set7000ToPressedButton(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Set the bits of $7000 to correspond to all currently pressed buttons.\n
    Dpad Left = 0\n
    Dpad Right = 1\n
    Dpad Down = 2\n
    Dpad Up = 3\n
    X = 4\n
    A = 5\n
    Y = 6\n
    B = 7"""

    _opcode: int = 0xCA


class Set7000ToTappedButton(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Set the bits of $7000 to correspond to an individual tapped button.\n
    Dpad Left = 0\n
    Dpad Right = 1\n
    Dpad Down = 2\n
    Dpad Up = 3\n
    X = 4\n
    A = 5\n
    Y = 6\n
    B = 7"""

    _opcode: int = 0xCB


# inventory / party


class AddCoins(UsableEventScriptCommand, EventScriptCommand):
    """The given number will be added to the player's coin count."""

    _size: int = 2
    _amount: Union[ShortVar, UInt8]

    @property
    def amount(self) -> Union[ShortVar, UInt8]:
        """The number of coins to grant."""
        return self._amount

    def set_amount(self, amount: int) -> None:
        """Set the number of coins to grant."""
        if 0 <= amount <= 0xFF:
            self._amount = UInt8(amount)
        else:
            assert amount == 0x7000
            self._amount = ShortVar(amount)

    def __init__(self, amount: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_amount(amount)

    def render(self) -> bytearray:
        if isinstance(self.amount, ShortVar):
            return super().render(bytearray([0xFD, 0x52]))
        return super().render(0x52, self.amount)


class Dec7000FromCoins(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Decrease the player's coin count by the amount stored to $7000."""

    _opcode = bytearray([0xFD, 0x53])


class AddFrogCoins(UsableEventScriptCommand, EventScriptCommand):
    """The given number will be added to the player's Frog Coin count."""

    _size: int = 2
    _amount: Union[ShortVar, UInt8]

    @property
    def amount(self) -> Union[ShortVar, UInt8]:
        """The number of Frog Coins to grant."""
        return self._amount

    def set_amount(self, amount: int) -> None:
        """Set the number of Frog Coins to grant."""
        if 0 <= amount <= 0xFF:
            self._amount = UInt8(amount)
        else:
            assert amount == 0x7000
            self._amount = ShortVar(amount)

    def __init__(self, amount: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_amount(amount)

    def render(self) -> bytearray:
        if isinstance(self.amount, ShortVar):
            return super().render(bytearray([0xFD, 0x54]))
        return super().render(0x53, self.amount)


class Dec7000FromFrogCoins(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Decrease the player's Frog Coin count by the amount stored to $7000."""

    _opcode = bytearray([0xFD, 0x55])


class Add7000ToCurrentFP(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Add the amount stored to $7000 to the player's current FP fill."""

    _opcode = bytearray([0xFD, 0x56])


class Dec7000FromCurrentFP(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Decrease the player's current FP fill by the amount stored to $7000."""

    _opcode: int = 0x57


class Add7000ToMaxFP(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Add the amount stored to $7000 to the player's current max FP threshold."""

    _opcode = bytearray([0xFD, 0x57])


class Dec7000FromCurrentHP(UsableEventScriptCommand, EventScriptCommand):
    """Decrease the given character's current HP fill by the amount stored to $7000."""

    _opcode: int = 0x57
    _size: int = 2
    _character: PartyCharacter

    @property
    def character(self) -> PartyCharacter:
        """The playable character whose HP to decrease."""
        return self._character

    def set_character(self, character: PartyCharacter) -> None:
        """Set the playable character whose HP to decrease."""
        self._character = character

    def __init__(
        self, character: PartyCharacter, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_character(character)

    def render(self) -> bytearray:
        return super().render(self.character)


class EquipItemToCharacter(UsableEventScriptCommand, EventScriptCommand):
    """Arbitrarily equip an item to a specified character.\n
    The item does not need to exist in the player's inventory."""

    _opcode: int = 0x54
    _size: int = 3
    _character: PartyCharacter
    _item: Type[Equipment]

    @property
    def character(self) -> PartyCharacter:
        """The playable character to equip the item to."""
        return self._character

    def set_character(self, character: PartyCharacter) -> None:
        """Designate the playable character to equip the item to."""
        self._character = character

    @property
    def item(self) -> Type[Equipment]:
        """The class of item to equip to the character."""
        return self._item

    def set_item(self, item: Type[Equipment]) -> None:
        """Set the class of item to equip to the character."""
        self._item = item

    def __init__(
        self,
        item: Type[Equipment],
        character: PartyCharacter,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_character(character)
        self.set_item(item)

    def render(self) -> bytearray:
        return super().render(self.character, self.item().item_id)


class IncEXPByPacket(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The amount of EXP belonging to the packet index designated by
    `SetEXPPacketTo7000` will be added to the EXP of all recruited characters."""

    _opcode = bytearray([0xFD, 0x48])


class CharacterJoinsParty(UsableEventScriptCommand, EventScriptCommand):
    """The specified character is recruited."""

    _opcode: int = 0x36
    _size: int = 2
    _character: PartyCharacter

    @property
    def character(self) -> PartyCharacter:
        """The character being recruited."""
        return self._character

    def set_character(self, character: PartyCharacter) -> None:
        """Indicate the character being recruited."""
        self._character = character

    def __init__(
        self, character: PartyCharacter, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_character(character)

    def render(self) -> bytearray:
        return super().render(self.character + (1 << 7))


class CharacterLeavesParty(UsableEventScriptCommand, EventScriptCommand):
    """The specified character is dismissed from the party."""

    _opcode: int = 0x36
    _size: int = 2
    _character: PartyCharacter

    @property
    def character(self) -> PartyCharacter:
        """The character being dismissed."""
        return self._character

    def set_character(self, character: PartyCharacter) -> None:
        """Indicate the character being dismissed."""
        self._character = character

    def __init__(
        self, character: PartyCharacter, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_character(character)

    def render(self) -> bytearray:
        return super().render(self.character & 0x7F)


class Store70A7ToEquipsInventory(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The item whose ID matches the current value of $70A7 is
    added to the equips inventory pocket."""

    _opcode = bytearray([0xFD, 0x51])


class AddToInventory(UsableEventScriptCommand, EventScriptCommand):
    """The item matching the given ID, or the ID stored at $70A7,
    will be added to the appropriate inventory pocket."""

    _size: int = 2
    _item: Union[Type[Item], ByteVar]

    @property
    def item(self) -> Union[Type[Item], ByteVar]:
        """The item (or variable) being stored to inventory."""
        return self._item

    def set_item(self, item: Union[Type[Item], ByteVar]) -> None:
        """Acceptable values: an item class, or ITEM_ID variable."""
        if isinstance(item, ByteVar):
            assert item == ITEM_ID
            self._item = ByteVar(item)
        else:
            assert issubclass(item, Item)
            self._item = item

    def __init__(
        self, item: Union[Type[Item], ByteVar], identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_item(item)

    def render(self) -> bytearray:
        if isinstance(self.item, ByteVar):
            return super().render(bytearray([0xFD, 0x50]))
        item = self.item
        return super().render(0x50, item().item_id)


class RemoveOneOfItemFromInventory(UsableEventScriptCommand, EventScriptCommand):
    """One item matching the given ID will be removed from inventory."""

    _opcode: int = 0x51
    _size: int = 2
    _item: Type[Item]

    @property
    def item(self) -> Type[Item]:
        """The item to remove one of from inventory."""
        return self._item

    def set_item(self, item: Type[Item]) -> None:
        """Set the item to remove one of from inventory."""
        self._item = item

    def __init__(self, item: Type[Item], identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_item(item)

    def render(self) -> bytearray:
        return super().render(self.item().item_id)


class RestoreAllFP(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The player's FP will be filled to its current maximum."""

    _opcode = bytearray([0xFD, 0x5C])


class RestoreAllHP(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """All recruited characters' HP will be filled to their current maximum."""

    _opcode = bytearray([0xFD, 0x58])


class SetEXPPacketTo7000(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Set the active EXP packet to the ID corresponding to the current value
    of $7000.\n
    This will be used by `IncEXPByPacket`."""

    _opcode = bytearray([0xFD, 0x64])


class Set7000ToIDOfMemberInSlot(UsableEventScriptCommand, EventScriptCommand):
    """The value of $7000 will be set to the character ID who currently
    occupies the given slot by party index (0 to 4)."""

    _opcode: int = 0x38
    _size: int = 2
    _slot: UInt8

    @property
    def slot(self) -> UInt8:
        """The slot of the character whose ID to store to $7000."""
        return self._slot

    def set_slot(self, slot: int) -> None:
        """The slot of the character whose ID to store to $7000."""
        assert 0 <= slot <= 4
        self._slot = UInt8(slot)

    def __init__(self, slot: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_slot(slot)

    def render(self) -> bytearray:
        return super().render(0x08 + self.slot)


class Set7000ToPartySize(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Store the total party size to $7000."""

    _opcode: int = 0x37


class StoreItemAt70A7QuantityTo7000(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """For the item whose ID matches the current value of $70A7,
    check how many of that item are currently in the player inventory,
    and store that amount to $7000."""

    _opcode = bytearray([0xFD, 0x5E])


class StoreCharacterEquipmentTo7000(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """For the given equipment type on the given character,
    store the ID of the currently equipped item to $7000"""

    _opcode = bytearray([0xFD, 0x5D])
    _size: int = 4
    _character: PartyCharacter
    _equip_slot: Type[Equipment]

    @property
    def character(self) -> PartyCharacter:
        """The character whose equipment to store."""
        return self._character

    def set_character(self, character: PartyCharacter) -> None:
        """Designate the character whose equipment to store."""
        self._character = character

    @property
    def equip_slot(self) -> Type[Equipment]:
        """The equipment type to check."""
        return self._equip_slot

    def set_equip_slot(self, equip_slot: Type[Equipment]) -> None:
        """Designate the equipment type to check."""
        assert equip_slot in [Weapon, Armor, Accessory]
        self._equip_slot = equip_slot

    def __init__(
        self,
        character: PartyCharacter,
        equip_slot: Type[Equipment],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_character(character)
        self.set_equip_slot(equip_slot)

    def render(self) -> bytearray:
        return super().render(self.character, self.equip_slot().item_id)


class StoreCurrentFPTo7000(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The current FP fill amount is stored to $7000."""

    _opcode: int = 0x58


class StoreEmptyItemInventorySlotCountTo7000(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """The number of available spaces in the player's main inventory pocket
    is stored to $7000."""

    _opcode: int = 0x55


class StoreCoinCountTo7000(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The player's current coin count is stored to $7000."""

    _opcode = bytearray([0xFD, 0x59])


class StoreItemAmountTo7000(UsableEventScriptCommand, EventScriptCommand):
    """Check how many of the given item are currently in the player's inventory,
    and store that amount to $7000."""

    _opcode = bytearray([0xFD, 0x58])
    _size: int = 3
    _item: Type[Item]

    @property
    def item(self) -> Type[Item]:
        """The item whose inventory quantity to check."""
        return self._item

    def set_item(self, item: Type[Item]) -> None:
        """Set the item whose inventory quantity to check."""
        self._item = item

    def __init__(self, item: Type[Item], identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_item(item)

    def render(self) -> bytearray:
        return super().render(self.item().item_id)


class StoreFrogCoinCountTo7000(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The player's current Frog Coin count is stored to $7000."""

    _opcode = bytearray([0xFD, 0x5A])


# yourself


class JmpIfMarioInAir(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """If the player is currently airborne, go to the section of code
    beginning with the specified identifier."""

    _opcode: int = 0x3D
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class MarioGlows(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The player will glow as they normally do during an EXP star animation."""

    _opcode = bytearray([0xFD, 0xF9])


# palettes & screen effects


class PaletteSet(UsableEventScriptCommand, EventScriptCommand):
    """(The inner workings of this command are unknown.)"""

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
        """The palette set to apply to the NPCs in the current level."""
        return self._palette_set

    def set_palette_set(self, palette_set: int) -> None:
        """Designate the palette set to apply to the NPCs in the current level."""
        self._palette_set = UInt8(palette_set)

    @property
    def row(self) -> UInt8:
        """The row offset relative to the palette."""
        return self._row

    def set_row(self, row: int) -> None:
        """Designate the row offset relative to palette for this command."""
        assert 1 <= row <= 16
        self._row = UInt8(row)

    @property
    def bit_4(self) -> bool:
        """(unknown)"""
        return self._bit_4

    def set_bit_4(self, bit_4: bool) -> None:
        """(unknown)"""
        self._bit_4 = bit_4

    @property
    def bit_5(self) -> bool:
        """(unknown)"""
        return self._bit_5

    def set_bit_5(self, bit_5: bool) -> None:
        """(unknown)"""
        self._bit_5 = bit_5

    @property
    def bit_6(self) -> bool:
        """(unknown)"""
        return self._bit_6

    def set_bit_6(self, bit_6: bool) -> None:
        """(unknown)"""
        self._bit_6 = bit_6

    @property
    def bit_7(self) -> bool:
        """(unknown)"""
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        """(unknown)"""
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


class PaletteSetMorphs(UsableEventScriptCommand, EventScriptCommand):
    """(The inner workings of this command are unknown.)"""

    _opcode: int = 0xB9
    _size: int = 4
    _palette_type: PaletteType
    _palette_set: UInt8
    _duration: UInt8
    _row: UInt8

    @property
    def palette_type(self) -> PaletteType:
        """The effect to use in applying this palette."""
        return self._palette_type

    def set_palette_type(self, palette_type: PaletteType) -> None:
        """Set the effect to use in applying this palette."""
        self._palette_type = palette_type

    @property
    def palette_set(self) -> UInt8:
        """The palette set to apply to the NPCs in the current level."""
        return self._palette_set

    def set_palette_set(self, palette_set: int) -> None:
        """Designate the palette set to apply to the NPCs in the current level."""
        self._palette_set = UInt8(palette_set)

    @property
    def duration(self) -> UInt8:
        """The number of frames over which this palette morph should occur."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Set the number of frames (0-15) over which this palette morph should occur."""
        assert 0 <= duration <= 15
        self._duration = UInt8(duration)

    @property
    def row(self) -> UInt8:
        """The row offset relative to the palette."""
        return self._row

    def set_row(self, row: int) -> None:
        """Designate the row offset relative to palette for this command."""
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


class PauseScriptUntilEffectDone(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The script will not continue until an active graphical effect has finished."""

    _opcode: int = 0x7F


class PixelateLayers(UsableEventScriptCommand, EventScriptCommand):
    """Pixelate the given layers according to the given stylistic rules."""

    _opcode: int = 0x84
    _size: int = 3
    _layers: Set[Layer]
    _pixel_size: UInt8
    _duration: UInt8

    @property
    def layers(self) -> Set[Layer]:
        """The list of layers to be pixelated."""
        return self._layers

    def set_layers(self, layers: Union[List[Layer], Set[Layer]]) -> None:
        """Overwrite the layers to be pixelated."""
        for layer in layers:
            assert layer in [LAYER_L1, LAYER_L2, LAYER_L3, LAYER_L4]
        self._layers = set(layers)

    @property
    def pixel_size(self) -> UInt8:
        """The size of the rendered pixels."""
        return self._pixel_size

    def set_pixel_size(self, pixel_size: int) -> None:
        """Set the size (0-15) of the rendered pixels."""
        assert 0 <= pixel_size <= 15
        self._pixel_size = UInt8(pixel_size)

    @property
    def duration(self) -> UInt8:
        """The number of frames over which to complete the pixel effect."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Set the number of frames (0-63) over which to complete the pixel effect."""
        assert 0 <= duration <= 63
        self._duration = UInt8(duration)

    def __init__(
        self,
        layers: Union[List[Layer], Set[Layer]],
        pixel_size: int,
        duration: int,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_layers(layers)
        self.set_pixel_size(pixel_size)
        self.set_duration(duration)

    def render(self) -> bytearray:
        layers: int = bits_to_int(cast(List[int], self.layers))
        arg_1 = UInt8(layers + (self.pixel_size << 4))
        return super().render(arg_1, self.duration)


class PrioritySet(UsableEventScriptCommand, EventScriptCommand):
    """(unknown)"""

    _opcode: int = 0x81
    _size: int = 4
    _mainscreen: Set[Layer]
    _subscreen: Set[Layer]
    _colour_math: Set[Layer]

    @property
    def mainscreen(self) -> Set[Layer]:
        """(unknown)"""
        return self._mainscreen

    def set_mainscreen(self, mainscreen: Union[List[Layer], Set[Layer]]) -> None:
        """(unknown)"""
        for layer in mainscreen:
            assert layer in [LAYER_L1, LAYER_L2, LAYER_L3, NPC_SPRITES]
        self._mainscreen = set(mainscreen)

    @property
    def subscreen(self) -> Set[Layer]:
        """(unknown)"""
        return self._subscreen

    def set_subscreen(self, subscreen: Union[List[Layer], Set[Layer]]) -> None:
        """(unknown)"""
        for layer in subscreen:
            assert layer in [LAYER_L1, LAYER_L2, LAYER_L3, NPC_SPRITES]
        self._subscreen = set(subscreen)

    @property
    def colour_math(self) -> Set[Layer]:
        """(unknown)"""
        return self._colour_math

    def set_colour_math(self, colour_math: Union[List[Layer], Set[Layer]]) -> None:
        """(unknown)"""
        for layer in colour_math:
            assert layer != LAYER_L4
        self._colour_math = set(colour_math)

    def __init__(
        self,
        mainscreen: Union[List[Layer], Set[Layer]],
        subscreen: Union[List[Layer], Set[Layer]],
        colour_math: Union[List[Layer], Set[Layer]],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_mainscreen(mainscreen)
        self.set_subscreen(subscreen)
        self.set_colour_math(colour_math)

    def render(self) -> bytearray:
        mainscreen: int = bits_to_int(cast(List[int], self.mainscreen))
        subscreen: int = bits_to_int(cast(List[int], self.subscreen))
        colour_math: int = bits_to_int(cast(List[int], self.colour_math))
        return super().render(mainscreen, subscreen, colour_math)


class ResetPrioritySet(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """(unknown)"""

    _opcode: int = 0x82


class ScreenFlashesWithColour(UsableEventScriptCommand, EventScriptCommand):
    """Briefly flash a colour over the whole screen."""

    _opcode: int = 0x83
    _size: int = 2
    _colour: Colour

    @property
    def colour(self) -> Colour:
        """The colour to flash."""
        return self._colour

    def set_colour(self, colour: Colour) -> None:
        """Set the colour to flash."""
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


class TintLayers(UsableEventScriptCommand, EventScriptCommand):
    """Tint the selected layers with an RGB value.\n
    RGB values must be divisible by 8."""

    _opcode: int = 0x80
    _size: int = 5
    _layers: List[Layer]
    _red: UInt8
    _green: UInt8
    _blue: UInt8
    _speed: UInt8
    _bit_15: bool

    @property
    def layers(self) -> List[Layer]:
        """The list of layers to be tinted."""
        return self._layers

    def set_layers(self, layers: List[Layer]) -> None:
        """Overwrite the list of layers to be tinted."""
        self._layers = layers

    @property
    def red(self) -> UInt8:
        """The red value of the RGB colour."""
        return self._red

    def set_red(self, red: int) -> None:
        """Set the red value of the RGB colour.\n
        Must be a multiple of 8 between 0 and 248."""
        assert 0 <= red <= 248 and red % 8 == 0
        self._red = UInt8(red)

    @property
    def green(self) -> UInt8:
        """The green value of the RGB colour."""
        return self._green

    def set_green(self, green: int) -> None:
        """Set the green value of the RGB colour.\n
        Must be a multiple of 8 between 0 and 248."""
        assert 0 <= green <= 248 and green % 8 == 0
        self._green = UInt8(green)

    @property
    def blue(self) -> UInt8:
        """The blue value of the RGB colour."""
        return self._blue

    def set_blue(self, blue: int) -> None:
        """Set the blue value of the RGB colour.\n
        Must be a multiple of 8 between 0 and 248."""
        assert 0 <= blue <= 248 and blue % 8 == 0
        self._blue = UInt8(blue)

    @property
    def speed(self) -> UInt8:
        """The speed at which to perform the tint."""
        return self._speed

    def set_speed(self, speed: int) -> None:
        """Set the speed at which to perform the tint."""
        self._speed = UInt8(speed)

    @property
    def bit_15(self) -> bool:
        """(unknown)"""
        return self._bit_15

    def set_bit_15(self, bit_15: bool) -> None:
        """(unknown)"""
        self._bit_15 = bit_15

    def __init__(
        self,
        layers: List[Layer],
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
        assembled_layers_raw: int = bits_to_int(cast(List[int], self.layers))
        assembled_layers = UInt8(assembled_layers_raw)
        return super().render(assembled_short, assembled_layers, self.speed)


# screen transitions


class CircleMaskExpandFromScreenCenter(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """A circle mask expands from the center to reveal the whole level."""

    _opcode: int = 0x82


class CircleMaskShrinkToScreenCenter(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """A circle mask shrinks to the screen center to black out most of the level."""

    _opcode: int = 0x7D


class CircleMaskShrinkToObject(UsableEventScriptCommand, EventScriptCommand):
    """A circle mask shrinks to surround a given object, blacking out most of the level."""

    _size: int = 4
    _static: bool
    _target: AreaObject
    _width: UInt8
    _speed: UInt8

    @property
    def static(self) -> bool:
        """(unknown)"""
        return self._static

    def set_static(self, static: bool) -> None:
        """(unknown)"""
        self._static = static

    @property
    def target(self) -> AreaObject:
        """The target which the circle mask will be following."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Set the target which the circle mask will be following."""
        self._target = target

    @property
    def width(self) -> UInt8:
        """The width of the circle mask in pixels."""
        return self._width

    def set_width(self, width: int) -> None:
        """Set the width of the circle mask in pixels."""
        self._width = UInt8(width)

    @property
    def speed(self) -> UInt8:
        """The speed at which the mask effect should complete."""
        return self._speed

    def set_speed(self, speed: int) -> None:
        """Set the speed at which the mask effect should complete."""
        self._speed = UInt8(speed)

    def __init__(
        self,
        target: AreaObject,
        width: int,
        speed: int,
        static: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_target(target)
        self.set_width(width)
        self.set_speed(speed)
        self.set_static(static)

    def render(self) -> bytearray:
        opcode: int = 0x8F if self.static else 0x87
        return super().render(opcode, self.target, self.width, self.speed)


class StarMaskExpandFromScreenCenter(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """A star mask expands from the center to reveal the whole level."""

    _opcode: int = 0x7A


class StarMaskShrinkToScreenCenter(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """A star mask shrinks to the screen center to black out most of the level."""

    _opcode: int = 0x7B


class FadeInFromBlack(UsableEventScriptCommand, EventScriptCommand):
    """Fade the screen in from being unloaded."""

    _sync: bool
    _duration: Optional[UInt8]

    @property
    def sync(self) -> bool:
        """If false, the fade must finish before the script can continue."""
        return self._sync

    def set_sync(self, sync: bool) -> None:
        """If false, the fade must finish before the script can continue."""
        self._sync = sync

    @property
    def duration(self) -> Optional[UInt8]:
        """The length of time in frames that the fade should take."""
        if self._duration is not None:
            return UInt8(self._duration)
        return self._duration

    def set_duration(self, duration: Optional[int] = None) -> None:
        """Define the length of time in frames that the fade should take."""
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


class FadeInFromColour(UsableEventScriptCommand, EventScriptCommand):
    """Draw an opaque colour over the screen, and then fade the screen in"""

    _opcode: int = 0x78
    _size: int = 3
    _duration: UInt8
    _colour: Colour

    @property
    def duration(self) -> UInt8:
        """The length of time in frames that the fade should take."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Define the length of time in frames that the fade should take."""
        self._duration = UInt8(duration)

    @property
    def colour(self) -> Colour:
        """The initial colour to draw over the screen."""
        return self._colour

    def set_colour(self, colour: Colour) -> None:
        """Set the initial colour to draw over the screen."""
        self._colour = colour

    def __init__(
        self, duration: int, colour: Colour, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_duration(duration)
        self.set_colour(colour)

    def render(self) -> bytearray:
        return super().render()


class FadeOutToBlack(UsableEventScriptCommand, EventScriptCommand):
    """Fade the screen out to solid black."""

    _sync: bool
    _duration: Optional[UInt8]

    @property
    def sync(self) -> bool:
        """If false, the fade must finish before the script can continue."""
        return self._sync

    def set_sync(self, sync: bool) -> None:
        """If false, the fade must finish before the script can continue."""
        self._sync = sync

    @property
    def duration(self) -> Optional[UInt8]:
        """The length of time in frames that the fade should take."""
        if self._duration is not None:
            return UInt8(self._duration)
        return self._duration

    def set_duration(self, duration: Optional[int] = None) -> None:
        """Define the length of time in frames that the fade should take."""
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


class FadeOutToColour(UsableEventScriptCommand, EventScriptCommand):
    """Fade the screen out to any solid colour."""

    _opcode: int = 0x79
    _size: int = 3
    _duration: UInt8
    _colour: Colour

    @property
    def duration(self) -> UInt8:
        """The length of time in frames that the fade should take."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Define the length of time in frames that the fade should take."""
        self._duration = UInt8(duration)

    @property
    def colour(self) -> Colour:
        """The final colour to draw over the screen."""
        return self._colour

    def set_colour(self, colour: Colour) -> None:
        """Set the final colour to draw over the screen."""
        self._colour = colour

    def __init__(
        self, duration: int, colour: Colour, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_duration(duration)
        self.set_colour(colour)

    def render(self) -> bytearray:
        return super().render()


class InitiateBattleMask(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Perform the screen effect that precedes a battle."""

    _opcode: int = 0x7E


# music


class SlowDownMusicTempoBy(UsableEventScriptCommand, EventScriptCommand):
    """Designate a numerical temp (0 to 127) by which to slow down the music."""

    _opcode: int = 0x97
    _size: int = 3
    _duration: UInt8
    _change: UInt8

    @property
    def duration(self) -> UInt8:
        """The time in frames over which the tempo change should gradually occur."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Set the time in frames over which the tempo change should gradually occur."""
        self._duration = UInt8(duration)

    @property
    def change(self) -> UInt8:
        """The difference in tempo to apply as a slowdown."""
        return self._change

    def set_change(self, change: int) -> None:
        """Set he difference in tempo to apply as a slowdown (0 to 127)."""
        assert 0 <= change <= 127
        self._change = UInt8(change)

    def __init__(
        self, duration: int, change: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_duration(duration)
        self.set_change(change)

    def render(self) -> bytearray:
        return super().render(self.duration, self.change)


class SpeedUpMusicTempoBy(UsableEventScriptCommand, EventScriptCommand):
    """Designate a numerical temp (0 to 127) by which to speed up the music."""

    _opcode: int = 0x97
    _size: int = 3
    _duration: UInt8
    _change: UInt8

    @property
    def duration(self) -> UInt8:
        """The time in frames over which the tempo change should gradually occur."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Set the time in frames over which the tempo change should gradually occur."""
        self._duration = UInt8(duration)

    @property
    def change(self) -> UInt8:
        """The difference in tempo to apply as a speedup."""
        return self._change

    def set_change(self, change: int) -> None:
        """Set he difference in tempo to apply as a speedup (0 to 127)."""
        assert 0 < change <= 128
        self._change = UInt8(change)

    def __init__(
        self, duration: int, change: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_duration(duration)
        self.set_change(change)

    def render(self) -> bytearray:
        return super().render(self.duration, 256 - self.change)


class DeactivateSoundChannels(UsableEventScriptCommand, EventScriptCommand):
    """Sound channels identified by the given bits (0-7) will be silenced."""

    _opcode = bytearray([0xFD, 0x94])
    _size: int = 3
    _bits: Set[int]

    @property
    def bits(self) -> Set[int]:
        """i.e. include bit 4 to silence channel 4"""
        return self._bits

    def set_bits(self, bits: Set[int]) -> None:
        """0-7. i.e. include bit 4 to silence channel 4"""
        for bit in bits:
            assert 0 <= bit <= 7
        self._bits = bits

    def __init__(
        self,
        bits: Set[int],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_bits(bits)

    def render(self) -> bytearray:
        flags = UInt8(bits_to_int(list(self.bits)))
        return super().render(flags)


class FadeInMusic(UsableEventScriptCommand, EventScriptCommand):
    """Fade music in from a silent state.\n
    It is recommended to use music ID constant names for this."""

    _opcode: int = 0x92
    _size: int = 2
    _music_id: UInt8

    @property
    def music(self) -> UInt8:
        """The ID of the music to fade in."""
        return self._music_id

    def set_music_id(self, music: int) -> None:
        """Set the ID of the music to fade in.\n
        It is recommended to use music ID constant names for this."""
        assert 0 <= music < TOTAL_MUSIC
        self._music_id = UInt8(music)

    def __init__(self, music: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_music_id(music)

    def render(self) -> bytearray:
        return super().render(self.music)


class FadeOutMusic(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The current background music fades out to silence."""

    _opcode: int = 0x93


class FadeOutMusicFDA3(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """The current background music fades out to silence.\n
    Unknown how this differs from `FadeOutMusic`."""

    _opcode = bytearray([0xFD, 0xA3])


class FadeOutMusicToVolume(UsableEventScriptCommand, EventScriptCommand):
    """Fade out the currently playing background music to a specified volume over a specified
    time period (in frames)."""

    _opcode: int = 0x95
    _size: int = 3
    _duration: UInt8
    _volume: UInt8

    @property
    def duration(self) -> UInt8:
        """The duration, in frames, over which to perform the fade."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Set the duration, in frames, over which to perform the fade."""
        self._duration = UInt8(duration)

    @property
    def volume(self) -> UInt8:
        """The final volume of the background music."""
        return self._volume

    def set_volume(self, volume: int) -> None:
        """Set the final volume of the background music."""
        self._volume = UInt8(volume)

    def __init__(
        self, duration: int, volume: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_duration(duration)
        self.set_volume(volume)

    def render(self) -> bytearray:
        return super().render(self.duration, self.volume)


class FadeOutSoundToVolume(UsableEventScriptCommand, EventScriptCommand):
    """Fade out the currently playing sound to a specified volume over a specified
    time period (in frames)."""

    _opcode: int = 0x9E
    _size: int = 3
    _duration: UInt8
    _volume: UInt8

    @property
    def duration(self) -> UInt8:
        """The duration, in frames, over which to perform the fade."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Set the duration, in frames, over which to perform the fade."""
        self._duration = UInt8(duration)

    @property
    def volume(self) -> UInt8:
        """The desired ending volume for the sound effect."""
        return self._volume

    def set_volume(self, volume: int) -> None:
        """Specify the desired ending volume for the sound effect."""
        self._volume = UInt8(volume)

    def __init__(
        self, duration: int, volume: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_duration(duration)
        self.set_volume(volume)

    def render(self) -> bytearray:
        return super().render(self.duration, self.volume)


class JmpIfAudioMemoryIsAtLeast(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """(unknown)"""

    _opcode = bytearray([0xFD, 0x96])
    _size: int = 5
    _threshold: UInt8

    @property
    def threshold(self) -> UInt8:
        """(unknown)"""
        return self._threshold

    def set_threshold(self, threshold: int) -> None:
        """(unknown)"""
        self._threshold = UInt8(threshold)

    def __init__(
        self,
        threshold: int,
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_threshold(threshold)

    def render(self) -> bytearray:
        return super().render(self.threshold, *self.destinations)


class JmpIfAudioMemoryEquals(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """(unknown)"""

    _opcode = bytearray([0xFD, 0x97])
    _size: int = 5
    _value: UInt8

    @property
    def value(self) -> UInt8:
        """(unknown)"""
        return self._value

    def set_value(self, value: int) -> None:
        """(unknown)"""
        self._value = UInt8(value)

    def __init__(
        self,
        value: int,
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_value(value)

    def render(self) -> bytearray:
        return super().render(self.value, *self.destinations)


class PlayMusic(UsableEventScriptCommand, EventScriptCommand):
    """Begin playing a specific background music track.\n
    It is recommended to use music ID constant names for this."""

    _opcode = bytearray([0xFD, 0x9E])
    _size: int = 3
    _music_id: UInt8

    @property
    def music(self) -> UInt8:
        """The ID of the music to play."""
        return self._music_id

    def set_music_id(self, music: int) -> None:
        """Set the ID of the music to play.\n
        It is recommended to use music ID constant names for this."""
        assert 0 <= music < TOTAL_MUSIC
        self._music_id = UInt8(music)

    def __init__(self, music: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_music_id(music)

    def render(self) -> bytearray:
        return super().render(self.music)


class PlayMusicAtCurrentVolume(UsableEventScriptCommand, EventScriptCommand):
    """Begin playing a specific background music track, at the same volume as the current track.\n
    It is recommended to use music ID constant names for this."""

    _opcode: int = 0x90
    _size: int = 2
    _music_id: UInt8

    @property
    def music(self) -> UInt8:
        """The ID of the music to play."""
        return self._music_id

    def set_music_id(self, music: int) -> None:
        """Set the ID of the music to play.\n
        It is recommended to use music ID constant names for this."""
        assert 0 <= music < TOTAL_MUSIC
        self._music_id = UInt8(music)

    def __init__(self, music: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_music_id(music)

    def render(self) -> bytearray:
        return super().render(self.music)


class PlayMusicAtDefaultVolume(UsableEventScriptCommand, EventScriptCommand):
    """Begin playing a specific background music track (at default volume).\n
    It is recommended to use music ID constant names for this."""

    _opcode: int = 0x91
    _size: int = 2
    _music_id: UInt8

    @property
    def music(self) -> UInt8:
        """The ID of the music to play."""
        return self._music_id

    def set_music_id(self, music: int) -> None:
        """Set the ID of the music to play.\n
        It is recommended to use music ID constant names for this."""
        assert 0 <= music < TOTAL_MUSIC
        self._music_id = UInt8(music)

    def __init__(self, music: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_music_id(music)

    def render(self) -> bytearray:
        return super().render(self.music)


class PlaySound(UsableEventScriptCommand, EventScriptCommand):
    """Play a sound effect by ID on the specified chanel.\n
    It is recommended to use contextual const names for sound effect IDs."""

    _sound: UInt8
    _channel: UInt8

    @property
    def sound(self) -> UInt8:
        """The ID of the sound to play."""
        return self._sound

    def set_sound(self, sound: int) -> None:
        """Set the ID of the sound to play.\n
        It is recommended to use contextual const names for sound effect IDs."""
        assert 0 <= sound < TOTAL_SOUNDS
        self._sound = UInt8(sound)

    @property
    def channel(self) -> UInt8:
        """The channel on which to play the sound."""
        return self._channel

    def set_channel(self, channel: int) -> None:
        """Set the channel on which to play the sound.\n
        Valid values are 4 or 6."""
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


class PlaySoundBalance(UsableEventScriptCommand, EventScriptCommand):
    """Play a sound effect at a given balance.\n
    It is recommended to use contextual const names for sound effect IDs."""

    _opcode: int = 0x9D
    _size: int = 3
    _sound: UInt8
    _balance: UInt8

    @property
    def sound(self) -> UInt8:
        """The ID of the sound to play."""
        return self._sound

    def set_sound(self, sound: int) -> None:
        """Set the ID of the sound to play.\n
        It is recommended to use contextual const names for sound effect IDs."""
        assert 0 <= sound < TOTAL_SOUNDS
        self._sound = UInt8(sound)

    @property
    def balance(self) -> UInt8:
        """The balance level to play the sound at."""
        return self._balance

    def set_balance(self, balance: int) -> None:
        """Set the balance level to play the sound at."""
        self._balance = UInt8(balance)

    def __init__(
        self, sound: int, balance: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_sound(sound)
        self.set_balance(balance)

    def render(self) -> bytearray:
        return super().render(self.sound, self.balance)


class PlaySoundBalanceFD9D(UsableEventScriptCommand, EventScriptCommand):
    """Play a sound effect at a given balance.\n
    Unknown how this differs from `PlaySoundBalance`.\n
    It is recommended to use contextual const names for sound effect IDs."""

    _opcode = bytearray([0xFD, 0x9D])
    _size: int = 4
    _sound: UInt8
    _balance: UInt8

    @property
    def sound(self) -> UInt8:
        """The ID of the sound to play."""
        return self._sound

    def set_sound(self, sound: int) -> None:
        """Set the ID of the sound to play.\n
        It is recommended to use contextual const names for sound effect IDs."""
        assert 0 <= sound < TOTAL_SOUNDS
        self._sound = UInt8(sound)

    @property
    def balance(self) -> UInt8:
        """The balance level to play the sound at."""
        return self._balance

    def set_balance(self, balance: int) -> None:
        """Set the balance level to play the sound at."""
        self._balance = UInt8(balance)

    def __init__(
        self, sound: int, balance: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_sound(sound)
        self.set_balance(balance)

    def render(self) -> bytearray:
        return super().render(self.sound, self.balance)


class SlowDownMusic(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Show down the current music to an unspecified tempo, over a constant duration."""

    _opcode = bytearray([0xFD, 0xA4])


class SpeedUpMusicToDefault(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Return the current music tempo to default, over a constant duration."""

    _opcode = bytearray([0xFD, 0xA5])


class StopMusic(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Stop playing the background music entirely."""

    _opcode: int = 0x94


class StopMusicFD9F(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Stop playing the background music entirely.\n
    It is unknown how this differs from `StopMusic`."""

    _opcode = bytearray([0xFD, 0x9F])


class StopMusicFDA0(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Stop playing the background music entirely.\n
    It is unknown how this differs from `StopMusic`."""

    _opcode = bytearray([0xFD, 0xA0])


class StopMusicFDA1(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Stop playing the background music entirely.\n
    It is unknown how this differs from `StopMusic`."""

    _opcode = bytearray([0xFD, 0xA1])


class StopMusicFDA2(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Stop playing the background music entirely.\n
    It is unknown how this differs from `StopMusic`."""

    _opcode = bytearray([0xFD, 0xA2])


class StopMusicFDA6(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Stop playing the background music entirely.\n
    It is unknown how this differs from `StopMusic`."""

    _opcode = bytearray([0xFD, 0xA6])


class StopSound(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Halt the playback of any sound effect that is currently playing."""

    _opcode: int = 0x9B


# dialogs


class AppendDialogAt7000ToCurrentDialog(UsableEventScriptCommand, EventScriptCommand):
    """The dialog whose ID corresponds to the current value of $7000
    will be appended to the end of a dialog that is already being displayed."""

    _opcode: int = 0x63
    _size: int = 2
    _closable: bool
    _sync: bool

    @property
    def closable(self) -> bool:
        """If false, the dialog will remain on screen instead of being clearable
        with the A button."""
        return self._closable

    def set_closable(self, closable: bool) -> None:
        """If false, the dialog will remain on screen instead of being clearable
        with the A button."""
        self._closable = closable

    @property
    def sync(self) -> bool:
        """If false, events will continue to run and the player can continue to move."""
        return self._sync

    def set_sync(self, sync: bool) -> None:
        """If false, events will continue to run and the player can continue to move."""
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


class CloseDialog(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """If there is an open dialog, it will be forcibly closed."""

    _opcode: int = 0x64


class JmpIfDialogOptionBSelected(UsableEventScriptCommand, EventScriptCommandWithJmps):
    """Depends on the results of a previously displayed dialog which
    had only 2 options. If the second option was selected, go to the
    section of code beginning with the command matching the given identifier."""

    _opcode: int = 0x66
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfDialogOptionBOrCSelected(
    UsableEventScriptCommand, EventScriptCommandWithJmps
):
    """Depends on the results of a previously displayed dialog which
    had 3 options. If the second or third option was selected, go to the
    section of code beginning with the command matching the
    first or second identifier, respectively."""

    _opcode: int = 0x67
    _size: int = 5

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class PauseScriptResumeOnNextDialogPageA(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """The active script will be paused until the next dialog page is loaded.\n
    Unknown how this differs from `PauseScriptResumeOnNextDialogPageB`."""

    _opcode = bytearray([0xFD, 0x60])


class PauseScriptResumeOnNextDialogPageB(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """The active script will be paused until the next dialog page is loaded.\n
    Unknown how this differs from `PauseScriptResumeOnNextDialogPageA`."""

    _opcode = bytearray([0xFD, 0x61])


class RunDialog(UsableEventScriptCommand, EventScriptCommand):
    """Display a dialog by ID, or whose ID matches the current value of $7000.\n
    If not displaying the dialog whose ID matches the value currently stored to $7000,
    it is recommended to use dialog ID constant names for this."""

    _dialog_id: Union[UInt16, ShortVar]
    _above_object: AreaObject
    _closable: bool
    _bit_6: bool
    _sync: bool
    _multiline: bool
    _use_background: bool

    @property
    def dialog_id(self) -> Union[UInt16, ShortVar]:
        """The ID of the dialog to display, or the var containing an ID to display."""
        return self._dialog_id

    def set_dialog_id(self, dialog_id: Union[int, ShortVar]) -> None:
        """Accepts one of two things:\n
        1. The ID of the dialog to display
        (it is recommended to use dialog ID constant names for this),\n
        2. A short var, whose value indicates the ID to run (only `PRIMARY_TEMP_7000` accepted).
        """
        if dialog_id == PRIMARY_TEMP_7000:
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
        """The NPC or other target which the dialog should be above."""
        return self._above_object

    def set_above_object(self, above_object: AreaObject) -> None:
        """Indicate the NPC or other target which the dialog should be above."""
        self._above_object = above_object

    @property
    def closable(self) -> bool:
        """If false, the dialog will remain on screen instead of being clearable
        with the A button."""
        return self._closable

    def set_closable(self, closable: bool) -> None:
        """If false, the dialog will remain on screen instead of being clearable
        with the A button."""
        self._closable = closable

    @property
    def bit_6(self) -> bool:
        """(unknown)"""
        return self._bit_6

    def set_bit_6(self, bit_6: bool) -> None:
        """(unknown)"""
        self._bit_6 = bit_6

    @property
    def sync(self) -> bool:
        """If false, events will continue to run and the player can continue to move."""
        return self._sync

    def set_sync(self, sync: bool) -> None:
        """If false, events will continue to run and the player can continue to move."""
        self._sync = sync

    @property
    def multiline(self) -> bool:
        """If true, the dialog will display up to 3 lines.\n
        If false, the dialog will display only 1 line."""
        return self._multiline

    def set_multiline(self, multiline: bool) -> None:
        """If true, the dialog will display up to 3 lines.\n
        If false, the dialog will display only 1 line."""
        self._multiline = multiline

    @property
    def use_background(self) -> bool:
        """If true, the dialog will be displayed over the parchment asset.\n
        If false, the dialog should be displayed as blue text over a transparent
        background, although this is not always respected."""
        return self._use_background

    def set_use_background(self, use_background: bool) -> None:
        """If true, the dialog will be displayed over the parchment asset.\n
        If false, the dialog should be displayed as blue text over a transparent
        background, although this is not always respected."""
        self._use_background = use_background

    def __init__(
        self,
        dialog_id: Union[int, ShortVar],
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


class RunDialogForDuration(UsableEventScriptCommand, EventScriptCommand):
    """Display a dialog by ID for a given duration in frames.\n
    It is recommended to use dialog ID constant names for this."""

    _opcode: int = 0x62
    _size: int = 3
    _dialog_id: UInt16
    _duration: UInt8
    _sync: bool

    @property
    def dialog_id(self) -> UInt16:
        """The ID of the dialog to display."""
        return self._dialog_id

    def set_dialog_id(self, dialog_id: int) -> None:
        """Set the ID of the dialog to display.\n
        It is recommended to use dialog ID constant names for this."""
        assert 0 <= dialog_id < TOTAL_DIALOGS
        self._dialog_id = UInt16(dialog_id)

    @property
    def duration(self) -> UInt8:
        """The duration, in frames, for which the dialog should be active."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Set the duration, in frames, for which the dialog should be active."""
        assert 0 <= duration <= 3
        self._duration = UInt8(duration)

    @property
    def sync(self) -> bool:
        """If false, events will continue to run and the player can continue to move."""
        return self._sync

    def set_sync(self, sync: bool) -> None:
        """If false, events will continue to run and the player can continue to move."""
        self._sync = sync

    def __init__(
        self,
        dialog_id: int,
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


class UnsyncDialog(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Event scripts and player movements will resume without waiting for the dialog to close."""

    _opcode: int = 0x65


# levels


class EnterArea(UsableEventScriptCommand, EventScriptCommand):
    """Immediately teleport to a specified level.\n
    It is recommended to use room ID constant names for this."""

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
        """The ID of the level to open."""
        return self._room_id

    def set_room_id(self, room_id: int) -> None:
        """Set the ID of the level to open.\n
        It is recommended to use room ID constant names for this."""
        assert 0 <= room_id < TOTAL_ROOMS
        self._room_id = UInt16(room_id)

    @property
    def face_direction(self) -> Direction:
        """The direction that the player will face when the room loads."""
        return self._face_direction

    def set_face_direction(self, face_direction: Direction) -> None:
        """Choose the direction that the player will face when the room loads."""
        self._face_direction = face_direction

    @property
    def x(self) -> UInt8:
        """The X coordinate at which the player will be standing when the room loads."""
        return self._x

    def set_x(self, x: int) -> None:
        """Set the X coordinate at which the player will be standing when the room loads."""
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        """The Y coordinate at which the player will be standing when the room loads."""
        return self._y

    def set_y(self, y: int) -> None:
        """Set the Y coordinate (0-127) at which the player will be standing
        when the room loads."""
        assert 0 <= y <= 127
        self._y = UInt8(y)

    @property
    def z(self) -> UInt8:
        """The Z coordinate at which the player will be standing when the room loads."""
        return self._z

    def set_z(self, z: int) -> None:
        """Set the Z coordinate (0-31) at which the player will be standing when the room loads."""
        assert 0 <= z <= 31
        self._z = UInt8(z)

    @property
    def z_add_half_unit(self) -> bool:
        """If true, adds half a unit to the player's starting Z coordinate."""
        return self._z_add_half_unit

    def set_z_add_half_unit(self, z_add_half_unit: bool) -> None:
        """If true, adds half a unit to the player's starting Z coordinate."""
        self._z_add_half_unit = z_add_half_unit

    @property
    def show_banner(self) -> bool:
        """If the room has an associated message, the message will be temporarily
        displayed at the top of the screen upon load if this is true."""
        return self._show_banner

    def set_show_banner(self, show_banner: bool) -> None:
        """If the room has an associated message, the message will be temporarily
        displayed at the top of the screen upon load if this is true."""
        self._show_banner = show_banner

    @property
    def run_entrance_event(self) -> bool:
        """If true, the entrance event associated to the room will run on load."""
        return self._run_entrance_event

    def set_run_entrance_event(self, run_entrance_event: bool) -> None:
        """If true, the entrance event associated to the room will run on load."""
        self._run_entrance_event = run_entrance_event

    def __init__(
        self,
        room_id: int,
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
        direction_z_arg = UInt8(self.z + (self.face_direction << 5))
        return super().render(room_short, self.x, y_z_arg, direction_z_arg)


class ApplyTileModToLevel(UsableEventScriptCommand, EventScriptCommand):
    """If the specified room has tile modifications available, this command
    can apply one.\n
    It is recommended to use room ID constant names for this."""

    _opcode: int = 0x6A
    _size: int = 3
    _room_id: UInt16
    _mod_id: UInt8
    _use_alternate: bool

    @property
    def room_id(self) -> UInt16:
        """The ID of the room applying a tile mod."""
        return self._room_id

    def set_room_id(self, room_id: int) -> None:
        """Set the ID of the room applying a tile mod.\n
        It is recommended to use room ID constant names for this."""
        assert 0 <= room_id < TOTAL_ROOMS
        self._room_id = UInt16(room_id)

    @property
    def mod_id(self) -> UInt8:
        """The ID of the mod to apply."""
        return self._mod_id

    def set_mod_id(self, mod_id: int) -> None:
        """Set the ID of the mod to apply (0-63).\n
        It is the dev's responsibility to make sure that the mod actually exists."""
        assert 0 <= mod_id <= 63
        self._mod_id = UInt8(mod_id)

    @property
    def use_alternate(self) -> bool:
        """(unknown)"""
        return self._use_alternate

    def set_use_alternate(self, use_alternate: bool) -> None:
        """(unknown)"""
        self._use_alternate = use_alternate

    def __init__(
        self,
        room_id: int,
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


class ApplySolidityModToLevel(UsableEventScriptCommand, EventScriptCommand):
    """If the specified room has collision modifications available, this command
    can apply one.\n
    It is recommended to use room ID constant names for this."""

    _opcode: int = 0x6B
    _size: int = 3
    _room_id: UInt16
    _mod_id: UInt8
    _permanent: bool

    @property
    def room_id(self) -> UInt16:
        """The ID of the room applying a collision mod."""
        return self._room_id

    def set_room_id(self, room_id: int) -> None:
        """Set the ID of the room applying a collision mod.\n
        It is recommended to use room ID constant names for this."""
        assert 0 <= room_id < TOTAL_ROOMS
        self._room_id = UInt16(room_id)

    @property
    def mod_id(self) -> UInt8:
        """The ID of the mod to apply."""
        return self._mod_id

    def set_mod_id(self, mod_id: int) -> None:
        """Set the ID of the mod to apply (0-63).\n
        It is the dev's responsibility to make sure that the mod actually exists."""
        assert 0 <= mod_id <= 63
        self._mod_id = UInt8(mod_id)

    @property
    def permanent(self) -> bool:
        """(unknown)"""
        return self._permanent

    def set_permanence(self, permanent: bool) -> None:
        """(unknown)"""
        self._permanent = permanent

    def __init__(
        self,
        room_id: int,
        mod_id: int,
        permanent: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_room_id(room_id)
        self.set_mod_id(mod_id)
        self.set_permanence(permanent)

    def render(self) -> bytearray:
        assembled_raw: int = self.room_id + (self.mod_id << 9) + (self.permanent << 15)
        return super().render(UInt16(assembled_raw))


class ExitToWorldMap(UsableEventScriptCommand, EventScriptCommand):
    """Leaves the given level forcibly, and returns to the world map.\n
    It is recommended to use overworld location ID constant names for this."""

    _opcode: int = 0x4B
    _size: int = 3
    _area: UInt8
    _bit_5: bool
    _bit_6: bool
    _bit_7: bool

    @property
    def area(self) -> UInt8:
        """The world map dot to return to."""
        return self._area

    def set_area(self, area: int) -> None:
        """Set the world map dot to return to.\n
        It is recommended to use overworld location ID constant names for this."""
        assert 0 <= area < TOTAL_WORLD_MAP_AREAS
        self._area = UInt8(area)

    @property
    def bit_5(self) -> bool:
        """(unknown)"""
        return self._bit_5

    def set_bit_5(self, bit_5: bool) -> None:
        """(unknown)"""
        self._bit_5 = bit_5

    @property
    def bit_6(self) -> bool:
        """(unknown)"""
        return self._bit_6

    def set_bit_6(self, bit_6: bool) -> None:
        """(unknown)"""
        self._bit_6 = bit_6

    @property
    def bit_7(self) -> bool:
        """(unknown)"""
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        """(unknown)"""
        self._bit_7 = bit_7

    def __init__(
        self,
        area: int,
        bit_5: bool = False,
        bit_6: bool = False,
        bit_7: bool = False,
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


class Set7000ToCurrentLevel(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Set the value of $7000 to the ID of the currently loaded level."""

    _opcode: int = 0xC3


# scenes


class DisplayIntroTitleText(UsableEventScriptCommand, EventScriptCommand):
    """Text that normally appears in the game intro. Unused in rando."""

    _opcode = bytearray([0xFD, 0x66])
    _size: int = 4
    _text: IntroTitleText
    _y: UInt8

    @property
    def text(self) -> IntroTitleText:
        """The predefined text to display."""
        return self._text

    def set_text(self, text: IntroTitleText) -> None:
        """Choose the predefined text to display."""
        self._text = text

    @property
    def y(self) -> UInt8:
        """The Y coord at which to display the text."""
        return self._y

    def set_y(self, y: int) -> None:
        """Set the Y coord at which to display the text."""
        self._y = UInt8(y)

    def __init__(
        self, text: IntroTitleText, y: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_text(text)
        self.set_y(y)

    def render(self) -> bytearray:
        return super().render()


class ExorCrashesIntoKeep(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Run the cutscene where Exor shatters the star road.\n
    Unused in rando."""

    _opcode = bytearray([0xFD, 0xF8])


class RunMenuOrEventSequence(UsableEventScriptCommand, EventScriptCommand):
    """Runs one of a various selection of menus or automatic cutscenes."""

    _opcode: int = 0x4F
    _size: int = 2
    _scene: Scene

    @property
    def scene(self) -> Scene:
        """The menu or cutscene to play."""
        return self._scene

    def set_scene(self, scene: Scene) -> None:
        """Choose the menu or cutscene to play."""
        self._scene = scene

    def __init__(self, scene: Scene, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_scene(scene)

    def render(self) -> bytearray:
        return super().render(self.scene)


class OpenSaveMenu(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Open the save menu."""

    _opcode = bytearray([0xFD, 0x4A])


class OpenShop(UsableEventScriptCommand, EventScriptCommand):
    """Open a shop by ID.\n
    It is recommended to use shop ID constant names for this."""

    _opcode: int = 0x4C
    _size: int = 2
    _shop_id: UInt8

    @property
    def shop_id(self) -> UInt8:
        """The ID of the shop to open."""
        return self._shop_id

    def set_shop_id(self, shop_id: int) -> None:
        """Set the ID of the shop to open.\n
        It is recommended to use shop ID constant names for this."""
        assert 0 <= shop_id < TOTAL_SHOPS
        self._shop_id = UInt8(shop_id)

    def __init__(self, shop_id: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_shop_id(shop_id)

    def render(self) -> bytearray:
        return super().render(self.shop_id)


class PauseScriptIfMenuOpen(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Pauses the running script if a menu is opened."""

    _opcode: int = 0x5B


class ResetAndChooseGame(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Reloads your last save. Character EXP is not reset."""

    _opcode: int = 0xFB


class ResetGame(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Reset to the file select screen (presumably?)."""

    _opcode: int = 0xFC


class RunEndingCredits(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Begin the ending credits sequence."""

    _opcode = bytearray([0xFD, 0x67])


class RunEventSequence(UsableEventScriptCommand, EventScriptCommand):
    """Run a special cutscene. Normally used for star pieces in the ending credits."""

    _opcode: int = 0x4E
    _size: int = 3
    _scene: Scene
    _value: UInt8

    @property
    def scene(self) -> Scene:
        """The specific cutscene to run."""
        return self._scene

    def set_scene(self, scene: Scene) -> None:
        """Choose the specific cutscene to run."""
        self._scene = scene

    @property
    def value(self) -> UInt8:
        """A value needed by the chosen cutscene."""
        return self._value

    def set_value(self, value: int) -> None:
        """Provide a value needed by the chosen cutscene."""
        self._value = UInt8(value)

    def __init__(
        self, scene: Scene, value: int = 0, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_scene(scene)
        self.set_value(value)

    def render(self) -> bytearray:
        return super().render(self.scene, self.value)


class RunLevelupBonusSequence(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Launch the levelup screen."""

    _opcode = bytearray([0xFD, 0x65])


class RunMenuTutorial(UsableEventScriptCommand, EventScriptCommand):
    """Run a specific menu tutorial."""

    _opcode = bytearray([0xFD, 0x4C])
    _size: int = 3
    _tutorial: Tutorial

    @property
    def tutorial(self) -> Tutorial:
        """The specific tutorial to run."""
        return self._tutorial

    def set_tutorial(self, tutorial: Tutorial) -> None:
        """Choose the specific tutorial to run."""
        self._tutorial = tutorial

    def __init__(self, tutorial: Tutorial, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_tutorial(tutorial)

    def render(self) -> bytearray:
        return super().render(self.tutorial)


class RunMolevilleMountainIntroSequence(
    UsableEventScriptCommand, EventScriptCommandNoArgs
):
    """Runs the Moleville Mountain sequence found in the original game's attract mode.
    Unused in rando."""

    _opcode = bytearray([0xFD, 0x4F])


class RunMolevilleMountainSequence(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Enter the Moleville Mountain minigame."""

    _opcode = bytearray([0xFD, 0x4E])


class RunStarPieceSequence(UsableEventScriptCommand, EventScriptCommand):
    """Run a star piece collection cutscene."""

    _opcode = bytearray([0xFD, 0x4D])
    _size: int = 3
    _star: UInt8

    @property
    def star(self) -> UInt8:
        """The specific star piece to collect."""
        return self._star

    def set_star(self, star: int) -> None:
        """Choose the specific star piece to collect (1-7)."""
        assert 1 <= star <= 7
        self._star = UInt8(star)

    def __init__(self, star: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_star(star)

    def render(self) -> bytearray:
        return super().render(self.star)


class StartBattleAtBattlefield(UsableEventScriptCommand, EventScriptCommand):
    """Enter into a battle with a given pack ID and battlefield.\n
    It is recommended to use pack ID constant names for this."""

    _opcode: int = 0x4A
    _pack_id: UInt8
    _battlefield: Battlefield

    @property
    def pack_id(self) -> UInt8:
        """The ID of the pack to fight."""
        return self._pack_id

    def set_pack_id(self, pack_id: int) -> None:
        """Set the ID of the pack to fight.\n
        It is recommended to use pack ID constant names for this."""
        self._pack_id = UInt8(pack_id)

    @property
    def battlefield(self) -> Battlefield:
        """The battlefield on which the battle should take place."""
        return self._battlefield

    def set_battlefield(self, battlefield: Battlefield) -> None:
        """The battlefield on which the battle should take place."""
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


class StartBattleWithPackAt700E(UsableEventScriptCommand, EventScriptCommandNoArgs):
    """Initiates a battle on the default battlefield associated to the current level
    against the pack ID matching the current value of $700E."""

    _opcode: int = 0x49
