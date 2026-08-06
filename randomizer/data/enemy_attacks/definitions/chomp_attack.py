from randomizer.types.attack import (EnemyAttack)


class ChompAttack(EnemyAttack):
    _index = 109
    _name = ' Chomp'
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 90

    _remake_name = " Monster Toss"


__all__ = ["ChompAttack"]
