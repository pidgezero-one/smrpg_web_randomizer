from randomizer.types.attack import (EnemyAttack)


class ShakerAttack(EnemyAttack):
    _index = 128
    _name = ' Shaker'
    _attack_level = 0
    _ohko = True
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = False
    _hit_rate = 99


__all__ = ["ShakerAttack"]
