from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X358166,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x358166 import (
    script as subroutine_0x358166,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X358166,
    start=0x358166,
    end=0x35816A,
    scripts=[
        subroutine_0x358166,
    ],
)
