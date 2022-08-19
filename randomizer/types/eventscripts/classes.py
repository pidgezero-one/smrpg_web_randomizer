from typing import Optional, Type, cast, Union
from randomizer.types.actionscripts.classes import ActionScript, ActionScriptCommand

from randomizer.types.common.classes import (
    Script,
    ScriptBank,
    ScriptCommand,
    ScriptCommandBasicShortOperation,
    ScriptCommandNoArgs,
    ScriptCommandShortAddrAndValueOnly,
    ScriptCommandWithJmps,
    ScriptCommandAnySizeMem,
    ScriptCommandShortMem,
)
from randomizer.types.constants.classes import AreaObject
from randomizer.types.eventscripts.constants.misc import TOTAL_SCRIPTS
from randomizer.types.numbers.classes import UInt16, UInt8
from randomizer.types.variables.classes import ShortVar, ByteVar
from randomizer.types.variables import variables


class EventScriptCommand(ScriptCommand):
    pass


class EventScriptCommandNoArgs(EventScriptCommand, ScriptCommandNoArgs):
    pass


class EventScriptCommandWithJmps(EventScriptCommand, ScriptCommandWithJmps):
    pass


class EventScriptCommandAnySizeMem(EventScriptCommand, ScriptCommandAnySizeMem):
    def __init__(
        self, address: Union[ByteVar, ShortVar], identifier: Optional[str] = None
    ) -> None:
        super().__init__(address, identifier)

        if self.address == variables.PRIMARY_TEMP_7000:
            self._size = 1
        else:
            self._size = 2


class EventScriptCommandShortMem(EventScriptCommand, ScriptCommandShortMem):
    pass


class EventScriptCommandShortAddrAndValueOnly(
    EventScriptCommand, ScriptCommandShortAddrAndValueOnly
):
    def __init__(
        self,
        address: Union[ByteVar, ShortVar],
        value: int,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(address, value, identifier)

        if self.address == variables.PRIMARY_TEMP_7000:
            self._size = 3
        else:
            self._size = 4


class EventScriptCommandBasicShortOperation(
    EventScriptCommand, ScriptCommandBasicShortOperation
):
    pass


class EventScriptCommandActionScriptContainer(EventScriptCommand):
    _header_size: int
    _subscript: ActionScript

    @property
    def header_size(self) -> int:
        return self._header_size

    @property
    def subscript(self) -> ActionScript:
        return self._subscript

    @property
    def size(self) -> int:
        return self.header_size + self.subscript.length


class Subscript(ActionScript):
    def _insert(self, n: int, command: ActionScriptCommand) -> None:
        assert self.length + command.size <= 0x7F
        super()._insert(n, command)

    def set_contents(self, script: "ActionScriptCommand[int]" = []) -> None:
        contents_length = sum(cast("int[int]", [c.size for c in script]))
        assert contents_length <= 0x7F
        super().set_contents(script)


class ActionQueueSubscript(Subscript):
    _sync: bool

    @property
    def sync(self) -> bool:
        return self._sync

    def set_sync(self, sync: bool) -> None:
        self._sync = sync

    def __init__(self, sync: bool, script: "ActionScript[int]" = []) -> None:
        self.set_sync(sync)
        super().__init__(script)

    @staticmethod
    def _header_byte(sync: bool, size: int) -> UInt8:
        return UInt8(size + ((not sync) << 7))

    def _insert(self, n: int, command: ActionScriptCommand) -> None:
        assert self._header_byte(self.sync, self.length + command.size) < 0xF0
        super()._insert(n, command)

    def set_contents(self, script: "ActionScriptCommand[int]" = []) -> None:
        contents_length = sum(cast("int[int]", [c.size for c in script]))
        assert self._header_byte(self.sync, contents_length) < 0xF0
        super().set_contents(script)


class ActionQueuePrototype(EventScriptCommandActionScriptContainer):
    _target: AreaObject
    _sync: bool
    _subscript: ActionQueueSubscript
    _header_size: int = 2

    @property
    def target(self) -> AreaObject:
        return self._target

    def set_target(self, target: AreaObject) -> None:
        self._target = target

    @property
    def sync(self) -> bool:
        return self._sync

    def set_sync(self, sync: bool) -> None:
        self.subscript.set_sync(sync)
        self._sync = sync

    @property
    def subscript(self) -> ActionQueueSubscript:
        return self._subscript

    def set_subscript(self, subscript: "ActionScriptCommand[int]") -> None:
        self.subscript.set_contents(subscript)

    def __init__(
        self,
        target: AreaObject,
        sync: bool = False,
        subscript: "ActionScriptCommand[int]" = [],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.subscript = ActionQueueSubscript()
        self.set_target(target)
        self.set_sync(sync)
        self.set_subscript(subscript)

    def render(self) -> bytearray:
        header_byte: UInt8 = UInt8(self.subscript.length + ((not self.sync) << 7))
        return super().render(self.target, header_byte, self.subscript.render())


class StartEmbeddedActionScriptPrototype(EventScriptCommandActionScriptContainer):
    _target: AreaObject
    _sync: bool
    _prefix: UInt8
    _subscript: Subscript
    _header_size: int = 3

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
    def prefix(self) -> UInt8:
        return self._prefix

    def set_prefix(self, prefix: int) -> None:
        assert prefix in [0xF0, 0xF1]
        self._prefix = UInt8(prefix)

    @property
    def subscript(self) -> Subscript:
        return self._subscript

    def set_subscript(self, subscript: "ActionScriptCommand[int]") -> None:
        self.subscript.set_contents(subscript)

    def __init__(
        self,
        target: AreaObject,
        prefix: int,
        sync: bool = False,
        subscript: "ActionScriptCommand[int]" = [],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.subscript = Subscript()
        self.set_target(target)
        self.set_prefix(prefix)
        self.set_sync(sync)
        self.set_subscript(subscript)

    def render(self) -> bytearray:
        header_byte: UInt8 = UInt8(self.subscript.length + ((not self.sync) << 7))
        return super().render(
            self.target, self.prefix, header_byte, self.subscript.render()
        )


class NonEmbeddedActionQueuePrototype(EventScriptCommandActionScriptContainer):
    _subscript: ActionScript
    _header_size: int = 0

    @property
    def subscript(self) -> ActionScript:
        return self._subscript

    def set_subscript(self, subscript: "ActionScriptCommand[int]") -> None:
        self.subscript.set_contents(subscript)

    def __init__(
        self,
        subscript: "ActionScriptCommand[int]" = [],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.subscript = Subscript()
        self.set_subscript(subscript)

    def render(self) -> bytearray:
        return super().render(self.subscript.render())


class EventScript(Script):
    _contents: "EventScriptCommand[int]"

    def _insert(self, n: int, command: EventScriptCommand) -> None:
        super()._insert(n, command)

    def _get_index_of_nth_command_of_type(
        self, n: int, cls: Type[EventScriptCommand]
    ) -> int:
        return super()._get_index_of_nth_command_of_type(n, cls)

    @property
    def contents(self) -> "EventScriptCommand[int]":
        return self._contents

    def set_contents(self, script: "EventScriptCommand[int]" = []) -> None:
        super().set_contents(script)

    def __init__(self, script: "EventScriptCommand[int]" = []) -> None:
        super().__init__(script)

    @property
    def length(self) -> int:
        return sum(cast("int[int]", [c.size for c in self.contents]))

    def insert_before_nth_command(self, n: int, command: EventScriptCommand) -> None:
        super().insert_before_nth_command(n, command)

    def insert_after_nth_command(self, n: int, command: EventScriptCommand) -> None:
        super().insert_after_nth_command(n, command)

    def insert_before_nth_command_of_type(
        self, n: int, cls: Type[EventScriptCommand], command: EventScriptCommand
    ) -> None:
        super().insert_before_nth_command_of_type(n, cls, command)

    def insert_after_nth_command_of_type(
        self, n: int, cls: Type[EventScriptCommand], command: EventScriptCommand
    ) -> None:
        super().insert_after_nth_command_of_type(n, cls, command)

    def insert_before_identifier(
        self, identifier: str, command: EventScriptCommand
    ) -> None:
        super().insert_before_identifier(identifier, command)

    def insert_after_identifier(
        self, identifier: str, command: EventScriptCommand
    ) -> None:
        super().insert_after_identifier(identifier, command)


class EventScriptBank(ScriptBank):
    _scripts: "EventScript[int]"
    _pointer_table_start: int
    _start: int
    _end: int

    @property
    def pointer_table_start(self) -> int:
        return self._pointer_table_start

    def set_pointer_table_start(self, pointer_table_start: int) -> None:
        self._pointer_table_start = pointer_table_start

    @property
    def start(self) -> int:
        return self._start

    def set_start(self, start: int) -> None:
        self._start = start

    @property
    def end(self) -> int:
        return self._end

    def set_end(self, end: int) -> None:
        self._end = end

    @property
    def script_count(self) -> UInt16:
        return (self.start - self.pointer_table_start) // 2

    @property
    def scripts(self) -> "EventScript[int]":
        return self._scripts

    def set_contents(self, scripts: "EventScript[int]" = []) -> None:
        assert len(scripts) == self.script_count
        super().set_contents(scripts)

    def replace_script(self, n: int, script: EventScript) -> None:
        assert 0 <= n < self.script_count
        super().replace_script(script)

    def __init__(
        self,
        pointer_table_start: int,
        start: int,
        end: int,
        script: "EventScript[int]" = [],
    ) -> None:
        self.set_pointer_table_start(pointer_table_start)
        self.set_start(start)
        self.set_end(end)
        super().__init__(script)

    def _associate_address(
        self, command: Union[EventScriptCommand, ActionScriptCommand], position: int
    ) -> int:

        key: str = command.identifier.name
        if key in self.addresses:
            raise Exception("duplicate command identifier found: %s" % key)
        self.addresses[key] = position

        if isinstance(command, EventScriptCommandActionScriptContainer):
            position += command.header_size
            action_command: ActionScriptCommand
            for action_command in command.subscript:
                position = self._associate_address(action_command, position)
        else:
            position += command.size

        if position >= self.end:
            raise Exception(
                "command exceeded max bank size: %s @ %06x" % (key, position)
            )
        return position

    def render(self) -> bytearray:
        position: int = self._start

        script: EventScript
        command: EventScriptCommand

        # build command name and pointer table : address table
        for script in self.scripts:
            self.pointer_bytes.extend(UInt16(position & 0xFFFF).little_endian())
            for command in script:
                position = self._associate_address(command, position)

        # replace jump placeholders with addresses
        for script in self.scripts:
            self._populate_jumps(script)
            commands_with_subscripts = [
                cmd
                for cmd in script
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
            raise Exception(
                "Event script output too long: got %s expected %s"
                % (final_length, expected_length)
            )
        buffer: "int[int]" = [0xFF] * expected_length - final_length
        self.script_bytes.extend(buffer)

        return self.pointer_bytes + self.script_bytes


class EventScriptController:
    _banks: "EventScriptBank[int]"

    @property
    def banks(self) -> "EventScriptBank[int]":
        return self._banks

    def set_banks(self, banks: "EventScriptBank[int]") -> None:
        self._banks = banks

    def __init__(self):
        bank_0x1E = EventScriptBank(0x1E0000, 0x1E0C00, 0x1F0000)
        bank_0x1F = EventScriptBank(0x1F0000, 0x1F0C00, 0x200000)
        bank_0x20 = EventScriptBank(0x200000, 0x200800, 0x20E000)
        banks: "EventScriptBank[int]" = [bank_0x1E, bank_0x1F, bank_0x20]
        self.set_banks(banks)

    def get_script_by_id(self, id: int) -> EventScript:
        assert 0 <= id < TOTAL_SCRIPTS
        bank_0x1E: EventScriptBank = self.banks[0]
        bank_0x1F: EventScriptBank = self.banks[1]
        bank_0x20: EventScriptBank = self.banks[2]
        range_0x1E = range(0, bank_0x1E.script_count)
        range_0x1F = range(
            bank_0x1E.script_count, bank_0x1E.script_count + bank_0x1F.script_count
        )
        range_0x20 = range(
            bank_0x1E.script_count + bank_0x1F.script_count,
            bank_0x1E.script_count + bank_0x1F.script_count + bank_0x20.script_count,
        )
        if id in range_0x1E:
            return bank_0x1E.scripts[id]
        elif id in range_0x1F:
            relative_id: int = id - range_0x1F[0]
            return bank_0x1F.scripts[relative_id]
        elif id in range_0x20:
            relative_id: int = id - range_0x20[0]
            return bank_0x20.scripts[relative_id]
        else:
            raise Exception("could not find script id %i for some reason" % id)
