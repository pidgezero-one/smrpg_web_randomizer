from randomizer.types.spell import (EnemySpell)
from smrpgpatchbuilder.datatypes.spells.enums import (
    EffectType,
    Element,
    SpellType,
    Status,
)


class SandStormSpell(EnemySpell):
    _index = 83
    _title = " Sand Storm"
    _fp = 6
    _power = 16
    _hit_rate = 90
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
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
    _status_effects = [Status.FEAR]


__all__ = ["SandStormSpell"]
