from randomizer.types.attack import (EnemyAttack)


class DUMMYAttack4(EnemyAttack):
    _index = 101
    _name = 'DUMMY'
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 90


__all__ = ["DUMMYAttack4"]
