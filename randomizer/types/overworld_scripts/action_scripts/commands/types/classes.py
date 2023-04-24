"""Basic types supporting the creation of action script commands"""

from typing import Optional, Type, Union

from randomizer.types.items import Item
from randomizer.types.numbers import UInt8
from randomizer.types.scripts_common import (
    ScriptCommand,
    ScriptCommandAnySizeMem,
    ScriptCommandBasicShortOperation,
    ScriptCommandNoArgs,
    ScriptCommandShortAddrAndValueOnly,
    ScriptCommandShortMem,
    ScriptCommandWithJmps,
)

from randomizer.types.overworld_scripts.arguments import PRIMARY_TEMP_700C
from randomizer.types.overworld_scripts.arguments.types import ShortVar, ByteVar


class ActionScriptCommand(ScriptCommand):
    """Base class for any command in a NPC action script."""


class ActionScriptCommandWithJmps(ActionScriptCommand, ScriptCommandWithJmps):
    """Base class for any command in a NPC action script that contains at least one goto."""


class ActionScriptCommandNoArgs(ActionScriptCommand, ScriptCommandNoArgs):
    """Base class for any command in a NPC action script that takes no arguments."""


class ActionScriptCommandAnySizeMem(ActionScriptCommand, ScriptCommandAnySizeMem):
    """Base class for any command in a NPC action script that can accept either an
    8 bit or 16 bit var."""

    def __init__(
        self, address: Union[ShortVar, ByteVar], identifier: Optional[str] = None
    ) -> None:
        super().__init__(address, identifier)

        if self.address == PRIMARY_TEMP_700C:
            self._size = 1
        else:
            self._size = 2


class ActionScriptCommandShortMem(ActionScriptCommand, ScriptCommandShortMem):
    """Base class for any command in a NPC action script that accepts only
    an 8 bit var."""


class ActionScriptCommandShortAddrAndValueOnly(
    ActionScriptCommand, ScriptCommandShortAddrAndValueOnly
):
    """Base class for any command in a NPC action script that accepts
    an 8 bit var and a literal value (either a number or an item class)."""

    def __init__(
        self,
        address: ShortVar,
        value: Union[int, Type[Item]],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(address, value, identifier)

        if self.address == PRIMARY_TEMP_700C:
            self._size = 3
        else:
            self._size = 4


class ActionScriptCommandBasicShortOperation(
    ActionScriptCommand, ScriptCommandBasicShortOperation
):
    """Base class for any command in a NPC action script that performs math
    on an 8 bit var."""


class ActionScriptCommandByteSteps(ActionScriptCommand):
    """Base class for any command in a NPC action script that accepts a
    number of steps as an 8 bit int."""

    _steps: UInt8
    _size: int = 2

    @property
    def steps(self) -> UInt8:
        """The number of steps for this measurement."""
        return self._steps

    def set_steps(self, steps: int) -> None:
        """Set the number of steps for this measurement."""
        self._steps = UInt8(steps)

    def __init__(self, steps: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_steps(steps)

    def render(self) -> bytearray:
        return super().render(self.steps)


class ActionScriptCommandBytePixels(ActionScriptCommand):
    """Base class for any command in a NPC action script that accepts a
    number of pixels as an 8 bit int."""

    _pixels: UInt8
    _size: int = 2

    @property
    def pixels(self) -> UInt8:
        """The number of pixels for this measurement."""
        return self._pixels

    def set_pixels(self, value: int) -> None:
        """Set the number of pixels for this measurement."""
        self._pixels = UInt8(value)

    def __init__(self, pixels: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_pixels(pixels)

    def render(self) -> bytearray:
        return super().render(self.pixels)


class ActionScriptCommandXYBytes(ActionScriptCommand):
    """Base class for any command in a NPC action script that accepts an
    X and Y coordinate, each as 8 bit ints."""

    _size: int = 3
    _x: UInt8
    _y: UInt8

    @property
    def x(self) -> UInt8:
        """The X coordinate"""
        return self._x

    def set_x(self, x: int) -> None:
        """Set the X coordinate"""
        self._x = UInt8(x)

    @property
    def y(self) -> UInt8:
        """The Y coordinate"""
        return self._y

    def set_y(self, y: int) -> None:
        """Set the Y coordinate"""
        self._y = UInt8(y)

    def __init__(self, x: int, y: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_x(x)
        self.set_y(y)

    def render(self) -> bytearray:
        return super().render(self.x, self.y)


class UsableActionScriptCommand(ActionScriptCommand):
    """Subclass for commands that can actually be used in a script
    (no prototypes)."""
