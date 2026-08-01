from randomizer.types.attack import (EnemyAttack)


class PierceAttack(EnemyAttack):
    _index = 80
    _name = ' Pierce'
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 90


__all__ = ["PierceAttack"]
