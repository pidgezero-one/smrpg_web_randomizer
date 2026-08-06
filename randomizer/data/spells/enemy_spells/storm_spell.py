from randomizer.types.spell import (EnemySpell)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class StormSpell(EnemySpell):
    _index = 75
    _title = " Storm"
    _fp = 12
    _power = 108
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
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


__all__ = ["StormSpell"]
