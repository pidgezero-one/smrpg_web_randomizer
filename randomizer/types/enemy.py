from smrpgpatchbuilder.datatypes.enemies.classes import Enemy as EnemyBase
from smrpgpatchbuilder.datatypes.spells.enums import Element, Status


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
    def remake_name(self) -> str:
        return self._remake_name or self._name

    @property
    def boss(self) -> bool:
        """Returns True if this enemy is a boss (uses ohko_immune as indicator)."""
        return self._ohko_immune

    def build_psychopath_text(self) -> str:
        """Generate Psychopath text showing elemental weaknesses/immunities and status vulnerabilities.

        Returns:
            Psychopath message string with special characters for game display.
        """
        desc = ''

        # Elemental immunities/resistances
        if self.resistances:
            desc += '\x7C'  # Shield icon
            for element in [Element.FIRE, Element.ICE, Element.THUNDER, Element.JUMP]:
                if element in self.resistances:
                    desc += element.dialog_char
        else:
            desc += '\x20' * 5

        desc += '\x20'

        # Elemental weaknesses
        if self.weaknesses:
            desc += '\x7B'  # Weakness icon
            for element in [Element.FIRE, Element.ICE, Element.THUNDER, Element.JUMP]:
                if element in self.weaknesses:
                    desc += element.dialog_char
        else:
            desc += '\x20' * 5

        desc += '\x20\x20'

        # Status vulnerabilities (inverse of immunities)
        # Check which statuses this enemy is NOT immune to
        status_checks = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
        vulnerabilities = [s for s in status_checks if s not in self.status_immunities]

        if vulnerabilities:
            for status in status_checks:
                if status in vulnerabilities:
                    desc += status.dialog_char
            # Death vulnerability (not OHKO immune)
            if not self.ohko_immune:
                desc += '\x84\x84'
        else:
            desc += '\x20' * 6

        desc += '\x02'

        return desc
