from randomizer.types.spell import (EnemySpell)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class DummySpell49(EnemySpell):
    _index = 116
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 3
    _power = 10
    _hit_rate = 99
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


__all__ = ["DummySpell49"]
