from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3AC795,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3AC795 import (
    script as subroutine_0x3AC795,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3AC795,
    start=0x3AC795,
    end=0x3AC7B1,
    scripts=[
        subroutine_0x3AC795,
    ],
)
