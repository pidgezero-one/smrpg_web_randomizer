from randomizer.types.spell import (EnemySpell)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class SolidifySpell(EnemySpell):
    _index = 89
    _title = " Solidify"
    _fp = 15
    _power = 47
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.ICE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


__all__ = ["SolidifySpell"]
