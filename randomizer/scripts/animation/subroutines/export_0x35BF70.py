from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35BF70,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35BF70 import (
    script as subroutine_0x35BF70,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35BF70,
    start=0x35BF70,
    end=0x35C123,
    scripts=[
        subroutine_0x35BF70,
    ],
)
