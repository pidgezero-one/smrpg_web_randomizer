from randomizer.types.attack import (EnemyAttack)


class ATKMATKneg5Attack(EnemyAttack):
    _index = 55
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 100


__all__ = ["ATKMATKneg5Attack"]
