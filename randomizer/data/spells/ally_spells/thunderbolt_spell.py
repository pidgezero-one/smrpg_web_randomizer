from randomizer.types.spell import (CharacterSpell, palette_to_bytes)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (NO_MODIFIERS)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (
    ONE_TIMING_FOR_125_DMG_ONLY,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class ThunderboltSpell(CharacterSpell):
    _index = 21
    _title = "Thunderbolt"
    _prefix = ItemPrefix.STAR
    _fp = 2
    _power = 15
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.THUNDER
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
    _timing_modifiers = ONE_TIMING_FOR_125_DMG_ONLY
    _damage_modifiers = NO_MODIFIERS
    _description = ' Hit "Y" just\n before bolt\n ends!'

    @property
    def title(self) -> str:
        if self.element == Element.FIRE:
            return "Fire Bolt"
        elif self.element == Element.ICE:
            return "Ice Bolt"
        elif self.element == Element.JUMP:
            return "Earth Bolt"
        else:
            return self._title

    @property
    def description(self) -> str:
        if self.element == Element.FIRE:
            return ' Hit "Y" just\n before fire bolt\n ends!'
        elif self.element == Element.ICE:
            return ' Hit "Y" just\n before ice bolt\n ends!'
        elif self.element == Element.JUMP:
            return ' Hit "Y" just\n before earth\n bolt ends!'
        else:
            return self._description

    @property
    def palette_patch(self) -> dict[int, bytearray]:
        active = 0x33C40C
        d = {}
        if self.element == Element.JUMP:
            d[active] = palette_to_bytes([0xF01880, 0x008008, 0x00C820, 0xC0F800])
        elif self.element == Element.ICE:
            d[active] = palette_to_bytes([0xF01880, 0x0070A0, 0x00C8C8, 0x98F8F8])
        elif self.element == Element.FIRE:
            d[active] = palette_to_bytes([0xF01880, 0x880000, 0xC86000, 0xF8B800])
        return d


__all__ = ["ThunderboltSpell"]
