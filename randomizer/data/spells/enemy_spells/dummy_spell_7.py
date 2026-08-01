from randomizer.types.spell import (EnemySpell)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class DummySpell7(EnemySpell):
    _index = 33
    _title = "Dummy"
    _prefix = ItemPrefix.EMPTY_SPACE
    _fp = 15
    _power = 60
    _hit_rate = 80
    _spell_type = SpellType.DAMAGE
    _element = Element.NONE
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


__all__ = ["DummySpell7"]
