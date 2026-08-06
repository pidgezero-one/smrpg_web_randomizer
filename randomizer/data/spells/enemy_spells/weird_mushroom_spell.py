from randomizer.types.spell import (EnemySpell)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class WeirdMushroomSpell(EnemySpell):
    _index = 96
    _title = " Weird Mushroom"
    _fp = 0
    _power = 30
    _hit_rate = 100
    _spell_type = SpellType.HEAL
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = True
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = True
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


__all__ = ["WeirdMushroomSpell"]
