from randomizer.types.spell import (CharacterSpell)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (
    X00625_MODIFIER,
)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (TIMED_JUMPS)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class StarRainSpell(CharacterSpell):
    _index = 26
    _title = "Star Rain"
    _prefix = ItemPrefix.STAR
    _fp = 14
    _power = 55
    _hit_rate = 100
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
    _timing_modifiers = TIMED_JUMPS
    _damage_modifiers = X00625_MODIFIER
    _description = ' Star showers!\n Hit "Y" just\n upon contact!'


__all__ = ["StarRainSpell"]
