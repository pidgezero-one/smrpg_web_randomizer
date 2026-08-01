from randomizer.types.spell import (CharacterSpell)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (NO_MODIFIERS)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (
    ROTATE_1_TARGET_IF_TIMED_ALL,
)
from smrpgpatchbuilder.datatypes.spells.enums import (
    EffectType,
    Element,
    SpellType,
    Status,
)


class MuteSpell(CharacterSpell):
    _index = 10
    _title = "Mute"
    _prefix = ItemPrefix.STAR
    _fp = 3
    _power = 0
    _hit_rate = 99
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
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [Status.MUTE]
    _timing_modifiers = ROTATE_1_TARGET_IF_TIMED_ALL
    _damage_modifiers = NO_MODIFIERS
    _description = " Halt magic\n attack(s)!"


__all__ = ["MuteSpell"]
