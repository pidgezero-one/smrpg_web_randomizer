from randomizer.types.spell import (CharacterSpell)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (NO_MODIFIERS)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (CHARGE_ONLY)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class GenoFlashSpell(CharacterSpell):
    _index = 20
    _title = "Geno Flash"
    _prefix = ItemPrefix.STAR
    _fp = 16
    _power = 60
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
    _description = " Build power!\n Beam hits\n all foes!"

    @property
    def title(self) -> str:
        if self.element == Element.JUMP:
            return "Earth Flash"
        elif self.element == Element.ICE:
            return "Ice Flash"
        elif self.element == Element.THUNDER:
            return "ThunderFlash"
        else:
            return self._title
        
    @property
    def description(self) -> str:
        if self.element == Element.JUMP:
            return ' Build power!\n Earth beam hits\n all foes!'
        elif self.element == Element.ICE:
            return ' Build power!\n Ice beam hits\n all foes!'
        elif self.element == Element.THUNDER:
            return ' Build power!\n Thunder beam hits\n all foes!'
        else:
            return self._description

    @property
    def palette_patch(self) -> dict[int, bytearray]:
        # Geno Flash is a hardware screen effect (SEF0000_GENO_FLASH) - the sun
        # gradient is generated procedurally by the SA-1 color-math HDMA pipeline,
        # not from a CGRAM palette. Element variation is conveyed via sound only.
        return {}


__all__ = ["GenoFlashSpell"]
