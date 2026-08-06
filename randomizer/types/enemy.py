from smrpgpatchbuilder.datatypes.enemies.classes import Enemy as EnemyBase
from smrpgpatchbuilder.datatypes.spells.enums import Element, Status

from randomizer.data.variables import psychopath_symbols as sym


class Enemy(EnemyBase):
    _remake_name: str | None = None

    # Stat scaling ratios - define what percentage of the stat pool this enemy should receive
    # These can be overridden in subclasses for bosses with specific scaling needs
    _ratio_hp: float = 1.0
    _ratio_attack: float = 1.0
    _ratio_defense: float = 1.0
    _ratio_magic_attack: float = 1.0
    _ratio_magic_defense: float = 1.0
    _ratio_evade: float = 1.0
    _ratio_magic_evade: float = 1.0

    # Per-enemy ceilings for scaled attack/magic_attack. Leaves headroom for in-battle
    # buffs like ATKMATK5 (+5) so the working 16-bit stat doesn't pin at 255 and overflow.
    _max_shuffled_attack: int = 255
    _max_shuffled_magic_attack: int = 255

    @property
    def ratio_hp(self) -> float:
        return self._ratio_hp

    @property
    def ratio_attack(self) -> float:
        return self._ratio_attack

    @property
    def ratio_defense(self) -> float:
        return self._ratio_defense

    @property
    def ratio_magic_attack(self) -> float:
        return self._ratio_magic_attack

    @property
    def ratio_magic_defense(self) -> float:
        return self._ratio_magic_defense

    @property
    def ratio_evade(self) -> float:
        return self._ratio_evade

    @property
    def ratio_magic_evade(self) -> float:
        return self._ratio_magic_evade

    @property
    def max_shuffled_attack(self) -> int:
        return self._max_shuffled_attack

    @property
    def max_shuffled_magic_attack(self) -> int:
        return self._max_shuffled_magic_attack

    @property
    def remake_name(self) -> str:
        return self._remake_name or self._name

    @property
    def boss(self) -> bool:
        """Returns True if this enemy is a boss (uses ohko_immune as indicator)."""
        return self._ohko_immune

    def build_psychopath_text(self) -> str:
        """Generate Psychopath text showing elemental weaknesses/immunities and status vulnerabilities.

        Uses EMPTY as an invisible placeholder for missing elements/statuses, and
        strips the trailing run before returning -- the encoder does NOT trim it for
        us, and psychopath data is tight (~20 bytes/enemy).

        Format: [resist_icon elements] [weak_icon elements] [V statuses ohko]

        Every symbol is emitted as a raw chr(): the codes are randomizer-owned
        glyphs in the dialogue font's blank slots, and the encoder passes unmapped
        characters through as their ordinal. See
        :mod:randomizer.data.variables.psychopath_symbols -- in particular, none
        of these may land on 0x7B-0x7E, which item names need for ! # - '.

        Returns:
            Psychopath message string with special characters for game display.
        """
        EMPTY = chr(sym.EMPTY)  # invisible placeholder

        ELEMENT_CHARS = {
            Element.ICE: chr(sym.ICE),
            Element.FIRE: chr(sym.FIRE),
            Element.THUNDER: chr(sym.THUNDER),
            Element.JUMP: chr(sym.JUMP),
        }

        STATUS_CHARS = {
            Status.SLEEP: chr(sym.SLEEP),
            Status.FEAR: chr(sym.FEAR),
            Status.MUTE: chr(sym.MUTE),
            Status.POISON: chr(sym.POISON),
        }

        desc = ''

        # Elemental resistances - collect present elements, then pad with empty
        element_order = [Element.FIRE, Element.ICE, Element.THUNDER, Element.JUMP]
        resist_elements = [e for e in element_order if e in self.resistances]
        if resist_elements:
            desc += chr(sym.RESISTANCE)
            for element in resist_elements:
                desc += ELEMENT_CHARS[element]
            desc += EMPTY

        # Elemental weaknesses - collect present elements, then pad with empty
        weak_elements = [e for e in element_order if e in self.weaknesses]
        if weak_elements:
            desc += chr(sym.WEAKNESS)
            for element in weak_elements:
                desc += ELEMENT_CHARS[element]
            desc += EMPTY

        # Status vulnerabilities (inverse of immunities) - collect present, then pad
        status_order = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
        vulnerabilities = [s for s in status_order if s not in self.status_immunities]

        # Check if there are any vulnerabilities (status or OHKO)
        has_status_vulns = len(vulnerabilities) > 0
        has_ohko_vuln = not self.ohko_immune

        if has_status_vulns or has_ohko_vuln:
            # Add "V" prefix for vulnerabilities section
            desc += 'V'
            for status in vulnerabilities:
                desc += STATUS_CHARS[status]
            # Pad to 4 statuses
            # OHKO vulnerability
            if has_ohko_vuln:
                desc += chr(sym.OHKO) * 2
        # Strip trailing EMPTY placeholders (must strip full substring, not individual chars)
        while desc.endswith(EMPTY):
            desc = desc[:-len(EMPTY)]
        if desc == '':
            desc = "(none)"

        return desc
