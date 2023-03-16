"""Base classes supporting monster battle script assembly."""

from typing import List, Optional, Tuple, Type
from randomizer.types.monster_scripts.commands import StartCounterCommands
from randomizer.types.monster_scripts.constants.classes import Target
from randomizer.types.monster_scripts.constants.misc import (
    BANK_RANGE_1_END,
    BANK_RANGE_1_START,
    BANK_RANGE_2_END,
    BANK_RANGE_2_START,
    POINTER_TABLE_START,
)
from randomizer.types.monster_scripts.constants.targets import SELF
from randomizer.types.scripts_common.classes import (
    Script,
    ScriptBank,
    ScriptBankTooLongException,
    ScriptCommand,
    ScriptCommandNoArgs,
)
from randomizer.types.numbers.classes import UInt16, UInt4, UInt8


class MonsterScriptCommand(ScriptCommand):
    """Base class for any command in a monster's battle script."""


class MonsterScriptCommandNoArgs(MonsterScriptCommand, ScriptCommandNoArgs):
    """Base class for any command in a monster's battle script that takes no arguments."""


class MonsterScriptCommandOneVar(MonsterScriptCommand):
    """Base class for any command in a monster's battle script that takes one 0x7EE00X variable."""

    _variable: int

    @property
    def variable(self) -> int:
        """The 0x7EE00X variable used by this command."""
        return self._variable

    def set_variable(self, variable: int) -> None:
        """Designate the 0x7EE00X variable that is to be used by this command."""
        assert 0x7EE000 <= variable <= 0x7EE00F
        self._variable = int(variable)

    def render_var(self):
        """Get the representation of this variable as a patch byte."""
        return UInt4(self.variable & 0x0F)

    def __init__(self, variable: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_variable(variable)


class MonsterScriptCommandOneTarget(MonsterScriptCommand):
    """Base class for any command in a monster's battle script that has one target."""

    _target: Target

    @property
    def target(self) -> Target:
        """The target to be.... targeted.... by this command"""
        return self._target

    def set_target(self, target: Target) -> None:
        """Designate this command's target"""
        self._target = target

    def __init__(self, target: Target, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_target(target)


class MonsterScriptCommandOneTargetLimited(MonsterScriptCommand):
    """Base class for any command that takes one target, where the target value can only
    fall within the range of targets beginning with MONSTER_1_SET and ending with SELF."""

    _target: Target

    @property
    def target(self) -> Target:
        """The target to be.... targeted.... by this command"""
        return self._target

    def set_target(self, target: Target) -> None:
        """Designate this command's target"""
        assert 0x13 <= target <= 0x1B
        self._target = target

    def __init__(self, target: Target, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self) -> bytearray:
        byte1: int
        if self.target == SELF:
            byte1 = 0
        else:
            byte1 = UInt8(self.target - 0x12)
        return super().render(byte1)


class MonsterScript(Script[MonsterScriptCommand]):
    """Base class for a single monster battle script, a list of script command subclasses."""

    _contents: List[MonsterScriptCommand]

    @property
    def contents(self) -> List[MonsterScriptCommand]:
        return self._contents

    def append(self, command: MonsterScriptCommand) -> None:
        super().append(command)

    def extend(self, commands: List[MonsterScriptCommand]) -> None:
        super().extend(commands)

    def set_contents(self, script: Optional[List[MonsterScriptCommand]] = None) -> None:
        super().set_contents(script)

    def __init__(self, script: Optional[List[MonsterScriptCommand]] = None) -> None:
        super().__init__(script)

    def insert_before_nth_command(self, n: int, command: MonsterScriptCommand) -> None:
        super().insert_before_nth_command(n, command)

    def insert_after_nth_command(self, n: int, command: MonsterScriptCommand) -> None:
        super().insert_after_nth_command(n, command)

    def insert_before_nth_command_of_type(
        self, n: int, cls: Type[MonsterScriptCommand], command: MonsterScriptCommand
    ) -> None:
        super().insert_before_nth_command_of_type(n, cls, command)

    def insert_after_nth_command_of_type(
        self, n: int, cls: Type[MonsterScriptCommand], command: MonsterScriptCommand
    ) -> None:
        super().insert_after_nth_command_of_type(n, cls, command)

    def insert_before_identifier(
        self, identifier: str, command: MonsterScriptCommand
    ) -> None:
        super().insert_before_identifier(identifier, command)

    def insert_after_identifier(
        self, identifier: str, command: MonsterScriptCommand
    ) -> None:
        super().insert_after_identifier(identifier, command)

    def replace_at_index(self, index: int, content: MonsterScriptCommand) -> None:
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

    def replace_script(self, n: int, script: MonsterScript) -> None:
        assert 0 <= n < self.script_count
        super().replace_script(n, script)

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
                    else:
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
