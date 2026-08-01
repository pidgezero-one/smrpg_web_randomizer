from randomizer.types.spell import (CharacterSpell)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (X05_MODIFIER)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (
    MULTIPLE_BUTTON_PRESSES,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class SuperJumpSpell(CharacterSpell):
    _index = 2
    _title = "Super Jump"
    _prefix = ItemPrefix.STAR
    _fp = 7
    _power = 45
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
    _timing_modifiers = MULTIPLE_BUTTON_PRESSES
    _damage_modifiers = X05_MODIFIER
    _description = ' Push "Y"\n prior to hit\n for DAMAGE!'

    @property
    def title(self) -> str:
        if self.element == Element.FIRE:
            return "Fire S.Jump"
        elif self.element == Element.ICE:
            return "Ice S.Jump"
        elif self.element == Element.THUNDER:
            return "Thndr S.Jump"
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


__all__ = ["SuperJumpSpell"]
