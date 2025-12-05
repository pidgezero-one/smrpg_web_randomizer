from smrpgpatchbuilder.datatypes.enemy_attacks.classes import EnemyAttack as EnemyAttackBase
from typing import Optional

class EnemyAttack(EnemyAttackBase):
    _remake_name: Optional[str] = None

    @property
    def remake_name(self) -> str:
        return self._remake_name or self._name
