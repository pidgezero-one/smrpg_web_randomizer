from randomizer.types.attack import (EnemyAttack)


class JinxedAttack(EnemyAttack):
    _index = 119
    _name = ' Jinxed'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 100


__all__ = ["JinxedAttack"]
