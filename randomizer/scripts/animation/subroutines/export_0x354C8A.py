from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X354C8A,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x354C8A import (
    script as subroutine_0x354C8A,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X354C8A,
    start=0x354C8A,
    end=0x354CF8,
    scripts=[
        subroutine_0x354C8A,
    ],
)
