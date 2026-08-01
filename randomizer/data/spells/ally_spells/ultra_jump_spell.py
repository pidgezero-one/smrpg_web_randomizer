from randomizer.types.spell import (CharacterSpell)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (
    X0125_MODIFIER_WITH_MULTI_TARGETING,
)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (
    ONE_PLUS_MORE_TARGETS_WITH_PRESSES,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class UltraJumpSpell(CharacterSpell):
    _index = 4
    _title = "Ultra Jump"
    _prefix = ItemPrefix.STAR
    _fp = 11
    _power = 65
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.JUMP
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
    _timing_modifiers = ONE_PLUS_MORE_TARGETS_WITH_PRESSES
    _damage_modifiers = X0125_MODIFIER_WITH_MULTI_TARGETING
    _description = ' Push "Y"\n prior to hit\n for DAMAGE!'

    @property
    def title(self) -> str:
        if self.element == Element.FIRE:
            return "Fire U.Jump"
        elif self.element == Element.ICE:
            return "Ice U.Jump"
        elif self.element == Element.THUNDER:
            return "Thndr U.Jump"
        else:
            return self._title
        
    @property
    def description(self) -> str:
        if self.element == Element.FIRE:
            return ' Push "Y"\n prior to hit for\n FIRE DAMAGE!'
        elif self.element == Element.ICE:
            return ' Push "Y"\n prior to hit for\n ICE DAMAGE!'
        elif self.element == Element.THUNDER:
            return ' Push "Y"\n prior to hit for\n THUNDER\n DAMAGE!'
        else:
            return self._description


__all__ = ["UltraJumpSpell"]
