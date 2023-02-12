from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X02F50E,
)
from .contents.subroutine_0x02F50E import script as subroutine_0x02F50E

bank = AnimationScriptBank(
    name=SUBROUTINES_0X02F50E,
    start=0x02F50E,
    end=0x02F51D,
    scripts=[
        subroutine_0x02F50E,
    ],
)
