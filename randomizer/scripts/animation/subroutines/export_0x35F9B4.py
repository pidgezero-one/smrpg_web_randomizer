from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35F9B4,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35F9B4 import (
    script as subroutine_0x35F9B4,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F9B4,
    start=0x35F9B4,
    end=0x35FA94,
    scripts=[
        subroutine_0x35F9B4,
    ],
)
