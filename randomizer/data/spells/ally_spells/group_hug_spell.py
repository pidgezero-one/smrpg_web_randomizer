from randomizer.types.spell import (CharacterSpell)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (NO_MODIFIERS)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (
    ONE_TIMING_FOR_125_DMG_ONLY,
)
from smrpgpatchbuilder.datatypes.spells.enums import (
    EffectType,
    Element,
    SpellType,
    Status,
)


class GroupHugSpell(CharacterSpell):
    _index = 7
    _title = "Group Hug"
    _prefix = ItemPrefix.STAR
    _fp = 4
    _power = 30
    _hit_rate = 100
    _spell_type = SpellType.HEAL
    _effect_type = EffectType.NULLIFY
    _element = Element.NONE
    _check_stats = False
    _ignore_defense = True
    _check_ohko = False
    _usable_outside_of_battle = True
    _quad9s = False
    _hide_num = False
    _target_others = False
    _target_enemies = False
    _target_party = True
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _status_effects = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
        Status.BERSERK,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]
    _timing_modifiers = ONE_TIMING_FOR_125_DMG_ONLY
    _damage_modifiers = NO_MODIFIERS
    _description = " Heal group!\n HP/status$"


__all__ = ["GroupHugSpell"]
