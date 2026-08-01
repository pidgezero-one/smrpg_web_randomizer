from randomizer.types.spell import (CharacterSpell, palette_to_bytes)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (
    X00625_MODIFIER,
)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (
    MULTIPLE_BUTTON_PRESSES,
)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class SuperFlameSpell(CharacterSpell):
    _index = 3
    _title = "Super Flame"
    _prefix = ItemPrefix.STAR
    _fp = 9
    _power = 40
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.FIRE
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
    _damage_modifiers = X00625_MODIFIER
    _description = ' Fire blast!\n Push "Y"\n repeatedly!'

    _remake_name = "SuperFireball"

    @property
    def title(self) -> str:
        if self.element == Element.JUMP:
            return "Super Earth"
        elif self.element == Element.ICE:
            return "Super Ice"
        elif self.element == Element.THUNDER:
            return "SuperThunder"
        else:
            return self._title

    @property
    def remake_name(self) -> str:
        if self.element == Element.JUMP:
            return "S. EarthBall"
        elif self.element == Element.ICE:
            return "S. Ice Ball"
        elif self.element == Element.THUNDER:
            return "S. ThndrBall"
        else:
            return self._remake_name or self.title

    @property
    def description(self) -> str:
        if self.element == Element.JUMP:
            return ' Earth blast!\n Push "Y"\n repeatedly!'
        elif self.element == Element.ICE:
            return ' Ice blast!\n Push "Y"\n repeatedly!'
        elif self.element == Element.THUNDER:
            return ' Thunder blast!\n Push "Y"\n repeatedly!'
        else:
            return self._description

    @property
    def palette_patch(self) -> dict[int, bytearray]:
        active = 0x253000 + 30 * 817
        fade = 0x253000 + 30 * 815
        d = {}
        if self.element == Element.JUMP:
            d[active] = palette_to_bytes(
                [
                    0x80F800,
                    0x78F800,
                    0x30D800,
                    0x38C800,
                    0x18B000,
                    0x008000,
                    0x78F800,
                    0xA8F800,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                ]
            )
            d[fade] = palette_to_bytes(
                [
                    0xF8F8F8,
                    0xB8F800,
                    0x78F800,
                    0x30D800,
                    0x38C800,
                    0x18B000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                ]
            )
        elif self.element == Element.ICE:
            d[active] = palette_to_bytes(
                [
                    0xF8F8D0,
                    0x00F8F8,
                    0x00D0F8,
                    0x00A8F8,
                    0x0080F8,
                    0x0058F8,
                    0x0028F8,
                    0x0028F8,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                ]
            )
            d[fade] = palette_to_bytes(
                [
                    0xF8F8F8,
                    0xA0F8F8,
                    0x40F8F8,
                    0x38D0F8,
                    0x30A8F8,
                    0x1850F8,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                ]
            )
        elif self.element == Element.THUNDER:
            d[active] = palette_to_bytes(
                [
                    0xF8F8F8,
                    0xB8F8F8,
                    0xF8F8F8,
                    0xB8F8F8,
                    0xF8F8F8,
                    0xB8F8F8,
                    0xF8F8F8,
                    0xB8F8F8,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                    0x0000D0,
                ]
            )
            d[fade] = palette_to_bytes(
                [
                    0xF8F8F8,
                    0xB8F0F8,
                    0xB8E0F8,
                    0xB0E0F8,
                    0xA0D0F8,
                    0x80D0F8,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                    0x000000,
                ]
            )
        return d


__all__ = ["SuperFlameSpell"]
