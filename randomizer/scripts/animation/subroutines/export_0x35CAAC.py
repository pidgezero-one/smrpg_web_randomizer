from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35CAAC,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35CAAC import (
    script as subroutine_0x35CAAC,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35CAAC,
    start=0x35CAAC,
    end=0x35CF28,
    scripts=[
        subroutine_0x35CAAC,
    ],
)
