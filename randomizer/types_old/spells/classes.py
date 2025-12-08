"""Base classes fors spells."""

from typing import TYPE_CHECKING

from randomizer.types.items import SpellLearn
from randomizer.types.numbers import  ByteField, UInt16, UInt8
from randomizer.types.patch import Patch

from .ids.misc import (
    ALLY_SPELL_POINTER_TABLE_START,
    SPELL_BASE_DESC_ADDRESS)


if TYPE_CHECKING:
    from randomizer.types.world import GameWorld

class CharacterSpell(TODOImportCharacterSpell, SpellLearn):
    """Grouping class for character-specific spells."""

    _world: "GameWorld" | None = None
    
    @property
    def world(self) -> "GameWorld":
        """The seed's game world instance."""
        assert self._world is not None
        return self._world
    
    def __init__(self):
        super().__init__()
        self._world = world


class CloneSpell(CharacterSpell):
    """Spell class that allows an ally spell to be repeated with a different name."""

    _ref_ptr: int = 0
    _parent_spell: CharacterSpell

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
    def parent_spell(self) -> CharacterSpell:
        """The spell that this is a clone of."""
        return self._parent_spell

    def set_parent_spell(self, parent_spell: CharacterSpell) -> None:
        """Designate which spell this is a clone of."""
        self._parent_spell = parent_spell

    @property
    def fp(self) -> UInt8:
        """The FP cost of this spell."""
        return self._parent_spell.fp

    @property
    def power(self) -> UInt8:
        """The base power of this spell."""
        return self._parent_spell.power

    @property
    def hit_rate(self) -> UInt8:
        """The likelihood that this spell will hit a target."""
        return self._parent_spell.hit_rate

    @property
    def index(self) -> UInt8:
        """The ID of this spell as known to SMRPG."""
        return UInt8(self._index)

    @property
    def anim_ptr(self) -> int:
        """The pointer for where the spell's animation begins.
        TODO: (deprecate this)"""
        return self._parent_spell.anim_ptr

    @property
    def desc_ptr(self) -> int:
        """The pointer for where the spell's description begins."""
        return self._parent_spell.desc_ptr

    @property
    def spell_type(self) -> SpellType:
        """Damage vs. heal."""
        return self._parent_spell.spell_type

    @property
    def effect_type(self) -> EffectType:
        """Inflict vs. nullify."""
        return self._parent_spell.effect_type

    @property
    def inflict(self) -> InflictFunction:
        """A special property of the spell on contact, i.e. jump counter."""
        return self._parent_spell.inflict

    @property
    def element(self) -> Element:
        """The spell's infused element."""
        return self._parent_spell.element

    @property
    def check_stats(self) -> bool:
        """(unknown)"""
        return self._parent_spell.check_stats

    @property
    def ignore_defense(self) -> bool:
        """If true, the target's defense is not factored into output calculation."""
        return self._parent_spell.ignore_defense

    @property
    def check_ohko(self) -> bool:
        """(unknown)"""
        return self._parent_spell.check_ohko

    @property
    def usable_outside_of_battle(self) -> bool:
        """If true, the spell can be used in the X menu when not in battle."""
        return self._parent_spell.usable_outside_of_battle

    @property
    def quad9s(self) -> bool:
        """If true, the spell does max damage."""
        return self._parent_spell.quad9s

    @property
    def hide_num(self) -> bool:
        """If true, the damage output will not be shown."""
        return self._parent_spell.hide_num

    @property
    def target_others(self) -> bool:
        """If true, this spell targets all possible targets instead of just one."""
        return self._parent_spell.target_others

    @property
    def target_enemies(self) -> bool:
        """If true, this spell targets opponents."""
        return self._parent_spell.target_enemies

    @property
    def target_party(self) -> bool:
        """If true, this spell targets your own party."""
        return self._parent_spell.target_party

    @property
    def target_wounded(self) -> bool:
        """If true, this spell targets party members who are KOed."""
        return self._parent_spell.target_wounded

    @property
    def target_one_party(self) -> bool:
        """(unknown)"""
        return self._parent_spell.target_one_party

    @property
    def target_not_self(self) -> bool:
        """If true, the caster is excluded from targeting."""
        return self._parent_spell.target_not_self

    @property
    def status_effects(self) -> list[Status]:
        """A list of status effects inflicted by this spell."""
        return self._parent_spell.status_effects

    @property
    def boosts(self) -> list[TempStatBuff]:
        """A list of stat boosts applied by this spell."""
        return self._parent_spell.boosts

    @property
    def world(self) -> "GameWorld":
        """The seed's game world instance."""
        assert self._world is not None
        return self._world

    def __str__(self):
        return f"<{self.name}>"

    def __repr__(self):
        return str(self)

    @property
    def name(self) -> str:
        """The class name of this spell."""
        return self.__class__.__name__

    def __init__(self, world: "GameWorld", spell: CharacterSpell | None):
        super().__init__(world)
        if spell is not None:
            original_spell = world.get_spell_instance(type(spell))
            assert isinstance(original_spell, CharacterSpell)
            self.set_parent_spell(original_spell)

    def get_patch(self) -> Patch:
        """Get patch for this spell."""
        patch = super().get_patch()

        patch.add_data(
            ALLY_SPELL_POINTER_TABLE_START + self.index * 2,
            ByteField(UInt16(self.ref_ptr & 0xFFFF)).as_bytes())
        patch.add_data(
            SPELL_BASE_DESC_ADDRESS + self.index * 2,
            ByteField(UInt16(self.desc_ptr & 0xFFFF)).as_bytes())

        return patch

