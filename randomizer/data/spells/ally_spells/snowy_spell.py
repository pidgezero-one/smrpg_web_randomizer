from randomizer.types.spell import (CharacterSpell, palette_to_bytes)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (
    X00625_MODIFIER,
)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (ROTATE_ONLY)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class SnowySpell(CharacterSpell):
    _index = 25
    _title = "Snowy"
    _prefix = ItemPrefix.STAR
    _fp = 12
    _power = 40
    _hit_rate = 100
    _spell_type = SpellType.DAMAGE
    _element = Element.ICE
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
    _timing_modifiers = ROTATE_ONLY
    _damage_modifiers = X00625_MODIFIER
    _description = " Snowman\n fells foes!"

    @property
    def title(self) -> str:
        if self.element == Element.FIRE:
            return "Firey"
        elif self.element == Element.THUNDER:
            return "Thundery"
        elif self.element == Element.JUMP:
            return "Earthy"
        else:
            return self._title
        
    @property
    def description(self) -> str:
        if self.element == Element.FIRE:   
            return ' Fiery snowman\n fells foes!'
        elif self.element == Element.THUNDER:
            return ' Thundery\n snowman fells\n foes!'
        elif self.element == Element.JUMP:
            return ' Earthy snowman\n fells foes!'
        else:
            return self._description

    @property
    def palette_patch(self) -> dict[int, bytearray]:
        upper = 0x33BAAE
        lower = 0x33BD2D
        d = {}
        if self.element == Element.JUMP:
            d[upper] = palette_to_bytes([0x28A000, 0x00D000, 0x00A800, 0x008000])
            d[lower] = palette_to_bytes([0x000000, 0x00D000])
        elif self.element == Element.THUNDER:
            d[upper] = palette_to_bytes([0x28A000, 0xF8F8F8, 0xC0F8F8, 0x68F8F8])
            d[lower] = palette_to_bytes([0x000000, 0xF8F8F8])
        elif self.element == Element.FIRE:
            d[upper] = palette_to_bytes([0x28A000, 0xD8B000, 0xB86000, 0x980000])
            d[lower] = palette_to_bytes([0x000000, 0xD8B000])
        return d


__all__ = ["SnowySpell"]
