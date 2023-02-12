from copy import deepcopy
from typing import List, Optional, Set, Type
from randomizer.types.enemy_attacks.classes import EnemyAttack
from randomizer.types.items.classes import Item
from randomizer.types.spells.enums import SpellElement, SpellStatusEffects

from randomizer.types.monster_scripts.constants.classes import CommandType, Target
from randomizer.types.monster_scripts.constants.misc import TOTAL_ATTACKS
from randomizer.utils.number import bits_to_int
from .classes import (
    MonsterScriptCommand,
    MonsterScriptCommandNoArgs,
    MonsterScriptCommandOneTarget,
    MonsterScriptCommandOneTargetLimited,
    MonsterScriptCommandOneVar,
)
from randomizer.types.numbers.classes import UInt16, UInt4, UInt8
from randomizer.types.spells.classes import Spell


class Attack(MonsterScriptCommand):

    _attack_1: Type[EnemyAttack]
    _attack_2: Optional[Type[EnemyAttack]]
    _attack_3: Optional[Type[EnemyAttack]]

    @property
    def attack_1(self) -> Type[EnemyAttack]:
        return self._attack_1

    def set_attack_1(self, attack_1: Type[EnemyAttack]) -> None:
        self.set_attacks(attack_1, self.attack_2, self.attack_3)

    @property
    def attack_2(self) -> Optional[Type[EnemyAttack]]:
        return self._attack_2

    def set_attack_2(self, attack_2: Optional[Type[EnemyAttack]]) -> None:
        self.set_attacks(self.attack_1, attack_2, self.attack_3)

    @property
    def attack_3(self) -> Optional[Type[EnemyAttack]]:
        return self._attack_3

    def set_attack_3(self, attack_3: Optional[Type[EnemyAttack]]) -> None:
        self.set_attacks(self.attack_1, self.attack_2, attack_3)

    def set_attacks(
        self,
        attack_1: Type[EnemyAttack],
        attack_2: Optional[Type[EnemyAttack]],
        attack_3: Optional[Type[EnemyAttack]],
    ) -> None:
        a1index = attack_1().index
        if attack_2 == None or attack_3 == None:
            assert attack_2 == None and attack_3 == None
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
        if self.attack_2 == None and self.attack_3 == None:
            return super().render(self.attack_1().index)
        assert self.attack_2 is not None and self.attack_3 is not None
        return super().render(
            0xE0, self.attack_1().index, self.attack_2().index, self.attack_3().index
        )


class SetTarget(MonsterScriptCommand):
    _opcode: int = 0xE2

    _target: Target

    @property
    def target(self) -> Target:
        return self._target

    def set_target(self, target: Target) -> None:
        self._target = target

    def __init__(self, target: Target, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_target(target)

    def render(self) -> bytearray:
        return super().render(self.target)


class RunBattleDialog(MonsterScriptCommand):
    _opcode: int = 0xE3

    _dialog_id: UInt8

    @property
    def dialog_id(self) -> UInt8:
        return self._dialog_id

    def set_dialog_id(self, dialog_id: int) -> None:
        self._dialog_id = UInt8(dialog_id)

    def __init__(self, dialog_id: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_dialog_id(dialog_id)

    def render(self) -> bytearray:
        return super().render(self.dialog_id)


class RunBattleEvent(MonsterScriptCommand):
    _opcode: int = 0xE5

    _event_id: UInt8

    @property
    def event_id(self) -> UInt8:
        return self._event_id

    def set_event_id(self, event_id: int) -> None:
        assert event_id <= 102
        self._event_id = UInt8(event_id)

    def __init__(self, event_id: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_event_id(event_id)

    def render(self) -> bytearray:
        return super().render(self.event_id)


class IncreaseVarBy1(MonsterScriptCommandOneVar):
    _opcode = bytearray([0xE6, 0x00])

    def render(self) -> bytearray:
        return super().render(self.render_var())


class DecreaseVarBy1(IncreaseVarBy1):
    _opcode = bytearray([0xE6, 0x01])


class SetVarBits(MonsterScriptCommandOneVar):
    _opcode = bytearray([0xE7, 0x00])

    _bits: Set[int] = set()

    @property
    def bits(self) -> Set[int]:
        return self._bits

    def set_bits(self, bits: List[int]) -> None:
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
    _opcode = bytearray([0xE7, 0x01])


class ClearVar(MonsterScriptCommandOneVar):
    _opcode = bytearray(0xE8)

    def render(self) -> bytearray:
        return super().render(self.render_var())


class RemoveTarget(MonsterScriptCommandOneTarget):
    _opcode = bytearray([0xEA, 0x00, 0x00])

    def render(self) -> bytearray:
        return super().render(self.target)


class CallTarget(MonsterScriptCommandOneTarget):
    _opcode = bytearray([0xEA, 0x01, 0x00])

    def render(self) -> bytearray:
        return super().render(self.target)


class MakeInvulnerable(MonsterScriptCommandOneTarget):
    _opcode = bytearray([0xEB, 0x00, 0x00])

    def render(self) -> bytearray:
        return super().render(self.target)


class MakeVulnerable(MonsterScriptCommandOneTarget):
    _opcode = bytearray([0xEB, 0x01, 0x00])

    def render(self) -> bytearray:
        return super().render(self.target)


class ExitBattle(MonsterScriptCommandNoArgs):
    _opcode: int = 0xEC


class Set7EE005ToRandomNumber(MonsterScriptCommand):
    _opcode: int = 0xED

    _upper_bound: UInt8

    @property
    def upper_bound(self) -> UInt8:
        return self._upper_bound

    def set_upper_bound(self, upper_bound: int) -> None:
        self._upper_bound = UInt8(upper_bound)

    def __init__(self, upper_bound: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_upper_bound(upper_bound)

    def render(self) -> bytearray:
        return super().render(self.upper_bound)


class CastSpell(MonsterScriptCommand):

    _spell_1: Type[Spell]
    _spell_2: Optional[Type[Spell]]
    _spell_3: Optional[Type[Spell]]

    @property
    def spell_1(self) -> Type[Spell]:
        return self._spell_1

    def set_spell_1(self, spell_1: Type[Spell]) -> None:
        self.set_spells(spell_1, self.spell_2, self.spell_3)

    @property
    def spell_2(self) -> Optional[Type[Spell]]:
        return self._spell_2

    def set_spell_2(self, spell_2: Optional[Type[Spell]]) -> None:
        self.set_spells(self.spell_1, spell_2, self.spell_3)

    @property
    def spell_3(self) -> Optional[Type[Spell]]:
        return self._spell_3

    def set_spell_3(self, spell_3: Optional[Type[Spell]]) -> None:
        self.set_spells(self.spell_1, self.spell_2, spell_3)

    def set_spells(
        self,
        spell_1: Type[Spell],
        spell_2: Optional[Type[Spell]],
        spell_3: Optional[Type[Spell]],
    ) -> None:
        s1index = spell_1().index
        if spell_2 == None or spell_3 == None:
            assert spell_2 == None and spell_3 == None
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
        if self.spell_2 == None and self.spell_3 == None:
            return super().render(0xEF, self.spell_1().index)
        assert self.spell_2 is not None and self.spell_3 is not None
        return super().render(
            0xF0, self.spell_1().index, self.spell_2().index, self.spell_3().index
        )


class DoMonsterBehaviour(MonsterScriptCommand):
    _opcode: int = 0xF1

    _animation_id: UInt8

    @property
    def animation_id(self) -> UInt8:
        return self._animation_id

    def set_animation_id(self, animation_id: int) -> None:
        assert 0 <= animation_id <= 53
        self._animation_id = UInt8(animation_id)

    def __init__(self, animation_id: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_animation_id(animation_id)

    def render(self) -> bytearray:
        return super().render(self.animation_id)


class SetUntargetable(MonsterScriptCommandOneTargetLimited):
    _opcode = bytearray([0xF2, 0x00])


class SetTargetable(MonsterScriptCommandOneTargetLimited):
    _opcode = bytearray([0xF2, 0x01])


class EnableCommand(MonsterScriptCommand):
    _opcode = bytearray([0xF3, 0x00])

    _commands: List[CommandType]

    @property
    def commands(self) -> List[CommandType]:
        return self._commands

    def set_commands(self, commands: List[CommandType]) -> None:
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
    _opcode = bytearray([0xF3, 0x01])


class RemoveAllInventory(MonsterScriptCommandNoArgs):
    _opcode = bytearray([0xF4, 0x00, 0x00, 0x00])


class RestoreInventory(MonsterScriptCommandNoArgs):
    _opcode = bytearray([0xF4, 0x00, 0x01, 0x00])


class IfTargetedByCommand(MonsterScriptCommand):
    _opcode = bytearray([0xFC, 0x01])

    _commands: List[CommandType]

    @property
    def commands(self) -> List[CommandType]:
        return self._commands

    def set_commands(self, commands: List[CommandType]) -> None:
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
    _opcode = bytearray([0xFC, 0x02])

    _spells: List[Type[Spell]]

    @property
    def spells(self) -> List[Type[Spell]]:
        return self._spells

    def set_commands(self, spells: List[Type[Spell]]) -> None:
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
    _opcode = bytearray([0xFC, 0x03])

    _items: List[Type[Item]]

    @property
    def items(self) -> List[Type[Item]]:
        return self._items

    def set_commands(self, items: List[Type[Item]]) -> None:
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
    _opcode = bytearray([0xFC, 0x04])

    _elements: List[SpellElement]

    @property
    def elements(self) -> List[SpellElement]:
        return self._elements

    def set_elements(self, elements: List[SpellElement]) -> None:
        assert len(elements) == len(set(elements))
        self._elements = deepcopy(elements)

    def __init__(
        self, elements: List[SpellElement], identifier: Optional[str] = None
    ) -> None:
        super().__init__(identifier)
        self.set_elements(elements)

    def render(self) -> bytearray:
        return super().render(sum(self.elements), 0x00)


class IfTargetedByRegularAttack(MonsterScriptCommandNoArgs):
    _opcode = bytearray([0xF4, 0x05, 0x00, 0x00])


class IfHPBelow(MonsterScriptCommand):
    _opcode = bytearray([0xFC, 0x07])

    _threshold: UInt16

    @property
    def threshold(self) -> UInt16:
        return self._threshold

    def set_threshold(self, threshold: int) -> None:
        self._threshold = UInt16(threshold)

    def __init__(self, threshold: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_threshold(threshold)

    def render(self) -> bytearray:
        return super().render(self.threshold)


class IfTargetAfflictedBy(MonsterScriptCommandOneTarget):
    _opcode = bytearray([0xFC, 0x08])

    _statuses: List[SpellStatusEffects]

    @property
    def statuses(self) -> List[SpellStatusEffects]:
        return self._statuses

    def set_statuses(self, statuses: List[SpellStatusEffects]) -> None:
        assert len(statuses) == len(set(statuses))
        self._statuses = deepcopy(statuses)

    def __init__(
        self,
        target: Target,
        statuses: List[SpellStatusEffects],
        identifier: Optional[str] = None,
    ) -> None:
        super().__init__(target, identifier)
        self.set_statuses(statuses)

    def render(self) -> bytearray:
        return super().render(
            self.target, bits_to_int([int(status) for status in self.statuses])
        )


class IfTargetNotAfflictedBy(IfTargetAfflictedBy):
    _opcode = bytearray([0xFC, 0x09])


class IfTurnCounterEquals(MonsterScriptCommand):
    _opcode = bytearray([0xFC, 0x0A])

    _phase: UInt8

    @property
    def phase(self) -> UInt8:
        return self._phase

    def set_phase(self, phase: int) -> None:
        self._phase = UInt8(phase)

    def __init__(self, phase: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_phase(phase)

    def render(self) -> bytearray:
        return super().render(self.phase, 0x00)


class IfVarLessThan(MonsterScriptCommandOneVar):
    _opcode = bytearray([0xFC, 0x0C])

    _threshold: UInt8

    @property
    def threshold(self) -> UInt8:
        return self._threshold

    def set_threshold(self, threshold: int) -> None:
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
    _opcode = bytearray([0xFC, 0x0D])


class IfTargetAlive(MonsterScriptCommandOneTarget):
    _opcode = bytearray([0xFC, 0x10, 0x00])


class IfTargetKOed(MonsterScriptCommandOneTarget):
    _opcode = bytearray([0xFC, 0x10, 0x01])


class IfVarBitsSet(SetVarBits):
    _opcode = bytearray([0xFC, 0x11])


class IfVarBitsClear(ClearVarBits):
    _opcode = bytearray([0xFC, 0x12])


class IfCurrentlyInFormationID(MonsterScriptCommand):
    _opcode = bytearray([0xFC, 0x13])

    _formation_id: UInt16

    @property
    def formation_id(self) -> UInt16:
        return self._formation_id

    def set_formation_id(self, formation_id: int) -> None:
        self._formation_id = UInt16(formation_id)

    def __init__(self, formation_id: int, identifier: Optional[str] = None) -> None:
        super().__init__(identifier)
        self.set_formation_id(formation_id)

    def render(self) -> bytearray:
        return super().render(self.formation_id)


class IfLastMonsterStanding(MonsterScriptCommandNoArgs):
    _opcode = bytearray([0xFC, 0x14, 0x00, 0x00])


class Wait1Turn(MonsterScriptCommandNoArgs):
    _opcode: int = 0xFD


class Wait1TurnandRestartScript(MonsterScriptCommandNoArgs):
    _opcode: int = 0xFE


class StartCounterCommands(MonsterScriptCommandNoArgs):
    _opcode: int = 0xFF
