from typing import Optional, cast, Type

from constants.misc import TOTAL_SCRIPTS

from randomizer.types.common.classes import (
    Script,
    ScriptBank,
    ScriptCommand,
    ScriptCommandAnySizeMem,
    ScriptCommandBasicShortOperation,
    ScriptCommandNoArgs,
    ScriptCommandShortAddrAndValueOnly,
    ScriptCommandShortMem,
    ScriptCommandWithJmps,
    TransformableIdentifier,
)
from randomizer.types.numbers.classes import UInt16, UInt8
from randomizer.types.variables import variables


class ActionScriptCommand(ScriptCommand):
    pass


class ActionScriptCommandWithJmps(ActionScriptCommand, ScriptCommandWithJmps):
    pass


class ActionScriptCommandNoArgs(ActionScriptCommand, ScriptCommandNoArgs):
    pass


class ActionScriptCommandAnySizeMem(ActionScriptCommand, ScriptCommandAnySizeMem):
    def __init__(self, address: int, identifier: Optional[str] = None) -> None:
        super().__init__(address, identifier)

        if self.address == variables.PRIMARY_TEMP_700C:
            self._size = 1
        else:
            self._size = 2


class ActionScriptCommandShortMem(ActionScriptCommand, ScriptCommandShortMem):
    pass


class ActionScriptCommandShortAddrAndValueOnly(
    ActionScriptCommand, ScriptCommandShortAddrAndValueOnly
):
    def __init__(
        self, address: int, value: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(address, value, identifier)

        if self.address == variables.PRIMARY_TEMP_700C:
            self._size = 3
        else:
            self._size = 4


class ActionScriptCommandBasicShortOperation(
    ActionScriptCommand, ScriptCommandBasicShortOperation
):
    pass


class ActionScriptCommandByteSteps(ActionScriptCommand):
    _steps: UInt8
    _size: int = 2

    @property
    def steps(self) -> UInt8:
        return self._steps

    def set_steps(self, steps: int) -> None:
        self._steps = UInt8(steps)

    def __init__(self, steps: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_steps(steps)

    def render(self) -> bytearray:
        return super().render(self.steps)


class ActionScriptCommandBytePixels(ActionScriptCommand):
    _pixels: UInt8
    _size: int = 2

    @property
    def pixels(self) -> UInt8:
        return self._pixels

    def set_pixels(self, value: int) -> None:
        self._pixels = UInt8(value)

    def __init__(self, pixels: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_pixels(pixels)

    def render(self) -> bytearray:
        return super().render(self.pixels)


class ActionScriptCommandXYBytes(ActionScriptCommand):
    _size: int = 3
    _x: UInt8
    _y: UInt8

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

    def __init__(self, x: int, y: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_x(x)
        self.set_y(y)

    def render(self) -> bytearray:
        return super().render(self.x, self.y)


class ActionScript(Script):
    _contents: "ActionScriptCommand[int]"

    def _insert(self, n: int, command: ActionScriptCommand) -> None:
        super()._insert(n, command)

    def _get_index_of_nth_command_of_type(
        self, n: int, cls: Type[ActionScriptCommand]
    ) -> int:
        return super()._get_index_of_nth_command_of_type(n, cls)

    @property
    def contents(self) -> "ActionScriptCommand[int]":
        return self._contents

    def set_contents(self, script: "ActionScriptCommand[int]" = []) -> None:
        super().set_contents(script)

    def __init__(self, script: "ActionScriptCommand[int]" = []) -> None:
        super().__init__(script)

    @property
    def length(self) -> int:
        return sum(cast("int[int]", [c.size for c in self.contents]))

    def insert_before_nth_command(self, n: int, command: ActionScriptCommand) -> None:
        super().insert_before_nth_command(n, command)

    def insert_after_nth_command(self, n: int, command: ActionScriptCommand) -> None:
        super().insert_after_nth_command(n, command)

    def insert_before_nth_command_of_type(
        self, n: int, cls: Type[ActionScriptCommand], command: ActionScriptCommand
    ) -> None:
        super().insert_before_nth_command_of_type(n, cls, command)

    def insert_after_nth_command_of_type(
        self, n: int, cls: Type[ActionScriptCommand], command: ActionScriptCommand
    ) -> None:
        super().insert_after_nth_command_of_type(n, cls, command)

    def insert_before_identifier(
        self, identifier: str, command: ActionScriptCommand
    ) -> None:
        super().insert_before_identifier(identifier, command)

    def insert_after_identifier(
        self, identifier: str, command: ActionScriptCommand
    ) -> None:
        super().insert_after_identifier(identifier, command)


class ActionScriptBank(ScriptBank):
    _scripts: "ActionScript[int]"
    _pointer_table_start: int = 0x210000
    _start: int = 0x210800
    _end: int = 0x21C000

    @property
    def scripts(self) -> "ActionScript[int]":
        return self._scripts

    def set_contents(self, scripts: "ActionScript[int]" = []) -> None:
        assert len(scripts) == TOTAL_SCRIPTS
        super().set_contents(scripts)

    def replace_script(self, n: int, script: ActionScript) -> None:
        assert 0 <= n < TOTAL_SCRIPTS
        super().replace_script(script)

    def __init__(self, script: "ActionScript[int]" = []) -> None:
        super().__init__(script)

    def render(self) -> bytearray:
        addresses: dict[str, int] = {}
        position: self._start
        pointer_bytes = bytearray()
        script_bytes = bytearray()

        script: ActionScript
        command: ActionScriptCommand
        destination: TransformableIdentifier

        # build command name : address table
        for script in self.scripts:
            pointer_bytes.extend(UInt16(position & 0xFFFF).little_endian())
            for command in script:
                addresses[command.identifier.name] = position
                position += command.size

        # replace jump placeholders with addresses
        for script in self.scripts:
            for command in script:
                if isinstance(command, ActionScriptCommandWithJmps):
                    for destination in command.destinations:
                        key: str = destination.name
                        if key not in addresses:
                            raise Exception(
                                "couldn't find destination %s in %s"
                                % (key, command.identifier.name)
                            )
                        destination.set_address(addresses[key] % 0xFFFF)

        # finalize bytes
        for script in self.scripts:
            script_bytes.extend(script.render())

        # fill empty bytes
        expected_length: int = self.end - self.start
        final_length: int = len(script_bytes)
        if final_length > expected_length:
            raise Exception(
                "action script output too long: got %s expected %s"
                % (final_length, expected_length)
            )
        buffer: "int[int]" = [0xFF] * expected_length - final_length
        script_bytes.extend(bytearray(buffer))

        return pointer_bytes + script_bytes
