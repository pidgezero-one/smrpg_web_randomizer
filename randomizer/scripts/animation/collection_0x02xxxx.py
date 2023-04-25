"""bank 0x02xxxx export"""

from randomizer.types.battle_animation_scripts.types import (
    AnimationScriptBankCollection,
)
from .flower_bonus.bank import bank as flower_bonus
from .toad_tutorial.bank import bank as toad_tutorial
from .subroutines.export_0x02F50E import bank as subroutine_0x02F50E

collection = AnimationScriptBankCollection(
    [
        flower_bonus,
        toad_tutorial,
        subroutine_0x02F50E,
    ]
)
