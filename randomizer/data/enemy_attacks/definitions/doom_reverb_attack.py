from randomizer.types.attack import (EnemyAttack)
from smrpgpatchbuilder.datatypes.spells.enums import (Status)


class DoomReverbAttack(EnemyAttack):
    _index = 35
    _name = ' Doom Reverb'
    _attack_level = 0
    _ohko = False
    _damageless_flag_1 = True
    _hide_numbers = True
    _damageless_flag_2 = True
    _hit_rate = 90
    _status_effects = [Status.MUTE]


__all__ = ["DoomReverbAttack"]
