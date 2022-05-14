from randomizer.types.actionscripts.constants.classes import ActionScriptCommandName
from randomizer.types.eventscripts.constants.classes import EventScriptCommandName
from randomizer.types.variables.classes import ByteVar, ShortVar
from ..numbers.classes import UInt16
from typing import Union
import uuid


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
    _command_name: Union[ActionScriptCommandName, EventScriptCommandName]
    _identifier: TransformableIdentifier
    _opcode: Union[bytearray, int]
    _size: int

    @property
    def opcode(self) -> Union[int, bytearray]:
        return self._opcode

    @property
    def command_name(self) -> Union[ActionScriptCommandName, EventScriptCommandName]:
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
