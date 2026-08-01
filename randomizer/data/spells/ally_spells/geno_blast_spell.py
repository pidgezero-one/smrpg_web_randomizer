from randomizer.types.spell import (CharacterSpell)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (NO_MODIFIERS)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (CHARGE_ONLY)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class GenoBlastSpell(CharacterSpell):
    _index = 19
    _title = "Geno Blast"
    _prefix = ItemPrefix.STAR
    _fp = 12
    _power = 50
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
    _timing_modifiers = CHARGE_ONLY
    _damage_modifiers = NO_MODIFIERS
    _description = " Beam hits\n all foes!\n Energize!"


__all__ = ["GenoBlastSpell"]
