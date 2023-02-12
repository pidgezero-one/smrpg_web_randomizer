from typing import List, Optional, Sequence, Tuple, Type, cast
from randomizer.types.monster_scripts.commands import StartCounterCommands
from randomizer.types.monster_scripts.constants.classes import Target
from randomizer.types.monster_scripts.constants.targets import SELF
from randomizer.types.scripts_common.classes import (
    Script,
    ScriptBank,
    ScriptCommand,
    ScriptCommandNoArgs,
)
from randomizer.types.numbers.classes import UInt16, UInt4


class MonsterScriptCommand(ScriptCommand):
    pass


class MonsterScriptCommandNoArgs(MonsterScriptCommand, ScriptCommandNoArgs):
    pass


class MonsterScriptCommandOneVar(MonsterScriptCommand):

    _variable: int

    @property
    def variable(self) -> int:
        return self._variable

    def set_variable(self, variable: int) -> None:
        assert 0x7EE000 <= variable <= 0x7EE00F
        self._variable = int(variable)

    def render_var(self):
        return UInt4(self.variable & 0x0F)

    def __init__(self, variable: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_variable(variable)


class MonsterScriptCommandOneTarget(MonsterScriptCommand):

    _target: Target

    @property
    def target(self) -> Target:
        return self._target

    def set_target(self, target: Target) -> None:
        self._target = target

    def __init__(self, target: Target, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_target(target)


class MonsterScriptCommandOneTargetLimited(MonsterScriptCommand):

    _target: Target

    @property
    def target(self) -> Target:
        return self._target

    def set_target(self, target: Target) -> None:
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
            byte1 = self.target - 0x12
        return super().render(byte1)


class MonsterScript(Script[MonsterScriptCommand]):
    _contents: List[MonsterScriptCommand]

    @property
    def contents(self) -> List[MonsterScriptCommand]:
        return self._contents

    def append(self, command: MonsterScriptCommand) -> None:
        super().append(command)

    def extend(self, commands: List[MonsterScriptCommand]) -> None:
        super().extend(commands)

    def set_contents(self, script: List[MonsterScriptCommand] = []) -> None:
        super().set_contents(script)

    def __init__(self, script: List[MonsterScriptCommand] = []) -> None:
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

    def delete_at_index(self, index: int) -> None:
        super().delete_at_index(index)


class MonsterScriptBank(ScriptBank[MonsterScript]):
    _scripts: List[MonsterScript]
    _rom_ranges: List[List[int]] = []
    _pointer_table_start: int = 0x3930AA
    _range_1_start: int = 0x3932AA
    _range_1_end: int = 0x3959F4
    _range_2_start: int = 0x39F400
    _range_2_end: int = 0x3A0000

    @property
    def range_1_start(self) -> int:
        return self._range_1_start

    @property
    def range_1_end(self) -> int:
        return self._range_1_end

    @property
    def range_2_start(self) -> int:
        return self._range_2_start

    @property
    def range_2_end(self) -> int:
        return self._range_2_end

    @property
    def script_count(self) -> UInt16:
        return UInt16((self.start - self.pointer_table_start) // 2)

    @property
    def scripts(self) -> List[MonsterScript]:
        return self._scripts

    def set_contents(self, scripts: List[MonsterScript] = []) -> None:
        assert len(scripts) == self.script_count
        super().set_contents(scripts)

    def replace_script(self, n: int, script: MonsterScript) -> None:
        assert 0 <= n < self.script_count
        super().replace_script(n, script)

    def __init__(
        self,
        scripts: List[MonsterScript] = [],
    ) -> None:
        super().__init__(scripts)

    def render(self) -> Tuple[bytearray, bytearray]:

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

            # reuse pointers where possible, i.e. two enemies use the same script (henchmen and non-henchmen)
            rendered_script = script.render()
            if rendered_script in already_rendered:
                existing_script_index = already_rendered.index(rendered_script)
                ptr = already_rendered_ptrs[existing_script_index]
            else:
                script_size = len(rendered_script)
                if position_1 + script_size > self.range_1_end:
                    if position_2 + script_size > self.range_2_end:
                        raise Exception("no room for monster script %i" % script_index)
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
