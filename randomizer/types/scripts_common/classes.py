from typing import (
    Dict,
    Generic,
    List,
    Optional,
    Tuple,
    TypeVar,
    Union,
    Type,
    cast,
)
import uuid
from copy import deepcopy

from randomizer.types.items.classes import Item

from randomizer.types.overworld_scripts.variables.classes import ByteVar, ShortVar
from randomizer.types.numbers.classes import Int8, UInt16, UInt8


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
        return str(uuid.uuid4())

    def __init__(self, identifier: Optional[str] = None) -> None:
        if identifier is None or len(identifier) == 0:
            identifier = self._generate_identifier()
        self._identifier = TransformableIdentifier(identifier)

    def render(self, *args, **kwargs) -> bytearray:
        output = bytearray([])
        if hasattr(self, "_opcode"):
            if isinstance(self._opcode, bytearray):
                output.extend(self._opcode)
            elif isinstance(self._opcode, int) and 0 <= self._opcode <= 0xFF:
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
            elif isinstance(arg, UInt8):
                output.append(arg.to_byte())
            elif isinstance(arg, Int8):
                output.append(arg.to_byte())
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
    _destinations: List[TransformableIdentifier] = []

    @property
    def destinations(self) -> List[TransformableIdentifier]:
        return self._destinations

    def set_destinations(self, destinations: List[str]) -> None:
        self._destinations = [TransformableIdentifier(dest) for dest in destinations]

    def set_destination(self, destination: str, index: int) -> None:
        self._destinations[index] = TransformableIdentifier(destination)

    def __init__(
        self, destinations: List[str], identifier: Optional[str] = None
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

    def set_address(self, address: Union[ShortVar, ByteVar]) -> None:
        self._address = address

    def __init__(
        self, address: Union[ByteVar, ShortVar], identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_address(address)


class ScriptCommandShortMem(ScriptCommand):
    _address: ShortVar

    @property
    def address(self) -> ShortVar:
        return self._address

    def set_address(self, address: ShortVar) -> None:
        self._address = address

    def __init__(self, address: ShortVar, identifier: Optional[str] = None) -> None:
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

    def set_address(self, address: ShortVar) -> None:
        self._address = ShortVar(address)

    @property
    def value(self) -> UInt16:
        return self._value

    def set_value(self, value: Union[int, Type[Item]]) -> None:
        if not isinstance(value, int) and issubclass(value, Item):
            value = value().item_id
        self._value = UInt16(value)

    def __init__(
        self,
        address: ShortVar,
        value: Union[int, Type[Item]],
        identifier: Optional[str] = None,
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


TScriptCommand = TypeVar("TScriptCommand", bound=ScriptCommand)


class Script(Generic[TScriptCommand]):
    _contents: List[TScriptCommand] = []

    @property
    def contents(self) -> List[TScriptCommand]:
        return self._contents

    def append(self, command: TScriptCommand) -> None:
        self._contents.append(command)

    def extend(self, commands: List[TScriptCommand]) -> None:
        self._contents.extend(commands)

    def _insert(self, n: int, command: TScriptCommand) -> None:
        assert 0 <= n < len(self._contents)
        self._contents.insert(n, command)

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
                for i, cmd in enumerate(self._contents)
                if cmd.identifier.name == identifier
            ),
            -1,
        )
        if index == -1:
            raise Exception("could not find %s" % identifier)
        return index

    def set_contents(self, script: Optional[List[TScriptCommand]] = None) -> None:
        """Overwrite this script's command list."""
        if script is None:
            script = []
        self._contents = deepcopy(script)

    def __init__(self, script: Optional[List[TScriptCommand]] = None) -> None:
        if script is None:
            script = []
        self.set_contents(script)

    @property
    def length(self) -> int:
        return sum(cast(List[int], [c.size for c in self.contents]))

    def insert_before_nth_command(self, n: int, command: TScriptCommand) -> None:
        self._insert(n, command)

    def insert_after_nth_command(self, n: int, command: TScriptCommand) -> None:
        self._insert(n + 1, command)

    def insert_before_nth_command_of_type(
        self,
        n: int,
        cls: Type[TScriptCommand],
        command: TScriptCommand,
    ) -> None:
        index: int = self._get_index_of_nth_command_of_type(n, cls)
        self._insert(index, command)

    def insert_after_nth_command_of_type(
        self,
        n: int,
        cls: Type[TScriptCommand],
        command: TScriptCommand,
    ) -> None:
        index: int = self._get_index_of_nth_command_of_type(n, cls)
        self._insert(index + 1, command)

    def insert_before_identifier(
        self, identifier: str, command: TScriptCommand
    ) -> None:
        index: int = self._get_index_of_identifier(identifier)
        self._insert(index + 1, command)

    def insert_after_identifier(self, identifier: str, command: TScriptCommand) -> None:
        index: int = self._get_index_of_identifier(identifier)
        self._insert(index, command)

    def replace_at_index(self, index: int, content: TScriptCommand) -> None:
        self._contents[index] = content

    def replace_by_name(self, identifier: str, content: TScriptCommand) -> None:
        index: int = self._get_index_of_identifier(identifier)
        self._contents[index] = content

    def delete_at_index(self, index: int) -> None:
        del self._contents[index]

    def get_command_by_name(self, identifier: str) -> Tuple[int, TScriptCommand]:
        index = next(
            (
                i
                for i, command in enumerate(self._contents)
                if command.identifier.name == identifier
            ),
            -1,
        )
        if index == -1:
            raise Exception("%s not found" % identifier)
        return index, self._contents[index]

    def render(self):
        output = bytearray()
        script: ScriptCommand
        for script in self._contents:
            output += script.render()
        return output


TScript = TypeVar("TScript", bound=Script)


class ScriptBank(Generic[TScript]):
    _scripts: List[TScript] = []
    _pointer_table_start: int
    _start: int
    _end: int

    _addresses: Dict[str, int]
    _pointer_bytes: bytearray
    _script_bytes: bytearray

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
    def scripts(self) -> List[TScript]:
        return self._scripts

    def set_contents(self, scripts: Optional[List[TScript]] = None) -> None:
        if scripts is None:
            scripts = []
        self._scripts = deepcopy(scripts)

    def replace_script(self, n: int, script: TScript) -> None:
        self._scripts[n] = deepcopy(script)

    def __init__(self, scripts: Optional[List[TScript]]) -> None:
        if scripts is None:
            scripts = []
        self.set_contents(scripts)
        self._addresses = {}
        self._pointer_bytes = bytearray()
        self._script_bytes = bytearray()

    @property
    def addresses(self) -> Dict[str, int]:
        return self._addresses

    @property
    def pointer_bytes(self) -> bytearray:
        return self._pointer_bytes

    @property
    def script_bytes(self) -> bytearray:
        return self._script_bytes

    def _set_identifier_addresses(
        self, identifiers: List[TransformableIdentifier]
    ) -> None:
        destination: TransformableIdentifier
        for destination in identifiers:
            key: str = destination.name
            if key not in self.addresses:
                raise Exception("couldn't find destination %s" % (key))
            destination.set_address(self.addresses[key] % 0xFFFF)

    def _populate_jumps(self, script: Script) -> None:
        affected_commands = [
            cmd for cmd in script.contents if isinstance(cmd, ScriptCommandWithJmps)
        ]
        for command in affected_commands:
            self._set_identifier_addresses(command.destinations)


class IdentifierException(Exception):
    """An exception to raise when an erroneous operation occurs on command identifiers."""


class ScriptBankTooLongException(Exception):
    """An exception to be called when the generated bytes for a script bank exceed the
    allotted length."""


class InvalidCommandArgumentException(Exception):
    """An exception to be called when a given argument is invalid for the command class."""


class InvalidOpcodeException(Exception):
    """An exception to be called when a given opcode is invalid for the command class."""
