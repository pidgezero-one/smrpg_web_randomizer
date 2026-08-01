from randomizer.types.spell import (CharacterSpell, palette_to_bytes)
from smrpgpatchbuilder.datatypes.items.enums import (ItemPrefix)
from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import (
    X00625_MODIFIER,
)
from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import (BUTTON_MASH)
from smrpgpatchbuilder.datatypes.spells.enums import (Element, SpellType)


class PsychBombSpell(CharacterSpell):
    _index = 11
    _title = "Psych Bomb"
    _prefix = ItemPrefix.STAR
    _fp = 15
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
    _timing_modifiers = BUTTON_MASH
    _damage_modifiers = X00625_MODIFIER
    _description = " Make me mad\n and...BOOM!"

    @property
    def title(self) -> str:
        if self.element == Element.JUMP:
            return "Earth Bomb"
        elif self.element == Element.ICE:
            return "Ice Bomb"
        elif self.element == Element.THUNDER:
            return "Thunder Bomb"
        else:
            return self._title
        
    @property
    def description(self) -> str:
        if self.element == Element.JUMP:
            return ' Make me mad\n and my earth\n bomb will go...\n BOOM!'
        elif self.element == Element.ICE:
            return ' Make me mad\n and my ice\n bomb will go...\n BOOM!'
        elif self.element == Element.THUNDER:
            return ' Make me mad\n and my thunder\n bomb will go...\n BOOM!'
        else:
            return self._description

    @property
    def palette_patch(self) -> dict[int, bytearray]:
        # Dome palette at ROM 0x334C34 (relocated by move_spell_gfx; vanilla 0x33510C is dead).
        # 32 bytes / 16 colors. Layout: c0=bright flash, c1..c11=11-step gradient, c12=dim,
        # c13..c15=bright flash. Verified by CGRAM dump during cast.
        base = 0x334C34
        intensities = [96, 104, 144, 176, 216, 248, 216, 176, 144, 104, 96]
        if self.element == Element.THUNDER:
            channels = lambda v: (v << 16) | (v << 8)  # R&G
        elif self.element == Element.ICE:
            channels = lambda v: (v << 8) | v          # G&B
        elif self.element == Element.JUMP:
            channels = lambda v: v << 8                # G
        else:
            return {}
        colors = [channels(248)] + [channels(i) for i in intensities] + [channels(80)] + [channels(248)] * 3
        return {base: palette_to_bytes(colors)}


__all__ = ["PsychBombSpell"]
