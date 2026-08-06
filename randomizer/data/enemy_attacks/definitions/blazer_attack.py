from randomizer.types.attack import (EnemyAttack)


class BlazerAttack(EnemyAttack):
    _index = 30
    _name = ' Blazer'
    _attack_level = 0
    _ohko = True
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = False
    _hit_rate = 90


__all__ = ["BlazerAttack"]
