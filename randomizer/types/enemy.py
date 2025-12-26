from smrpgpatchbuilder.datatypes.enemies.classes import Enemy as EnemyBase
from smrpgpatchbuilder.datatypes.spells.enums import Element, Status


class Enemy(EnemyBase):
    _remake_name: str | None = None

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
