from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3588F4,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3588F4 import (
    script as subroutine_0x3588F4,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3588F4,
    start=0x3588F4,
    end=0x358915,
    scripts=[
        subroutine_0x3588F4,
    ],
)
