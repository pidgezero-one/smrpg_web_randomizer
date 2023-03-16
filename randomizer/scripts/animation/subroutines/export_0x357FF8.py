from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X357FF8,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x357FF8 import (
    script as subroutine_0x357FF8,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X357FF8,
    start=0x357FF8,
    end=0x358071,
    scripts=[
        subroutine_0x357FF8,
    ],
)
