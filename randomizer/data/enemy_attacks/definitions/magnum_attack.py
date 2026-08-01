from randomizer.types.attack import (EnemyAttack)


class MagnumAttack(EnemyAttack):
    _index = 82
    _name = ' Magnum'
    _attack_level = 0
    _ohko = True
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = False
    _hit_rate = 90


__all__ = ["MagnumAttack"]
