from randomizer.types.spell import (CharacterSpell)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (
    X00625_MODIFIER,
)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (ROTATE_ONLY)
from smrpgpatchbuilder.datatypes.spells.enums import (
    EffectType,
    Element,
    SpellType,
    Status,
)


class PoisonGasSpell(CharacterSpell):
    _index = 13
    _title = "Poison Gas"
    _prefix = ItemPrefix.STAR
    _fp = 10
    _power = 20
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
    _status_effects = [Status.POISON]
    _timing_modifiers = ROTATE_ONLY
    _damage_modifiers = X00625_MODIFIER
    _description = " Poison foes!"


__all__ = ["PoisonGasSpell"]
