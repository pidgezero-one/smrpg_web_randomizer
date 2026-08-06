from randomizer.types.attack import (EnemyAttack)


class BOBOMBSUPERAttack(EnemyAttack):
    _index = 78
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 100


__all__ = ["BOBOMBSUPERAttack"]
