from typing import Union, Callable
from constants import command_names
import uuid
from ..numbers.classes import UInt16, UInt8
from ..variables.classes import ByteVar, Flag, ShortVar
from randomizer.utils.memsize import cast_address
from randomizer.utils.constsize import cast_const


class TransformableIdentifier(str):
    pass


class ActionScriptCommand:
    command_name: command_names.ActionScriptCommandName
    identifier: TransformableIdentifier

    def _generate_identifier(self) -> str:
        return self.command_name + "_" + str(uuid.uuid4())

    def __init__(self, identifier: str = None) -> None:
        if identifier is None or len(identifier) == 0:
            identifier = self._generate_identifier()
        self.identifier = TransformableIdentifier(identifier)


class ActionScriptCommandNoArgs(ActionScriptCommand):
    def __init__(self, identifier: str = None) -> None:
        super().__init__(identifier)


class ActionScriptCommandAnySizeMem(ActionScriptCommand):
    address: Union[ShortVar, ByteVar]

    def __init__(self, address: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.address = cast_address(address)


class ActionScriptCommandShortMem(ActionScriptCommand):
    address: ShortVar

    def __init__(self, address: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.address = ShortVar(address)


class ActionScriptCommandSingleJmp(ActionScriptCommand):
    destination: TransformableIdentifier

    def __init__(self, destination: str, identifier: str = None) -> None:
        assert destination is not None and len(destination) > 0
        super().__init__(identifier)
        self.destination = TransformableIdentifier(destination)


class ActionScriptCommandShortAddrAndValueOnly(ActionScriptCommand):
    address: ShortVar
    value: UInt16

    def __init__(self, address: int, value: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.address = ShortVar(address)
        self.value = UInt16(value)


class ActionScriptCommandBasicShortOperation(ActionScriptCommand):
    value: UInt16

    def __init__(self, value: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.value = UInt16(value)


class ActionScriptCommandByteSteps(ActionScriptCommand):
    steps: UInt8

    def __init__(self, steps: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.steps = UInt8(steps)


class ActionScriptCommandBytePixels(ActionScriptCommand):
    pixels: UInt8

    def __init__(self, pixels: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.pixels = UInt8(pixels)


class ActionScriptCommandXYBytes(ActionScriptCommand):
    x: UInt8
    y: UInt8

    def __init__(self, x: int, y: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.x = UInt8(x)
        self.y = UInt8(y)
