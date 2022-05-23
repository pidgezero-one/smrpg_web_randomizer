from typing import Optional, Union, Type
import uuid
from copy import deepcopy

from randomizer.types.variables.classes import ByteVar, ShortVar
from randomizer.types.numbers.classes import UInt16
from randomizer.utils.memsize import cast_address


class TransformableIdentifier:
    _name: str
    _address: int

    def __init__(self, name: str) -> None:
        assert name is not None and len(name) > 0
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @property
    def address(self) -> int:
        return self._address

    def render_address(self) -> bytearray:
        return UInt16(self._address & 0xFFFF).little_endian()

    def set_address(self, address: int) -> None:
        assert (
            0x1E0C00 <= address <= 0x1EFFFF
            or 0x1F0C00 <= address <= 0x1FFFFF
            or 0x200800 <= address <= 0x20DFFF
        )
        self._address = address

    def __str__(self):
        return self._name


class ScriptCommand:
    _identifier: TransformableIdentifier
    _opcode: Union[bytearray, int]
    _size: int

    @property
    def opcode(self) -> Union[int, bytearray]:
        return self._opcode

    @property
    def identifier(self) -> TransformableIdentifier:
        return self._identifier

    @property
    def size(self) -> int:
        return self._size

    def _generate_identifier(self) -> str:
        return self._command_name + "_" + str(uuid.uuid4())

    def __init__(self, identifier: Optional[str] = None) -> None:
        if identifier is None or len(identifier) == 0:
            identifier = self._generate_identifier()
        self._identifier = TransformableIdentifier(identifier)

    def render(self, *args, **kwargs) -> bytearray:
        output = bytearray([])
        if hasattr(self, "_opcode"):
            if isinstance(self._opcode, bytearray):
                output.extend(self._opcode)
            elif isinstance(self._opcode, int) and 0 <= arg <= 0xFF:
                output.append(self._opcode)
            else:
                raise Exception(
                    "illegal opcode in %s: %r" % (self.identifier, self._opcode)
                )
        for arg in args:
            if isinstance(arg, ShortVar) or isinstance(arg, ByteVar):
                output.append(arg.to_byte())
            elif isinstance(arg, UInt16):
                output.extend(arg.little_endian())
            elif isinstance(arg, int) and 0 <= arg <= 0xFF:
                output.append(arg)
            elif isinstance(arg, bytearray):
                output.extend(arg)
            elif isinstance(arg, TransformableIdentifier):
                output.extend(arg.render_address())
            else:
                raise Exception(
                    "unknown argument type in %s: %s (%r)"
                    % (self.identifier, type(arg), arg)
                )
        if len(output) != self.size:
            raise Exception(
                "%s output wrong length: %r length %i, expected %i"
                % (self.identifier.name, args, len(output), self.size)
            )
        return output


class ScriptCommandWithJmps(ScriptCommand):
    _destinations: "TransformableIdentifier[int]"

    @property
    def destinations(self) -> "TransformableIdentifier[int]":
        return self._destinations

    def set_destinations(self, destinations: "str[int]") -> None:
        self._destinations = [TransformableIdentifier(dest) for dest in destinations]

    def set_destination(self, destination: str, index: int) -> None:
        self._destinations[index] = TransformableIdentifier(destination)

    def __init__(
        self, destinations: "str[int]", identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_destinations(destinations)


class ScriptCommandNoArgs(ScriptCommand):
    def __init__(self, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        if isinstance(self.opcode, bytearray):
            self._size = len(self.opcode)
        else:
            self._size = 1


class ScriptCommandAnySizeMem(ScriptCommand):
    _address: Union[ShortVar, ByteVar]

    @property
    def address(self) -> Union[ShortVar, ByteVar]:
        return self._address

    def set_address(self, address: int) -> None:
        self._address = cast_address(address)

    def __init__(self, address: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_address(address)


class ScriptCommandShortMem(ScriptCommand):
    _address: ShortVar

    @property
    def address(self) -> ShortVar:
        return self._address

    def set_address(self, address: int) -> None:
        self._address = cast_address(address)

    def __init__(self, address: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_address(address)

    def render(self) -> bytearray:
        return super().render(self.address.to_byte())


class ScriptCommandShortAddrAndValueOnly(ScriptCommand):
    _address: ShortVar
    _value: UInt16

    @property
    def address(self) -> ShortVar:
        return self._address

    def set_address(self, address: int) -> None:
        self._address = ShortVar(address)

    @property
    def value(self) -> UInt16:
        return self._value

    def set_value(self, value: int) -> None:
        self._value = UInt16(value)

    def __init__(
        self, address: int, value: int, identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_address(address)
        self.set_value(value)


class ScriptCommandBasicShortOperation(ScriptCommand):
    _value: UInt16
    _size: int = 4

    @property
    def value(self) -> UInt16:
        return self._value

    def set_value(self, value: int) -> None:
        self._value = UInt16(value)

    def __init__(self, value: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_value(value)

    def render(self) -> bytearray:
        return super().render(self.value)


class Script:
    _contents: "ScriptCommand[int]"

    def _insert(self, n: int, command: ScriptCommand) -> None:
        assert 0 <= n < len(self.contents)
        self.contents.insert(n, command)

    def _get_index_of_nth_command_of_type(
        self, n: int, cls: Type[ScriptCommand]
    ) -> int:
        try:
            index: int = [
                i for i, cmd in enumerate(self.contents) if isinstance(cmd, cls)
            ][n]
        except:
            raise Exception("could not find %i instances of %r" % (n, cls))
        return index

    def _get_index_of_identifier(self, identifier: str) -> int:
        index = next(
            (
                i
                for i, cmd in enumerate(self.contents)
                if cmd.identifier.name == identifier
            ),
            -1,
        )
        if index == -1:
            raise Exception("could not find %s" % identifier)
        return index

    def set_contents(self, script: "ScriptCommand[int]" = []) -> None:
        self._contents = deepcopy(script)

    def __init__(self, script: "ScriptCommand[int]" = []) -> None:
        self.set_contents(script)

    def insert_before_nth_command(self, n: int, command: ScriptCommand) -> None:
        self._insert(n, command)

    def insert_after_nth_command(self, n: int, command: ScriptCommand) -> None:
        self._insert(n + 1, command)

    def insert_before_nth_command_of_type(
        self, n: int, cls: Type[ScriptCommand], command: ScriptCommand
    ) -> None:
        index: int = self._get_index_of_nth_command_of_type(n, cls)
        self._insert(index, command)

    def insert_after_nth_command_of_type(
        self, n: int, cls: Type[ScriptCommand], command: ScriptCommand
    ) -> None:
        index: int = self._get_index_of_nth_command_of_type(n, cls)
        self._insert(index + 1, command)

    def insert_before_identifier(self, identifier: str, command: ScriptCommand) -> None:
        index: int = self._get_index_of_identifier(identifier)
        self._insert(index + 1, command)

    def insert_after_identifier(self, identifier: str, command: ScriptCommand) -> None:
        index: int = self._get_index_of_identifier(identifier)
        self._insert(index, command)

    def render(self):
        output = bytearray()
        script: ScriptCommand
        for script in self.contents:
            output += script.render()
        return output


class ScriptBank:
    _scripts: "Script[int]"
    _pointer_table_start: int
    _start: int
    _end: int

    @property
    def pointer_table_start(self) -> int:
        return self._pointer_table_start

    @property
    def start(self) -> int:
        return self._start

    @property
    def end(self) -> int:
        return self._end

    @property
    def scripts(self) -> "Script[int]":
        return self._scripts

    def set_contents(self, scripts: "Script[int]" = []) -> None:
        self._scripts = deepcopy(scripts)

    def replace_script(self, n: int, script: Script) -> None:
        self._scripts[n] = deepcopy(script)

    def __init__(self, script: "Script[int]" = []) -> None:
        self.set_contents(script)
