from randomizer.types.spell import (CharacterSpell)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (NO_MODIFIERS)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (
    TIMED_FOR_9999_SET_ENEMY_HP_0,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class GenoWhirlSpell(CharacterSpell):
    _index = 18
    _title = "Geno Whirl"
    _prefix = ItemPrefix.STAR
    _fp = 8
    _power = 45
    _hit_rate = 100
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
    _timing_modifiers = TIMED_FOR_9999_SET_ENEMY_HP_0
    _damage_modifiers = NO_MODIFIERS
    _description = ' Press "Y" prior\nto contact for\ncritical hit!'


__all__ = ["GenoWhirlSpell"]
