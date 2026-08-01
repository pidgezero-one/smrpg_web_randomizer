from randomizer.types.spell import (CharacterSpell)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (NO_MODIFIERS)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (
    TIME_TO_ACTIVATE_HP_READ,
)
from smrpgpatchbuilder.datatypes.spells.enums import (
    Element,
    InflictFunction,
    SpellType,
)


class PsychopathSpell(CharacterSpell):
    _index = 23
    _title = "Psychopath"
    _prefix = ItemPrefix.STAR
    _fp = 1
    _power = 0
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _inflict = InflictFunction.SCAN
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = True
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = TIME_TO_ACTIVATE_HP_READ
    _damage_modifiers = NO_MODIFIERS
    _description = " See foe's HP\n and...secrets!"

    _remake_name = "Thought Peek"


__all__ = ["PsychopathSpell"]
