from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A81C4,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A81C4 import (
    script as subroutine_0x3A81C4,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A81C4,
    start=0x3A81C4,
    end=0x3A81EB,
    scripts=[
        subroutine_0x3A81C4,
    ],
)
