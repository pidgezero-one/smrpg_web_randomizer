from randomizer.types.attack import (EnemyAttack)


class TerrapunchAttack(EnemyAttack):
    _index = 126
    _name = ' Terrapunch'
    _attack_level = 2
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = False
    _damageless_flag_2 = False
    _hit_rate = 95


__all__ = ["TerrapunchAttack"]
