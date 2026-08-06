from randomizer.types.spell import (EnemySpell)
from smrpgpatchbuilder.datatypes.spells.enums import (
    Element,
    InflictFunction,
    SpellType,
)


class EscapeSpell(EnemySpell):
    _index = 77
    _title = " Escape"
    _fp = 0
    _power = 0
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
    _inflict = InflictFunction.NO_DMG
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False


__all__ = ["EscapeSpell"]
