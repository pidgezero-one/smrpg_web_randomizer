from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X357B73,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x357B73 import (
    script as subroutine_0x357B73,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X357B73,
    start=0x357B73,
    end=0x357C43,
    scripts=[
        subroutine_0x357B73,
    ],
)
