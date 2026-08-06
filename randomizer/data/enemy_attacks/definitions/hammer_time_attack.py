from randomizer.types.attack import (EnemyAttack)


class HammerTimeAttack(EnemyAttack):
    _index = 96
    _name = ' Hammer Time'
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 90


__all__ = ["HammerTimeAttack"]
