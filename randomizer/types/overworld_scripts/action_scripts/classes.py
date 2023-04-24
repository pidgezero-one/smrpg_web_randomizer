"""Base classes supporting NPC action script assembly."""

from typing import List, Optional, Type, Dict


from randomizer.types.numbers import UInt16
from randomizer.types.scripts_common import (
    IdentifierException,
    Script,
    ScriptBank,
    ScriptBankTooLongException,
)

from .commands.types import (
    UsableActionScriptCommand,
)
from .ids import (
    TOTAL_SCRIPTS,
)


class ActionScript(Script[UsableActionScriptCommand]):
    """Base class for a single NPC action script, a list of script command subclasses."""

    _contents: List[UsableActionScriptCommand]

    @property
    def contents(self) -> List[UsableActionScriptCommand]:
        return self._contents

    def append(self, command: UsableActionScriptCommand) -> None:
        super().append(command)

    def extend(self, commands: List[UsableActionScriptCommand]) -> None:
        super().extend(commands)

    def set_contents(
        self, script: Optional[List[UsableActionScriptCommand]] = None
    ) -> None:
        super().set_contents(script)

    def __init__(
        self, script: Optional[List[UsableActionScriptCommand]] = None
    ) -> None:
        super().__init__(script)

    def insert_before_nth_command(
        self, index: int, command: UsableActionScriptCommand
    ) -> None:
        super().insert_before_nth_command(index, command)

    def insert_after_nth_command(
        self, index: int, command: UsableActionScriptCommand
    ) -> None:
        super().insert_after_nth_command(index, command)

    def insert_before_nth_command_of_type(
        self,
        ordinality: int,
        cls: Type[UsableActionScriptCommand],
        command: UsableActionScriptCommand,
    ) -> None:
        super().insert_before_nth_command_of_type(ordinality, cls, command)

    def insert_after_nth_command_of_type(
        self,
        ordinality: int,
        cls: Type[UsableActionScriptCommand],
        command: UsableActionScriptCommand,
    ) -> None:
        super().insert_after_nth_command_of_type(ordinality, cls, command)

    def insert_before_identifier(
        self, identifier: str, command: UsableActionScriptCommand
    ) -> None:
        super().insert_before_identifier(identifier, command)

    def insert_after_identifier(
        self, identifier: str, command: UsableActionScriptCommand
    ) -> None:
        super().insert_after_identifier(identifier, command)

    def replace_at_index(self, index: int, content: UsableActionScriptCommand) -> None:
        super().replace_at_index(index, content)


class ActionScriptBank(ScriptBank):
    """Base class for the collection of NPC action scripts."""

    _scripts: List[ActionScript]
    _pointer_table_start: int = 0x210000
    _start: int = 0x210800
    _end: int = 0x21C000

    _addresses: Dict[str, int]
    _pointer_bytes: bytearray
    _script_bytes: bytearray

    @property
    def scripts(self) -> List[ActionScript]:
        return self._scripts

    def set_contents(self, scripts: Optional[List[ActionScript]] = None) -> None:
        if scripts is None:
            scripts = []
        assert len(scripts) == TOTAL_SCRIPTS
        super().set_contents(scripts)

    def replace_script(self, index: int, script: ActionScript) -> None:
        assert 0 <= index < TOTAL_SCRIPTS
        super().replace_script(index, script)

    def __init__(self, scripts: Optional[List[ActionScript]] = None) -> None:
        super().__init__(scripts)

    @property
    def addresses(self) -> Dict[str, int]:
        return self._addresses

    @property
    def pointer_bytes(self) -> bytearray:
        return self._pointer_bytes

    @property
    def script_bytes(self) -> bytearray:
        return self._script_bytes

    def _associate_address(
        self, command: UsableActionScriptCommand, position: int
    ) -> int:
        key: str = command.identifier.name
        if key in self.addresses:
            raise IdentifierException(f"duplicate command identifier found: {key}")
        self.addresses[key] = position

        position += command.size

        if position >= self.end:
            raise ScriptBankTooLongException(
                f"command exceeded max bank size: {key} @ {position:06X}"
            )
        return position

    def render(self) -> bytearray:
        """Return this script set as ROM patch data."""
        position: int = self._start

        script: ActionScript
        command: UsableActionScriptCommand

        # build command name : address table
        for script in self.scripts:
            self.pointer_bytes.extend(UInt16(position & 0xFFFF).little_endian())
            for command in script.contents:
                position = self._associate_address(command, position)

        # replace jump placeholders with addresses
        for script in self.scripts:
            self._populate_jumps(script)

        # finalize bytes
        for script in self.scripts:
            self.script_bytes.extend(script.render())

        # fill empty bytes
        expected_length: int = self.end - self.start
        final_length: int = len(self.script_bytes)
        if final_length > expected_length:
            raise ScriptBankTooLongException(
                f"action script output too long: got {final_length} expected {expected_length}"
            )
        buffer: List[int] = [0xFF] * (expected_length - final_length)
        self.script_bytes.extend(buffer)

        return self.pointer_bytes + self.script_bytes
