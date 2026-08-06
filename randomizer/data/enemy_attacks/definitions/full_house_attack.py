from randomizer.types.attack import (EnemyAttack)


class FullHouseAttack(EnemyAttack):
    _index = 22
    _name = ' Full House'
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95

    _remake_name = " Card Toss"


__all__ = ["FullHouseAttack"]
