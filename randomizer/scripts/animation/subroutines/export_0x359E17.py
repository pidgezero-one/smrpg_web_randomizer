from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X359E17,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x359E17 import (
    script as subroutine_0x359E17,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X359E17,
    start=0x359E17,
    end=0x359F19,
    scripts=[
        subroutine_0x359E17,
    ],
)
