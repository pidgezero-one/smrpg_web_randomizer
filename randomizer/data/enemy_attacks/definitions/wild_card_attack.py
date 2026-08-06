from randomizer.types.attack import (EnemyAttack)


class WildCardAttack(EnemyAttack):
    _index = 23
    _name = ' Wild Card'
    _attack_level = 3
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95

    _remake_name = " Card Rain"


__all__ = ["WildCardAttack"]
