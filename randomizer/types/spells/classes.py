# Data module for spell data.

from copy import deepcopy
from typing import List, Optional, Type
from randomizer.types.items.classes import SpellLearn
from randomizer.types.spells.constants.classes import DamageModifiers, TimingProperties
from randomizer.types.spells.constants.misc import (
    SPELL_BASE_ADDRESS,
    SPELL_BASE_NAME_ADDRESS,
    SPELL_DAMAGE_MODIFIERS_BASE_ADDRESS,
    SPELL_TIMING_MODIFIERS_BASE_ADDRESS,
)
from randomizer.types.spells.enums import (
    EffectType,
    InflictFunction,
    SpellElement,
    SpellStatusEffects,
    SpellType,
    SpellBoosts,
)
from randomizer.logic import utils
from randomizer.types.patch.classes import Patch

from randomizer.types.numbers.classes import UInt16, UInt8
from randomizer.types.world.classes import GameWorld


class Spell:
    """Class representing a magic spell to be randomized."""

    # Default per-spell attributes.
    _index: int = 0
    _fp: int = 0
    _power: int = 0
    _hit_rate: int = 0

    _title: str = ""

    _anim_ptr: int = 0  # I'm not writing an assembler for this yet
    _desc_ptr: int = 0

    _spell_type: SpellType = SpellType.Damage
    _effect_type: EffectType
    _inflict: InflictFunction
    _element: SpellElement.NoElement

    _checkStats: bool = False
    _ignoreDefense: bool = False
    _checkOHKO: bool = False
    _overworldUsable: bool = False
    _quad9s: bool = False
    _hideNum: bool = False

    _targetOthers: bool = False
    _targetEnemies: bool = False
    _targetParty: bool = False
    _targetWounded: bool = False
    _targetOneParty: bool = False
    _targetNotSelf: bool = False
    _status_effects: List[SpellStatusEffects] = []
    _boosts: List[SpellBoosts] = []

    _world: Optional[GameWorld] = None

    @property
    def fp(self) -> UInt8:
        return UInt8(self._fp)

    def set_fp(self, fp: int) -> None:
        assert 0 <= fp <= 31
        self._fp = fp

    @property
    def power(self) -> UInt8:
        return UInt8(self._power)

    def set_power(self, power: int) -> None:
        assert UInt8(power)
        self._power = power

    @property
    def hit_rate(self) -> UInt8:
        return UInt8(self._hit_rate)

    def set_hit_rate(self, hit_rate: int) -> None:
        assert UInt8(hit_rate)
        self._hit_rate = hit_rate

    @property
    def index(self) -> UInt8:
        return UInt8(self._index)

    @property
    def title(self) -> str:
        return self._title

    @property
    def anim_ptr(self) -> int:
        return self._anim_ptr

    @property
    def desc_ptr(self) -> int:
        return self._desc_ptr

    @property
    def spell_type(self) -> SpellType:
        return self._spell_type

    def set_spell_type(self, spell_type: SpellType) -> None:
        self._spell_type = spell_type

    @property
    def effect_type(self) -> EffectType:
        return self._effect_type

    def set_effect_type(self, effect_type: EffectType) -> None:
        self._effect_type = effect_type

    @property
    def inflict(self) -> InflictFunction:
        return self._inflict

    def set_inflict(self, inflict: InflictFunction) -> None:
        self._inflict = inflict

    @property
    def element(self) -> SpellElement:
        return self._element

    def set_element(self, element: SpellElement) -> None:
        self._element = element

    @property
    def checkStats(self) -> bool:
        return self._checkStats

    def set_checkStats(self, checkStats: bool) -> None:
        self._checkStats = checkStats

    @property
    def ignoreDefense(self) -> bool:
        return self._ignoreDefense

    def set_ignoreDefense(self, ignoreDefense: bool) -> None:
        self._ignoreDefense = ignoreDefense

    @property
    def checkOHKO(self) -> bool:
        return self._checkOHKO

    def set_checkOHKO(self, checkOHKO: bool) -> None:
        self._checkOHKO = checkOHKO

    @property
    def overworldUsable(self) -> bool:
        return self._overworldUsable

    def set_overworldUsable(self, overworldUsable: bool) -> None:
        self._overworldUsable = overworldUsable

    @property
    def quad9s(self) -> bool:
        return self._quad9s

    def set_quad9s(self, quad9s: bool) -> None:
        self._quad9s = quad9s

    @property
    def hideNum(self) -> bool:
        return self._hideNum

    def set_hideNum(self, hideNum: bool) -> None:
        self._hideNum = hideNum

    @property
    def targetOthers(self) -> bool:
        return self._targetOthers

    def set_targetOthers(self, targetOthers: bool) -> None:
        self._targetOthers = targetOthers

    @property
    def targetEnemies(self) -> bool:
        return self._targetEnemies

    def set_targetEnemies(self, targetEnemies: bool) -> None:
        self._targetEnemies = targetEnemies

    @property
    def targetParty(self) -> bool:
        return self._targetParty

    def set_targetParty(self, targetParty: bool) -> None:
        self._targetParty = targetParty

    @property
    def targetWounded(self) -> bool:
        return self._targetWounded

    def set_targetWounded(self, targetWounded: bool) -> None:
        self._targetWounded = targetWounded

    @property
    def targetOneParty(self) -> bool:
        return self._targetOneParty

    def set_targetOneParty(self, targetOneParty: bool) -> None:
        self._targetOneParty = targetOneParty

    @property
    def targetNotSelf(self) -> bool:
        return self._targetNotSelf

    def set_targetNotSelf(self, targetNotSelf: bool) -> None:
        self._targetNotSelf = targetNotSelf

    @property
    def status_effects(self) -> List[SpellStatusEffects]:
        return deepcopy(self._status_effects)

    def set_status_effects(self, status_effects: List[SpellStatusEffects]) -> None:
        self._status_effects = deepcopy(status_effects)

    @property
    def boosts(self) -> List[SpellBoosts]:
        return deepcopy(self._boosts)

    def set_boosts(self, boosts: List[SpellBoosts]) -> None:
        assert len(boosts) == len(set(boosts))
        self._boosts = deepcopy(boosts)

    @property
    def world(self) -> GameWorld:
        assert self._world is not None
        return self._world

    def __init__(self, world: Optional[GameWorld] = None):
        self._world = world

        if len(self._status_effects) == 0:
            self._status_effects = []
        if len(self._boosts) == 0:
            self._boosts = []

    def __str__(self):
        return "<{}>".format(self.name)

    def __repr__(self):
        return str(self)

    @property
    def name(self):
        return self.__class__.__name__

    def get_patch(self):
        """Get patch for this spell.

        :return: Patch data.
        :rtype: randomizer.logic.patch.Patch
        """
        patch = Patch()

        # FP is byte 3, power is byte 6, hit rate is byte 7.  Each spell is 12 bytes.
        base_addr = SPELL_BASE_ADDRESS + (self.index * 12)
        patch.add_data(
            base_addr,
            (self.checkStats * 0x01)
            + (self.ignoreDefense * 0x02)
            + (self.checkOHKO * 0x20)
            + (self.overworldUsable * 0x80),
        )
        if self.spell_type is None:
            st = 0
        else:
            st = self.spell_type.value
        if self.effect_type is None:
            et = 0
        else:
            et = self.effect_type.value
        if self.element is None:
            el = 0
        else:
            el = self.element.value
        if self.inflict is None:
            iv = 0xFF
        else:
            iv = self.inflict.value
        patch.add_data(base_addr + 1, st + et + (self.quad9s * 0x08))
        patch.add_data(base_addr + 2, utils.ByteField(self.fp).as_bytes())
        patch.add_data(
            base_addr + 3,
            (self.targetOthers * 0x02)
            + (self.targetEnemies * 0x04)
            + (self.targetParty * 0x10)
            + (self.targetWounded * 0x20)
            + (self.targetOneParty * 0x40)
            + (self.targetNotSelf * 0x80),
        )
        patch.add_data(base_addr + 4, el)
        data = utils.ByteField(self.power).as_bytes()
        data += utils.ByteField(self.hit_rate).as_bytes()
        patch.add_data(base_addr + 5, data)
        effects = 0
        for i in self.status_effects:
            effects += 2**i
        patch.add_data(base_addr + 7, effects)
        buffs = 0
        for i in self.boosts:
            buffs += 2**i
        patch.add_data(base_addr + 8, buffs)
        patch.add_data(base_addr + 10, iv)
        patch.add_data(base_addr + 11, (self.hideNum * 0x04))

        return patch


class CharacterSpell(Spell, SpellLearn):
    """Grouping class for character-specific spells."""

    base_title: str = ""

    _timing_modifiers = TimingProperties(0)
    _damage_modifiers = DamageModifiers(0)

    @property
    def timing_modifiers(self) -> TimingProperties:
        return self._timing_modifiers

    def set_timing_modifiers(self, timing_modifiers: TimingProperties) -> None:
        self._timing_modifiers = timing_modifiers

    @property
    def damage_modifiers(self) -> DamageModifiers:
        return self._damage_modifiers

    def set_damage_modifiers(self, damage_modifiers: DamageModifiers) -> None:
        self._damage_modifiers = damage_modifiers

    def get_patch(self):
        """Get patch for this spell.

        :return: Patch data.
        :rtype: randomizer.logic.patch.Patch
        """
        patch = super().get_patch()

        name_bytes = "\x40" + self.title
        name_bytes += " " * (15 - len(name_bytes))
        patch.add_data(SPELL_BASE_NAME_ADDRESS + (self.index * 15), name_bytes)
        if self.timing_modifiers != 0:
            patch.add_data(
                SPELL_TIMING_MODIFIERS_BASE_ADDRESS + self.index * 2,
                utils.ByteField(self.timing_modifiers).as_bytes(),
            )
        if self.damage_modifiers != 0:
            patch.add_data(
                SPELL_DAMAGE_MODIFIERS_BASE_ADDRESS + self.index * 2,
                utils.ByteField(self.damage_modifiers).as_bytes(),
            )

        return patch


class CloneSpell(CharacterSpell):
    """Spell class that allows an ally spell to be repeated with a different name."""

    _ref_ptr: int = 0
    _parent_spell: Type[CharacterSpell]

    def set_title(self, title: str) -> None:
        self._title = title

    @property
    def ref_ptr(self) -> int:
        return self._ref_ptr

    def set_ref_ptr(self, ref_ptr: int) -> None:
        self._ref_ptr = ref_ptr

    def set_desc_ptr(self, desc_ptr: int) -> None:
        self._desc_ptr = desc_ptr

    @property
    def parent_spell(self) -> Type[CharacterSpell]:
        return self._parent_spell

    def _set_parent_spell(self, parent_spell: Type[CharacterSpell]) -> None:
        self._parent_spell = parent_spell

    def __init__(self, world: Optional[GameWorld], title: str, spell: CharacterSpell):
        super().__init__(world)
        self.set_title(title)
        self.set_fp(spell.fp)
        self.set_power(spell.power)
        self.set_hit_rate(spell.hit_rate)
        self.set_ref_ptr(spell.anim_ptr)
        self.set_desc_ptr(spell.desc_ptr)
        self.set_checkStats(spell.checkStats)
        self.set_ignoreDefense(spell.ignoreDefense)
        self.set_checkOHKO(spell.checkOHKO)
        self.set_overworldUsable(spell.overworldUsable)
        self.set_spell_type(spell.spell_type)
        self.set_effect_type(spell.effect_type)
        self.set_quad9s(spell.quad9s)
        self.set_targetOthers(spell.targetOthers)
        self.set_targetEnemies(spell.targetEnemies)
        self.set_targetParty(spell.targetParty)
        self.set_targetWounded(spell.targetWounded)
        self.set_targetOneParty(spell.targetOneParty)
        self.set_targetNotSelf(spell.targetNotSelf)
        self.set_element(spell.element)
        self.set_status_effects(spell.status_effects)
        self.set_boosts(spell.boosts)
        self.set_inflict(spell.inflict)
        self.set_hideNum(spell.hideNum)
        self.set_timing_modifiers(spell.timing_modifiers)
        self.set_damage_modifiers(spell.damage_modifiers)
        self._set_parent_spell(type(spell))

    def get_patch(self):
        """Get patch for this spell.

        :return: Patch data.
        :rtype: randomizer.logic.patch.Patch
        """
        patch = super().get_patch()

        patch.add_data(
            0x35C992 + self.index * 2,
            utils.ByteField(UInt16(self.ref_ptr & 0xFFFF)).as_bytes(),
        )
        patch.add_data(
            0x3A2B80 + self.index * 2,
            utils.ByteField(UInt16(self.desc_ptr & 0xFFFF)).as_bytes(),
        )

        return patch


class EnemySpell(Spell):
    """Grouping class for enemy-specific spells."""

    @property
    def title(self):
        return self.__class__.__name__

    def get_patch(self):
        """Get patch for this spell.

        Returns:
            randomizer.logic.patch.Patch: Patch data.

        """
        patch = super().get_patch()

        # Add status effects for enemy attacks, if any.
        base_addr = SPELL_BASE_ADDRESS + (self.index * 12)
        data = utils.BitMapSet(1, self.status_effects).as_bytes()
        patch.add_data(base_addr + 7, data)

        return patch
