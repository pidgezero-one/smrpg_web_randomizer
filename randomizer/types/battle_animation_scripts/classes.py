"""Base classes supporting battle animation script assembly."""

from typing import List, Optional, Dict, Type, Union
from randomizer.types.items.classes import Item
from randomizer.types.scripts_common.classes import (
    IdentifierException,
    Script,
    ScriptBank,
    ScriptBankTooLongException,
    ScriptCommand,
    ScriptCommandNoArgs,
    ScriptCommandWithJmps,
    TransformableIdentifier,
)
from randomizer.types.numbers.classes import Int16, UInt16, UInt8
from .constants.classes import Origin


class AnimationScriptCommand(ScriptCommand):
    """Base class that all animation script command classes inherit from."""

    def verify_position(self, position: int) -> None:
        """Issues a warning if commands labeled as queuestart are not at their intended address."""
        if "queuestart_" in self.identifier.name:
            chunks = "_".split(self.identifier.name)
            if len(chunks) == 2:
                try:
                    expected_addr: int = int(chunks[1], 16)
                    if expected_addr != position:
                        print(
                            f"warning: {self.identifier.name} has moved to 0x{position:06X}"
                        )
                except ValueError:
                    pass


class AnimationScriptCommandNoArgs(AnimationScriptCommand, ScriptCommandNoArgs):
    """Base class of animation script command classes that take no arguments."""


class AnimationScriptCommandWithJmps(AnimationScriptCommand, ScriptCommandWithJmps):
    """Base class of animation script command classes that use gotos."""


class AnimationScriptAMEMCommand(AnimationScriptCommand):
    """Base class of animation script command classes that target AMEM."""

    _amem: UInt8

    @property
    def amem(self) -> UInt8:
        """AMEM target address in range $60-$6F"""
        return self._amem

    def set_amem(self, amem: int) -> None:
        """Set AMEM target address from 0x60 to 0x6F"""
        assert 0x60 <= amem <= 0x6F
        self._amem = UInt8(amem)

    def _amem_bits(self) -> int:
        return self.amem & 0x0F


class AnimationScriptAMEM6XSoloCommand(AnimationScriptAMEMCommand):
    """Base class of animation script command classes that target AMEM $6X
    and take no other arguments."""

    _size: int = 2

    def __init__(self, amem: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_amem(amem)

    def render(self) -> bytearray:
        return super().render(self._amem_bits())


class AnimationScriptAMEM6XCommand(AnimationScriptAMEMCommand):
    """Base class of animation script command classes that target AMEM $6X."""

    _size: int = 4


class AnimationScriptAMEMAndConst(AnimationScriptAMEM6XCommand):
    """Perform an AND operation between an AMEM in range $60-$6F and a constant value."""

    _value: UInt16

    @property
    def value(self) -> UInt16:
        """The const value to perform the AND operation against"""
        return self._value

    def set_value(self, value: int) -> None:
        """Set the const value to perform the AND operation against"""
        self._value = UInt16(value)


class AnimationScriptAMEMAnd7E(AnimationScriptAMEM6XCommand):
    """Perform an AND operation between an AMEM in range $60-$6F and a value stored at $7Exxxx."""

    _address: int

    @property
    def address(self) -> int:
        """The address containing the value to perform the AND operation against, $7Exxxx"""
        return self._address

    def set_address(self, address: int) -> None:
        """Set the address containing the value to perform the AND operation against, $7Exxxx"""
        assert 0x7E0000 <= address <= 0x7EFFFF
        self._address = address


class AnimationScriptAMEMAnd7F(AnimationScriptAMEM6XCommand):
    """Perform an AND operation between an AMEM in range $60-$6F and a value stored at $7Fxxxx."""

    _address: int

    @property
    def address(self) -> int:
        """The address containing the value to perform the AND operation against, $7Fxxxx"""
        return self._address

    def set_address(self, address: int) -> None:
        """Set the address containing the value to perform the AND operation against, $7Fxxxx"""
        assert 0x7F0000 <= address <= 0x7FFFFF
        self._address = address


class AnimationScriptAMEMAndAMEM(AnimationScriptAMEM6XCommand):
    """Perform an AND operation between an AMEM in range $60-$6F
    and another AMEM in range $60-$6F."""

    _source_amem: UInt8

    @property
    def source_amem(self) -> UInt8:
        """The AMEM in range $60-$6F being compared against"""
        return self._source_amem

    def set_source_amem(self, amem: int) -> None:
        """Set the AMEM in range $60-$6F being compared against"""
        assert 0x60 <= amem <= 0x6F
        self._source_amem = UInt8(amem)


class AnimationScriptAMEMAndOMEM(AnimationScriptAMEM6XCommand):
    """Perform an AND operation between an AMEM in range $60-$6F
    and the value at an OMEM address."""

    _omem: UInt8

    @property
    def omem(self) -> UInt8:
        """The OMEM address being compared against"""
        return self._omem

    def set_omem(self, omem: int) -> None:
        """Set the OMEM address being compared against"""
        self._omem = UInt8(omem)


class AnimationScriptUnknownJmp2X(AnimationScriptCommandWithJmps):
    """Performs a Goto. Context of other parameters is unknown."""

    _size: int = 6

    _byte_1: UInt8

    @property
    def byte_1(self) -> UInt8:
        """Unknown argument"""
        return self._byte_1

    def set_byte_1(self, byte_1: int) -> None:
        """Set value of unknown argument"""
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
    """Stores coordinates relative to a given origin to AMEM."""

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
        """The point at which the x-y-z coords are relative to."""
        return self._origin

    def set_origin(self, origin: Origin) -> None:
        """Set the point at which the x-y-z coords are relative to."""
        self._origin = origin

    @property
    def x(self) -> Int16:
        """Relative X coord."""
        return self._x

    def set_x(self, x: int) -> None:
        """Set relative X coord."""
        self._x = Int16(x)

    @property
    def y(self) -> Int16:
        """Relative Y coord."""
        return self._y

    def set_y(self, y: int) -> None:
        """Set relative Y coord."""
        self._y = Int16(y)

    @property
    def z(self) -> Int16:
        """Relative Z coord."""
        return self._z

    def set_z(self, z: int) -> None:
        """Set relative Z coord."""
        self._z = Int16(z)

    @property
    def do_set_x(self) -> bool:
        """X coord will only be committed to AMEM if this is set to true."""
        return self._do_set_x

    def set_do_set_x(self, do_set_x: bool) -> None:
        """Set whether or not the X coord should be committed to AMEM."""
        self._do_set_x = do_set_x

    @property
    def do_set_y(self) -> bool:
        """Y coord will only be committed to AMEM if this is set to true."""
        return self._do_set_y

    def set_do_set_y(self, do_set_y: bool) -> None:
        """Set whether or not the Y coord should be committed to AMEM."""
        self._do_set_y = do_set_y

    @property
    def do_set_z(self) -> bool:
        """Z coord will only be committed to AMEM if this is set to true."""
        return self._do_set_z

    def set_do_set_z(self, do_set_z: bool) -> None:
        """Set whether or not the Z coord should be committed to AMEM."""
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
    """Base class for commands that fade objects."""

    _opcode: int = 0x85
    _size: int = 3

    _duration: UInt8

    @property
    def duration(self) -> UInt8:
        """Fade duration in frames."""
        return self._duration

    def set_duration(self, duration: int) -> None:
        """Set fade duration, in frames."""
        self._duration = UInt8(duration)

    def __init__(self, duration: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_duration(duration)


class AnimationScriptShakeObject(AnimationScriptCommand):
    """Base class for commands that shake objects."""

    _opcode: int = 0x86
    _size: int = 7

    _amount: UInt8
    _speed: UInt16

    @property
    def amount(self) -> UInt8:
        """Number of shakes."""
        return self._amount

    def set_amount(self, amount: int) -> None:
        """Set number of shakes."""
        self._amount = UInt8(amount)

    @property
    def speed(self) -> UInt16:
        """Shake speed."""
        return self._speed

    def set_speed(self, speed: int) -> None:
        """Set shake speed."""
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
    """Base class for commands that act on an inventory item."""

    _size: int = 3

    _item_id: UInt8

    @property
    def item_id(self) -> UInt8:
        """Item ID."""
        return self._item_id

    def set_item_id(self, item: Type[Item]) -> None:
        """Set item ID."""
        assert issubclass(item, Item)
        self._item_id = UInt8(item().item_id)

    def __init__(self, item: Type[Item], identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_item_id(item)


class AnimationScript(Script[AnimationScriptCommand]):
    """Base class for a single animation script, a list of script command subclasses."""

    _contents: List[AnimationScriptCommand] = []

    @property
    def contents(self) -> List[AnimationScriptCommand]:
        return self._contents

    def append(self, command: AnimationScriptCommand) -> None:
        super().append(command)

    def extend(self, commands: List[AnimationScriptCommand]) -> None:
        super().extend(commands)

    def set_contents(
        self, script: Optional[List[AnimationScriptCommand]] = None
    ) -> None:
        super().set_contents(script)

    def __init__(self, script: Optional[List[AnimationScriptCommand]] = None) -> None:
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

    def render(self, _: Optional[int] = None) -> bytearray:
        output = bytearray()
        command: AnimationScriptCommand
        for command in self._contents:
            output += command.render()
        return output


class BattleAnimationScript(AnimationScript):
    """Special base battle animation script class for battle event cutscenes."""

    _header: List[TransformableIdentifier]

    @property
    def header(self) -> List[TransformableIdentifier]:
        """A list of gotos that are important to this script."""
        return self._header

    @property
    def header_size(self) -> int:
        """The length of the header gotos, used for script rendering purposes."""
        return len(self._header) * 2 + 2

    def __init__(
        self,
        header: Optional[List[str]] = None,
        script: Optional[List[AnimationScriptCommand]] = None,
    ) -> None:
        if header is None:
            header = []
        self._header = [TransformableIdentifier(identifier) for identifier in header]
        super().__init__(script)

    def render(self, position: Optional[int] = None) -> bytearray:
        if position is None:
            raise ValueError
        true_address: bytearray = UInt16(
            (position & 0xFFFF) + 2 + len(self._header)
        ).little_endian()
        header: bytearray = bytearray()
        for dest in self.header:
            header += dest.render_address()
        return true_address + header + super().render()


class SubroutineOrBanklessScript(AnimationScript):
    """Base class for scripts that don't belong to banks, where banks
    typically consist of multiple scripts indicated by ID. This class is
    appropriate for subroutines, or scripts without an ID-separated bank
    such as monster behaviours or Toad tutorials."""

    _expected_size: int = 0

    @property
    def expected_size(self) -> int:
        """The length of bytes that this script should ultimately equal when compiled."""
        return self._expected_size

    def __init__(
        self, expected_size: int, script: Optional[List[AnimationScriptCommand]] = None
    ) -> None:
        self._expected_size = expected_size
        super().__init__(script)

    def render(self) -> bytearray:
        output = super().render()
        # These HAVE to match the original size. We can't fuck around with subroutines too much
        assert len(output) == self.expected_size
        return output


class AnimationScriptBank(ScriptBank[AnimationScript]):
    """Base class for a collection of scripts that belong to the same bank (ie 0x##0000)
    and are separated by IDs."""

    _scripts: List[Union[AnimationScript, BattleAnimationScript]]
    _pointer_table_start: int
    _start: int
    _end: int
    _name: str

    @property
    def pointer_table_start(self) -> int:
        """Address where this bank's pointer table starts. The pointer table
        contains a list of 2-byte little endian pointers that indicate where
        individual scripts start. i.e. the pointer at index 2 in this table
        corresponds to the start of the script having ID 2 (0-based indexing)."""
        return self._pointer_table_start

    def set_pointer_table_start(self, pointer_table_start: int) -> None:
        """Sets the address where this bank's pointer table starts."""
        self._pointer_table_start = pointer_table_start

    @property
    def start(self) -> int:
        return self._start

    def set_start(self, start: int) -> None:
        """Sets the address where rendered scripts should start writing to."""
        self._start = start

    @property
    def end(self) -> int:
        return self._end

    def set_end(self, end: int) -> None:
        """The total length of rendered scripts should not exceed this address."""
        self._end = end

    @property
    def script_count(self) -> UInt16:
        """The number of scripts that the pointer table's size accommodates."""
        return UInt16((self.start - self.pointer_table_start) // 2)

    @property
    def scripts(self) -> List[Union[AnimationScript, BattleAnimationScript]]:
        return self._scripts

    @property
    def name(self) -> str:
        """An arbitrary key for this particular bank. Used to reference and modify
        the contents of this bank externally."""
        return self._name

    def set_name(self, name: str) -> None:
        """Set an arbitrary key for this particular bank. Used to reference and modify
        the contents of this bank externally."""
        self._name = name

    def set_contents(self, scripts: Optional[List[AnimationScript]] = None) -> None:
        """Overwrite the entire list of scripts belonging to this bank."""
        if scripts is None:
            scripts = []
        assert len(scripts) == self.script_count
        super().set_contents(scripts)

    def replace_script(self, n: int, script: AnimationScript) -> None:
        """Overwrite the contents of the script at index n."""
        assert 0 <= n < self.script_count
        super().replace_script(n, script)

    def get_command_by_name(self, identifier: str) -> AnimationScriptCommand:
        """Return a single command whose unique identifier matches the name provided."""
        for script in self._scripts:
            for command in script.contents:
                if command.identifier.name == identifier:
                    return command
        raise IdentifierException(f"{identifier} not found")

    def replace_command_by_name(
        self, identifier: str, contents: AnimationScriptCommand
    ) -> None:
        """Overwrite a single command whose unique identifier matches the name provided."""
        for script_id, script in enumerate(self._scripts):
            for index, command in enumerate(script.contents):
                if command.identifier.name == identifier:
                    self._scripts[script_id].contents[index] = contents
                    return
        raise IdentifierException(f"{identifier} not found")

    def set_addresses(self, addrs: Dict[str, int]) -> None:
        """This should ONLY be used when the parent ScriptBankCollection is rendering
        all of its constituent banks. Replaces the identifier-address dict."""
        self._addresses = addrs

    def __init__(
        self,
        name: str,
        start: int,
        end: int,
        pointer_table_start: int = 0,
        scripts: Optional[List[AnimationScript]] = None,
    ) -> None:
        self.set_pointer_table_start(pointer_table_start)
        self.set_start(start)
        self.set_end(end)
        self.set_name(name)
        super().__init__(scripts)

    def associate_address(self, command: AnimationScriptCommand, position: int) -> int:
        """Associates an identifier and an address as a key-value pair in the addresses dict."""
        key: str = command.identifier.name
        if key in self.addresses:
            raise IdentifierException(f"duplicate command identifier found: {key}")
        self.addresses[key] = position

        position += command.size

        if position >= self.end:
            raise IdentifierException(
                f"command exceeded max bank size: {key} @ {position:06x}"
            )
        return position

    def render(self) -> bytearray:
        """Generate the bytes representing the current state of this bank to be written
        to the ROM."""
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
            rendered_script = script.render()
            position += len(rendered_script)
            self.script_bytes.extend(rendered_script)

        # fill empty bytes
        expected_length: int = self.end - self.start
        final_length: int = len(self.script_bytes)
        if final_length > expected_length:
            raise ScriptBankTooLongException(
                f"action script output too long: got {final_length} expected {expected_length}"
            )
        buffer: List[int] = [0xFF] * (expected_length - final_length)
        self.script_bytes.extend(buffer)

        if self.pointer_table_start != 0:
            return self.pointer_bytes + self.script_bytes
        else:
            return self.script_bytes


class AnimationScriptBankCollection:
    """The container for all battle animation script banks, and bankless scripts, to be used in
    this seed."""

    _banks: List[AnimationScriptBank]

    @property
    def banks(self) -> List[AnimationScriptBank]:
        """Returns all the banks in the collection."""
        return self._banks

    def get_bank(self, name: str) -> AnimationScriptBank:
        """Get a bank by a unique string identifier."""
        return next(bank for bank in self.banks if bank.name == name)

    def render(self) -> Dict[int, bytearray]:
        """Returns a dict where the keys correspond to the bank names, and the values
        are the bytes rendered of their current state to be written to the ROM."""
        script_bank: AnimationScriptBank
        merged_dicts: Dict[str, int] = {}
        output: Dict[int, bytearray] = {}

        for script_bank in self.banks:
            position: int = script_bank.start

            script: Union[AnimationScript, BattleAnimationScript]
            command: AnimationScriptCommand

            # build command name : address table for ENTIRE bank
            for script in script_bank.scripts:
                if script_bank.pointer_table_start != 0:
                    script_bank.pointer_bytes.extend(
                        UInt16(position & 0xFFFF).little_endian()
                    )
                if isinstance(script, BattleAnimationScript):
                    position += script.header_size
                for command in script.contents:
                    position = script_bank.associate_address(command, position)
                merged_dicts.update(script_bank.addresses)

        for script_bank in self.banks:
            script_bank.set_addresses(merged_dicts)
            output[script_bank.start] = script_bank.render()

        return output

    def __init__(self, banks: List[AnimationScriptBank]) -> None:
        self._banks = banks
