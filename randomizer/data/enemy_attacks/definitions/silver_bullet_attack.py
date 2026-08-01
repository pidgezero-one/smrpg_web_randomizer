from randomizer.types.attack import (EnemyAttack)


class SilverBulletAttack(EnemyAttack):
    _index = 125
    _name = 'Silver Bullet'
    _attack_level = 0
    _ohko = True
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = False
    _hit_rate = 99


__all__ = ["SilverBulletAttack"]
