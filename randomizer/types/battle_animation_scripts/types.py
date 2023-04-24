"""Base classes supporting battle animation script assembly."""

from typing import List, Optional, Dict, Type, Union

from randomizer.types.scripts_common import (
    IdentifierException,
    Script,
    ScriptBank,
    ScriptBankTooLongException,
    TransformableIdentifier,
)
from randomizer.types.numbers import UInt16

from randomizer.types.battle_animation_scripts.commands.types import (
    UsableAnimationScriptCommand,
)


class AnimationScript(Script[UsableAnimationScriptCommand]):
    """Base class for a single animation script, a list of script command subclasses."""

    _contents: List[UsableAnimationScriptCommand] = []

    @property
    def contents(self) -> List[UsableAnimationScriptCommand]:
        return self._contents

    def append(self, command: UsableAnimationScriptCommand) -> None:
        super().append(command)

    def extend(self, commands: List[UsableAnimationScriptCommand]) -> None:
        super().extend(commands)

    def set_contents(
        self, script: Optional[List[UsableAnimationScriptCommand]] = None
    ) -> None:
        super().set_contents(script)

    def __init__(
        self, script: Optional[List[UsableAnimationScriptCommand]] = None
    ) -> None:
        super().__init__(script)

    def insert_before_nth_command(
        self, index: int, command: UsableAnimationScriptCommand
    ) -> None:
        super().insert_before_nth_command(index, command)

    def insert_after_nth_command(
        self, index: int, command: UsableAnimationScriptCommand
    ) -> None:
        super().insert_after_nth_command(index, command)

    def insert_before_nth_command_of_type(
        self,
        ordinality: int,
        cls: Type[UsableAnimationScriptCommand],
        command: UsableAnimationScriptCommand,
    ) -> None:
        super().insert_before_nth_command_of_type(ordinality, cls, command)

    def insert_after_nth_command_of_type(
        self,
        ordinality: int,
        cls: Type[UsableAnimationScriptCommand],
        command: UsableAnimationScriptCommand,
    ) -> None:
        super().insert_after_nth_command_of_type(ordinality, cls, command)

    def insert_before_identifier(
        self, identifier: str, command: UsableAnimationScriptCommand
    ) -> None:
        super().insert_before_identifier(identifier, command)

    def insert_after_identifier(
        self, identifier: str, command: UsableAnimationScriptCommand
    ) -> None:
        super().insert_after_identifier(identifier, command)

    def replace_at_index(
        self, index: int, content: UsableAnimationScriptCommand
    ) -> None:
        super().replace_at_index(index, content)

    def render(self, _: Optional[int] = None) -> bytearray:
        output = bytearray()
        command: UsableAnimationScriptCommand
        for command in self._contents:
            output += command.render()
        return output


class BattleAnimationScript(AnimationScript):
    """Special base battle animation script class for battle event cutscenes."""

    _header: List[TransformableIdentifier]

    @property
    def header(self) -> List[TransformableIdentifier]:
        """A list of gotos that are important to this script."""
        return self._header

    @property
    def header_size(self) -> int:
        """The length of the header gotos, used for script rendering purposes."""
        return len(self._header) * 2 + 2

    def __init__(
        self,
        header: Optional[List[str]] = None,
        script: Optional[List[UsableAnimationScriptCommand]] = None,
    ) -> None:
        if header is None:
            header = []
        self._header = [TransformableIdentifier(identifier) for identifier in header]
        super().__init__(script)

    def render(self, position: Optional[int] = None) -> bytearray:
        if position is None:
            raise ValueError
        true_address: bytearray = UInt16(
            (position & 0xFFFF) + 2 + len(self._header)
        ).little_endian()
        header: bytearray = bytearray()
        for dest in self.header:
            header += dest.render_address()
        return true_address + header + super().render()


class SubroutineOrBanklessScript(AnimationScript):
    """Base class for scripts that don't belong to banks, where banks
    typically consist of multiple scripts indicated by ID. This class is
    appropriate for subroutines, or scripts without an ID-separated bank
    such as monster behaviours or Toad tutorials."""

    _expected_size: int = 0

    @property
    def expected_size(self) -> int:
        """The length of bytes that this script should ultimately equal when compiled."""
        return self._expected_size

    def __init__(
        self,
        expected_size: int,
        script: Optional[List[UsableAnimationScriptCommand]] = None,
    ) -> None:
        self._expected_size = expected_size
        super().__init__(script)

    def render(self) -> bytearray:
        output = super().render()
        # These HAVE to match the original size. We can't fuck around with subroutines too much
        assert len(output) == self.expected_size
        return output


class AnimationScriptBank(ScriptBank[AnimationScript]):
    """Base class for a collection of scripts that belong to the same bank (ie 0x##0000)
    and are separated by IDs."""

    _scripts: List[Union[AnimationScript, BattleAnimationScript]]
    _pointer_table_start: int
    _start: int
    _end: int
    _name: str

    @property
    def pointer_table_start(self) -> int:
        """Address where this bank's pointer table starts. The pointer table
        contains a list of 2-byte little endian pointers that indicate where
        individual scripts start. i.e. the pointer at index 2 in this table
        corresponds to the start of the script having ID 2 (0-based indexing)."""
        return self._pointer_table_start

    def set_pointer_table_start(self, pointer_table_start: int) -> None:
        """Sets the address where this bank's pointer table starts."""
        self._pointer_table_start = pointer_table_start

    @property
    def start(self) -> int:
        return self._start

    def set_start(self, start: int) -> None:
        """Sets the address where rendered scripts should start writing to."""
        self._start = start

    @property
    def end(self) -> int:
        return self._end

    def set_end(self, end: int) -> None:
        """The total length of rendered scripts should not exceed this address."""
        self._end = end

    @property
    def script_count(self) -> UInt16:
        """The number of scripts that the pointer table's size accommodates."""
        return UInt16((self.start - self.pointer_table_start) // 2)

    @property
    def scripts(self) -> List[Union[AnimationScript, BattleAnimationScript]]:
        return self._scripts

    @property
    def name(self) -> str:
        """An arbitrary key for this particular bank. Used to reference and modify
        the contents of this bank externally."""
        return self._name

    def set_name(self, name: str) -> None:
        """Set an arbitrary key for this particular bank. Used to reference and modify
        the contents of this bank externally."""
        self._name = name

    def set_contents(self, scripts: Optional[List[AnimationScript]] = None) -> None:
        """Overwrite the entire list of scripts belonging to this bank."""
        if scripts is None:
            scripts = []
        assert len(scripts) == self.script_count
        super().set_contents(scripts)

    def replace_script(self, index: int, script: AnimationScript) -> None:
        """Overwrite the contents of the script at index n."""
        assert 0 <= index < self.script_count
        super().replace_script(index, script)

    def get_command_by_name(self, identifier: str) -> UsableAnimationScriptCommand:
        """Return a single command whose unique identifier matches the name provided."""
        for script in self._scripts:
            for command in script.contents:
                if command.identifier.name == identifier:
                    return command
        raise IdentifierException(f"{identifier} not found")

    def replace_command_by_name(
        self, identifier: str, contents: UsableAnimationScriptCommand
    ) -> None:
        """Overwrite a single command whose unique identifier matches the name provided."""
        for script_id, script in enumerate(self._scripts):
            for index, command in enumerate(script.contents):
                if command.identifier.name == identifier:
                    self._scripts[script_id].contents[index] = contents
                    return
        raise IdentifierException(f"{identifier} not found")

    def set_addresses(self, addrs: Dict[str, int]) -> None:
        """This should ONLY be used when the parent ScriptBankCollection is rendering
        all of its constituent banks. Replaces the identifier-address dict."""
        self._addresses = addrs

    def __init__(
        self,
        name: str,
        start: int,
        end: int,
        pointer_table_start: int = 0,
        scripts: Optional[List[AnimationScript]] = None,
    ) -> None:
        self.set_pointer_table_start(pointer_table_start)
        self.set_start(start)
        self.set_end(end)
        self.set_name(name)
        super().__init__(scripts)

    def associate_address(
        self, command: UsableAnimationScriptCommand, position: int
    ) -> int:
        """Associates an identifier and an address as a key-value pair in the addresses dict."""
        key: str = command.identifier.name
        if key in self.addresses:
            raise IdentifierException(f"duplicate command identifier found: {key}")
        self.addresses[key] = position

        position += command.size

        if position >= self.end:
            raise IdentifierException(
                f"command exceeded max bank size: {key} @ {position:06x}"
            )
        return position

    def render(self) -> bytearray:
        """Generate the bytes representing the current state of this bank to be written
        to the ROM."""
        position: int = self._start

        script: Union[AnimationScript, BattleAnimationScript]

        # replace jump placeholders with addresses
        for script in self.scripts:
            self._populate_jumps(script)
            if isinstance(script, BattleAnimationScript):
                self._set_identifier_addresses(script.header)

        # finalize bytes
        for script in self.scripts:
            script.contents[0].verify_position(position)
            rendered_script = script.render()
            position += len(rendered_script)
            self.script_bytes.extend(rendered_script)

        # fill empty bytes
        expected_length: int = self.end - self.start
        final_length: int = len(self.script_bytes)
        if final_length > expected_length:
            raise ScriptBankTooLongException(
                f"action script output too long: got {final_length} expected {expected_length}"
            )
        buffer: List[int] = [0xFF] * (expected_length - final_length)
        self.script_bytes.extend(buffer)

        if self.pointer_table_start != 0:
            return self.pointer_bytes + self.script_bytes
        return self.script_bytes


class AnimationScriptBankCollection:
    """The container for all battle animation script banks, and bankless scripts, to be used in
    this seed."""

    _banks: List[AnimationScriptBank]

    @property
    def banks(self) -> List[AnimationScriptBank]:
        """Returns all the banks in the collection."""
        return self._banks

    def get_bank(self, name: str) -> AnimationScriptBank:
        """Get a bank by a unique string identifier."""
        return next(bank for bank in self.banks if bank.name == name)

    def render(self) -> Dict[int, bytearray]:
        """Returns a dict where the keys correspond to the bank names, and the values
        are the bytes rendered of their current state to be written to the ROM."""
        script_bank: AnimationScriptBank
        merged_dicts: Dict[str, int] = {}
        output: Dict[int, bytearray] = {}

        for script_bank in self.banks:
            position: int = script_bank.start

            script: Union[AnimationScript, BattleAnimationScript]
            command: UsableAnimationScriptCommand

            # build command name : address table for ENTIRE bank
            for script in script_bank.scripts:
                if script_bank.pointer_table_start != 0:
                    script_bank.pointer_bytes.extend(
                        UInt16(position & 0xFFFF).little_endian()
                    )
                if isinstance(script, BattleAnimationScript):
                    position += script.header_size
                for command in script.contents:
                    position = script_bank.associate_address(command, position)
                merged_dicts.update(script_bank.addresses)

        for script_bank in self.banks:
            script_bank.set_addresses(merged_dicts)
            output[script_bank.start] = script_bank.render()

        return output

    def __init__(self, banks: List[AnimationScriptBank]) -> None:
        self._banks = banks
