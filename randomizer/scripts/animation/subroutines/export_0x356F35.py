from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X356F35,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x356F35 import (
    script as subroutine_0x356F35,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X356F35,
    start=0x356F35,
    end=0x357345,
    scripts=[
        subroutine_0x356F35,
    ],
)
