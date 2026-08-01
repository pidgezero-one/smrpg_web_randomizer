from randomizer.types.spell import (CharacterSpell, palette_to_bytes)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (NO_MODIFIERS)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (
    ONE_TIMING_FOR_125_OR_15X_DMG,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class ShockerSpell(CharacterSpell):
    _index = 24
    _title = "Shocker"
    _prefix = ItemPrefix.STAR
    _fp = 8
    _power = 60
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.THUNDER
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
    _description = ' Hit "Y" just\n before bolt\n ends!'

    @property
    def title(self) -> str:
        if self.element == Element.FIRE:
            return "Fire Shocker"
        elif self.element == Element.ICE:
            return "Ice Shocker"
        elif self.element == Element.JUMP:
            return "EarthShocker"
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
        active = 0x330BB8
        d = {}
        if self.element == Element.JUMP:
            d[active] = palette_to_bytes(
                [
                    0x000000,
                    0xA0F8A0,
                    0x50F850,
                    0x00F800,
                    0x00F800,
                    0x00E800,
                    0x00C800,
                    0x00A800,
                    0x008000,
                    0x007800,
                    0x004000,
                    0x004800,
                    0x002000,
                    0x001010,
                ]
            )
        elif self.element == Element.ICE:
            d[active] = palette_to_bytes(
                [
                    0x000000,
                    0xF8E0E0,
                    0xC0F8F8,
                    0xA0F8F8,
                    0x80F8F8,
                    0x60F8F8,
                    0x48F8F8,
                    0x00B0B0,
                    0x008080,
                    0x007878,
                    0x004040,
                    0x004848,
                    0x002020,
                    0x001010,
                ]
            )
        elif self.element == Element.FIRE:
            d[active] = palette_to_bytes(
                [
                    0x000000,
                    0xF8E0E0,
                    0xF8C0C0,
                    0xF8A0A0,
                    0xF88080,
                    0xF86060,
                    0xF84848,
                    0xB00000,
                    0x800000,
                    0x780000,
                    0x400000,
                    0x480000,
                    0x200000,
                    0x100000,
                ]
            )
        return d


__all__ = ["ShockerSpell"]
