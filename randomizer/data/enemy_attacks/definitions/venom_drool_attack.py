from randomizer.types.attack import (EnemyAttack)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class VenomDroolAttack(EnemyAttack):
    _index = 42
    _name = ' Venom Drool'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = False
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 95
    _status_effects = [Status.POISON]


__all__ = ["VenomDroolAttack"]
