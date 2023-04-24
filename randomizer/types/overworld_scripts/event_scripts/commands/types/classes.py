"""Base classes supporting event script assembly."""

from typing import List, Optional, Type, cast, Union
from randomizer.types.overworld_scripts.action_scripts import (
    ActionScript,
)
from randomizer.types.overworld_scripts.action_scripts.commands.types import (
    UsableActionScriptCommand,
)
from randomizer.types.items import Item

from randomizer.types.scripts_common.classes import (
    ScriptCommand,
    ScriptCommandBasicShortOperation,
    ScriptCommandNoArgs,
    ScriptCommandShortAddrAndValueOnly,
    ScriptCommandWithJmps,
    ScriptCommandAnySizeMem,
    ScriptCommandShortMem,
)
from randomizer.types.overworld_scripts.arguments.types import (
    AreaObject,
    ShortVar,
    ByteVar,
)
from randomizer.types.overworld_scripts.arguments import PRIMARY_TEMP_7000

from randomizer.types.numbers import UInt8


class EventScriptCommand(ScriptCommand):
    """Base class for any command in an event script."""


class EventScriptCommandWithJmps(EventScriptCommand, ScriptCommandWithJmps):
    """Base class for any command in an event script that contains at least one goto."""


class EventScriptCommandNoArgs(EventScriptCommand, ScriptCommandNoArgs):
    """Base class for any command in an event script that takes no arguments."""


class EventScriptCommandAnySizeMem(EventScriptCommand, ScriptCommandAnySizeMem):
    """Base class for any command in an event script that can accept either an
    8 bit or 16 bit var."""

    def __init__(
        self, address: Union[ByteVar, ShortVar], identifier: Optional[str] = None
    ) -> None:
        super().__init__(address, identifier)

        if self.address == PRIMARY_TEMP_7000:
            self._size = 1
        else:
            self._size = 2


class EventScriptCommandShortMem(EventScriptCommand, ScriptCommandShortMem):
    """Base class for any command in an event script that accepts only
    an 8 bit var."""


class EventScriptCommandShortAddrAndValueOnly(
    EventScriptCommand, ScriptCommandShortAddrAndValueOnly
):
    """Base class for any command in an event script that accepts
    an 8 bit var and a literal value (either a number or an item class)."""

    def __init__(
        self,
        address: ShortVar,
        value: Union[int, Type[Item]],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(address, value, identifier)

        if self.address == PRIMARY_TEMP_7000:
            self._size = 3
        else:
            self._size = 4


class EventScriptCommandBasicShortOperation(
    EventScriptCommand, ScriptCommandBasicShortOperation
):
    """Base class for any command in an event script that performs math
    on an 8 bit var."""


class EventScriptCommandActionScriptContainer(EventScriptCommand):
    """Base class for commands in an event script that includes
    and runs a NPC action script."""

    _header_size: int
    _subscript: ActionScript

    @property
    def header_size(self) -> int:
        """The expected size of the bytes indicating information about
        the subscript before the subscript contents begin."""
        return self._header_size

    @property
    def subscript(self) -> ActionScript:
        """The contents of the NPC action script that this command runs."""
        return self._subscript

    @property
    def size(self) -> int:
        """The length of this command as a whole."""
        return self.header_size + self.subscript.length


class Subscript(ActionScript):
    """Base class for an action script to be used as typing for
    action command subscripts inside event commands. This is specifically
    intended for commands whose subscript must be 127 bytes in length or
    shorter."""

    def _insert(self, index: int, command: UsableActionScriptCommand) -> None:
        assert self.length + command.size <= 0x7F
        super()._insert(index, command)

    def set_contents(
        self, script: Optional[List[UsableActionScriptCommand]] = None
    ) -> None:
        """Overwrite the contents of the action script command list."""
        if script is None:
            script = []
        contents_length = sum(cast(List[int], [c.size for c in script]))
        assert contents_length <= 0x7F
        super().set_contents(script)


class ActionSubcriptCommandPrototype(EventScriptCommandActionScriptContainer):
    """Base class for action queues, must be 127 bytes or less."""

    _target: AreaObject
    _sync: bool
    _subscript: Subscript
    _header_size: int = 2

    @property
    def target(self) -> AreaObject:
        """The field NPC that this queue should run on."""
        return self._target

    def set_target(self, target: AreaObject) -> None:
        """Designate the field NPC that this queue should run on."""
        self._target = target

    @property
    def sync(self) -> bool:
        """If false, the action script must complete before any further commands in the
        event script can continue."""
        return self._sync

    def set_sync(self, sync: bool) -> None:
        """If false, the action script must complete before any further commands in the
        event script can continue."""
        self._sync = sync

    @property
    def subscript(self) -> Subscript:
        """The collection of NPC action script commands to be run."""
        return self._subscript

    def set_subscript(self, subscript: List[UsableActionScriptCommand]) -> None:
        """Overwrite the collection of NPC action script commands to be run."""
        self.subscript.set_contents(subscript)

    def __init__(
        self,
        target: AreaObject,
        sync: bool = False,
        subscript: Optional[List[UsableActionScriptCommand]] = None,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_target(target)
        self.set_sync(sync)
        if subscript is None:
            subscript = []
        self.set_subscript(subscript)


class ActionQueuePrototype(ActionSubcriptCommandPrototype):
    """Base class for action queues, must be 127 bytes or less.
    Cannot be forcibly stopped, overall command length is shorter."""

    def render(self) -> bytearray:
        header_byte: UInt8 = UInt8(self.subscript.length + ((not self.sync) << 7))
        return super().render(self.target, header_byte, self.subscript.render())


class StartEmbeddedActionScriptPrototype(ActionSubcriptCommandPrototype):
    """Base class for action queues, must be 127 bytes or less.
    Can be forcibly stopped, overall command length is longer."""

    _prefix: UInt8
    _header_size: int = 3

    @property
    def prefix(self) -> UInt8:
        """(unknown, but must be 0xF0 or 0xF1)"""
        return self._prefix

    def set_prefix(self, prefix: int) -> None:
        """(unknown, but must be 0xF0 or 0xF1)"""
        assert prefix in [0xF0, 0xF1]
        self._prefix = UInt8(prefix)

    def __init__(
        self,
        target: AreaObject,
        prefix: int,
        sync: bool = False,
        subscript: Optional[List[UsableActionScriptCommand]] = None,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(target, sync, subscript, identifier)
        self.set_prefix(prefix)

    def render(self) -> bytearray:
        header_byte: UInt8 = UInt8(self.subscript.length + ((not self.sync) << 7))
        return super().render(
            self.target, self.prefix, header_byte, self.subscript.render()
        )


class NonEmbeddedActionQueuePrototype(EventScriptCommandActionScriptContainer):
    """Non-embedded action queues are commands representing code that the game
    runs as an action script instead of an event script.\n
    When assembled, these queues contain no header to indicate where they begin.
    The game understands  where these scripts are intended to begin via ASM that
    exists outside of the scope of the script bank.\n"""

    _subscript: ActionScript
    _header_size: int = 0

    @property
    def subscript(self) -> ActionScript:
        """The contents to be run by this queue."""
        return self._subscript

    def set_subscript(self, subscript: List[UsableActionScriptCommand]) -> None:
        """Overwrite the contents to be run by this queue."""
        self.subscript.set_contents(subscript)

    def __init__(
        self,
        subscript: Optional[List[UsableActionScriptCommand]],
        identifier: Optional[str] = None,
    ) -> None:
        if subscript is None:
            subscript = []
        super().__init__(identifier)
        self._subscript = Subscript()
        self.set_subscript(subscript)

    def render(self) -> bytearray:
        return super().render(self.subscript.render())


class UsableEventScriptCommand(EventScriptCommand):
    """Subclass for commands that can actually be used in a script
    (no prototypes)."""
