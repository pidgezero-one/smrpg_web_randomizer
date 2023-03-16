from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X354E1F,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x354E1F import (
    script as subroutine_0x354E1F,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X354E1F,
    start=0x354E1F,
    end=0x354E6B,
    scripts=[
        subroutine_0x354E1F,
    ],
)
