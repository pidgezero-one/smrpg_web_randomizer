from randomizer.types.attack import (EnemyAttack)


class LastShotAttack(EnemyAttack):
    _index = 99
    _name = ' Last Shot!'
    _attack_level = 3
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 100

    _remake_name = " Last Shot"


__all__ = ["LastShotAttack"]
