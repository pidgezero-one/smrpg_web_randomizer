from randomizer.types.attack import (EnemyAttack)


class FinalClawAttack(EnemyAttack):
    _index = 18
    _name = ' Final Claw'
    _attack_level = 0
    _ohko = True
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = False
    _hit_rate = 100


__all__ = ["FinalClawAttack"]
