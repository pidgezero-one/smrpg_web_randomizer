from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35691B,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35691B import (
    script as subroutine_0x35691B,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35691B,
    start=0x35691B,
    end=0x356968,
    scripts=[
        subroutine_0x35691B,
    ],
)
