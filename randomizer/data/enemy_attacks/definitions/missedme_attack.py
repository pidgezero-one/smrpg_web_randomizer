from randomizer.types.attack import (EnemyAttack)


class MissedmeAttack(EnemyAttack):
    _index = 112
    _name = ' Missed me!'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 95


__all__ = ["MissedmeAttack"]
