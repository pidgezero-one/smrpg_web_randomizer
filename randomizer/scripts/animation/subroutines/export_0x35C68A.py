from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35C68A,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35C68A import (
    script as subroutine_0x35C68A,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35C68A,
    start=0x35C68A,
    end=0x35C711,
    scripts=[
        subroutine_0x35C68A,
    ],
)
