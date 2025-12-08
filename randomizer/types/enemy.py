from smrpgpatchbuilder.datatypes.enemies.classes import Enemy as EnemyBase
class Enemy(EnemyBase):
    _remake_name: str | None = None

    @property
    def remake_name(self) -> str:
        return self._remake_name or self._name
