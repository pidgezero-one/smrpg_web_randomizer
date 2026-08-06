from randomizer.types.spell import (CharacterSpell)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (NO_MODIFIERS)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (
    TIMED_GIVES_TARGET_DEFENSE_UP_BUFF,
)
from smrpgpatchbuilder.datatypes.spells.enums import (
    EffectType,
    Element,
    SpellType,
    TempStatBuff,
)


class GenoBoostSpell(CharacterSpell):
    _index = 17
    _title = "Geno Boost"
    _prefix = ItemPrefix.STAR
    _fp = 4
    _power = 0
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _effect_type = EffectType.INFLICT
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = False
    _check_ohko = False
    _usable_outside_of_battle = False
    _quad9s = False
    _hide_num = True
    _target_others = True
    _target_enemies = False
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _boosts = [TempStatBuff(3), TempStatBuff(4)]
    _timing_modifiers = TIMED_GIVES_TARGET_DEFENSE_UP_BUFF
    _damage_modifiers = NO_MODIFIERS
    _description = ' Attack up!\n Push "Y" just\n before end!'


__all__ = ["GenoBoostSpell"]
