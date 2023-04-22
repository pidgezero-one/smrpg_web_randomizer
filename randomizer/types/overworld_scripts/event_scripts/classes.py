"""Base classes supporting event script assembly."""

from typing import List, Optional, Type, cast, Union
from randomizer.types.overworld_scripts.action_scripts.classes import (
    ActionScript,
    ActionScriptCommand,
)
from randomizer.types.items.classes import Item

from randomizer.types.scripts_common.classes import (
    IdentifierException,
    Script,
    ScriptBank,
    ScriptBankTooLongException,
    ScriptCommand,
    ScriptCommandBasicShortOperation,
    ScriptCommandNoArgs,
    ScriptCommandShortAddrAndValueOnly,
    ScriptCommandWithJmps,
    ScriptCommandAnySizeMem,
    ScriptCommandShortMem,
)
from randomizer.types.overworld_scripts.constants.classes import AreaObject
from randomizer.types.overworld_scripts.event_scripts.constants.misc import (
    TOTAL_SCRIPTS,
)
from randomizer.types.numbers.classes import UInt16, UInt8
from randomizer.types.overworld_scripts.variables.classes import ShortVar, ByteVar
from randomizer.types.overworld_scripts.variables.variables import PRIMARY_TEMP_7000


class EventScriptCommand(ScriptCommand):
    """Base class for any command in an event script."""


class EventScriptCommandWithJmps(EventScriptCommand, ScriptCommandWithJmps):
    """Base class for any command in an event script that contains at least one goto."""


class EventScriptCommandNoArgs(EventScriptCommand, ScriptCommandNoArgs):
    """Base class for any command in an event script that takes no arguments."""


class EventScriptCommandAnySizeMem(EventScriptCommand, ScriptCommandAnySizeMem):
    """Base class for any command in an event script that can accept either an
    8 bit or 16 bit var."""

    def __init__(
        self, address: Union[ByteVar, ShortVar], identifier: Optional[str] = None
    ) -> None:
        super().__init__(address, identifier)

        if self.address == PRIMARY_TEMP_7000:
            self._size = 1
        else:
            self._size = 2


class EventScriptCommandShortMem(EventScriptCommand, ScriptCommandShortMem):
    """Base class for any command in an event script that accepts only
    an 8 bit var."""


class EventScriptCommandShortAddrAndValueOnly(
    EventScriptCommand, ScriptCommandShortAddrAndValueOnly
):
    """Base class for any command in an event script that accepts
    an 8 bit var and a literal value (either a number or an item class)."""

    def __init__(
        self,
        address: ShortVar,
        value: Union[int, Type[Item]],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(address, value, identifier)

        if self.address == PRIMARY_TEMP_7000:
            self._size = 3
        else:
            self._size = 4


class EventScriptCommandBasicShortOperation(
    EventScriptCommand, ScriptCommandBasicShortOperation
):
    """Base class for any command in an event script that performs math
    on an 8 bit var."""


class EventScriptCommandActionScriptContainer(EventScriptCommand):
    """Base class for commands in an event script that includes
    and runs a NPC action script."""

    _header_size: int
    _subscript: ActionScript

    @property
    def header_size(self) -> int:
        """The expected size of the bytes indicating information about
        the subscript before the subscript contents begin."""
        return self._header_size

    @property
    def subscript(self) -> ActionScript:
        """The contents of the NPC action script that this command runs."""
        return self._subscript

    @property
    def size(self) -> int:
        """The length of this command as a whole."""
        return self.header_size + self.subscript.length


class Subscript(ActionScript):
    """Base class for an action script to be used as typing for
    action command subscripts inside event commands. This is specifically
    intended for commands whose subscript must be 127 bytes in length or
    shorter."""

    def _insert(self, index: int, command: ActionScriptCommand) -> None:
        assert self.length + command.size <= 0x7F
        super()._insert(index, command)

    def set_contents(self, script: Optional[List[ActionScriptCommand]] = None) -> None:
        """Overwrite the contents of the action script command list."""
        if script is None:
            script = []
        contents_length = sum(cast(List[int], [c.size for c in script]))
        assert contents_length <= 0x7F
        super().set_contents(script)


class ActionSubcriptCommandPrototype(EventScriptCommandActionScriptContainer):
    """Base class for action queues, must be 127 bytes or less."""

    _target: AreaObject
    _sync: bool
    _subscript: Subscript
    _header_size: int = 2

    @property
    def target(self) -> AreaObject:
        """The field NPC that this queue should run on."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the field NPC that this queue should run on."""
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
    def subscript(self) -> Subscript:
        """The collection of NPC action script commands to be run."""
        return self._subscript

    def set_subscript(self, subscript: List[ActionScriptCommand]) -> None:
        """Overwrite the collection of NPC action script commands to be run."""
        self.subscript.set_contents(subscript)

    def __init__(
        self,
        target: AreaObject,
        sync: bool = False,
        subscript: Optional[List[ActionScriptCommand]] = None,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_target(target)
        self.set_sync(sync)
        if subscript is None:
            subscript = []
        self.set_subscript(subscript)


class ActionQueuePrototype(ActionSubcriptCommandPrototype):
    """Base class for action queues, must be 127 bytes or less.
    Cannot be forcibly stopped, overall command length is shorter."""

    def render(self) -> bytearray:
        header_byte: UInt8 = UInt8(self.subscript.length + ((not self.sync) << 7))
        return super().render(self.target, header_byte, self.subscript.render())


class StartEmbeddedActionScriptPrototype(ActionSubcriptCommandPrototype):
    """Base class for action queues, must be 127 bytes or less.
    Can be forcibly stopped, overall command length is longer."""

    _prefix: UInt8
    _header_size: int = 3

    @property
    def prefix(self) -> UInt8:
        """(unknown, but must be 0xF0 or 0xF1)"""
        return self._prefix

    def set_prefix(self, prefix: int) -> None:
        """(unknown, but must be 0xF0 or 0xF1)"""
        assert prefix in [0xF0, 0xF1]
        self._prefix = UInt8(prefix)

    def __init__(
        self,
        target: AreaObject,
        prefix: int,
        sync: bool = False,
        subscript: Optional[List[ActionScriptCommand]] = None,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(target, sync, subscript, identifier)
        self.set_prefix(prefix)

    def render(self) -> bytearray:
        header_byte: UInt8 = UInt8(self.subscript.length + ((not self.sync) << 7))
        return super().render(
            self.target, self.prefix, header_byte, self.subscript.render()
        )


class NonEmbeddedActionQueuePrototype(EventScriptCommandActionScriptContainer):
    """Non-embedded action queues are commands representing code that the game
    runs as an action script instead of an event script.\n
    When assembled, these queues contain no header to indicate where they begin.
    The game understands  where these scripts are intended to begin via ASM that
    exists outside of the scope of the script bank.\n"""

    _subscript: ActionScript
    _header_size: int = 0

    @property
    def subscript(self) -> ActionScript:
        """The contents to be run by this queue."""
        return self._subscript

    def set_subscript(self, subscript: List[ActionScriptCommand]) -> None:
        """Overwrite the contents to be run by this queue."""
        self.subscript.set_contents(subscript)

    def __init__(
        self,
        subscript: Optional[List[ActionScriptCommand]],
        identifier: Optional[str] = None,
    ) -> None:
        if subscript is None:
            subscript = []
        super().__init__(identifier)
        self._subscript = Subscript()
        self.set_subscript(subscript)

    def render(self) -> bytearray:
        return super().render(self.subscript.render())


class EventScript(Script[EventScriptCommand]):
    """Base class for a single event script, a list of script command subclasses."""

    _contents: List[EventScriptCommand]

    @property
    def contents(self) -> List[EventScriptCommand]:
        return self._contents

    def append(self, command: EventScriptCommand) -> None:
        super().append(command)

    def extend(self, commands: List[EventScriptCommand]) -> None:
        super().extend(commands)

    def set_contents(self, script: Optional[List[EventScriptCommand]] = None) -> None:
        super().set_contents(script)

    def __init__(self, script: Optional[List[EventScriptCommand]] = None) -> None:
        super().__init__(script)

    def insert_before_nth_command(
        self, index: int, command: EventScriptCommand
    ) -> None:
        super().insert_before_nth_command(index, command)

    def insert_after_nth_command(self, index: int, command: EventScriptCommand) -> None:
        super().insert_after_nth_command(index, command)

    def insert_before_nth_command_of_type(
        self,
        ordinality: int,
        cls: Type[EventScriptCommand],
        command: EventScriptCommand,
    ) -> None:
        super().insert_before_nth_command_of_type(ordinality, cls, command)

    def insert_after_nth_command_of_type(
        self,
        ordinality: int,
        cls: Type[EventScriptCommand],
        command: EventScriptCommand,
    ) -> None:
        super().insert_after_nth_command_of_type(ordinality, cls, command)

    def insert_before_identifier(
        self, identifier: str, command: EventScriptCommand
    ) -> None:
        super().insert_before_identifier(identifier, command)

    def insert_after_identifier(
        self, identifier: str, command: EventScriptCommand
    ) -> None:
        super().insert_after_identifier(identifier, command)

    def replace_at_index(self, index: int, content: EventScriptCommand) -> None:
        super().replace_at_index(index, content)


class EventScriptBank(ScriptBank[EventScript]):
    """Base class for a collection of NPC action scripts
    that should belong to the same $##xxxx bank (1E, 1F, or 20)."""

    _scripts: List[EventScript]
    _pointer_table_start: int
    _start: int
    _end: int

    @property
    def pointer_table_start(self) -> int:
        """The beginning address for this bank's pointer table."""
        return self._pointer_table_start

    def set_pointer_table_start(self, pointer_table_start: int) -> None:
        """Set the beginning address for this bank's pointer table."""
        self._pointer_table_start = pointer_table_start

    @property
    def start(self) -> int:
        """The beginning address for this bank's scripts content, indexed by the
        pointer table."""
        return self._start

    def set_start(self, start: int) -> None:
        """Set the beginning address for this bank's scripts content, indexed by the
        pointer table."""
        self._start = start

    @property
    def end(self) -> int:
        """The address at which this bank's scripts should have finished by."""
        return self._end

    def set_end(self, end: int) -> None:
        """Set the address at which this bank's scripts should have finished by."""
        self._end = end

    @property
    def script_count(self) -> UInt16:
        """The total number of scripts included in this bank."""
        return UInt16((self.start - self.pointer_table_start) // 2)

    @property
    def scripts(self) -> List[EventScript]:
        return self._scripts

    def set_contents(self, scripts: Optional[List[EventScript]] = None) -> None:
        if scripts is None:
            scripts = []
        assert len(scripts) == self.script_count
        super().set_contents(scripts)

    def replace_script(self, index: int, script: EventScript) -> None:
        assert 0 <= index < self.script_count
        super().replace_script(index, script)

    def __init__(
        self,
        pointer_table_start: int,
        start: int,
        end: int,
        scripts: Optional[List[EventScript]],
    ) -> None:
        self.set_pointer_table_start(pointer_table_start)
        self.set_start(start)
        self.set_end(end)
        super().__init__(scripts)

    def _associate_address(
        self, command: Union[EventScriptCommand, ActionScriptCommand], position: int
    ) -> int:
        key: str = command.identifier.name
        if key in self.addresses:
            raise IdentifierException(f"duplicate command identifier found: {key}")
        self.addresses[key] = position

        if isinstance(command, EventScriptCommandActionScriptContainer):
            position += command.header_size
            action_command: ActionScriptCommand
            for action_command in command.subscript.contents:
                position = self._associate_address(action_command, position)
        else:
            position += command.size

        if position >= self.end:
            raise ScriptBankTooLongException(
                f"command exceeded max bank size: {key} @ {position:06X}"
            )
        return position

    def render(self) -> bytearray:
        """Return this script set as ROM patch data."""
        position: int = self._start

        script: EventScript
        command: EventScriptCommand

        # build command name and pointer table : address table
        for script in self.scripts:
            self.pointer_bytes.extend(UInt16(position & 0xFFFF).little_endian())
            for command in script.contents:
                position = self._associate_address(command, position)

        # replace jump placeholders with addresses
        for script in self.scripts:
            self._populate_jumps(script)
            commands_with_subscripts = [
                cmd
                for cmd in script.contents
                if isinstance(cmd, EventScriptCommandActionScriptContainer)
            ]
            for command in commands_with_subscripts:
                self._populate_jumps(command.subscript)

        # finalize bytes
        for script in self.scripts:
            self.script_bytes.extend(script.render())

        # fill empty bytes
        expected_length: int = self.end - self.start
        final_length: int = len(self.script_bytes)
        if final_length > expected_length:
            raise ScriptBankTooLongException(
                f"event script output too long: got {final_length} expected {expected_length}"
            )
        buffer: List[int] = [0xFF] * (expected_length - final_length)
        self.script_bytes.extend(buffer)

        return self.pointer_bytes + self.script_bytes


class EventScriptController:
    """Contains all event script banks. Allows lookup by identifier in any bank."""

    _banks: List[EventScriptBank]

    @property
    def banks(self) -> List[EventScriptBank]:
        """List of event script banks."""
        return self._banks

    def set_banks(self, banks: List[EventScriptBank]) -> None:
        """Overwrite the list of event script banks."""
        self._banks = banks

    def __init__(self, banks: List[EventScriptBank]):
        assert len(banks) == 3
        assert (
            len(banks[0].scripts) + len(banks[1].scripts) + len(banks[2].scripts)
            == TOTAL_SCRIPTS
        )
        self.set_banks(banks)

    def get_script_by_id(self, script_id: int) -> EventScript:
        """Get one script from any bank by absolute ID.\n
        It is recommended to use event name constants for this."""
        assert 0 <= script_id < TOTAL_SCRIPTS
        bank_0x1e: EventScriptBank = self.banks[0]
        bank_0x1f: EventScriptBank = self.banks[1]
        bank_0x20: EventScriptBank = self.banks[2]
        range_0x1e = range(0, bank_0x1e.script_count)
        range_0x1f = range(
            bank_0x1e.script_count, bank_0x1e.script_count + bank_0x1f.script_count
        )
        range_0x20 = range(
            bank_0x1e.script_count + bank_0x1f.script_count,
            bank_0x1e.script_count + bank_0x1f.script_count + bank_0x20.script_count,
        )
        if script_id in range_0x1e:
            return bank_0x1e.scripts[script_id]
        if script_id in range_0x1f:
            relative_id: int = script_id - range_0x1f[0]
            return bank_0x1f.scripts[relative_id]
        if script_id in range_0x20:
            relative_id: int = script_id - range_0x20[0]
            return bank_0x20.scripts[relative_id]
        raise IdentifierException(f"could not find script id {id} for some reason")
