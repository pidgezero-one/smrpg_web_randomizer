from randomizer.types.spell import (CharacterSpell)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (NO_MODIFIERS)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (
    TIMED_HEALS_ALL_HP_TO_FIRST_TARGET,
)
from smrpgpatchbuilder.datatypes.spells.enums import (
    Element,
    InflictFunction,
    SpellType,
)


class ComeBackSpell(CharacterSpell):
    _index = 9
    _title = "Come Back"
    _prefix = ItemPrefix.STAR
    _fp = 2
    _power = 0
    _hit_rate = 100
    _spell_type = SpellType.HEAL
    _element = Element.NONE
    _inflict = InflictFunction.REVIVE
    _check_stats = False
    _ignore_defense = True
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = False
    _target_party = False
    _target_wounded = True
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = TIMED_HEALS_ALL_HP_TO_FIRST_TARGET
    _damage_modifiers = NO_MODIFIERS
    _description = " Revive one...\n or more pals!"


__all__ = ["ComeBackSpell"]
