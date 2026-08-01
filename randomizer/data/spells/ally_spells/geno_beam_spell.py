from randomizer.types.spell import (CharacterSpell)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (NO_MODIFIERS)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (CHARGE_ONLY)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class GenoBeamSpell(CharacterSpell):
    _index = 16
    _title = "Geno Beam"
    _prefix = ItemPrefix.STAR
    _fp = 3
    _power = 40
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
    _timing_modifiers = CHARGE_ONLY
    _damage_modifiers = NO_MODIFIERS
    _description = ' Hold "Y" until\n just before\n discharge!'

    @property
    def title(self) -> str:
        if self.element == Element.FIRE:
            return "Fire Beam"
        elif self.element == Element.THUNDER:
            return "Thunder Beam"
        elif self.element == Element.JUMP:
            return "Earth Beam"
        else:
            return self._title

    @property
    def description(self) -> str:
        if self.element == Element.FIRE:
            return ' A fiery beam!\n Hold "Y" until\n just before\n discharge!'
        elif self.element == Element.THUNDER:
            return ' A thunderous beam!\n Hold "Y" until\n just before\n discharge!'
        elif self.element == Element.JUMP:
            return ' Earthen beam!\n Hold "Y" until\n just before\n discharge!'
        else:
            return self._description

    @property
    def palette_patch(self) -> dict[int, bytearray]:
        # not sure if this will actually work...
        offset = 0x251158
        d = {}
        if self.element == Element.JUMP:
            d[offset] = bytearray([0x04])
        elif self.element == Element.THUNDER:
            d[offset] = bytearray([0x03])
        elif self.element == Element.FIRE:
            d[offset] = bytearray([0x01])
        return d


__all__ = ["GenoBeamSpell"]
