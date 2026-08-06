from randomizer.types.attack import (EnemyAttack)
from smrpgpatchbuilder.datatypes.spells.enums import (TempStatBuff)


class MagicForceAttack(EnemyAttack):
    _index = 81
    _name = ' Magic Force'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 100
    _buffs = [TempStatBuff(3), TempStatBuff(5)]


__all__ = ["MagicForceAttack"]
