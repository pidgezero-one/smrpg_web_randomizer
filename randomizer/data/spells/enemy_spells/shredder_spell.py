from randomizer.types.spell import (EnemySpell)
from smrpgpatchbuilder.datatypes.spells.enums import (
    EffectType,
    Element,
    SpellType,
    TempStatBuff,
)


class ShredderSpell(EnemySpell):
    _index = 98
    _title = " Shredder"
    _fp = 8
    _power = 0
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.NULLIFY
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = True
    _target_others = False
    _target_enemies = True
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _boosts = [TempStatBuff(3), TempStatBuff(4), TempStatBuff(5), TempStatBuff(6)]


__all__ = ["ShredderSpell"]
