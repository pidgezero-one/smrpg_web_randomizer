"""Base classes supporting monster battle script assembly."""

from typing import List, Optional, Tuple, Type

from randomizer.types.numbers.classes import UInt16
from randomizer.types.scripts_common.classes import (
    Script,
    ScriptBank,
    ScriptBankTooLongException,
)

from .commands.types import UsableMonsterScriptCommand
from .commands import StartCounterCommands
from .ids import (
    BANK_RANGE_1_END,
    BANK_RANGE_1_START,
    BANK_RANGE_2_END,
    BANK_RANGE_2_START,
    POINTER_TABLE_START,
)


class MonsterScript(Script[UsableMonsterScriptCommand]):
    """Base class for a single monster battle script, a list of script command subclasses."""

    _contents: List[UsableMonsterScriptCommand]

    @property
    def contents(self) -> List[UsableMonsterScriptCommand]:
        return self._contents

    def append(self, command: UsableMonsterScriptCommand) -> None:
        super().append(command)

    def extend(self, commands: List[UsableMonsterScriptCommand]) -> None:
        super().extend(commands)

    def set_contents(
        self, script: Optional[List[UsableMonsterScriptCommand]] = None
    ) -> None:
        super().set_contents(script)

    def __init__(
        self, script: Optional[List[UsableMonsterScriptCommand]] = None
    ) -> None:
        super().__init__(script)

    def insert_before_nth_command(
        self, index: int, command: UsableMonsterScriptCommand
    ) -> None:
        super().insert_before_nth_command(index, command)

    def insert_after_nth_command(
        self, index: int, command: UsableMonsterScriptCommand
    ) -> None:
        super().insert_after_nth_command(index, command)

    def insert_before_nth_command_of_type(
        self,
        ordinality: int,
        cls: Type[UsableMonsterScriptCommand],
        command: UsableMonsterScriptCommand,
    ) -> None:
        super().insert_before_nth_command_of_type(ordinality, cls, command)

    def insert_after_nth_command_of_type(
        self,
        ordinality: int,
        cls: Type[UsableMonsterScriptCommand],
        command: UsableMonsterScriptCommand,
    ) -> None:
        super().insert_after_nth_command_of_type(ordinality, cls, command)

    def insert_before_identifier(
        self, identifier: str, command: UsableMonsterScriptCommand
    ) -> None:
        super().insert_before_identifier(identifier, command)

    def insert_after_identifier(
        self, identifier: str, command: UsableMonsterScriptCommand
    ) -> None:
        super().insert_after_identifier(identifier, command)

    def replace_at_index(self, index: int, content: UsableMonsterScriptCommand) -> None:
        super().replace_at_index(index, content)


class MonsterScriptBank(ScriptBank[MonsterScript]):
    """Base class for the collection of monster battle scripts.
    Battle scripts are not stored in a contiguous range, but
    rather two separate ranges that share a pointer table."""

    _scripts: List[MonsterScript]
    _rom_ranges: List[List[int]] = []
    _pointer_table_start: int = POINTER_TABLE_START
    _range_1_start: int = BANK_RANGE_1_START
    _range_1_end: int = BANK_RANGE_1_END
    _range_2_start: int = BANK_RANGE_2_START
    _range_2_end: int = BANK_RANGE_2_END

    @property
    def range_1_start(self) -> int:
        """The address at which the first script bank begins."""
        return self._range_1_start

    @property
    def range_1_end(self) -> int:
        """The address at which the first script bank ends."""
        return self._range_1_end

    @property
    def range_2_start(self) -> int:
        """The address at which the second script bank begins."""
        return self._range_2_start

    @property
    def range_2_end(self) -> int:
        """The address at which the second script bank ends."""
        return self._range_2_end

    @property
    def script_count(self) -> UInt16:
        """The expected total number of individual scripts to be included across both ranges."""
        return UInt16((self.start - self.pointer_table_start) // 2)

    @property
    def scripts(self) -> List[MonsterScript]:
        return self._scripts

    def set_contents(self, scripts: Optional[List[MonsterScript]] = None) -> None:
        if scripts is None:
            scripts = []
        assert len(scripts) == self.script_count
        super().set_contents(scripts)

    def replace_script(self, index: int, script: MonsterScript) -> None:
        assert 0 <= index < self.script_count
        super().replace_script(index, script)

    def __init__(
        self,
        scripts: Optional[List[MonsterScript]] = None,
    ) -> None:
        super().__init__(scripts)

    def render(self) -> Tuple[bytearray, bytearray]:
        """Return this script as two bytearrays
        (one per range, the first including the pointer table)
        which are to be included in the ROM patch."""

        script: MonsterScript

        position_1 = self.range_1_start
        position_2 = self.range_2_start

        ptr_bank = bytearray()

        bank_1 = bytearray()
        bank_2 = bytearray()

        already_rendered = [bytearray()] * 256
        already_rendered_ptrs = [bytearray()] * 256

        for script_index, script in enumerate(self.scripts):
            # make sure there is only one section that starts counter commands
            counter_starts = [
                c for c in script.contents if isinstance(c, StartCounterCommands)
            ]
            assert len(counter_starts) <= 1

            # reuse pointers where possible, i.e. two enemies use the same script
            # (henchmen and non-henchmen)
            rendered_script = script.render()
            if rendered_script in already_rendered:
                existing_script_index = already_rendered.index(rendered_script)
                ptr = already_rendered_ptrs[existing_script_index]
            else:
                script_size = len(rendered_script)
                if position_1 + script_size > self.range_1_end:
                    if position_2 + script_size > self.range_2_end:
                        raise ScriptBankTooLongException(
                            f"no room for monster script {script_index}"
                        )
                    position_2 += script_size
                    ptr = UInt16(position_2 & 0xFFFF).little_endian()
                    bank_2 += rendered_script
                else:
                    position_1 += script_size
                    ptr = UInt16(position_1 & 0xFFFF).little_endian()
                    bank_1 += rendered_script
                already_rendered = rendered_script
                already_rendered_ptrs[script_index] = ptr
            ptr_bank += ptr

        expected_size_1 = self.range_1_end - self.range_1_start
        expected_size_2 = self.range_2_end - self.range_2_start

        if len(bank_1) < expected_size_1:
            bank_1 += bytearray([0xFF] * expected_size_1)
        if len(bank_2) < expected_size_2:
            bank_2 += bytearray([0xFF] * expected_size_2)
        assert len(bank_1) == expected_size_1
        assert len(bank_2) == expected_size_2

        return ptr_bank + bank_1, bank_2
