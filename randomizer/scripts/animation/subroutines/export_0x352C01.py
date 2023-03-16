from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X352C01,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x352C01 import (
    script as subroutine_0x352C01,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X352C01,
    start=0x352C01,
    end=0x352C08,
    scripts=[
        subroutine_0x352C01,
    ],
)
