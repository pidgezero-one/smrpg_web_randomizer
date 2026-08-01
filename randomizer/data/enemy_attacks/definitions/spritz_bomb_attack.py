from randomizer.types.attack import (EnemyAttack)


class SpritzBombAttack(EnemyAttack):
    _index = 26
    _name = ' Spritz Bomb'
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 90


__all__ = ["SpritzBombAttack"]
