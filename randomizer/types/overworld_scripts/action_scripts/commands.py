"""Individual NPC action script command classes.
These are the building blocks of NPC action scripts."""

from typing import List, Optional, Set, Type, Union
from randomizer.types.items.classes import Item

from randomizer.types.overworld_scripts.action_scripts.classes import (
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
from randomizer.types.overworld_scripts.action_scripts.constants.classes import (
    SequenceSpeed,
    VRAMPriority,
)
from randomizer.types.overworld_scripts.action_scripts.constants.misc import (
    TOTAL_SCRIPTS as TOTAL_ACTION_SCRIPTS,
)

from randomizer.types.overworld_scripts.event_scripts.constants.misc import (
    TOTAL_SCRIPTS as TOTAL_EVENT_SCRIPTS,
)

from randomizer.types.overworld_scripts.constants.classes import (
    AreaObject,
    Direction,
    Coord,
)
from randomizer.types.overworld_scripts.constants.misc import TOTAL_ROOMS, TOTAL_SOUNDS
from randomizer.types.overworld_scripts.constants.coords import COORD_F
from randomizer.types.numbers.classes import UInt16, UInt4, UInt8
from randomizer.types.overworld_scripts.packets.classes import Packet
from randomizer.types.overworld_scripts.variables.variables import PRIMARY_TEMP_700C
from randomizer.types.overworld_scripts.variables.classes import ByteVar, Flag, ShortVar
from randomizer.types.scripts_common.classes import InvalidCommandArgumentException
from randomizer.utils.number import bits_to_int, bools_to_int

# script operations


class JmpToScript(ActionScriptCommand):
    """Goto action script by ID.\n
    It is highly recommended to use contextual action script
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
        It is highly recommended to use contextual action script
        const names for this."""
        assert 0 <= destination < TOTAL_ACTION_SCRIPTS
        self._destination = UInt16(destination)

    def __init__(self, destination: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_destination(destination)

    def render(self) -> bytearray:
        return super().render(self.destination)


class Jmp(ActionScriptCommandWithJmps):
    """Goto a specific command by command identifier."""

    _opcode: int = 0xD2
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpToSubroutine(ActionScriptCommandWithJmps):
    """Run a specific action script as a subroutine, by command identifier."""

    _opcode: int = 0xD3
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class StartLoopNFrames(ActionScriptCommand):
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


class StartLoopNTimes(ActionScriptCommand):
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


class EndLoop(ActionScriptCommandNoArgs):
    """If previous commands were part of a loop, this is where the loop ends."""

    _opcode: int = 0xD7


class Pause(ActionScriptCommand):
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


class JmpToStartOfThisScript(ActionScriptCommandNoArgs):
    """Return to the beginning of the script containing this command"""

    _opcode: int = 0xF9


class JmpToStartOfThisScriptFA(ActionScriptCommandNoArgs):
    """(unknown)"""

    _opcode: int = 0xFA


class Return(ActionScriptCommandNoArgs):
    """Exits the execution of the current script or subroutine."""

    _opcode: int = 0xFE


class EndAll(ActionScriptCommandNoArgs):
    """Exits the execution of the current script or subroutine, as well as
    any events that may have called this script as a subroutine."""

    _opcode: int = 0xFF


class Db(ActionScriptCommand):
    """Catch-all command class representing any command not represented by other
    ActionScriptCommand subclasses.
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


# visibility & collision


class VisibilityOn(ActionScriptCommandNoArgs):
    """The NPC running this script will have its sprite become visible."""

    _opcode: int = 0x00


class VisibilityOff(ActionScriptCommandNoArgs):
    """The NPC running this script will have its sprite become invisible.\n
    This does not impact or deactivate the NPC's collision data."""

    _opcode: int = 0x01


class ResetProperties(ActionScriptCommandNoArgs):
    """The NPC's sprite is reset to its default state (mold 0 or sequence 0).
    Some other changes made by action script commands may also be reversed."""

    _opcode: int = 0x09


class OverwriteSolidity(ActionScriptCommand):
    """Change the NPC's collision behavioural rules within the current room.
    This will completely overwrite both set AND unset bits for the NPC."""

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
        """(unknown)"""
        return self._bit_0

    def set_bit_0(self, bit_0: bool) -> None:
        """(unknown)"""
        self._bit_0 = bit_0

    @property
    def cant_walk_under(self) -> bool:
        """If true, neither the player nor any NPCs can walk under this NPC."""
        return self._cant_walk_under

    def set_cant_walk_under(self, cant_walk_under: bool) -> None:
        """If true, neither the player nor any NPCs can walk under this NPC."""
        self._cant_walk_under = cant_walk_under

    @property
    def cant_pass_walls(self) -> bool:
        """If false, this NPC can walk through walls."""
        return self._cant_pass_walls

    def set_cant_pass_walls(self, cant_pass_walls: bool) -> None:
        """If false, this NPC can walk through walls."""
        self._cant_pass_walls = cant_pass_walls

    @property
    def cant_jump_through(self) -> bool:
        """If true, neither the player nor any NPCs can jump through this NPC."""
        return self._cant_jump_through

    def set_cant_jump_through(self, cant_jump_through: bool) -> None:
        """If true, neither the player nor any NPCs can jump through this NPC."""
        self._cant_jump_through = cant_jump_through

    @property
    def bit_4(self) -> bool:
        """(unknown)"""
        return self._bit_4

    def set_bit_4(self, bit_4: bool) -> None:
        """(unknown)"""
        self._bit_4 = bit_4

    @property
    def cant_pass_npcs(self) -> bool:
        """If false, this NPC can walk through other NPCs on the field."""
        return self._cant_pass_npcs

    def set_cant_pass_npcs(self, cant_pass_npcs: bool) -> None:
        """If false, this NPC can walk through other NPCs on the field."""
        self._cant_pass_npcs = cant_pass_npcs

    @property
    def cant_walk_through(self) -> bool:
        """If false, the player and other NPCs on the field can walk through this NPC."""
        return self._cant_walk_through

    def set_cant_walk_through(self, cant_walk_through: bool) -> None:
        """If false, the player and other NPCs on the field can walk through this NPC."""
        self._cant_walk_through = cant_walk_through

    @property
    def bit_7(self) -> bool:
        """(unknown)"""
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        """(unknown)"""
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
    """Change the NPC's collision behavioural rules within the current room.
    Specified bits will be set, unspecified bits will be unchanged."""

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
        """(unknown)"""
        return self._bit_0

    def set_bit_0(self, bit_0: bool) -> None:
        """(unknown)"""
        self._bit_0 = bit_0

    @property
    def cant_walk_under(self) -> bool:
        """If true, neither the player nor any NPCs can walk under this NPC."""
        return self._cant_walk_under

    def set_cant_walk_under(self, cant_walk_under: bool) -> None:
        """If true, neither the player nor any NPCs can walk under this NPC."""
        self._cant_walk_under = cant_walk_under

    @property
    def cant_pass_walls(self) -> bool:
        """If false, this NPC can walk through walls."""
        return self._cant_pass_walls

    def set_cant_pass_walls(self, cant_pass_walls: bool) -> None:
        """If false, this NPC can walk through walls."""
        self._cant_pass_walls = cant_pass_walls

    @property
    def cant_jump_through(self) -> bool:
        """If true, neither the player nor any NPCs can jump through this NPC."""
        return self._cant_jump_through

    def set_cant_jump_through(self, cant_jump_through: bool) -> None:
        """If true, neither the player nor any NPCs can jump through this NPC."""
        self._cant_jump_through = cant_jump_through

    @property
    def bit_4(self) -> bool:
        """(unknown)"""
        return self._bit_4

    def set_bit_4(self, bit_4: bool) -> None:
        """(unknown)"""
        self._bit_4 = bit_4

    @property
    def cant_pass_npcs(self) -> bool:
        """If false, this NPC can walk through other NPCs on the field."""
        return self._cant_pass_npcs

    def set_cant_pass_npcs(self, cant_pass_npcs: bool) -> None:
        """If false, this NPC can walk through other NPCs on the field."""
        self._cant_pass_npcs = cant_pass_npcs

    @property
    def cant_walk_through(self) -> bool:
        """If false, the player and other NPCs on the field can walk through this NPC."""
        return self._cant_walk_through

    def set_cant_walk_through(self, cant_walk_through: bool) -> None:
        """If false, the player and other NPCs on the field can walk through this NPC."""
        self._cant_walk_through = cant_walk_through

    @property
    def bit_7(self) -> bool:
        """(unknown)"""
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        """(unknown)"""
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
    """Change the NPC's collision behavioural rules within the current room.
    Bits set to "True" in this command will be cleared (as confusing as that sounds),
    unspecified bits will be unchanged."""

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
        """(unknown)"""
        return self._bit_0

    def set_bit_0(self, bit_0: bool) -> None:
        """(unknown)"""
        self._bit_0 = bit_0

    @property
    def cant_walk_under(self) -> bool:
        """If true, neither the player nor any NPCs can walk under this NPC."""
        return self._cant_walk_under

    def set_cant_walk_under(self, cant_walk_under: bool) -> None:
        """If true, neither the player nor any NPCs can walk under this NPC."""
        self._cant_walk_under = cant_walk_under

    @property
    def cant_pass_walls(self) -> bool:
        """If false, this NPC can walk through walls."""
        return self._cant_pass_walls

    def set_cant_pass_walls(self, cant_pass_walls: bool) -> None:
        """If false, this NPC can walk through walls."""
        self._cant_pass_walls = cant_pass_walls

    @property
    def cant_jump_through(self) -> bool:
        """If true, neither the player nor any NPCs can jump through this NPC."""
        return self._cant_jump_through

    def set_cant_jump_through(self, cant_jump_through: bool) -> None:
        """If true, neither the player nor any NPCs can jump through this NPC."""
        self._cant_jump_through = cant_jump_through

    @property
    def bit_4(self) -> bool:
        """(unknown)"""
        return self._bit_4

    def set_bit_4(self, bit_4: bool) -> None:
        """(unknown)"""
        self._bit_4 = bit_4

    @property
    def cant_pass_npcs(self) -> bool:
        """If false, this NPC can walk through other NPCs on the field."""
        return self._cant_pass_npcs

    def set_cant_pass_npcs(self, cant_pass_npcs: bool) -> None:
        """If false, this NPC can walk through other NPCs on the field."""
        self._cant_pass_npcs = cant_pass_npcs

    @property
    def cant_walk_through(self) -> bool:
        """If false, the player and other NPCs on the field can walk through this NPC."""
        return self._cant_walk_through

    def set_cant_walk_through(self, cant_walk_through: bool) -> None:
        """If false, the player and other NPCs on the field can walk through this NPC."""
        self._cant_walk_through = cant_walk_through

    @property
    def bit_7(self) -> bool:
        """(unknown)"""
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        """(unknown)"""
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
    """(unknown how this differs from solidity bits)"""

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
        """(unknown)"""
        return self._bit_0

    def set_bit_0(self, bit_0: bool) -> None:
        """(unknown)"""
        self._bit_0 = bit_0

    @property
    def cant_walk_under(self) -> bool:
        """If true, neither the player nor any NPCs can walk under this NPC."""
        return self._cant_walk_under

    def set_cant_walk_under(self, cant_walk_under: bool) -> None:
        """If true, neither the player nor any NPCs can walk under this NPC."""
        self._cant_walk_under = cant_walk_under

    @property
    def cant_pass_walls(self) -> bool:
        """If false, this NPC can walk through walls."""
        return self._cant_pass_walls

    def set_cant_pass_walls(self, cant_pass_walls: bool) -> None:
        """If false, this NPC can walk through walls."""
        self._cant_pass_walls = cant_pass_walls

    @property
    def cant_jump_through(self) -> bool:
        """If true, neither the player nor any NPCs can jump through this NPC."""
        return self._cant_jump_through

    def set_cant_jump_through(self, cant_jump_through: bool) -> None:
        """If true, neither the player nor any NPCs can jump through this NPC."""
        self._cant_jump_through = cant_jump_through

    @property
    def bit_4(self) -> bool:
        """(unknown)"""
        return self._bit_4

    def set_bit_4(self, bit_4: bool) -> None:
        """(unknown)"""
        self._bit_4 = bit_4

    @property
    def cant_pass_npcs(self) -> bool:
        """If false, this NPC can walk through other NPCs on the field."""
        return self._cant_pass_npcs

    def set_cant_pass_npcs(self, cant_pass_npcs: bool) -> None:
        """If false, this NPC can walk through other NPCs on the field."""
        self._cant_pass_npcs = cant_pass_npcs

    @property
    def cant_walk_through(self) -> bool:
        """If false, the player and other NPCs on the field can walk through this NPC."""
        return self._cant_walk_through

    def set_cant_walk_through(self, cant_walk_through: bool) -> None:
        """If false, the player and other NPCs on the field can walk through this NPC."""
        self._cant_walk_through = cant_walk_through

    @property
    def bit_7(self) -> bool:
        """(unknown)"""
        return self._bit_7

    def set_bit_7(self, bit_7: bool) -> None:
        """(unknown)"""
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
    """Set the rules for how this NPC's sprite overlaps with the player's."""

    _opcode: int = 0x13
    _size: int = 2
    _priority: VRAMPriority

    @property
    def priority(self) -> VRAMPriority:
        """The priority rule."""
        return self._priority

    def set_priority(self, priority: VRAMPriority) -> None:
        """Set the priority rule."""
        self._priority = priority

    def __init__(
        self, priority: VRAMPriority, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_priority(priority)

    def render(self) -> bytearray:
        return super().render(self.priority)


class SetPriority(ActionScriptCommand):
    """(unknown how this differs from vram priority)"""

    _opcode = bytearray([0xFD, 0x0F])
    _size: int = 3
    _priority: int

    @property
    def priority(self) -> int:
        """The priority level."""
        return self._priority

    def set_priority(self, priority: int) -> None:
        """Set the priority level."""
        assert 0 <= priority <= 3
        self._priority = priority

    def __init__(self, priority: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_priority(priority)

    def render(self) -> bytearray:
        return super().render(self.priority)


class ShadowOn(ActionScriptCommandNoArgs):
    """Begin showing the NPC's shadow when airborne."""

    _opcode = bytearray([0xFD, 0x00])


class ShadowOff(ActionScriptCommandNoArgs):
    """The NPC's shadow when airborne will no longer be visible."""

    _opcode = bytearray([0xFD, 0x01])


class FloatingOn(ActionScriptCommandNoArgs):
    """When run, the NPC is not affected by gravity."""

    _opcode = bytearray([0xFD, 0x02])


class FloatingOff(ActionScriptCommandNoArgs):
    """When run, the NPC becomes affected by gravity."""

    _opcode = bytearray([0xFD, 0x03])


# memory


class SetObjectMemoryBits(ActionScriptCommand):
    """(unknown)"""

    _size: int = 2
    _arg_1: int
    _bits: Set[int]

    @property
    def arg_1(self) -> int:
        """(unknown)"""
        return self._arg_1

    def set_arg_1(self, arg_1: int) -> None:
        """(unknown)"""
        assert arg_1 in [0x0D, 0x0B, 0x0E]
        self._arg_1 = arg_1

    @property
    def bits(self) -> Set[int]:
        """(unknown)"""
        return self.bits

    def set_bits(self, bits: Union[List[int], Set[int]]) -> None:
        """(unknown)"""
        for bit in bits:
            assert 0 <= bit <= 7
        self._bits = set(bits)

    def __init__(
        self,
        arg_1: int,
        bits: Union[List[int], Set[int]],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_arg_1(arg_1)
        self.set_bits(bits)

    def render(self) -> bytearray:
        flags: int = UInt8(bits_to_int(list(self.bits)))
        if self.arg_1 == 0x0D:
            return super().render(0x11, flags)
        if self.arg_1 == 0x0B:
            return super().render(0x12, flags)
        if self.arg_1 == 0x0E:
            return super().render(0x14, flags)
        raise InvalidCommandArgumentException(
            f"illegal args for {self.identifier.name}: {flags}"
        )


class ObjectMemorySetBit(ActionScriptCommand):
    """(unknown)"""

    _size: int = 2
    _arg_1: int
    _bits: Set[int]

    @property
    def arg_1(self) -> int:
        """(unknown)"""
        return self._arg_1

    @property
    def bits(self) -> Set[int]:
        """(unknown)"""
        return self._bits

    def set_props(self, arg_1: int, bits: Union[List[int], Set[int]]) -> None:
        """(unknown)"""
        props_input = (arg_1, bits)
        assert props_input in [
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
        self._bits = set(bits)

    def __init__(
        self,
        arg_1: int,
        bits: Union[List[int], Set[int]],
        identifier: Optional[str] = None,
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
            raise InvalidCommandArgumentException(
                f"illegal args for {self.identifier.name}: {args}"
            )
        return super().render(opcode)


class ObjectMemoryClearBit(ActionScriptCommand):
    """(unknown)"""

    _size: int = 2
    _arg_1: int
    _bits: Set[int]

    @property
    def arg_1(self) -> int:
        """(unknown)"""
        return self._arg_1

    @property
    def bits(self) -> Set[int]:
        """(unknown)"""
        return self._bits

    def set_props(self, arg_1: int, bits: Union[List[int], Set[int]]) -> None:
        """(unknown)"""
        props_input = (arg_1, bits)
        assert props_input in [
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
        self._bits = set(bits)

    def __init__(
        self,
        arg_1: int,
        bits: Union[List[int], Set[int]],
        identifier: Optional[str] = None,
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
            raise InvalidCommandArgumentException(
                f"illegal args for {self.identifier.name}: {args}"
            )
        return super().render(opcode)


class ObjectMemoryModifyBits(ActionScriptCommand):
    """(unknown)"""

    _size: int = 2
    _arg_1: int
    _set_bits: Set[int]
    _clear_bits: Set[int]

    @property
    def arg_1(self) -> int:
        """(unknown)"""
        return self._arg_1

    @property
    def set_bits(self) -> Set[int]:
        """(unknown)"""
        return self._set_bits

    @property
    def clear_bits(self) -> Set[int]:
        """(unknown)"""
        return self._clear_bits

    def set_props(
        self,
        arg_1: int,
        set_bits: Union[List[int], Set[int]],
        clear_bits: Union[List[int], Set[int]],
    ) -> None:
        """(unknown)"""
        props_input = (arg_1, list(set_bits), list(clear_bits))
        assert props_input in [
            (0x09, [5], [4, 6]),
            (0x0C, [4], [3, 5]),
        ]
        self._arg_1 = arg_1
        self._set_bits = set(set_bits)
        self._clear_bits = set(clear_bits)

    def __init__(
        self,
        arg_1: int,
        set_bits: Optional[Union[List[int], Set[int]]] = None,
        clear_bits: Optional[Union[List[int], Set[int]]] = None,
        identifier: Optional[str] = None,
    ) -> None:
        if set_bits is None:
            set_bits = set()
        if clear_bits is None:
            clear_bits = set()
        super().__init__(identifier)
        self.set_props(arg_1, set_bits, clear_bits)

    def render(self) -> bytearray:
        args = (self.arg_1, self.set_bits, self.clear_bits)
        if args == (0x09, [5], [4, 6]):
            return super().render(0xFD, 0x0E)
        if args == (0x0C, [4], [3, 5]):
            return super().render(0xFD, 0x15)
        raise InvalidCommandArgumentException(
            f"illegal args for {self.identifier.name}: {args}"
        )


class SetBit(ActionScriptCommand):
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


class ClearBit(ActionScriptCommand):
    """Clear a bit in the range of long-term memory bits dedicated for use in
    event and action scripts.\n
    It is recommended to specify the bit using the const names defined for
    these particular bits."""

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


class JmpIfBitSet(ActionScriptCommandWithJmps):
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


class JmpIfBitClear(ActionScriptCommandWithJmps):
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


class SetMem704XAt700CBit(ActionScriptCommandNoArgs):
    """For the literal value currently stored at $700C, set the bit that
    corresponds to this index (starting from $7040 bit 0).\n
    For example, if $700C is set to 5, then $7040 bit 5 will be set. If
    $700C is set to 12, then $7041 bit 4 will be set."""

    _opcode: int = 0xA3


class ClearMem704XAt700CBit(ActionScriptCommandNoArgs):
    """For the literal value currently stored at $700C, clear the bit that
    corresponds to this index (starting from $7040 bit 0).\n
    For example, if $700C is set to 5, then $7040 bit 5 will be cleared. If
    $700C is set to 12, then $7041 bit 4 will be cleared."""

    _opcode: int = 0xA7


class JmpIfMem704XAt700CBitSet(ActionScriptCommandWithJmps):
    """Jump to a point in script bank indicated by the provided identifier,
    but only if the bit corresponding to the index indicated by the value
    of $700C is set.\n
    For example, if $700C is set to 5, then this command will jump to the code
    beginning at the given identifier if $7040 bit 5 is set. If $700C is set
    to 12, then the jump will occur if $7041 bit 4 is set."""

    _opcode: int = 0xDB
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfMem704XAt700CBitClear(ActionScriptCommandWithJmps):
    """Jump to a point in script bank indicated by the provided identifier,
    but only if the bit corresponding to the index indicated by the value
    of $700C is clear.\n
    For example, if $700C is set to 5, then this command will jump to the code
    beginning at the given identifier if $7040 bit 5 is clear. If $700C is set
    to 12, then the jump will occur if $7041 bit 4 is clear."""

    _size: int = 3
    _opcode: int = 0xDF

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class SetVarToConst(ActionScriptCommand):
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
        if address == PRIMARY_TEMP_700C or isinstance(address, ByteVar):
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
        if self.address == PRIMARY_TEMP_700C:
            return super().render(0xAC, UInt16(self.value))
        if isinstance(self.address, ShortVar):
            return super().render(0xB0, self.address, UInt16(self.value))
        raise InvalidCommandArgumentException(
            f"illegal args for {self.identifier.name}: 0x{self.address:04x}: {self.value}"
        )


class AddConstToVar(ActionScriptCommand):
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
        if address == PRIMARY_TEMP_700C or isinstance(address, ByteVar):
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
        if self.address == PRIMARY_TEMP_700C:
            return super().render(0xAD, UInt16(self.value))
        if isinstance(self.address, ShortVar):
            return super().render(0xB1, self.address, UInt16(self.value))
        raise InvalidCommandArgumentException(
            f"illegal args for {self.identifier.name}: 0x{self.address:04x}: {self.value}"
        )


class Inc(ActionScriptCommandAnySizeMem):
    """Increase the given variable by 1."""

    def render(self) -> bytearray:
        if isinstance(self.address, ByteVar):
            return super().render(0xAA, self.address)
        if self.address == PRIMARY_TEMP_700C:
            return super().render(0xAE)
        if isinstance(self.address, ShortVar):
            return super().render(0xB2, self.address)
        raise InvalidCommandArgumentException(
            f"illegal args for {self.identifier.name}: 0x{self.address:04x}"
        )


class Dec(ActionScriptCommandAnySizeMem):
    """Decrease the given variable by 1."""

    def render(self) -> bytearray:
        if isinstance(self.address, ByteVar):
            return super().render(0xAB, self.address)
        if self.address == PRIMARY_TEMP_700C:
            return super().render(0xAF)
        if isinstance(self.address, ShortVar):
            return super().render(0xB3, self.address)
        raise InvalidCommandArgumentException(
            f"illegal args for {self.identifier.name}: 0x{self.address:04x}"
        )


class CopyVarToVar(ActionScriptCommand):
    """Copy the value from one variable to another variable."""

    _from_var: Union[ShortVar, ByteVar]
    _to_var: Union[ShortVar, ByteVar]

    def set_addresses(self, from_var=None, to_var=None):
        """Set the source variable, destination variable, or both.\n
        Can accept either two 16 bit ShortVars, or $700C and one ByteVar or ShortVar.
        Cannot accept two ByteVars."""
        if from_var is None:
            from_var = self.from_var
        if to_var is None:
            to_var = self.to_var
        if isinstance(from_var, ByteVar) and isinstance(to_var, ByteVar):
            raise InvalidCommandArgumentException(
                f"illegal args for {self.identifier.name}: 0x{from_var:04x} 0x{to_var:04x}"
            )
        if PRIMARY_TEMP_700C not in (self.from_var, self.to_var):
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
        if self.to_var == PRIMARY_TEMP_700C and isinstance(self.from_var, ByteVar):
            return super().render(0xB4, self.from_var)
        if self.from_var == PRIMARY_TEMP_700C and isinstance(self.to_var, ByteVar):
            return super().render(0xB5, self.to_var)
        if self.to_var == PRIMARY_TEMP_700C and isinstance(self.from_var, ShortVar):
            return super().render(0xBA, self.from_var)
        if self.from_var == PRIMARY_TEMP_700C and isinstance(self.to_var, ShortVar):
            return super().render(0xBB, self.to_var)
        if isinstance(self.from_var, ShortVar) and isinstance(self.to_var, ShortVar):
            return super().render(0xBC, self.from_var, self.to_var)
        raise InvalidCommandArgumentException(
            f"""illegal args for {self.identifier.name}: 
            0x{self.from_var:04x} 0x{self.to_var:04x}"""
        )


class CompareVarToConst(ActionScriptCommandShortAddrAndValueOnly):
    """Compare the value stored at a given variable to a literal constant.
    The result of this comparison can be used in JmpIfComparisonResultIs... commands
    or JmpIfLoadedMemory... commands."""

    def render(self) -> bytearray:
        if self.address == PRIMARY_TEMP_700C:
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


class Compare700CToVar(ActionScriptCommandShortMem):
    """Compare the value stored at $700C to the value stored at a given variable.
    The result of this comparison can be used in JmpIfComparisonResultIs... commands
    or JmpIfLoadedMemory... commands."""

    _opcode: int = 0xC1
    _size: int = 2


class JmpIfComparisonResultIsGreaterOrEqual(ActionScriptCommandWithJmps):
    """Depending on the result of an earlier CompareVarToConst or Compare700CToVar,
    jump to the code indicated by the given identifier if the comparison result
    returned greater or equal."""

    _opcode: int = 0xEC
    _size = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfComparisonResultIsLesser(ActionScriptCommandWithJmps):
    """Depending on the result of an earlier CompareVarToConst or Compare700CToVar,
    jump to the code indicated by the given identifier if the comparison result
    returned lesser."""

    _opcode: int = 0xED
    _size = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class SetVarToRandom(ActionScriptCommandShortAddrAndValueOnly):
    """Set the given variable to a random number between 0 and the
    given upper bound."""

    def render(self) -> bytearray:
        if self.address == PRIMARY_TEMP_700C:
            return super().render(0xB6, self.value)
        return super().render(0xB7, self.address, self.value)


class AddVarTo700C(ActionScriptCommandShortMem):
    """Add the value stored at the given variable to $700C."""

    _opcode: int = 0xB8
    _size: int = 2


class DecVarFrom700C(ActionScriptCommandShortMem):
    """Subtract the value stored at the given variable to $700C."""

    _opcode: int = 0xB9
    _size: int = 2


class SwapVars(ActionScriptCommand):
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


class Move70107015To7016701B(ActionScriptCommandNoArgs):
    """Copy the 16 bit values stored at $7010, $7012, and $7014
    to replace the 16 bit values stored at $7016, $7018, and $701A."""

    _opcode: int = 0xBE


class Move7016701BTo70107015(ActionScriptCommandNoArgs):
    """Copy the 16 bit values stored at $7016, $7018, and $701A
    to replace the 16 bit values stored at $7010, $7012, and $7014."""

    _opcode: int = 0xBF


class JmpIfVarEqualsConst(ActionScriptCommandWithJmps):
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
        if address == PRIMARY_TEMP_700C or isinstance(address, ByteVar):
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
        if self.address == PRIMARY_TEMP_700C:
            return super().render(0xE2, UInt16(self.value), *self.destinations)
        if isinstance(self.address, ShortVar):
            return super().render(
                0xE4, self.address, UInt16(self.value), *self.destinations
            )
        raise InvalidCommandArgumentException(
            f"illegal args for {self.identifier.name}: 0x{self.address:04x}: {self.value}"
        )


class JmpIfVarNotEqualsConst(ActionScriptCommandWithJmps):
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
        if address == PRIMARY_TEMP_700C or isinstance(address, ByteVar):
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
        if self.address == PRIMARY_TEMP_700C:
            return super().render(0xE3, UInt16(self.value), *self.destinations)
        if isinstance(self.address, ShortVar):
            return super().render(
                0xE5, self.address, UInt16(self.value), *self.destinations
            )
        raise InvalidCommandArgumentException(
            f"illegal args for {self.identifier.name}: 0x{self.address:04x}: {self.value}"
        )


class JmpIf700CAllBitsClear(ActionScriptCommandWithJmps):
    """If all of the stated bits are clear on $700C, go to to the script command
    indicated by the given identifier."""

    _opcode: int = 0xE6
    _size = 5
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


class JmpIf700CAnyBitsSet(ActionScriptCommandWithJmps):
    """If any of the stated bits are set on $700C, go to to the script command
    indicated by the given identifier."""

    _opcode: int = 0xE7
    _size = 5
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


class JmpIfRandom2of3(ActionScriptCommandWithJmps):
    """There is a 2/3 chance that, when this command is executed, a goto will be performed
    to the command indicated by the given identifier."""

    _opcode: int = 0xE9
    _size: int = 5

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfRandom1of2(ActionScriptCommandWithJmps):
    """There is a 50/50 chance that, when this command is executed, a goto will be performed
    to the command indicated by the given identifier."""

    _opcode: int = 0xE8
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfLoadedMemoryIs0(ActionScriptCommandWithJmps):
    """'Loaded Memory' in most cases refers to the result of a comparison command.
    Jump to the code indicated by the given identifier if the comparison result was zero
    (both values were equal)."""

    _opcode: int = 0xEA
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfLoadedMemoryIsAboveOrEqual0(ActionScriptCommandWithJmps):
    """'Loaded Memory' in most cases refers to the result of a comparison command.
    Jump to the code indicated by the given identifier if the comparison result indicated
    that the first value was less than or equal the second value."""

    _opcode: int = 0xEF
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfLoadedMemoryIsBelow0(ActionScriptCommandWithJmps):
    """'Loaded Memory' in most cases refers to the result of a comparison command.
    Jump to the code indicated by the given identifier if the comparison result indicated
    that the first value was greater than the second value."""

    _opcode: int = 0xEE
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class JmpIfLoadedMemoryIsNot0(ActionScriptCommandWithJmps):
    """'Loaded Memory' in most cases refers to the result of a comparison command.
    Jump to the code indicated by the given identifier if the comparison result was not zero
    (values were not equal, irrespective of which was larger or smaller)."""

    _opcode: int = 0xEB
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


class Mem700CAndConst(ActionScriptCommandBasicShortOperation):
    """Perform an AND operation between the value of $700C and a given literal number,
    save the result to $700C."""

    _opcode = bytearray([0xFD, 0xB0])


class Mem700CAndVar(ActionScriptCommandShortMem):
    """Perform an AND operation between the value of $700C and a given variable,
    save the result to $700C."""

    _opcode = bytearray([0xFD, 0xB3])
    _size: int = 3


class Mem700COrConst(ActionScriptCommandBasicShortOperation):
    """Perform an OR operation between the value of $700C and a given literal number,
    save the result to $700C."""

    _opcode = bytearray([0xFD, 0xB1])


class Mem700COrVar(ActionScriptCommandShortMem):
    """Perform an OR operation between the value of $700C and a given variable,
    save the result to $700C."""

    _opcode = bytearray([0xFD, 0xB4])
    _size: int = 3


class Mem700CXorConst(ActionScriptCommandBasicShortOperation):
    """Perform a XOR operation between the value of $700C and a given literal number,
    save the result to $700C."""

    _opcode = bytearray([0xFD, 0xB2])


class Mem700CXorVar(ActionScriptCommandShortMem):
    """Perform a XOR operation between the value of $700C and a given variable,
    save the result to $700C."""

    _opcode = bytearray([0xFD, 0xB5])
    _size: int = 3


class VarShiftLeft(ActionScriptCommand):
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


class LoadMemory(ActionScriptCommandShortMem):
    """(unknown)"""

    _opcode = 0xD6
    _size: int = 3


# sequencing


class SetSpriteSequence(ActionScriptCommand):
    """Change the active sprite sequence or static mold for the NPC."""

    _opcode: int = 0x08
    _size: int = 3
    _index: UInt8
    _sprite_offset: UInt4
    _is_mold: bool = False
    _is_sequence: bool = False
    _looping: bool = False
    _mirror_sprite: bool = False

    @property
    def index(self) -> UInt8:
        """The index of the sequence or mold to display for the NPC."""
        return self._index

    def set_index(self, index: int) -> None:
        """Designate the index of the sequence or mold to display for the NPC."""
        self._index = UInt8(index)

    @property
    def sprite_offset(self) -> UInt4:
        """Shift the sprite index up by the given amount.\n
        For example, if the NPC uses sprite ID #31 by default, a value of 2 for this
        method would instead make it shift to sprite ID #33.\n
        Value must be between 0 and 7."""
        return self._sprite_offset

    def set_sprite_offset(self, sprite_offset: int) -> None:
        """Designate the amount to shift the sprite index up by.\n
        For example, if the NPC uses sprite ID #31 by default, a value of 2 for this
        method would instead make it shift to sprite ID #33.\n
        Value must be between 0 and 7."""
        assert 0 <= sprite_offset <= 7
        self._sprite_offset = UInt4(sprite_offset)

    @property
    def is_mold(self) -> bool:
        """If true, this command will load a specific static mold instead of
        an animation sequence."""
        return self._is_mold

    def set_is_mold(self, is_mold: bool) -> None:
        """If true, this command will load a specific static mold instead of
        an animation sequence."""
        self._is_mold = is_mold

    @property
    def is_sequence(self) -> bool:
        """(unknown how this actually works)"""
        return self._is_sequence

    def set_is_sequence(self, is_sequence: bool) -> None:
        """(unknown how this actually works)"""
        self._is_sequence = is_sequence

    @property
    def looping(self) -> bool:
        """If true, the sprite sequence will loop infinitely.\n
        If false, the sprite sequence will play once, and the NPC will remain
        in the position of the sequence's final frame.\n
        This has no effect if you are loading a mold and not a sequence."""
        return self._looping

    def set_looping(self, looping: bool) -> None:
        """If true, the sprite sequence will loop infinitely.\n
        If false, the sprite sequence will play once, and the NPC will remain
        in the position of the sequence's final frame.\n
        This has no effect if you are loading a mold and not a sequence."""
        self._looping = looping

    @property
    def mirror_sprite(self) -> bool:
        """If true, the sprite will be mirrored horizontally from its default position."""
        return self._mirror_sprite

    def set_mirror_sprite(self, mirror_sprite: bool) -> None:
        """If true, the sprite will be mirrored horizontally from its default position."""
        self._mirror_sprite = mirror_sprite

    def __init__(
        self,
        index: int,
        sprite_offset: int = 0,
        is_mold: bool = False,
        is_sequence: bool = False,
        looping: bool = False,
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
        self.set_looping(looping)
        self.set_mirror_sprite(mirror_sprite)

    def render(self) -> bytearray:
        bit_array = [False] * 16
        bit_array[3] = self.is_mold
        bit_array[4] = not self.looping
        bit_array[6] = self.is_sequence
        bit_array[15] = self.mirror_sprite
        flags: int = bools_to_int(*bit_array)
        arg = UInt16((self.index << 8) | self.sprite_offset | flags)
        return super().render(arg)


class SequencePlaybackOn(ActionScriptCommandNoArgs):
    """Causes the NPC's active sprite sequence to resume."""

    _opcode: int = 0x02


class SequencePlaybackOff(ActionScriptCommandNoArgs):
    """Halts the NPC's active sprite sequence."""

    _opcode: int = 0x03


class SequenceLoopingOn(ActionScriptCommandNoArgs):
    """Causes the NPC's active sprite sequence to loop infinitely."""

    _opcode: int = 0x04


class SequenceLoopingOff(ActionScriptCommandNoArgs):
    """Causes the NPC's active sprite sequence to half upon completion of its
    current iteration."""

    _opcode: int = 0x05


class _SetAnimationSpeed(ActionScriptCommand):
    """Applies a pre-set multiplier to either the duration of each frame in the NPC's
    active sequence, or the NPC's walking speed, or both."""

    _opcode: int = 0x10
    _size: int = 2
    _speed: SequenceSpeed
    _sequence: bool = False
    _walking: bool = False

    @property
    def speed(self) -> SequenceSpeed:
        """The speed at which to perform this action."""
        return self._speed

    def set_speed(self, speed: SequenceSpeed) -> None:
        """Designate the speed at which to perform this action."""
        self._speed = speed
        assert self.speed or self.sequence

    @property
    def sequence(self) -> bool:
        """If true, this change will apply to the character's sequence playback speed."""
        return self._sequence

    def set_sequence(self, sequence: bool) -> None:
        """If true, this change will apply to the character's sequence playback speed."""
        self._sequence = sequence
        assert self.speed or self.sequence

    @property
    def walking(self) -> bool:
        """If true, this change will apply to the character's walking speed."""
        return self._walking

    def set_walking(self, walking: bool) -> None:
        """If true, this change will apply to the character's walking speed."""
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
    """Applies a pre-set multiplier to the duration of each frame in the NPC's
    active sequence."""

    def __init__(
        self,
        speed: SequenceSpeed,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(speed, sequence=True, walking=False, identifier=identifier)


class SetWalkingSpeed(_SetAnimationSpeed):
    """Applies a pre-set multiplier to the NPC's walking speed."""

    def __init__(
        self,
        speed: SequenceSpeed,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(speed, sequence=False, walking=True, identifier=identifier)


class SetAllSpeeds(_SetAnimationSpeed):
    """Applies a pre-set multiplier to both the duration of each frame in the NPC's
    active sequence and the NPC's walking speed."""

    def __init__(
        self,
        speed: SequenceSpeed,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(speed, sequence=True, walking=True, identifier=identifier)


class EmbeddedAnimationRoutine(ActionScriptCommand):
    """(unknown)"""

    _args: bytearray
    _size: int = 16

    @property
    def args(self) -> bytearray:
        """(unknown)"""
        return self._args

    def set_args(self, args: bytearray) -> None:
        """(unknown)"""
        assert len(args) == 16
        assert args[0] in [0x26, 0x27, 0x28]
        self._args = args

    def __init__(self, args: bytearray, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_args(args)

    def render(self) -> bytearray:
        return super().render(self.args)


class MaximizeSequenceSpeed(ActionScriptCommandNoArgs):
    """Set the NPC's sequence speed to its highest value.\n
    Not known if this actually works."""

    _opcode: int = 0x85


class MaximizeSequenceSpeed86(ActionScriptCommandNoArgs):
    """Set the NPC's sequence speed to its highest value.\n
    Not known if this actually works."""

    _opcode: int = 0x86


# positioning


class FixedFCoordOn(ActionScriptCommandNoArgs):
    """The NPC will not change from the direction it is currently facing,
    regardless of any other movements makes."""

    _opcode: int = 0x06


class FixedFCoordOff(ActionScriptCommandNoArgs):
    """The direction the NPC faces will depend on its other actions and
    not be locked."""

    _opcode: int = 0x07


class JmpIfObjectWithinRange(ActionScriptCommandWithJmps):
    """If this NPC and the specified NPC are less than the given number of tiles
    apart (ignoring Z axis), go to the section of code indicated by the identifier."""

    _opcode: int = 0x3A
    _size: int = 6
    _comparing_npc: AreaObject
    _usually: UInt8
    _tiles: UInt8

    @property
    def comparing_npc(self) -> AreaObject:
        """The object to check if this NPC is within range of."""
        return self._comparing_npc

    def set_comparing_npc(self, comparing_npc: AreaObject) -> None:
        """Designate te object to check if this NPC is within range of."""
        self._comparing_npc = comparing_npc

    @property
    def usually(self) -> UInt8:
        """(unknown)"""
        return self._usually

    def set_usually(self, usually: int) -> None:
        """(unknown)"""
        self._usually = UInt8(usually)

    @property
    def tiles(self) -> UInt8:
        """The upper threshold of tiles separating this NPC from the specified NPC
        which will trigger the goto."""
        return self._tiles

    def set_tiles(self, tiles: int) -> None:
        """Set the upper threshold of tiles separating this NPC from the specified NPC
        which will trigger the goto."""
        self._tiles = UInt8(tiles)

    def __init__(
        self,
        comparing_npc: AreaObject,
        usually: int,
        tiles: int,
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_comparing_npc(comparing_npc)
        self.set_usually(usually)
        self.set_tiles(tiles)

    def render(self) -> bytearray:
        return super().render(
            self.comparing_npc, self.usually, self.tiles, *self.destinations
        )


class JmpIfObjectWithinRangeSameZ(ActionScriptCommandWithJmps):
    """If this NPC and the specified NPC are less than the given number of tiles
    apart (on the same Z axis), go to the section of code indicated by the identifier.
    """

    _opcode: int = 0x3B
    _size: int = 6
    _comparing_npc: AreaObject
    _usually: UInt8
    _tiles: UInt8

    @property
    def comparing_npc(self) -> AreaObject:
        """The object to check if this NPC is within range of."""
        return self._comparing_npc

    def set_comparing_npc(self, comparing_npc: AreaObject) -> None:
        """Designate te object to check if this NPC is within range of."""
        self._comparing_npc = comparing_npc

    @property
    def usually(self) -> UInt8:
        """(unknown)"""
        return self._usually

    def set_usually(self, usually: int) -> None:
        """(unknown)"""
        self._usually = UInt8(usually)

    @property
    def tiles(self) -> UInt8:
        """The upper threshold of tiles separating this NPC from the specified NPC
        which will trigger the goto."""
        return self._tiles

    def set_tiles(self, tiles: int) -> None:
        """Set the upper threshold of tiles separating this NPC from the specified NPC
        which will trigger the goto."""
        self._tiles = UInt8(tiles)

    def __init__(
        self,
        comparing_npc: AreaObject,
        usually: int,
        tiles: int,
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_comparing_npc(comparing_npc)
        self.set_usually(usually)
        self.set_tiles(tiles)

    def render(self) -> bytearray:
        return super().render(
            self.comparing_npc, self.usually, self.tiles, *self.destinations
        )


class Walk1StepEast(ActionScriptCommandNoArgs):
    """Walk 1 step east"""

    _opcode: int = 0x40


class Walk1StepSoutheast(ActionScriptCommandNoArgs):
    """Walk 1 step southeast"""

    _opcode: int = 0x41


class Walk1StepSouth(ActionScriptCommandNoArgs):
    """Walk 1 step south"""

    _opcode: int = 0x42


class Walk1StepSouthwest(ActionScriptCommandNoArgs):
    """Walk 1 step southwest"""

    _opcode: int = 0x43


class Walk1StepWest(ActionScriptCommandNoArgs):
    """Walk 1 step west"""

    _opcode: int = 0x44


class Walk1StepNorthwest(ActionScriptCommandNoArgs):
    """Walk 1 step northwest"""

    _opcode: int = 0x45


class Walk1StepNorth(ActionScriptCommandNoArgs):
    """Walk 1 step note"""

    _opcode: int = 0x46


class Walk1StepNortheast(ActionScriptCommandNoArgs):
    """Walk 1 step northeast"""

    _opcode: int = 0x47


class Walk1StepFDirection(ActionScriptCommandNoArgs):
    """Walk 1 step in the direction the NPC is currently facing"""

    _opcode: int = 0x48


class AddZCoord1Step(ActionScriptCommandNoArgs):
    """Rise 1 step on the Z axis"""

    _opcode: int = 0x4A


class DecZCoord1Step(ActionScriptCommandNoArgs):
    """Lower 1 step on the Z axis"""

    _opcode: int = 0x4B


class WalkEastSteps(ActionScriptCommandByteSteps):
    """Walk the given number of steps eastward."""

    _opcode: int = 0x50


class WalkSoutheastSteps(ActionScriptCommandByteSteps):
    """Walk the given number of steps southeastward."""

    _opcode: int = 0x51


class WalkSouthSteps(ActionScriptCommandByteSteps):
    """Walk the given number of steps southward."""

    _opcode: int = 0x52


class WalkSouthwestSteps(ActionScriptCommandByteSteps):
    """Walk the given number of steps southwestward."""

    _opcode: int = 0x53


class WalkWestSteps(ActionScriptCommandByteSteps):
    """Walk the given number of steps westward."""

    _opcode: int = 0x54


class WalkNorthwestSteps(ActionScriptCommandByteSteps):
    """Walk the given number of steps northwestward."""

    _opcode: int = 0x55


class WalkNorthSteps(ActionScriptCommandByteSteps):
    """Walk the given number of steps northward."""

    _opcode: int = 0x56


class WalkNortheastSteps(ActionScriptCommandByteSteps):
    """Walk the given number of steps northeastward."""

    _opcode: int = 0x57


class WalkFDirectionSteps(ActionScriptCommandByteSteps):
    """Walk the given number of steps in the direction the NPC is currently facing."""

    _opcode: int = 0x58


class ShiftZ20Steps(ActionScriptCommandNoArgs):
    """Shift 20 steps upward on the Z axis."""

    _opcode: int = 0x59


class ShiftZUpSteps(ActionScriptCommandByteSteps):
    """Shift the given number of steps upward on the Z axis."""

    _opcode: int = 0x5A


class ShiftZDownSteps(ActionScriptCommandByteSteps):
    """Shift the given number of steps downward on the Z axis."""

    _opcode: int = 0x5B


class ShiftZUp20Steps(ActionScriptCommandNoArgs):
    """Shift 20 steps upward on the Z axis."""

    _opcode: int = 0x5C


class ShiftZDown20Steps(ActionScriptCommandNoArgs):
    """Shift 20 steps downward on the Z axis."""

    _opcode: int = 0x5D


class WalkEastPixels(ActionScriptCommandBytePixels):
    """Walk the given number of pixels eastward."""

    _opcode: int = 0x60


class WalkSoutheastPixels(ActionScriptCommandBytePixels):
    """Walk the given number of pixels southeastward."""

    _opcode: int = 0x61


class WalkSouthPixels(ActionScriptCommandBytePixels):
    """Walk the given number of pixels southward."""

    _opcode: int = 0x62


class WalkSouthwestPixels(ActionScriptCommandBytePixels):
    """Walk the given number of pixels southwestward."""

    _opcode: int = 0x63


class WalkWestPixels(ActionScriptCommandBytePixels):
    """Walk the given number of pixels westward."""

    _opcode: int = 0x64


class WalkNorthwestPixels(ActionScriptCommandBytePixels):
    """Walk the given number of pixels northwestward."""

    _opcode: int = 0x65


class WalkNorthPixels(ActionScriptCommandBytePixels):
    """Walk the given number of pixels northward."""

    _opcode: int = 0x66


class WalkNortheastPixels(ActionScriptCommandBytePixels):
    """Walk the given number of pixels northeastward."""

    _opcode: int = 0x67


class WalkFDirectionPixels(ActionScriptCommandBytePixels):
    """Walk the given number of pixels in the direction the NPC is currently facing."""

    _opcode: int = 0x68


class WalkFDirection16Pixels(ActionScriptCommandNoArgs):
    """Walk 16 pixels in the direction the NPC is currently facing."""

    _opcode: int = 0x69


class ShiftZUpPixels(ActionScriptCommandBytePixels):
    """Shift the given number of pixels upward on the Z axis."""

    _opcode: int = 0x6A


class ShiftZDownPixels(ActionScriptCommandBytePixels):
    """Shift the given number of pixels downward on the Z axis."""

    _opcode: int = 0x6B


class FaceEast(ActionScriptCommandNoArgs):
    """Face eastward."""

    _opcode: int = 0x70


class FaceEast7C(ActionScriptCommandNoArgs):
    """Face eastward (unknown if this is different from FaceEast)."""

    _opcode: int = 0x7C


class FaceSoutheast(ActionScriptCommandNoArgs):
    """Face southeastward."""

    _opcode: int = 0x71


class FaceSouth(ActionScriptCommandNoArgs):
    """Face southward."""

    _opcode: int = 0x72


class FaceSouthwest(ActionScriptCommandNoArgs):
    """Face southwestward."""

    _opcode: int = 0x73


class FaceSouthwest7D(ActionScriptCommandNoArgs):
    """Face southwestward (unknown if this is different from FaceSouthwest)."""

    _opcode: int = 0x7D


class FaceWest(ActionScriptCommandNoArgs):
    """Face westward."""

    _opcode: int = 0x74


class FaceNorthwest(ActionScriptCommandNoArgs):
    """Face northwestward."""

    _opcode: int = 0x75


class FaceNorth(ActionScriptCommandNoArgs):
    """Face northward."""

    _opcode: int = 0x76


class FaceNortheast(ActionScriptCommandNoArgs):
    """Face northeastward."""

    _opcode: int = 0x77


class FaceMario(ActionScriptCommandNoArgs):
    """Face toward the player."""

    _opcode: int = 0x78


class TurnClockwise45Degrees(ActionScriptCommandNoArgs):
    """Turn clockwise 45 degrees once."""

    _opcode: int = 0x79


class TurnRandomDirection(ActionScriptCommandNoArgs):
    """Turn any random direction supported by the NPC's VRAMsetting."""

    _opcode: int = 0x7A


class TurnClockwise45DegreesNTimes(ActionScriptCommand):
    """Turn clockwise 45 degrees, repeated a given number of times."""

    _opcode: int = 0x7B
    _size: int = 2
    _count: UInt8

    @property
    def count(self) -> UInt8:
        """The number of times to turn clockwise."""
        return self._count

    def set_count(self, count: int) -> None:
        """Set the number of times to turn clockwise."""
        self._count = UInt8(count)

    def __init__(self, count: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_count(count)

    def render(self) -> bytearray:
        return super().render(self.count)


class JumpToHeight(ActionScriptCommand):
    """The NPC jumps off its current surface to a given height (unknown units)."""

    _size: int = 3
    _height: UInt16
    _silent: bool = False

    @property
    def height(self) -> UInt16:
        """(Units unknown)"""
        return self._height

    def set_height(self, height: int) -> None:
        """(Units unknown)"""
        self._height = UInt16(height)

    @property
    def silent(self) -> bool:
        """If true, this jump action will not make a sound effect."""
        return self._silent

    def set_silent(self, silent: bool) -> None:
        """If true, this jump action will not make a sound effect."""
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
        return super().render(0x7F, self.height)


class WalkToXYCoords(ActionScriptCommandXYBytes):
    """Walk to the indicated X-Y coordinates (performs walking animation)."""

    _opcode: int = 0x80


class WalkXYSteps(ActionScriptCommandXYBytes):
    """Walk the indicated number of steps in the X and Y directions
    (performs walking animation)."""

    _opcode: int = 0x81


class ShiftToXYCoords(ActionScriptCommandXYBytes):
    """Shift to the indicated X-Y coordinates (does not perform walking animation)."""

    _opcode: int = 0x82


class ShiftXYSteps(ActionScriptCommandXYBytes):
    """Shift the indicated number of steps in the X and Y directions
    (does not perform walking animation)."""

    _opcode: int = 0x83


class ShiftXYPixels(ActionScriptCommandXYBytes):
    """Shift the indicated number of pixels in the X and Y directions
    (does not perform walking animation)."""

    _opcode: int = 0x84


class TransferToObjectXY(ActionScriptCommand):
    """Instantly teleport to the X/Y coordinates of the specified object
    (ignore Z coord)."""

    _opcode: int = 0x87
    _size: int = 2
    _target_npc: AreaObject

    @property
    def target_npc(self) -> AreaObject:
        """The NPC whose X/Y coords this NPC should teleport to."""
        return self._target_npc

    def set_target_npc(self, target_npc: AreaObject) -> None:
        """Designate the NPC whose X/Y coords this NPC should teleport to."""
        self._target_npc = target_npc

    def __init__(
        self,
        target_npc: AreaObject,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_target_npc(target_npc)

    def render(self) -> bytearray:
        return super().render(self.target_npc)


class TransferToObjectXYZ(ActionScriptCommand):
    """Instantly teleport to the X/Y/Z coordinates of the specified object."""

    _opcode: int = 0x95
    _size: int = 2
    _target_npc: AreaObject

    @property
    def target_npc(self) -> AreaObject:
        """The NPC whose X/Y/Z coords this NPC should teleport to."""
        return self._target_npc

    def set_target_npc(self, target_npc: AreaObject) -> None:
        """Designate the NPC whose X/Y/Z coords this NPC should teleport to."""
        self._target_npc = target_npc

    def __init__(
        self,
        target_npc: AreaObject,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_target_npc(target_npc)

    def render(self) -> bytearray:
        return super().render(self.target_npc)


class RunAwayShift(ActionScriptCommandNoArgs):
    """(unknown)"""

    _opcode: int = 0x88


class TransferTo70167018(ActionScriptCommandNoArgs):
    """Instantly transfer this NPC to the X/Y pixel coordinates represented by the
    values currently stored at $7016 and $7018."""

    _opcode: int = 0x89


class TransferTo70167018701A(ActionScriptCommandNoArgs):
    """Transfer this NPC to the X/Y/Z pixel coordinates represented by the
    values currently stored at $7016, $7018, and $701A."""

    _opcode: int = 0x99


class WalkTo70167018(ActionScriptCommandNoArgs):
    """This NPC walks to the X/Y pixel coordinates represented by the
    values currently stored at $7016 and $7018."""

    _opcode: int = 0x8A


class WalkTo70167018701A(ActionScriptCommandNoArgs):
    """This NPC walks to the X/Y/Z pixel coordinates represented by the
    values currently stored at $7016, $7018, and $701A."""

    _opcode: int = 0x98


class BounceToXYWithHeight(ActionScriptCommand):
    """This NPC jumps to a given X/Y coord set while also jumping to the specified height."""

    _opcode: int = 0x90
    _size: int = 4
    _x: UInt8
    _y: UInt8
    _height: UInt8

    @property
    def x(self) -> UInt8:
        """The X coordinate at which the NPC should land."""
        return self._x

    def set_x(self, x: int) -> None:
        """Set the X coordinate at which the NPC should land."""
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        """The Y coordinate at which the NPC should land."""
        return self._y

    def set_y(self, y: int) -> None:
        """Set the Y coordinate at which the NPC should land."""
        self._y = UInt8(y)

    @property
    def height(self) -> UInt8:
        """(Units unknown)"""
        return self._height

    def set_height(self, height: int) -> None:
        """(Units unknown)"""
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
    """This NPC jumps the ground distance given by an X/Y coord set
    while also jumping to the specified height."""

    _opcode: int = 0x91
    _size: int = 4
    _x: UInt8
    _y: UInt8
    _height: UInt8

    @property
    def x(self) -> UInt8:
        """The X axis component of the NPC's jump distance."""
        return self._x

    def set_x(self, x: int) -> None:
        """Set the X axis component of the NPC's jump distance."""
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        """The Y axis component of the NPC's jump distance."""
        return self._y

    def set_y(self, y: int) -> None:
        """Set the Y axis component of the NPC's jump distance."""
        self._y = UInt8(y)

    @property
    def height(self) -> UInt8:
        """(Units unknown)"""
        return self._height

    def set_height(self, height: int) -> None:
        """(Units unknown)"""
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
    """Instantly teleport to the given X/Y/Z coordinates, facing the given direction."""

    _opcode: int = 0x92
    _size: int = 4
    _x: UInt8
    _y: UInt8
    _z: UInt8
    _direction: Direction

    @property
    def x(self) -> UInt8:
        """The X coordinate at which to place the NPC."""
        return self._x

    def set_x(self, x: int) -> None:
        """Set the X coordinate at which to place the NPC."""
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        """The Y coordinate at which to place the NPC."""
        return self._y

    def set_y(self, y: int) -> None:
        """Set the Y coordinate at which to place the NPC."""
        self._y = UInt8(y)

    @property
    def z(self) -> UInt8:
        """The Z coordinate at which to place the NPC."""
        return self._z

    def set_z(self, z: int) -> None:
        """Set the Z coordinate (0-31) at which to place the NPC."""
        assert 0 <= z <= 31
        self._z = UInt8(z)

    @property
    def direction(self) -> Direction:
        """The direction which the NPC should face upon successful transfer."""
        return self._direction

    def set_direction(self, direction: Direction) -> None:
        """Set the direction which the NPC should face upon successful transfer."""
        self._direction = direction

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
    """Instantly teleport to coordinates which are X/Y/Z units away,
    facing the given direction."""

    _opcode: int = 0x93
    _size: int = 4
    _x: UInt8
    _y: UInt8
    _z: UInt8
    _direction: Direction

    @property
    def x(self) -> UInt8:
        """The X coordinate at which to place the NPC."""
        return self._x

    def set_x(self, x: int) -> None:
        """Set the X coordinate at which to place the NPC."""
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        """The Y coordinate at which to place the NPC."""
        return self._y

    def set_y(self, y: int) -> None:
        """Set the Y coordinate at which to place the NPC."""
        self._y = UInt8(y)

    @property
    def z(self) -> UInt8:
        """The Z coordinate at which to place the NPC."""
        return self._z

    def set_z(self, z: int) -> None:
        """Set the Z coordinate (0-31) at which to place the NPC."""
        assert 0 <= z <= 31
        self._z = UInt8(z)

    @property
    def direction(self) -> Direction:
        """The direction which the NPC should face upon successful transfer."""
        return self._direction

    def set_direction(self, direction: Direction) -> None:
        """Set the direction which the NPC should face upon successful transfer."""
        self._direction = direction

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
    """Instantly teleport to coordinates which are X/Y/Z pixels away,
    facing the given direction."""

    _opcode: int = 0x94
    _size: int = 4
    _x: UInt8
    _y: UInt8
    _z: UInt8
    _direction: Direction

    @property
    def x(self) -> UInt8:
        """The X coordinate at which to place the NPC."""
        return self._x

    def set_x(self, x: int) -> None:
        """Set the X coordinate at which to place the NPC."""
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        """The Y coordinate at which to place the NPC."""
        return self._y

    def set_y(self, y: int) -> None:
        """Set the Y coordinate at which to place the NPC."""
        self._y = UInt8(y)

    @property
    def z(self) -> UInt8:
        """The Z coordinate at which to place the NPC."""
        return self._z

    def set_z(self, z: int) -> None:
        """Set the Z coordinate (0-31) at which to place the NPC."""
        assert 0 <= z <= 31
        self._z = UInt8(z)

    @property
    def direction(self) -> Direction:
        """The direction which the NPC should face upon successful transfer."""
        return self._direction

    def set_direction(self, direction: Direction) -> None:
        """Set the direction which the NPC should face upon successful transfer."""
        self._direction = direction

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
    """Sets $700C to the pixel or isometric coordinate value of one dimension
    from any NPC's current coordinates."""

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
        """The specific coordinate whose value to store to $700C."""
        return self._coord

    def set_coord(self, coord: Coord) -> None:
        """Set the specific (not-F) coordinate whose value to store to $700C."""
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
        arg_1 = UInt8(
            (self.bit_7 << 7) + (self.is_isometric_not_pixel << 6) + self.target_npc
        )
        return super().render(opcode, arg_1)


class CreatePacketAtObjectCoords(ActionScriptCommandWithJmps):
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


class CreatePacketAt7010(ActionScriptCommandWithJmps):
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


class CreatePacketAt7010WithEvent(ActionScriptCommandWithJmps):
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
        assert 0 <= event_id < TOTAL_EVENT_SCRIPTS
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


class SummonObjectToSpecificLevel(ActionScriptCommand):
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
        arg_1 = UInt16(0x8000 + (self.target_npc << 9) + self.level_id)
        return super().render(arg_1)


class SummonObjectAt70A8ToCurrentLevel(ActionScriptCommandNoArgs):
    """The NPC whose relative ID is stored at $70A8 (usually the most recent NPC the player
    interacted with) will be summoned to the current level.\n
    This provides no effect if the NPC in question has not already been removed from the level.
    """

    _opcode: int = 0xF4


class RemoveObjectFromSpecificLevel(ActionScriptCommand):
    """Remove the specified NPC to the given level.\n
    This will not really do anything if the NPC has already been
    removed from the given level.\n
    It is recommended to use contextual room constant names for this."""

    _opcode: int = 0xF2
    _size: int = 3
    _target_npc: AreaObject
    _level_id: UInt16

    @property
    def target_npc(self) -> AreaObject:
        """The NPC to be removed from the given level."""
        return self._target_npc

    def set_target_npc(self, target_npc: AreaObject) -> None:
        """Designate the NPC to be removed to the given level."""
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
        arg_1 = UInt16((self.target_npc << 9) + self.level_id)
        assert 0 <= arg_1 <= 0x7FFF
        return super().render(arg_1)


class RemoveObjectAt70A8FromCurrentLevel(ActionScriptCommandNoArgs):
    """The NPC whose relative ID is stored at $70A8 (usually the most recent NPC the player
    interacted with) will be removed from the current level.\n
    This provides no effect if the NPC in question has already been removed from the level.
    """

    _opcode: int = 0xF5


class EnableObjectTriggerInSpecificLevel(ActionScriptCommand):
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
        arg_1 = UInt16(0x8000 + (self.target_npc << 9) + self.level_id)
        return super().render(arg_1)


class EnableTriggerOfObjectAt70A8InCurrentLevel(ActionScriptCommandNoArgs):
    """The NPC whose relative ID is stored at $70A8 (usually the most recent NPC the player
    interacted with) will have its object trigger enabled.\n
    Because you can't interact with a disabled NPC in order to automatically write it to
    $70A8 in the first place, this would require manually writing a value to $70A8 in order
    to use this command, and thus you won't see it very often as other similar commands
    are more useful.\n
    This provides no effect if the NPC in question has not already
    had its object trigger disabled."""

    _opcode: int = 0xF6


class DisableObjectTriggerInSpecificLevel(ActionScriptCommand):
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
        arg_1 = UInt16((self.target_npc << 9) + self.level_id)
        assert 0 <= arg_1 <= 0x7FFF
        return super().render(arg_1)


class DisableTriggerOfObjectAt70A8InCurrentLevel(ActionScriptCommandNoArgs):
    """The NPC whose relative ID is stored at $70A8 (usually the most recent NPC the player
    interacted with) will have its object trigger disabled.\n
    This provides no effect if the NPC in question has already
    had its object trigger disabled."""

    _opcode: int = 0xF7


class JmpIfObjectInSpecificLevel(ActionScriptCommandWithJmps):
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
        arg_1 = UInt16(0x8000 + (self.target_npc << 9) + self.level_id)
        return super().render(arg_1, *self.destinations)


class JmpIfObjectNotInSpecificLevel(ActionScriptCommandWithJmps):
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
        arg_1 = UInt16((self.target_npc << 9) + self.level_id)
        assert 0 <= arg_1 <= 0x7FFF
        return super().render(arg_1, *self.destinations)


class JmpIfObjectInAir(ActionScriptCommandWithJmps):
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


class Set700CToCurrentLevel(ActionScriptCommandNoArgs):
    """Set the value of $700C to the ID of the current level."""

    _opcode: int = 0xC3


# controls


class Set700CToPressedButton(ActionScriptCommandNoArgs):
    """Set the bits of $700C to correspond to all currently pressed buttons.\n
    Dpad Left = 0\n
    Dpad Right = 1\n
    Dpad Down = 2\n
    Dpad Up = 3\n
    X = 4\n
    A = 5\n
    Y = 6\n
    B = 7"""

    _opcode: int = 0xCA


class Set700CToTappedButton(ActionScriptCommandNoArgs):
    """Set the bits of $700C to correspond to an individual tapped button.\n
    Dpad Left = 0\n
    Dpad Right = 1\n
    Dpad Down = 2\n
    Dpad Up = 3\n
    X = 4\n
    A = 5\n
    Y = 6\n
    B = 7"""

    _opcode: int = 0xCB


# palettes


class SetPaletteRow(ActionScriptCommand):
    """Change the row offset of the default palette."""

    _opcode: int = 0x0D
    _size: int = 2
    _row: UInt8

    @property
    def row(self) -> UInt8:
        """The row offset relative to the default palette."""
        return self._row

    def set_row(self, row: int) -> None:
        """Designate the row offset relative to the default palette for this command."""
        assert 0 <= row <= 15
        self._row = UInt8(row)

    def __init__(self, row: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_row(row)

    def render(self) -> bytearray:
        return super().render(self.row)


class IncPaletteRowBy(ActionScriptCommand):
    """Increase the row offset relative to the current palette by a given amount."""

    _rows: UInt8

    @property
    def rows(self) -> UInt8:
        """The row offset to increase by, relative to the current palette."""
        return self._rows

    def set_rows(self, rows: int) -> None:
        """Designate the row offset to increase by, relative to the current palette,
        for this command."""
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
        if self.rows == 1:
            return super().render()
        return super().render(UInt8(0xF0 + self.rows))


# branching / jumps


class BPL262728(ActionScriptCommandNoArgs):
    """(unknown)"""

    _opcode: int = 0x21


class BMI262728(ActionScriptCommandNoArgs):
    """(unknown)"""

    _opcode: int = 0x22


class BPL2627(ActionScriptCommandNoArgs):
    """(unknown)"""

    _opcode: int = 0x2A


class UnknownJmp3C(ActionScriptCommandWithJmps):
    """(unknown)"""

    _opcode: int = 0x3C
    _size: int = 5
    _arg1: UInt8
    _arg2: UInt8

    @property
    def arg1(self) -> UInt8:
        """(unknown)"""
        return self._arg1

    def set_arg1(self, arg1: int) -> None:
        """(unknown)"""
        self._arg1 = UInt8(arg1)

    @property
    def arg2(self) -> UInt8:
        """(unknown)"""
        return self._arg2

    def set_arg2(self, arg2: int) -> None:
        """(unknown)"""
        self._arg2 = UInt8(arg2)

    def __init__(
        self,
        arg1: int,
        arg2: int,
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_arg1(arg1)
        self.set_arg1(arg2)

    def render(self) -> bytearray:
        return super().render(self.arg1, self.arg2, *self.destinations)


class JmpIfMarioInAir(ActionScriptCommandWithJmps):
    """If the player is currently airborne, go to the section of code
    beginning with the specified identifier."""

    _opcode: int = 0x3D
    _size: int = 3

    def render(self) -> bytearray:
        return super().render(*self.destinations)


# music


class StopSound(ActionScriptCommandNoArgs):
    """Halt the playback of any sound effect that is currently playing."""

    _opcode: int = 0x9B


class PlaySound(ActionScriptCommand):
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


class FadeOutSoundToVolume(ActionScriptCommand):
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
