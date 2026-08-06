from randomizer.types.attack import (EnemyAttack)


class InkBlastAttack(EnemyAttack):
    _index = 37
    _name = ' Ink Blast'
    _attack_level = 1
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


__all__ = ["InkBlastAttack"]
