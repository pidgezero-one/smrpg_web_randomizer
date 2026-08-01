from randomizer.types.attack import (EnemyAttack)


class Attack11(EnemyAttack):
    _index = 11
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 100


__all__ = ["Attack11"]
