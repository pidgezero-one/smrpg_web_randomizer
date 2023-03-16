from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A7333,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A7333 import (
    script as subroutine_0x3A7333,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A7333,
    start=0x3A7333,
    end=0x3A751A,
    scripts=[
        subroutine_0x3A7333,
    ],
)
