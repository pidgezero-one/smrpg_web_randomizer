from randomizer.types.spell import (CharacterSpell, palette_to_bytes)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (NO_MODIFIERS)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (
    ONE_TIMING_FOR_125_OR_15X_DMG,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class CrusherSpell(CharacterSpell):
    _index = 14
    _title = "Crusher"
    _prefix = ItemPrefix.STAR
    _fp = 12
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
    _target_others = True
    _target_enemies = True
    _target_party = False
    _target_wounded = False
    _target_one_party = True
    _target_not_self = False
    _timing_modifiers = ONE_TIMING_FOR_125_OR_15X_DMG
    _damage_modifiers = NO_MODIFIERS
    _description = ' Rock slide!\n Hit "Y" prior\n to contact!'

    @property
    def title(self) -> str:
        if self.element == Element.FIRE:
            return "Fire Crusher"
        elif self.element == Element.ICE:
            return "Ice Crusher"
        elif self.element == Element.THUNDER:
            return "ThndrCrusher"
        else:
            return self._title
        
    @property
    def description(self) -> str:
        if self.element == Element.FIRE:
            return ' Fire rock slide!\n Hit "Y" prior\n to contact!'
        elif self.element == Element.ICE:
            return ' Ice rock slide!\n Hit "Y" prior\n to contact!'
        elif self.element == Element.THUNDER:
            return ' Thunder rock\n slide! Hit "Y"\n prior to contact!'
        else:
            return self._description

    @property
    def palette_patch(self) -> dict[int, bytearray]:
        d = {}
        if self.element == Element.THUNDER:
            d[0x331A3D] = palette_to_bytes([0xF8F8E0, 0xF8F0C0, 0xF8F0B0, 0xF8F098, 0xF8E880, 0xF0E860, 0xF0E050, 0xF0E040, 0xF0E028, 0xF0D810, 0xC0B008, 0xB0A008, 0xA8A008, 0x989008, 0xF8F0A8])
        elif self.element == Element.ICE:
            d[0x331A3D] = palette_to_bytes([0x88D8D8, 0x70C8C8, 0x60C8C8, 0x50C0C0, 0x40B8B8, 0x30A0A0, 0x309090, 0x288888, 0x207078, 0x206060, 0x103838, 0x082830, 0x082828, 0x081818, 0x88D8D8])
        elif self.element == Element.FIRE:
            d[0x331A3D] = palette_to_bytes([0xD88888, 0xC87070, 0xC86060, 0xC05050, 0xB84040, 0xA03030, 0x903030, 0x882828, 0x782020, 0x602020, 0x381010, 0x300808, 0x280808, 0x180808, 0xD88888])
        return d


__all__ = ["CrusherSpell"]
