from randomizer.types.spell import (CharacterSpell)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (
    X00625_MODIFIER,
)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (BUTTON_MASH)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class BowserCrushSpell(CharacterSpell):
    _index = 15
    _title = "Bowser Crush"
    _prefix = ItemPrefix.STAR
    _fp = 16
    _power = 58
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
    _timing_modifiers = BUTTON_MASH
    _damage_modifiers = X00625_MODIFIER
    _description = " Bowser's\n ultimate weapon!"

    _remake_name = "Mecha Stomp"

    @property
    def title(self) -> str:
        if self.element == Element.FIRE:
            return "Fire Crush"
        elif self.element == Element.ICE:
            return "Ice Crush"
        elif self.element == Element.THUNDER:
            return "ThunderCrush"
        else:
            return self._title

    @property
    def remake_name(self) -> str:
        if self.element == Element.FIRE:
            return "Fire Stomp"
        elif self.element == Element.ICE:
            return "Ice Stomp"
        elif self.element == Element.THUNDER:
            return "ThunderStomp"
        else:
            return self._remake_name or self.title
        
    @property
    def description(self) -> str:
        if self.element == Element.FIRE:
            return " Bowser's\n ultimate fire\n weapon!"
        elif self.element == Element.ICE:
            return " Bowser's\n ultimate ice\n weapon!"
        elif self.element == Element.THUNDER:
            return " Bowser's\n ultimate thunder\n weapon!"
        else:
            return self._description

    @property
    def palette_patch(self) -> dict[int, bytearray]:
        # Bowser Crush is a hardware screen effect (HDMA color math against the
        # BG), not a sprite-palette effect. The visible green tint is generated
        # per-scanline by the color-math pipeline, so a CGRAM patch can't recolor
        # it. Element variation is conveyed via sound only.
        return {}


__all__ = ["BowserCrushSpell"]
