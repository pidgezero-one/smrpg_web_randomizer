from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A88FF,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A88FF import (
    script as subroutine_0x3A88FF,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A88FF,
    start=0x3A88FF,
    end=0x3A8A67,
    scripts=[
        subroutine_0x3A88FF,
    ],
)
