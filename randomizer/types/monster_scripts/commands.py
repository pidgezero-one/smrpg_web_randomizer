"""Individual monster battle script command classes.
These are the building blocks of monster battle scripts."""


from copy import deepcopy
from typing import List, Optional, Set, Type
from randomizer.types.enemy_attacks.classes import EnemyAttack
from randomizer.types.items.classes import Item
from randomizer.types.spells.enums import Element, Status

from randomizer.types.monster_scripts.constants.classes import CommandType, Target
from randomizer.types.monster_scripts.constants.misc import TOTAL_ATTACKS
from randomizer.utils.number import bits_to_int
from randomizer.types.monster_scripts.classes import (
    MonsterScriptCommand,
    MonsterScriptCommandNoArgs,
    MonsterScriptCommandOneTarget,
    MonsterScriptCommandOneTargetLimited,
    MonsterScriptCommandOneVar,
)
from randomizer.types.numbers.classes import UInt16, UInt8
from randomizer.types.spells.classes import Spell


class Attack(MonsterScriptCommand):
    """Issue an attack, or one of three attacks at random.
    Each of the three attacks do not have to be unique from each other."""

    _attack_1: Type[EnemyAttack]
    _attack_2: Optional[Type[EnemyAttack]]
    _attack_3: Optional[Type[EnemyAttack]]

    @property
    def attack_1(self) -> Type[EnemyAttack]:
        """The first (or only) attack that can be issued by this command."""
        return self._attack_1

    def set_attack_1(self, attack_1: Type[EnemyAttack]) -> None:
        """Set the first (or only) attack that can be issued by this command."""
        self.set_attacks(attack_1, self.attack_2, self.attack_3)

    @property
    def attack_2(self) -> Optional[Type[EnemyAttack]]:
        """The optional second attack that can be issued by this command."""
        return self._attack_2

    def set_attack_2(self, attack_2: Optional[Type[EnemyAttack]]) -> None:
        """Set the optional second attack that can be issued by this command.
        Will fail if attack_3 is None."""
        self.set_attacks(self.attack_1, attack_2, self.attack_3)

    @property
    def attack_3(self) -> Optional[Type[EnemyAttack]]:
        """The optional third attack that can be issued by this command."""
        return self._attack_3

    def set_attack_3(self, attack_3: Optional[Type[EnemyAttack]]) -> None:
        """Set the optional third attack that can be issued by this command.
        Will fail if attack_2 is None."""
        self.set_attacks(self.attack_1, self.attack_2, attack_3)

    def set_attacks(
        self,
        attack_1: Type[EnemyAttack],
        attack_2: Optional[Type[EnemyAttack]],
        attack_3: Optional[Type[EnemyAttack]],
    ) -> None:
        """Overwrite the attack (or three attacks) that can be issued by this command."""
        a1index = attack_1().index
        if attack_2 is None or attack_3 is None:
            assert attack_2 is None and attack_3 is None
            assert a1index <= TOTAL_ATTACKS
        else:
            assert 0 <= a1index <= TOTAL_ATTACKS or a1index == 251
        self._attack_1 = attack_1
        if attack_2 is not None:
            a2index = attack_2().index
            assert 0 <= a2index <= TOTAL_ATTACKS or a2index == 251
        self._attack_2 = attack_2
        if attack_3 is not None:
            a3index = attack_3().index
            assert 0 <= a3index <= TOTAL_ATTACKS or a3index == 251
        self._attack_3 = attack_3

    def __init__(
        self,
        attack_1: Type[EnemyAttack],
        attack_2: Optional[Type[EnemyAttack]] = None,
        attack_3: Optional[Type[EnemyAttack]] = None,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_attacks(
            attack_1,
            attack_2,
            attack_3,
        )

    def render(self) -> bytearray:
        if self.attack_2 is None and self.attack_3 is None:
            return super().render(self.attack_1().index)
        assert self.attack_2 is not None and self.attack_3 is not None
        return super().render(
            0xE0, self.attack_1().index, self.attack_2().index, self.attack_3().index
        )


class SetTarget(MonsterScriptCommandOneTarget):
    """Choose the target for the actions following this command."""

    _opcode: int = 0xE2

    def render(self) -> bytearray:
        return super().render(self.target)


class RunBattleDialog(MonsterScriptCommand):
    """Run a battle dialog (by ID)."""

    _opcode: int = 0xE3

    _dialog_id: UInt8

    @property
    def dialog_id(self) -> UInt8:
        """The ID of the dialog to run."""
        return self._dialog_id

    def set_dialog_id(self, dialog_id: int) -> None:
        """Set the ID of the dialog to run."""
        self._dialog_id = UInt8(dialog_id)

    def __init__(self, dialog_id: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_dialog_id(dialog_id)

    def render(self) -> bytearray:
        return super().render(self.dialog_id)


class RunBattleEvent(MonsterScriptCommand):
    """Run a battle event by ID. It is encouraged to use battle ID constants for this."""

    _opcode: int = 0xE5

    _event_id: UInt8

    @property
    def event_id(self) -> UInt8:
        """The ID of the battle event to run"""
        return self._event_id

    def set_event_id(self, event_id: int) -> None:
        """Set the ID of the battle event to run.
        It is encouraged to use battle ID constants for this."""
        assert event_id <= 102
        self._event_id = UInt8(event_id)

    def __init__(self, event_id: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_event_id(event_id)

    def render(self) -> bytearray:
        return super().render(self.event_id)


class IncreaseVarBy1(MonsterScriptCommandOneVar):
    """Increase the given 0x7EE00X variable by 1."""

    _opcode = bytearray([0xE6, 0x00])

    def render(self) -> bytearray:
        return super().render(self.render_var())


class DecreaseVarBy1(IncreaseVarBy1):
    """Decrease the given 0x7EE00X variable by 1."""

    _opcode = bytearray([0xE6, 0x01])


class SetVarBits(MonsterScriptCommandOneVar):
    """For the given 0x7EE00X variable, set bits denoted by an ordinality array."""

    _opcode = bytearray([0xE7, 0x00])

    _bits: Set[int] = set()

    @property
    def bits(self) -> Set[int]:
        """The ordinality array of bits to be set on the given variable."""
        return self._bits

    def set_bits(self, bits: List[int]) -> None:
        """Overwrite the ordinality array of bits to be set on the given variable."""
        for bit in bits:
            assert 0 <= bit <= 7
        self._bits = set(bits)

    def __init__(
        self, variable: int, bits: List[int], identifier: Optional[str] = None
    ) -> None:
        super().__init__(variable, identifier)
        self.set_bits(bits)

    def render(self) -> bytearray:
        return super().render(self.render_var(), bits_to_int(list(self.bits)))


class ClearVarBits(SetVarBits):
    """For the given 0x7EE00X variable, clear bits denoted by an ordinality array."""

    _opcode = bytearray([0xE7, 0x01])

    @property
    def bits(self) -> Set[int]:
        """The ordinality array of bits to be cleared on the given variable."""
        return super().bits

    # pylint: disable=W0246
    def set_bits(self, bits: List[int]) -> None:
        """Overwrite the ordinality array of bits to be cleared on the given variable."""
        super().set_bits(bits)

    def clear_bits(self, bits: List[int]) -> None:
        """Overwrite the ordinality array of bits to be cleared on the given variable."""
        self.set_bits(bits)


class ClearVar(MonsterScriptCommandOneVar):
    """Set the given 0x7EE00X variable to 0."""

    _opcode = bytearray(0xE8)

    def render(self) -> bytearray:
        return super().render(self.render_var())


class RemoveTarget(MonsterScriptCommandOneTarget):
    """The given target will no longer be active or targetable."""

    _opcode = bytearray([0xEA, 0x00, 0x00])

    def render(self) -> bytearray:
        return super().render(self.target)


class CallTarget(MonsterScriptCommandOneTarget):
    """The given target will become active and targetable."""

    _opcode = bytearray([0xEA, 0x01, 0x00])

    def render(self) -> bytearray:
        return super().render(self.target)


class MakeInvulnerable(MonsterScriptCommandOneTarget):
    """The given target will not take damage from any source."""

    _opcode = bytearray([0xEB, 0x00, 0x00])

    def render(self) -> bytearray:
        return super().render(self.target)


class MakeVulnerable(MonsterScriptCommandOneTarget):
    """The given target will be susceptible to damage.
    This reverses the effects of any previous MakeInvulnerable commands applied to this target."""

    _opcode = bytearray([0xEB, 0x01, 0x00])

    def render(self) -> bytearray:
        return super().render(self.target)


class ExitBattle(MonsterScriptCommandNoArgs):
    """Abort the battle and return to the level."""

    _opcode: int = 0xEC


class Set7EE005ToRandomNumber(MonsterScriptCommand):
    """Set a designated random number storage variable
    to a random number in a given range."""

    _opcode: int = 0xED

    _upper_bound: UInt8

    @property
    def upper_bound(self) -> UInt8:
        """The upper bound allowed on the random number range (lower bound 0).
        The upper bound is not included in the result set."""
        return self._upper_bound

    def set_upper_bound(self, upper_bound: int) -> None:
        """Set the upper bound allowed on the random number range (lower bound 0).
        The upper bound is not included in the result set."""
        self._upper_bound = UInt8(upper_bound)

    def __init__(self, upper_bound: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_upper_bound(upper_bound)

    def render(self) -> bytearray:
        return super().render(self.upper_bound)


class CastSpell(MonsterScriptCommand):
    """Cast an spell, or one of three spells at random.
    Each of the three spells do not have to be unique from each other."""

    _spell_1: Type[Spell]
    _spell_2: Optional[Type[Spell]]
    _spell_3: Optional[Type[Spell]]

    @property
    def spell_1(self) -> Type[Spell]:
        """The first (or only) spell that can be cast by this command."""
        return self._spell_1

    def set_spell_1(self, spell_1: Type[Spell]) -> None:
        """Set the first (or only) spell that can be cast by this command."""
        self.set_spells(spell_1, self.spell_2, self.spell_3)

    @property
    def spell_2(self) -> Optional[Type[Spell]]:
        """The optional second spell that can be cast by this command."""
        return self._spell_2

    def set_spell_2(self, spell_2: Optional[Type[Spell]]) -> None:
        """Set the optional second spell that can be cast by this command.
        Will fail if spell_3 is None."""
        self.set_spells(self.spell_1, spell_2, self.spell_3)

    @property
    def spell_3(self) -> Optional[Type[Spell]]:
        """The optional third spell that can be cast by this command."""
        return self._spell_3

    def set_spell_3(self, spell_3: Optional[Type[Spell]]) -> None:
        """Set the optional third spell that can be cast by this command.
        Will fail if spell_2 is None."""
        self.set_spells(self.spell_1, self.spell_2, spell_3)

    def set_spells(
        self,
        spell_1: Type[Spell],
        spell_2: Optional[Type[Spell]],
        spell_3: Optional[Type[Spell]],
    ) -> None:
        """Overwrite the spell (or three spells) that can be cast by this command."""
        s1index = spell_1().index
        if spell_2 is None or spell_3 is None:
            assert spell_2 is None and spell_3 is None
            assert s1index <= TOTAL_ATTACKS
        else:
            assert 0 <= s1index <= TOTAL_ATTACKS or s1index == 251
        self._spell_1 = spell_1
        if spell_2 is not None:
            s2index = spell_2().index
            assert 0 <= s2index <= TOTAL_ATTACKS or s2index == 251
        self._spell_2 = spell_2
        if spell_3 is not None:
            s3index = spell_3().index
            assert 0 <= s3index <= TOTAL_ATTACKS or s3index == 251
        self._spell_3 = spell_3

    def __init__(
        self,
        spell_1: Type[Spell],
        spell_2: Optional[Type[Spell]] = None,
        spell_3: Optional[Type[Spell]] = None,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(identifier)
        self.set_spells(
            spell_1,
            spell_2,
            spell_3,
        )

    def render(self) -> bytearray:
        if self.spell_2 is None and self.spell_3 is None:
            return super().render(0xEF, self.spell_1().index)
        assert self.spell_2 is not None and self.spell_3 is not None
        return super().render(
            0xF0, self.spell_1().index, self.spell_2().index, self.spell_3().index
        )


class DoMonsterBehaviour(MonsterScriptCommand):
    """Run a pre-set monster behaviour script by ID.
    It is recommended to use monster behaviour constants for this."""

    _opcode: int = 0xF1

    _animation_id: UInt8

    @property
    def animation_id(self) -> UInt8:
        """The ID of the monster behaviour to be run."""
        return self._animation_id

    def set_animation_id(self, animation_id: int) -> None:
        """Set the ID of the monster behaviour to be run."""
        assert 0 <= animation_id <= 53
        self._animation_id = UInt8(animation_id)

    def __init__(self, animation_id: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_animation_id(animation_id)

    def render(self) -> bytearray:
        return super().render(self.animation_id)


class SetUntargetable(MonsterScriptCommandOneTargetLimited):
    """The target will not be targetable by any following commands."""

    _opcode = bytearray([0xF2, 0x00])


class SetTargetable(MonsterScriptCommandOneTargetLimited):
    """The target will become targetable by following commands.
    This reverses the effects of any previous SetUntargetable commands applied to this target."""

    _opcode = bytearray([0xF2, 0x01])


class EnableCommand(MonsterScriptCommand):
    """Enable the given party command types (Attack, Spell, Item)."""

    _opcode = bytearray([0xF3, 0x00])

    _commands: List[CommandType]

    @property
    def commands(self) -> List[CommandType]:
        """The list of command types to be enabled by this command."""
        return self._commands

    def set_commands(self, commands: List[CommandType]) -> None:
        """Overwrite the list of command types to be enabled by this command."""
        assert len(commands) == len(set(commands))
        self._commands = deepcopy(commands)

    def __init__(
        self, commands: List[CommandType], identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_commands(commands)

    def render(self) -> bytearray:
        byte1 = 0
        for item in self.commands:
            byte1 += 1 << int(item)
        return super().render(byte1)


class DisableCommand(EnableCommand):
    """Disable the given party command types (Attack, Spell, Item)."""

    _opcode = bytearray([0xF3, 0x01])

    @property
    def commands(self) -> List[CommandType]:
        """The list of command types to be disabled by this command."""
        return super().commands

    # pylint: disable=W0246
    def set_commands(self, commands: List[CommandType]) -> None:
        """Overwrite the list of command types to be disabled by this command."""
        super().set_commands(commands)


class RemoveAllInventory(MonsterScriptCommandNoArgs):
    """Temporarily remove all items from party inventory."""

    _opcode = bytearray([0xF4, 0x00, 0x00, 0x00])


class RestoreInventory(MonsterScriptCommandNoArgs):
    """Restore all temporarily-removed items from party inventory,
    reversing the effects of RemoveAllInventory."""

    _opcode = bytearray([0xF4, 0x00, 0x01, 0x00])


class IfTargetedByCommand(MonsterScriptCommand):
    """Begin an if-block triggered by being targeted by any command in a list of command types.
    Any following commands between this one and the next Return command will only be executed
    if the condition of this command is met."""

    _opcode = bytearray([0xFC, 0x01])

    _commands: List[CommandType]

    @property
    def commands(self) -> List[CommandType]:
        """The list of commands which trigger the if-block."""
        return self._commands

    def set_commands(self, commands: List[CommandType]) -> None:
        """Overwrite the list of commands which trigger the if-block.
        Given commands must be unique, and there can only be one or two of them."""
        assert len(commands) == len(set(commands))
        assert len(commands) in [1, 2]
        self._commands = deepcopy(commands)

    def __init__(
        self, commands: List[CommandType], identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_commands(commands)

    def render(self) -> bytearray:
        effective_commands = deepcopy(self.commands)
        if len(effective_commands) == 1:
            effective_commands.append(effective_commands[0])

        return super().render(effective_commands[0] + 2, effective_commands[1] + 2)


class IfTargetedBySpell(MonsterScriptCommand):
    """Begin an if-block triggered by being targeted by any spell in a list of spells.
    Any following commands between this one and the next Return command will only be executed
    if the condition of this command is met."""

    _opcode = bytearray([0xFC, 0x02])

    _spells: List[Type[Spell]]

    @property
    def spells(self) -> List[Type[Spell]]:
        """The list of spells which trigger the if-block."""
        return self._spells

    def set_commands(self, spells: List[Type[Spell]]) -> None:
        """Overwrite the list of spells which trigger the if-block.
        Given spells must be unique, and there can only be one or two of them."""
        assert len(spells) == len(set(spells))
        assert len(spells) in [1, 2]
        self._spells = deepcopy(spells)

    def __init__(
        self, spells: List[Type[Spell]], identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_commands(spells)

    def render(self) -> bytearray:
        effective_spells = deepcopy(self.spells)
        if len(effective_spells) == 1:
            effective_spells.append(effective_spells[0])

        return super().render(effective_spells[0]().index, effective_spells[1]().index)


class IfTargetedByItem(MonsterScriptCommand):
    """Begin an if-block triggered by being targeted by an item in a list of items.
    Any following commands between this one and the next Return command will only be executed
    if the condition of this command is met."""

    _opcode = bytearray([0xFC, 0x03])

    _items: List[Type[Item]]

    @property
    def items(self) -> List[Type[Item]]:
        """The list of items which trigger the if-block."""
        return self._items

    def set_commands(self, items: List[Type[Item]]) -> None:
        """Overwrite the list of items which trigger the if-block.
        Given items must be unique, and there can only be one or two of them."""
        assert len(items) == len(set(items))
        assert len(items) in [1, 2]
        self._items = deepcopy(items)

    def __init__(
        self, items: List[Type[Item]], identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_commands(items)

    def render(self) -> bytearray:
        effective_items = deepcopy(self.items)
        if len(effective_items) == 1:
            effective_items.append(effective_items[0])

        return super().render(
            effective_items[0]().item_id, effective_items[1]().item_id
        )


class IfTargetedByElement(MonsterScriptCommand):
    """Begin an if-block triggered by being targeted by an item in a list of items.
    Any following commands between this one and the next Return command will only be executed
    if the condition of this command is met."""

    _opcode = bytearray([0xFC, 0x04])

    _elements: List[Element]

    @property
    def elements(self) -> List[Element]:
        """The list of elements which trigger the if-block."""
        return self._elements

    def set_elements(self, elements: List[Element]) -> None:
        """Overwrite the list of elements which trigger the if-block.
        Given elements must be unique."""
        assert len(elements) == len(set(elements))
        self._elements = deepcopy(elements)

    def __init__(
        self, elements: List[Element], identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_elements(elements)

    def render(self) -> bytearray:
        return super().render(
            sum(element.spell_value for element in self.elements), 0x00
        )


class IfTargetedByRegularAttack(MonsterScriptCommandNoArgs):
    """Begin an if-block triggered by being targeted by an A-attack.
    Any following commands between this one and the next Return command will only be executed
    if the condition of this command is met."""

    _opcode = bytearray([0xF4, 0x05, 0x00, 0x00])


class IfHPBelow(MonsterScriptCommand):
    """Begin an if-block triggered by the monster's HP falling below a certain threshold.
    Any following commands between this one and the next Return command will only be executed
    if the condition of this command is met."""

    _opcode = bytearray([0xFC, 0x07])

    _threshold: UInt16

    @property
    def threshold(self) -> UInt16:
        """The HP value to fall below in order to trigger this if-block."""
        return self._threshold

    def set_threshold(self, threshold: int) -> None:
        """Set the HP value to fall below in order to trigger this if-block."""
        self._threshold = UInt16(threshold)

    def __init__(self, threshold: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_threshold(threshold)

    def render(self) -> bytearray:
        return super().render(self.threshold)


class IfTargetAfflictedBy(MonsterScriptCommandOneTarget):
    """Begin an if-block triggered by the monster being afflicted by a status
    in a list of statuses.
    Any following commands between this one and the next Return command will only be executed
    if the condition of this command is met."""

    _opcode = bytearray([0xFC, 0x08])

    _statuses: List[Status]

    @property
    def statuses(self) -> List[Status]:
        """The list of statuses which trigger the if-block."""
        return self._statuses

    def set_statuses(self, statuses: List[Status]) -> None:
        """Overwrite the list of statuses which trigger the if-block.
        Given statuses must be unique."""
        assert len(statuses) == len(set(statuses))
        self._statuses = deepcopy(statuses)

    def __init__(
        self,
        target: Target,
        statuses: List[Status],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(target, identifier)
        self.set_statuses(statuses)

    def render(self) -> bytearray:
        return super().render(
            self.target, bits_to_int([status.spell_value for status in self.statuses])
        )


class IfTargetNotAfflictedBy(IfTargetAfflictedBy):
    """Begin an if-block triggered by the monster not being afflicted by a status
    in a list of statuses.
    Any following commands between this one and the next Return command will only be executed
    if the condition of this command is met."""

    _opcode = bytearray([0xFC, 0x09])

    @property
    def statuses(self) -> List[Status]:
        """The list of statuses which, if not afflicting the monster, trigger the if-block."""
        return super().statuses

    # pylint: disable=W0246
    def set_statuses(self, statuses: List[Status]) -> None:
        """Overwrite the list of statuses which, if not afflicting the monster,
        trigger the if-block.
        Given statuses must be unique."""
        super().set_statuses(statuses)


class IfTurnCounterEquals(MonsterScriptCommand):
    """Begin an if-block triggered by the turn counter reaching a given amount.
    Any following commands between this one and the next Return command will only be executed
    if the condition of this command is met."""

    _opcode = bytearray([0xFC, 0x0A])

    _phase: UInt8

    @property
    def phase(self) -> UInt8:
        """The number of turns which, when passed, trigger this if-block."""
        return self._phase

    def set_phase(self, phase: int) -> None:
        """Designate the number of turns which, when passed, trigger this if-block."""
        self._phase = UInt8(phase)

    def __init__(self, phase: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_phase(phase)

    def render(self) -> bytearray:
        return super().render(self.phase, 0x00)


class IfVarLessThan(MonsterScriptCommandOneVar):
    """Begin an if-block triggered by a certain variable value being below a given amount.
    Any following commands between this one and the next Return command will only be executed
    if the condition of this command is met."""

    _opcode = bytearray([0xFC, 0x0C])

    _threshold: UInt8

    @property
    def threshold(self) -> UInt8:
        """The value which, if the given variable is below it, will trigger this if-block."""
        return self._threshold

    def set_threshold(self, threshold: int) -> None:
        """Set the value which, if the given variable is below it, will trigger this if-block."""
        self._threshold = UInt8(threshold)

    def __init__(
        self,
        variable: int,
        threshold: int,
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(variable, identifier)
        self.set_threshold(threshold)

    def render(self) -> bytearray:
        return super().render(self.render_var(), self.threshold)


class IfVarEqualOrGreaterThan(IfVarLessThan):
    """Begin an if-block triggered by a certain variable value not being below a given amount.
    Any following commands between this one and the next Return command will only be executed
    if the condition of this command is met."""

    _opcode = bytearray([0xFC, 0x0D])

    @property
    def threshold(self) -> UInt8:
        """The value which, if the given variable is below it, will trigger this if-block."""
        return super().threshold

    # pylint: disable=W0246
    def set_threshold(self, threshold: int) -> None:
        """Set the value which, if the given variable is below it, will trigger this if-block."""
        super().set_threshold(threshold)


class IfTargetAlive(MonsterScriptCommandOneTarget):
    """Begin an if-block triggered by a certain target still being present in the battle.
    Any following commands between this one and the next Return command will only be executed
    if the condition of this command is met."""

    _opcode = bytearray([0xFC, 0x10, 0x00])


class IfTargetKOed(MonsterScriptCommandOneTarget):
    """Begin an if-block triggered by a certain target no longer being present in the battle.
    Any following commands between this one and the next Return command will only be executed
    if the condition of this command is met."""

    _opcode = bytearray([0xFC, 0x10, 0x01])


class IfVarBitsSet(SetVarBits):
    """Begin an if-block triggered by the given bits being set on the given variable.
    Any following commands between this one and the next Return command will only be executed
    if the condition of this command is met."""

    _opcode = bytearray([0xFC, 0x11])

    @property
    def bits(self) -> Set[int]:
        """The bits which, if set on the given variable, trigger this if-block."""
        return super().bits

    # pylint: disable=W0246
    def set_bits(self, bits: List[int]) -> None:
        """Set the bits which, if set on the given variable, trigger this if-block."""
        super().set_bits(bits)


class IfVarBitsClear(ClearVarBits):
    """Begin an if-block triggered by the given bits being cleared on the given variable.
    Any following commands between this one and the next Return command will only be executed
    if the condition of this command is met."""

    _opcode = bytearray([0xFC, 0x12])

    @property
    def bits(self) -> Set[int]:
        """The bits which, if cleared on the given variable, trigger this if-block."""
        return super().bits

    # pylint: disable=W0246
    def set_bits(self, bits: List[int]) -> None:
        """Set the bits which, if cleared on the given variable, trigger this if-block."""
        super().set_bits(bits)

    def clear_bits(self, bits: List[int]) -> None:
        """Set the bits which, if cleared on the given variable, trigger this if-block."""
        self.set_bits(bits)


class IfCurrentlyInFormationID(MonsterScriptCommand):
    """Begin an if-block which this monster will only run if the player is currently in battle
    against the formation indicated by this command's ID.
    It is highly encouraged to use formation constants for this.
    Any following commands between this one and the next Return command will only be executed
    if the condition of this command is met."""

    _opcode = bytearray([0xFC, 0x13])

    _formation_id: UInt16

    @property
    def formation_id(self) -> UInt16:
        """The formation ID which the player needs to be in battle against in order for
        the monster to run this if-block."""
        return self._formation_id

    def set_formation_id(self, formation_id: int) -> None:
        """Set the formation ID which the player needs to be in battle against in order for
        the monster to run this if-block.
        It is highly encouraged to use formation constants for this."""
        self._formation_id = UInt16(formation_id)

    def __init__(self, formation_id: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_formation_id(formation_id)

    def render(self) -> bytearray:
        return super().render(self.formation_id)


class IfLastMonsterStanding(MonsterScriptCommandNoArgs):
    """Begin an if-block triggered by the monster's turn arriving when no other monsters remain.
    Any following commands between this one and the next Return command will only be executed
    if the condition of this command is met."""

    _opcode = bytearray([0xFC, 0x14, 0x00, 0x00])


class Wait1Turn(MonsterScriptCommandNoArgs):
    """The monster's turn ends here, and will resume on the next line after this one on
    its next turn."""

    _opcode: int = 0xFD


class Wait1TurnandRestartScript(MonsterScriptCommandNoArgs):
    """The monster's turn ends here, and will resume at the beginning of its script on
    its next turn."""

    _opcode: int = 0xFE


class StartCounterCommands(MonsterScriptCommandNoArgs):
    """Begins the block of code indicating what the monster does in response to a player action
    that targeted it."""

    _opcode: int = 0xFF
