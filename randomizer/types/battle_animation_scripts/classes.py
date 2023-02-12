from typing import List, Optional, Dict, Type, Union
from randomizer.types.items.classes import Item
from randomizer.types.scripts_common.classes import (
    Script,
    ScriptBank,
    ScriptCommand,
    ScriptCommandNoArgs,
    ScriptCommandWithJmps,
    TransformableIdentifier,
)
from randomizer.types.numbers.classes import Int16, UInt16, UInt8
from .constants.classes import Origin


class AnimationScriptCommand(ScriptCommand):
    def verify_position(self, position: int) -> None:
        if "queuestart_" in self.identifier.name:
            chunks = "_".split(self.identifier.name)
            if len(chunks) == 2:
                try:
                    expected_addr: int = int(chunks[1], 16)
                    if expected_addr != position:
                        print(
                            "warning: %s has moved to 0x%06X"
                            % (self.identifier.name, position)
                        )
                except:
                    pass


class AnimationScriptCommandNoArgs(AnimationScriptCommand, ScriptCommandNoArgs):
    pass


class AnimationScriptCommandWithJmps(AnimationScriptCommand, ScriptCommandWithJmps):
    pass


class AnimationScriptAMEMCommand(AnimationScriptCommand):
    _amem: UInt8

    @property
    def amem(self) -> UInt8:
        return self._amem

    def set_amem(self, amem: int) -> None:
        assert 0x60 <= amem <= 0x6F
        self._amem = UInt8(amem)

    def _amem_bits(self) -> int:
        return self.amem & 0x0F


class AnimationScriptAMEM6XSoloCommand(AnimationScriptAMEMCommand):
    _size: int = 2

    def __init__(self, amem: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_amem(amem)

    def render(self) -> bytearray:
        return super().render(self._amem_bits())


class AnimationScriptAMEM6XCommand(AnimationScriptAMEMCommand):
    _size: int = 4


class AnimationScriptAMEMAndConst(AnimationScriptAMEM6XCommand):
    _value: UInt16

    @property
    def value(self) -> UInt16:
        return self._value

    def set_value(self, value: int) -> None:
        self._value = UInt16(value)


class AnimationScriptAMEMAnd7E(AnimationScriptAMEM6XCommand):
    _address: int

    @property
    def address(self) -> int:
        return self._address

    def set_address(self, address: int) -> None:
        assert 0x7E0000 <= address <= 0x7EFFFF
        self._address = address


class AnimationScriptAMEMAnd7F(AnimationScriptAMEM6XCommand):
    _address: int

    @property
    def address(self) -> int:
        return self._address

    def set_address(self, address: int) -> None:
        assert 0x7F0000 <= address <= 0x7FFFFF
        self._address = address


class AnimationScriptAMEMAndAMEM(AnimationScriptAMEM6XCommand):
    _source_amem: UInt8

    @property
    def source_amem(self) -> UInt8:
        return self._source_amem

    def set_source_amem(self, amem: int) -> None:
        assert 0x60 <= amem <= 0x6F
        self._source_amem = UInt8(amem)


class AnimationScriptAMEMAndOMEM(AnimationScriptAMEM6XCommand):
    _omem: UInt8

    @property
    def omem(self) -> UInt8:
        return self._omem

    def set_omem(self, omem: int) -> None:
        self._omem = UInt8(omem)


class AnimationScriptUnknownJmp2X(AnimationScriptCommandWithJmps):
    _size: int = 6

    _byte_1: UInt8

    @property
    def byte_1(self) -> UInt8:
        return self._byte_1

    def set_byte_1(self, byte_1: int) -> None:
        self._byte_1 = UInt8(byte_1)

    def __init__(
        self,
        byte_1: int,
        destinations: List[str],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(destinations, identifier)
        self.set_byte_1(byte_1)

    def render(self) -> bytearray:
        return super().render(self.byte_1, *self.destinations)


class SetAMEMToXYZCoords(AnimationScriptCommand):
    _size: int = 8

    _origin: Origin
    _x: Int16
    _y: Int16
    _z: Int16
    _do_set_x: bool
    _do_set_y: bool
    _do_set_z: bool

    @property
    def origin(self) -> Origin:
        return self._origin

    def set_origin(self, origin: Origin) -> None:
        self._origin = origin

    @property
    def x(self) -> Int16:
        return self._x

    def set_x(self, x: int) -> None:
        self._x = Int16(x)

    @property
    def y(self) -> Int16:
        return self._y

    def set_y(self, y: int) -> None:
        self._y = Int16(y)

    @property
    def z(self) -> Int16:
        return self._z

    def set_z(self, z: int) -> None:
        self._z = Int16(z)

    @property
    def do_set_x(self) -> bool:
        return self._do_set_x

    def set_do_set_x(self, do_set_x: bool) -> None:
        self._do_set_x = do_set_x

    @property
    def do_set_y(self) -> bool:
        return self._do_set_y

    def set_do_set_y(self, do_set_y: bool) -> None:
        self._do_set_y = do_set_y

    @property
    def do_set_z(self) -> bool:
        return self._do_set_z

    def set_do_set_z(self, do_set_z: bool) -> None:
        self._do_set_z = do_set_z

    def __init__(
        self,
        origin: Origin,
        x: int,
        y: int,
        z: int,
        set_x: bool = False,
        set_y: bool = False,
        set_z: bool = False,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_origin(origin)
        self.set_x(x)
        self.set_y(y)
        self.set_z(z)
        self.set_do_set_x(set_x)
        self.set_do_set_y(set_y)
        self.set_do_set_z(set_z)

    def render(self) -> bytearray:
        byte1 = (
            (self.origin << 4)
            + (self.do_set_x * 0x01)
            + (self.do_set_y * 0x02)
            + (self.do_set_z * 0x04)
        )
        return super().render(byte1)


class AnimationScriptFadeObject(AnimationScriptCommand):
    _opcode: int = 0x85
    _size: int = 3

    _duration: UInt8

    @property
    def duration(self) -> UInt8:
        return self._duration

    def set_duration(self, duration: int) -> None:
        self._duration = UInt8(duration)

    def __init__(self, duration: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_duration(duration)


class AnimationScriptShakeObject(AnimationScriptCommand):
    _opcode: int = 0x86
    _size: int = 7

    _amount: UInt8
    _speed: UInt16

    @property
    def amount(self) -> UInt8:
        return self._amount

    def set_amount(self, amount: int) -> None:
        self._amount = UInt8(amount)

    @property
    def speed(self) -> UInt16:
        return self._speed

    def set_speed(self, speed: int) -> None:
        assert speed <= 256
        self._speed = UInt16(speed)

    def __init__(
        self, amount: int, speed: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_amount(amount)
        self.set_speed(speed)

    def render(self, header) -> bytearray:
        return super().render(header, 0, 0, self.amount, self.speed)


class AnimationScriptCommandInventory(AnimationScriptCommand):
    _size: int = 3

    _item_id: UInt8

    @property
    def item_id(self) -> UInt8:
        return self._item_id

    def set_item_id(self, item: Type[Item]) -> None:
        assert issubclass(item, Item)
        self._item_id = UInt8(item().item_id)

    def __init__(self, item: Type[Item], identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_item_id(item)


class AnimationScript(Script[AnimationScriptCommand]):
    _contents: List[AnimationScriptCommand] = []

    @property
    def contents(self) -> List[AnimationScriptCommand]:
        return self._contents

    def append(self, command: AnimationScriptCommand) -> None:
        super().append(command)

    def extend(self, commands: List[AnimationScriptCommand]) -> None:
        super().extend(commands)

    def set_contents(self, script: List[AnimationScriptCommand] = []) -> None:
        super().set_contents(script)

    def __init__(self, script: List[AnimationScriptCommand] = []) -> None:
        super().__init__(script)

    def insert_before_nth_command(
        self, n: int, command: AnimationScriptCommand
    ) -> None:
        super().insert_before_nth_command(n, command)

    def insert_after_nth_command(self, n: int, command: AnimationScriptCommand) -> None:
        super().insert_after_nth_command(n, command)

    def insert_before_nth_command_of_type(
        self, n: int, cls: Type[AnimationScriptCommand], command: AnimationScriptCommand
    ) -> None:
        super().insert_before_nth_command_of_type(n, cls, command)

    def insert_after_nth_command_of_type(
        self, n: int, cls: Type[AnimationScriptCommand], command: AnimationScriptCommand
    ) -> None:
        super().insert_after_nth_command_of_type(n, cls, command)

    def insert_before_identifier(
        self, identifier: str, command: AnimationScriptCommand
    ) -> None:
        super().insert_before_identifier(identifier, command)

    def insert_after_identifier(
        self, identifier: str, command: AnimationScriptCommand
    ) -> None:
        super().insert_after_identifier(identifier, command)

    def replace_at_index(self, index: int, content: AnimationScriptCommand) -> None:
        super().replace_at_index(index, content)

    def delete_at_index(self, index: int) -> None:
        super().delete_at_index(index)

    def render(self, position: Optional[int] = None) -> bytearray:
        output = bytearray()
        script: AnimationScriptCommand
        for script in self._contents:
            output += script.render()
        return output


class BattleAnimationScript(AnimationScript):
    _header: List[TransformableIdentifier]

    @property
    def header(self) -> List[TransformableIdentifier]:
        return self._header

    @property
    def header_size(self) -> int:
        return len(self._header) * 2 + 2

    def __init__(
        self, header: List[str] = [], script: List[AnimationScriptCommand] = []
    ) -> None:
        self._header = [TransformableIdentifier(identifier) for identifier in header]
        super().__init__(script)

    def render(self, address: int) -> bytearray:
        true_address: bytearray = UInt16(
            (address & 0xFFFF) + 2 + len(self._header)
        ).little_endian()
        header: bytearray = bytearray()
        for dest in self.header:
            header += dest.render_address()
        return true_address + header + super().render()


class SubroutineOrBanklessScript(AnimationScript):
    _expected_size: int = 0

    @property
    def expected_size(self) -> int:
        return self._expected_size

    def __init__(
        self, expected_size: int, script: List[AnimationScriptCommand] = []
    ) -> None:
        self._expected_size = expected_size
        super().__init__(script)

    def render(self) -> bytearray:
        output = super().render()
        # These HAVE to match the original size. We can't fuck around with subroutines too much
        assert len(output) == self.expected_size
        return output


class AnimationScriptBank(ScriptBank[AnimationScript]):
    _scripts: List[Union[AnimationScript, BattleAnimationScript]]
    _pointer_table_start: int
    _start: int
    _end: int
    _name: str

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
        return UInt16((self.start - self.pointer_table_start) // 2)

    @property
    def scripts(self) -> List[Union[AnimationScript, BattleAnimationScript]]:
        return self._scripts

    @property
    def name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def set_contents(self, scripts: List[AnimationScript] = []) -> None:
        assert len(scripts) == self.script_count
        super().set_contents(scripts)

    def replace_script(self, n: int, script: AnimationScript) -> None:
        assert 0 <= n < self.script_count
        super().replace_script(n, script)

    def get_command_by_name(self, identifier: str) -> AnimationScriptCommand:
        for script in self._scripts:
            for command in script.contents:
                if command.identifier.name == identifier:
                    return command
        raise Exception("%s not found" % identifier)

    def replace_command_by_name(
        self, identifier: str, contents: AnimationScriptCommand
    ) -> None:
        for script_id, script in enumerate(self._scripts):
            for index, command in enumerate(script.contents):
                if command.identifier.name == identifier:
                    self._scripts[script_id].contents[index] = contents
                    return
        raise Exception("%s not found" % identifier)

    def __init__(
        self,
        name: str,
        start: int,
        end: int,
        pointer_table_start: int = 0,
        scripts: List[AnimationScript] = [],
    ) -> None:
        self.set_pointer_table_start(pointer_table_start)
        self.set_start(start)
        self.set_end(end)
        self.set_name(name)
        super().__init__(scripts)

    def associate_address(self, command: AnimationScriptCommand, position: int) -> int:

        key: str = command.identifier.name
        if key in self.addresses:
            raise Exception("duplicate command identifier found: %s" % key)
        self.addresses[key] = position

        position += command.size

        if position >= self.end:
            raise Exception(
                "command exceeded max bank size: %s @ %06x" % (key, position)
            )
        return position

    def render(self) -> bytearray:
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
            rendered_script = script.render(position)
            position += len(rendered_script)
            self.script_bytes.extend(rendered_script)

        # fill empty bytes
        expected_length: int = self.end - self.start
        final_length: int = len(self.script_bytes)
        if final_length > expected_length:
            raise Exception(
                "action script output too long: got %s expected %s"
                % (final_length, expected_length)
            )
        buffer: List[int] = [0xFF] * (expected_length - final_length)
        self.script_bytes.extend(buffer)

        if self.pointer_table_start != 0:
            return self.pointer_bytes + self.script_bytes
        else:
            return self.script_bytes


# header for battle event 22: bytearray([0x7C, 0x64]) - pointer to yarid subroutine 0x3A647C. which has to be inserted after event 22

# these counts arent 0 based
# header for battle event 70: little endian pointer to 4th command, 7th command
# header for battle event 85: little endian pointer to 7th command, 13th command
# All of the above point to any command that jumps to 0x3A7531?


class AnimationScriptBankCollection:
    _banks: List[AnimationScriptBank]

    @property
    def banks(self) -> List[AnimationScriptBank]:
        return self._banks

    def get_bank(self, name: str) -> AnimationScriptBank:
        return next(bank for bank in self.banks if bank.name == name)

    def render(self) -> Dict[int, bytearray]:
        scriptBank: AnimationScriptBank
        merged_dicts: Dict[str, int] = {}
        output: Dict[int, bytearray] = {}

        for scriptBank in self.banks:
            position: int = scriptBank.start

            script: Union[AnimationScript, BattleAnimationScript]
            command: AnimationScriptCommand

            # build command name : address table for ENTIRE bank
            for script in scriptBank.scripts:
                if scriptBank.pointer_table_start != 0:
                    scriptBank.pointer_bytes.extend(
                        UInt16(position & 0xFFFF).little_endian()
                    )
                if isinstance(script, BattleAnimationScript):
                    position += script.header_size
                for command in script.contents:
                    position = scriptBank.associate_address(command, position)
                merged_dicts.update(scriptBank.addresses)

        for scriptBank in self.banks:
            scriptBank._addresses = merged_dicts  # I know this is bad...
            output[scriptBank.start] = scriptBank.render()

        return output

    def __init__(self, banks: List[AnimationScriptBank]) -> None:
        self._banks = banks
