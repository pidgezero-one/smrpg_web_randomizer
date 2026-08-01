from randomizer.types.spell import (CharacterSpell)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (NO_MODIFIERS)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (
    ONE_TIMING_FOR_125_OR_15X_DMG,
)
from smrpgpatchbuilder.datatypes.spells.enums import (
    Element,
    InflictFunction,
    SpellType,
)


class JumpSpell(CharacterSpell):
    _index = 0
    _title = "Jump"
    _prefix = ItemPrefix.STAR
    _fp = 3
    _power = 25
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.JUMP
    _inflict = InflictFunction.INC_JUMP
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
    _timing_modifiers = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers = NO_MODIFIERS
    _description = ' Stomp foes! Press "Y" just before hit!'

    @property
    def title(self) -> str:
        if self.element == Element.FIRE:
            return "Fire Jump"
        elif self.element == Element.ICE:
            return "Ice Jump"
        elif self.element == Element.THUNDER:
            return "Thunder Jump"
        else:
            return self._title
        
    @property
    def description(self) -> str:
        if self.element == Element.FIRE:
            return ' Stomp foes with\n fire! Press "Y"\n just before hit!'
        elif self.element == Element.ICE:
            return ' Stomp foes with\n ice! Press "Y"\n just before hit!'
        elif self.element == Element.THUNDER:
            return ' Stomp foes with\n thunder! Press\n "Y" just\n before hit!'
        else:
            return self._description


__all__ = ["JumpSpell"]
