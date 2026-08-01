from randomizer.types.attack import (EnemyAttack)


class MultistrikeAttack(EnemyAttack):
    _index = 87
    _name = ' Multistrike'
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


__all__ = ["MultistrikeAttack"]
