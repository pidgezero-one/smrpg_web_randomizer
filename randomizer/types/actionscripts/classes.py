from typing import Union, cast, Type
from copy import deepcopy
import uuid

from constants.classes import ActionScriptCommandName
from constants.misc import TOTAL_SCRIPTS

from ..common.classes import TransformableIdentifier
from ..numbers.classes import UInt16, UInt8
from ..variables import variables
from ..variables.classes import ByteVar, ShortVar
from randomizer.utils.memsize import cast_address


class ActionScriptCommand:
    _command_name: ActionScriptCommandName
    _identifier: TransformableIdentifier
    _opcode: Union[bytearray, int]
    _size: int

    @property
    def opcode(self) -> Union[int, bytearray]:
        return self._opcode

    @property
    def command_name(self) -> ActionScriptCommandName:
        return self._command_name

    @property
    def identifier(self) -> TransformableIdentifier:
        return self._identifier

    @property
    def size(self) -> int:
        return self._size

    def _generate_identifier(self) -> str:
        return self._command_name + "_" + str(uuid.uuid4())

    def __init__(self, identifier: str = None) -> None:
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
                    "unknown argument type in %s: %s" % (self.identifier, type(arg))
                )
        if len(output) != self.size:
            raise Exception(
                "%s output wrong length: %r length %i, expected %i"
                % (self.identifier.name, args, len(output), self.size)
            )
        return output


class ActionScriptCommandWithJmps(ActionScriptCommand):
    _destinations: "TransformableIdentifier[int]"

    @property
    def destinations(self) -> "TransformableIdentifier[int]":
        return self._destinations

    def set_destinations(self, destinations: "str[int]") -> None:
        self._destinations = [TransformableIdentifier(dest) for dest in destinations]

    def set_destination(self, destination: str, index: int) -> None:
        self._destinations[index] = TransformableIdentifier(destination)

    def __init__(self, destinations: "str[int]", identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_destinations(destinations)


class ActionScriptCommandNoArgs(ActionScriptCommand):
    def __init__(self, identifier: str = None) -> None:
        super().__init__(identifier)
        if isinstance(self.opcode, bytearray):
            self._size = len(self.opcode)
        else:
            self._size = 1


class ActionScriptCommandAnySizeMem(ActionScriptCommand):
    _address: Union[ShortVar, ByteVar]

    @property
    def address(self) -> Union[ShortVar, ByteVar]:
        return self._address

    def set_address(self, address: int) -> None:
        self._address = cast_address(address)

    def __init__(self, address: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_address(address)

        if self.address == variables.PRIMARY_TEMP_700C:
            self._size = 1
        else:
            self._size = 2


class ActionScriptCommandShortMem(ActionScriptCommand):
    _address: ShortVar

    @property
    def address(self) -> ShortVar:
        return self._address

    def set_address(self, address: int) -> None:
        self._address = cast_address(address)

    def __init__(self, address: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_address(address)

    def render(self) -> bytearray:
        return super().render(self.address.to_byte())


class ActionScriptCommandShortAddrAndValueOnly(ActionScriptCommand):
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

    def __init__(self, address: int, value: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_address(address)
        self.set_value(value)

        if self.address == variables.PRIMARY_TEMP_700C:
            self._size = 3
        else:
            self._size = 4


class ActionScriptCommandBasicShortOperation(ActionScriptCommand):
    _value: UInt16
    _size: int = 4

    @property
    def value(self) -> UInt16:
        return self._value

    def set_value(self, value: int) -> None:
        self._value = UInt16(value)

    def __init__(self, value: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_value(value)

    def render(self) -> bytearray:
        return super().render(self.value)


class ActionScriptCommandByteSteps(ActionScriptCommand):
    _steps: UInt8
    _size: int = 2

    @property
    def steps(self) -> UInt8:
        return self._steps

    def set_steps(self, steps: int) -> None:
        self._steps = UInt8(steps)

    def __init__(self, steps: int, identifier: str = None) -> None:
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

    def __init__(self, pixels: int, identifier: str = None) -> None:
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

    def __init__(self, x: int, y: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.set_x(x)
        self.set_y(y)

    def render(self) -> bytearray:
        return super().render(self.x, self.y)


class ActionScript:
    _contents: "ActionScriptCommand[int]"

    def _insert(self, n: int, command: ActionScriptCommand) -> None:
        assert 0 <= n < len(self.contents)
        self.contents.insert(n, command)

    def _get_index_of_nth_command_of_type(
        self, n: int, cls: Type[ActionScriptCommand]
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

    @property
    def contents(self) -> "ActionScriptCommand[int]":
        return self._contents

    def set_contents(self, script: "ActionScriptCommand[int]" = []) -> None:
        self._contents = deepcopy(script)

    def __init__(self, script: "ActionScriptCommand[int]" = []) -> None:
        self.set_contents(script)

    @property
    def length(self) -> int:
        return sum(cast("int[int]", [c.size for c in self.contents]))

    def insert_before_nth_command(self, n: int, command: ActionScriptCommand) -> None:
        self.contents.insert(n, command)

    def insert_after_nth_command(self, n: int, command: ActionScriptCommand) -> None:
        self.contents.insert(n + 1, command)

    def insert_before_nth_command_of_type(
        self, n: int, cls: Type[ActionScriptCommand], command: ActionScriptCommand
    ) -> None:
        index: int = self._get_index_of_nth_command_of_type(n, cls)
        self.contents.insert(index, command)

    def insert_after_nth_command_of_type(
        self, n: int, cls: Type[ActionScriptCommand], command: ActionScriptCommand
    ) -> None:
        index: int = self._get_index_of_nth_command_of_type(n, cls)
        self.contents.insert(index + 1, command)

    def insert_before_identifier(
        self, identifier: str, command: ActionScriptCommand
    ) -> None:
        index: int = self._get_index_of_identifier(identifier)
        self.contents.insert(index + 1, command)

    def insert_after_identifier(
        self, identifier: str, command: ActionScriptCommand
    ) -> None:
        index: int = self._get_index_of_identifier(identifier)
        self.contents.insert(index, command)

    def render(self):
        output = bytearray()
        script: ActionScriptCommand
        for script in self.contents:
            output += script.render()
        return output


class ActionScriptBank:
    _scripts: "ActionScript[int]"
    _pointer_table_start: int = 0x210000
    _start: int = 0x210800
    _end: int = 0x21C000

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
    def scripts(self) -> "ActionScript[int]":
        return self._scripts

    def set_contents(self, scripts: "ActionScript[int]" = []) -> None:
        assert len(scripts) == TOTAL_SCRIPTS
        self._scripts = deepcopy(scripts)

    def replace_script(self, n: int, script: ActionScript) -> None:
        assert 0 <= n < TOTAL_SCRIPTS
        self._scripts[n] = deepcopy(script)

    def __init__(self, script: "ActionScript[int]" = []) -> None:
        self.set_contents(script)

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
            for command in script:
                addresses[command.identifier.name] = position
                position += command.size

        # replace jump placeholders with addresses
        for script in self.scripts:
            pointer_bytes.extend(UInt16(position & 0xFFFF).little_endian())
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
