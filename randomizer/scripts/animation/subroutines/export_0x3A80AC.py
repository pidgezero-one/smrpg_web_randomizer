from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A80AC,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A80AC import (
    script as subroutine_0x3A80AC,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A80AC,
    start=0x3A80AC,
    end=0x3A80B5,
    scripts=[
        subroutine_0x3A80AC,
    ],
)
