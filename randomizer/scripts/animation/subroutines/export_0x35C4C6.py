from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35C4C6,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35C4C6 import (
    script as subroutine_0x35C4C6,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35C4C6,
    start=0x35C4C6,
    end=0x35C5FD,
    scripts=[
        subroutine_0x35C4C6,
    ],
)
