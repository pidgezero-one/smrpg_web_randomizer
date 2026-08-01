from randomizer.types.spell import (EnemySpell)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class ElectroshockSpell(EnemySpell):
    _index = 73
    _title = " Electroshock"
    _fp = 10
    _power = 72
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.THUNDER
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


__all__ = ["ElectroshockSpell"]
