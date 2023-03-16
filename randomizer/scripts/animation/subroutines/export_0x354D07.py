from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X354D07,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x354D07 import (
    script as subroutine_0x354D07,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X354D07,
    start=0x354D07,
    end=0x354E00,
    scripts=[
        subroutine_0x354D07,
    ],
)
