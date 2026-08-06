from randomizer.types.attack import (EnemyAttack)


class MigraineAttack(EnemyAttack):
    _index = 84
    _name = ' Migraine'
    _attack_level = 0
    _ohko = True
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = False
    _hit_rate = 80


__all__ = ["MigraineAttack"]
