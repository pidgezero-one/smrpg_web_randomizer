from smrpgpatchbuilder.datatypes.enemies.classes import Enemy as EnemyBase
from typing import Optional

class Enemy(EnemyBase):
    _remake_name: Optional[str] = None

    @property
    def remake_name(self) -> str:
        return self._remake_name or self._name
