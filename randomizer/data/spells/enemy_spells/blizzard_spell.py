from randomizer.types.spell import (EnemySpell)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class BlizzardSpell(EnemySpell):
    _index = 84
    _title = " Blizzard"
    _fp = 8
    _power = 22
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


__all__ = ["BlizzardSpell"]
