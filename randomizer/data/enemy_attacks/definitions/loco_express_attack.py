from randomizer.types.attack import (EnemyAttack)


class LocoExpressAttack(EnemyAttack):
    _index = 114
    _name = ' Loco Express'
    _attack_level = 3
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 90


__all__ = ["LocoExpressAttack"]
