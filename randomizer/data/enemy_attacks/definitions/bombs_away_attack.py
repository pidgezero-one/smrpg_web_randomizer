from randomizer.types.attack import (EnemyAttack)


class BombsAwayAttack(EnemyAttack):
    _index = 122
    _name = ' Bombs Away'
    _attack_level = 3
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 90


__all__ = ["BombsAwayAttack"]
