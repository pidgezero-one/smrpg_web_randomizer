from randomizer.types.attack import (EnemyAttack)


class Attack9(EnemyAttack):
    _index = 9
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


__all__ = ["Attack9"]
