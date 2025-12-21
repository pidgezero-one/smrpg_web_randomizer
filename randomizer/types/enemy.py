from smrpgpatchbuilder.datatypes.enemies.classes import Enemy as EnemyBase
class Enemy(EnemyBase):
    _remake_name: str | None = None

    @property
    def remake_name(self) -> str:
        return self._remake_name or self._name

    @property
    def boss(self) -> bool:
        """Returns True if this enemy is a boss (uses ohko_immune as indicator)."""
        return self._ohko_immune
