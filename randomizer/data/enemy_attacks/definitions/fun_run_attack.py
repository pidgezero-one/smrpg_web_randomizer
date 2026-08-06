from randomizer.types.attack import (EnemyAttack)


class FunRunAttack(EnemyAttack):
    _index = 62
    _name = ' Fun & Run'
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


__all__ = ["FunRunAttack"]
