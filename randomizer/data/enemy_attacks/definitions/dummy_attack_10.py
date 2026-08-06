from randomizer.types.attack import (EnemyAttack)


class DUMMYAttack10(EnemyAttack):
    _index = 108
    _name = 'DUMMY'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 100


__all__ = ["DUMMYAttack10"]
