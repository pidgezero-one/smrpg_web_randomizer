"""Base classes fors spells."""

from copy import deepcopy
from typing import List, Optional, Type, TYPE_CHECKING

from randomizer.types.items import SpellLearn
from randomizer.types.numbers import BitMapSet, ByteField, UInt16, UInt8
from randomizer.types.patch import Patch

from .arguments.types import DamageModifiers, TimingProperties
from .ids.misc import (
    SPELL_BASE_ADDRESS,
    SPELL_BASE_NAME_ADDRESS,
    SPELL_DAMAGE_MODIFIERS_BASE_ADDRESS,
    SPELL_TIMING_MODIFIERS_BASE_ADDRESS,
    ALLY_SPELL_POINTER_TABLE_START,
    SPELL_BASE_DESC_ADDRESS,
)
from .enums import (
    EffectType,
    InflictFunction,
    Element,
    Status,
    SpellType,
    TempStatBuff,
)


if TYPE_CHECKING:
    from randomizer.types.world import GameWorld


class Spell:
    """Class representing a magic spell to be randomized."""

    # Default per-spell attributes.
    _index: int = 0
    _fp: int = 0
    _power: int = 0
    _hit_rate: int = 0

    _title: str = ""

    _anim_ptr: int = 0
    _desc_ptr: int = 0

    _spell_type: SpellType = SpellType.DAMAGE
    _effect_type: EffectType
    _inflict: InflictFunction
    _element = Element.NONE

    _check_stats: bool = False
    _ignore_defense: bool = False
    _check_ohko: bool = False
    _usable_outside_of_battle: bool = False
    _quad9s: bool = False
    _hide_num: bool = False

    _target_others: bool = False
    _target_enemies: bool = False
    _target_party: bool = False
    _target_wounded: bool = False
    _target_one_party: bool = False
    _target_not_self: bool = False
    _status_effects: List[Status] = []
    _boosts: List[TempStatBuff] = []

    _world: Optional["GameWorld"] = None

    @property
    def fp(self) -> UInt8:
        """The FP cost of this spell."""
        return UInt8(self._fp)

    def set_fp(self, fp: int) -> None:
        """Set the FP cost of this spell."""
        assert 0 <= fp <= 31
        self._fp = fp

    @property
    def power(self) -> UInt8:
        """The base power of this spell."""
        return UInt8(self._power)

    def set_power(self, power: int) -> None:
        """Set the base power of this spell."""
        assert UInt8(power)
        self._power = power

    @property
    def hit_rate(self) -> UInt8:
        """The likelihood that this spell will hit a target."""
        return UInt8(self._hit_rate)

    def set_hit_rate(self, hit_rate: int) -> None:
        """Specify the likelihood that this spell will hit a target."""
        assert UInt8(hit_rate)
        self._hit_rate = hit_rate

    @property
    def index(self) -> UInt8:
        """The ID of this spell as known to SMRPG."""
        return UInt8(self._index)

    @property
    def title(self) -> str:
        """The name of this spell as it appears in-game."""
        return self._title

    @property
    def anim_ptr(self) -> int:
        """The pointer for where the spell's animation begins.
        (deprecate this)"""
        return self._anim_ptr

    @property
    def desc_ptr(self) -> int:
        """The pointer for where the spell's description begins."""
        return self._desc_ptr

    @property
    def spell_type(self) -> SpellType:
        """Damage vs. heal."""
        return self._spell_type

    def set_spell_type(self, spell_type: SpellType) -> None:
        """Damage vs. heal."""
        self._spell_type = spell_type

    @property
    def effect_type(self) -> EffectType:
        """Inflict vs. nullify."""
        return self._effect_type

    def set_effect_type(self, effect_type: EffectType) -> None:
        """Inflict vs. nullify."""
        self._effect_type = effect_type

    @property
    def inflict(self) -> InflictFunction:
        """A special property of the spell on contact, i.e. jump counter."""
        return self._inflict

    def set_inflict(self, inflict: InflictFunction) -> None:
        """A special property of the spell on contact, i.e. jump counter."""
        self._inflict = inflict

    @property
    def element(self) -> Element:
        """The spell's infused element."""
        return self._element

    def set_element(self, element: Element) -> None:
        """Choose the spell's infused element."""
        self._element = element

    @property
    def check_stats(self) -> bool:
        """(unknown)"""
        return self._check_stats

    def set_check_stats(self, check_stats: bool) -> None:
        """(unknown)"""
        self._check_stats = check_stats

    @property
    def ignore_defense(self) -> bool:
        """If true, the target's defense is not factored into output calculation."""
        return self._ignore_defense

    def set_ignore_defense(self, ignore_defense: bool) -> None:
        """If true, the target's defense is not factored into output calculation."""
        self._ignore_defense = ignore_defense

    @property
    def check_ohko(self) -> bool:
        """(unknown)"""
        return self._check_ohko

    def set_check_ohko(self, check_ohko: bool) -> None:
        """(unknown)"""
        self._check_ohko = check_ohko

    @property
    def usable_outside_of_battle(self) -> bool:
        """If true, the spell can be used in the X menu when not in battle."""
        return self._usable_outside_of_battle

    def set_usable_outside_of_battle(self, usable_outside_of_battle: bool) -> None:
        """If true, the spell can be used in the X menu when not in battle."""
        self._usable_outside_of_battle = usable_outside_of_battle

    @property
    def quad9s(self) -> bool:
        """If true, the spell does max damage."""
        return self._quad9s

    def set_quad9s(self, quad9s: bool) -> None:
        """If true, the spell does max damage."""
        self._quad9s = quad9s

    @property
    def hide_num(self) -> bool:
        """If true, the damage output will not be shown."""
        return self._hide_num

    def set_hide_num(self, hide_num: bool) -> None:
        """If true, the damage output will not be shown."""
        self._hide_num = hide_num

    @property
    def target_others(self) -> bool:
        """If true, this spell targets all possible targets instead of just one."""
        return self._target_others

    def set_target_others(self, target_others: bool) -> None:
        """If true, this spell targets all possible targets instead of just one."""
        self._target_others = target_others

    @property
    def target_enemies(self) -> bool:
        """If true, this spell targets opponents."""
        return self._target_enemies

    def set_target_enemies(self, target_enemies: bool) -> None:
        """If true, this spell targets opponents."""
        self._target_enemies = target_enemies

    @property
    def target_party(self) -> bool:
        """If true, this spell targets your own party."""
        return self._target_party

    def set_target_party(self, target_party: bool) -> None:
        """If true, this spell targets your own party."""
        self._target_party = target_party

    @property
    def target_wounded(self) -> bool:
        """If true, this spell targets party members who are KOed."""
        return self._target_wounded

    def set_target_wounded(self, target_wounded: bool) -> None:
        """If true, this spell targets party members who are KOed."""
        self._target_wounded = target_wounded

    @property
    def target_one_party(self) -> bool:
        """(unknown)"""
        return self._target_one_party

    def set_target_one_party(self, target_one_party: bool) -> None:
        """(unknown)"""
        self._target_one_party = target_one_party

    @property
    def target_not_self(self) -> bool:
        """If true, the caster is excluded from targeting."""
        return self._target_not_self

    def set_target_not_self(self, target_not_self: bool) -> None:
        """If true, the caster is excluded from targeting."""
        self._target_not_self = target_not_self

    @property
    def status_effects(self) -> List[Status]:
        """A list of status effects inflicted by this spell."""
        return deepcopy(self._status_effects)

    def set_status_effects(self, status_effects: List[Status]) -> None:
        """Overwrite the list of status effects inflicted by this spell."""
        self._status_effects = deepcopy(status_effects)

    @property
    def boosts(self) -> List[TempStatBuff]:
        """A list of stat boosts applied by this spell."""
        return deepcopy(self._boosts)

    def set_boosts(self, boosts: List[TempStatBuff]) -> None:
        """Overwrite the list of stat boosts applied by this spell."""
        assert len(boosts) == len(set(boosts))
        self._boosts = deepcopy(boosts)

    @property
    def world(self) -> "GameWorld":
        """The seed's game world instance."""
        assert self._world is not None
        return self._world

    def __init__(self, world: Optional["GameWorld"] = None):
        self._world = world

        if len(self._status_effects) == 0:
            self._status_effects = []
        if len(self._boosts) == 0:
            self._boosts = []

    def __str__(self):
        return f"<{self.name}>"

    def __repr__(self):
        return str(self)

    @property
    def name(self) -> str:
        """The class name of this spell."""
        return self.__class__.__name__

    def get_patch(self) -> Patch:
        """Get patch for this spell."""
        patch = Patch()

        # FP is byte 3, power is byte 6, hit rate is byte 7.  Each spell is 12 bytes.
        base_addr = SPELL_BASE_ADDRESS + (self.index * 12)
        patch.add_data(
            base_addr,
            (self.check_stats * 0x01)
            + (self.ignore_defense * 0x02)
            + (self.check_ohko * 0x20)
            + (self.usable_outside_of_battle * 0x80),
        )
        spell_type: int = 0
        effect_type: int = 0
        element: int = 0
        inflict_value: int = 0

        if self.spell_type is not None:
            spell_type = self.spell_type.value
        if self.effect_type is not None:
            effect_type = self.effect_type.value
        if self.element is not None:
            element = self.element.value
        if self.inflict is not None:
            inflict_value = self.inflict.value
        patch.add_data(base_addr + 1, spell_type + effect_type + (self.quad9s * 0x08))
        patch.add_data(base_addr + 2, ByteField(self.fp).as_bytes())
        patch.add_data(
            base_addr + 3,
            (self.target_others * 0x02)
            + (self.target_enemies * 0x04)
            + (self.target_party * 0x10)
            + (self.target_wounded * 0x20)
            + (self.target_one_party * 0x40)
            + (self.target_not_self * 0x80),
        )
        patch.add_data(base_addr + 4, element)
        data = ByteField(self.power).as_bytes()
        data += ByteField(self.hit_rate).as_bytes()
        patch.add_data(base_addr + 5, data)
        effects = 0
        for index in self.status_effects:
            effects += 2**index.spell_value
        patch.add_data(base_addr + 7, effects)
        buffs = 0
        for boost in self.boosts:
            buffs += 2**boost
        patch.add_data(base_addr + 8, buffs)
        patch.add_data(base_addr + 10, inflict_value)
        patch.add_data(base_addr + 11, (self.hide_num * 0x04))

        return patch


class CharacterSpell(Spell, SpellLearn):
    """Grouping class for character-specific spells."""

    base_title: str = ""

    _timing_modifiers: TimingProperties = TimingProperties(0)
    _damage_modifiers: DamageModifiers = DamageModifiers(0)

    @property
    def timing_modifiers(self) -> TimingProperties:
        """The preset timed hit behaviour of this spell."""
        return self._timing_modifiers

    def set_timing_modifiers(self, timing_modifiers: TimingProperties) -> None:
        """Set the preset timed hit behaviour of this spell."""
        self._timing_modifiers = timing_modifiers

    @property
    def damage_modifiers(self) -> DamageModifiers:
        """(unknown)"""
        return self._damage_modifiers

    def set_damage_modifiers(self, damage_modifiers: DamageModifiers) -> None:
        """(unknown)"""
        self._damage_modifiers = damage_modifiers

    def get_patch(self) -> Patch:
        """Get patch for this spell."""
        patch = super().get_patch()

        name_bytes = "\x40" + self.title
        name_bytes += " " * (15 - len(name_bytes))
        patch.add_data(SPELL_BASE_NAME_ADDRESS + (self.index * 15), name_bytes)
        if self.timing_modifiers != 0:
            patch.add_data(
                SPELL_TIMING_MODIFIERS_BASE_ADDRESS + self.index * 2,
                ByteField(self.timing_modifiers).as_bytes(),
            )
        if self.damage_modifiers != 0:
            patch.add_data(
                SPELL_DAMAGE_MODIFIERS_BASE_ADDRESS + self.index * 2,
                ByteField(self.damage_modifiers).as_bytes(),
            )

        return patch


class CloneSpell(CharacterSpell):
    """Spell class that allows an ally spell to be repeated with a different name."""

    _ref_ptr: int = 0
    _parent_spell: Type[CharacterSpell]

    def set_title(self, title: str) -> None:
        """Designate the in-game name of this clone spell"""
        self._title = title

    @property
    def ref_ptr(self) -> int:
        """(don't remember what this does)"""
        return self._ref_ptr

    def set_ref_ptr(self, ref_ptr: int) -> None:
        """(don't remember what this does)"""
        self._ref_ptr = ref_ptr

    def set_desc_ptr(self, desc_ptr: int) -> None:
        """Set the pointer for where the spell's description begins.\n
        Will be the same as a non-clone spell."""
        self._desc_ptr = desc_ptr

    @property
    def parent_spell(self) -> Type[CharacterSpell]:
        """The spell that this is a clone of."""
        return self._parent_spell

    def _set_parent_spell(self, parent_spell: Type[CharacterSpell]) -> None:
        """Designate which spell this is a clone of."""
        self._parent_spell = parent_spell

    def __init__(self, world: Optional["GameWorld"], title: str, spell: CharacterSpell):
        super().__init__(world)
        self.set_title(title)
        self.set_fp(spell.fp)
        self.set_power(spell.power)
        self.set_hit_rate(spell.hit_rate)
        self.set_ref_ptr(spell.anim_ptr)
        self.set_desc_ptr(spell.desc_ptr)
        self.set_check_stats(spell.check_stats)
        self.set_ignore_defense(spell.ignore_defense)
        self.set_check_ohko(spell.check_ohko)
        self.set_usable_outside_of_battle(spell.usable_outside_of_battle)
        self.set_spell_type(spell.spell_type)
        self.set_effect_type(spell.effect_type)
        self.set_quad9s(spell.quad9s)
        self.set_target_others(spell.target_others)
        self.set_target_enemies(spell.target_enemies)
        self.set_target_party(spell.target_party)
        self.set_target_wounded(spell.target_wounded)
        self.set_target_one_party(spell.target_one_party)
        self.set_target_not_self(spell.target_not_self)
        self.set_element(spell.element)
        self.set_status_effects(spell.status_effects)
        self.set_boosts(spell.boosts)
        self.set_inflict(spell.inflict)
        self.set_hide_num(spell.hide_num)
        self.set_timing_modifiers(spell.timing_modifiers)
        self.set_damage_modifiers(spell.damage_modifiers)
        self._set_parent_spell(type(spell))

    def get_patch(self) -> Patch:
        """Get patch for this spell."""
        patch = super().get_patch()

        patch.add_data(
            ALLY_SPELL_POINTER_TABLE_START + self.index * 2,
            ByteField(UInt16(self.ref_ptr & 0xFFFF)).as_bytes(),
        )
        patch.add_data(
            SPELL_BASE_DESC_ADDRESS + self.index * 2,
            ByteField(UInt16(self.desc_ptr & 0xFFFF)).as_bytes(),
        )

        return patch


class EnemySpell(Spell):
    """Grouping class for enemy-specific spells."""

    @property
    def title(self) -> str:
        return self.__class__.__name__

    def get_patch(self) -> Patch:
        """Get patch for this spell."""
        patch = super().get_patch()

        # Add status effects for enemy attacks, if any.
        base_addr = SPELL_BASE_ADDRESS + (self.index * 12)
        data = BitMapSet(1, self.status_effects).as_bytes()
        patch.add_data(base_addr + 7, data)

        return patch
