from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X352E01,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x352E01 import (
    script as subroutine_0x352E01,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X352E01,
    start=0x352E01,
    end=0x352E09,
    scripts=[
        subroutine_0x352E01,
    ],
)
