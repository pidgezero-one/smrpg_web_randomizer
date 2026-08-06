from randomizer.types.spell import (EnemySpell)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class MegaDrainSpell(EnemySpell):
    _index = 70
    _title = " Mega Drain"
    _fp = 7
    _power = 40
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _element = Element.FIRE
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

    _remake_name = " Fire Saber"


__all__ = ["MegaDrainSpell"]
