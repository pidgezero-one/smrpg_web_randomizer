from randomizer.types.attack import (EnemyAttack)


class BOBOMBBOMBAttack(EnemyAttack):
    _index = 85
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 99


__all__ = ["BOBOMBBOMBAttack"]
