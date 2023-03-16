from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A8AE8,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A8AE8 import (
    script as subroutine_0x3A8AE8,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A8AE8,
    start=0x3A8AE8,
    end=0x3A8BB0,
    scripts=[
        subroutine_0x3A8AE8,
    ],
)
