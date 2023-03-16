from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35DC70,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35DC70 import (
    script as subroutine_0x35DC70,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35DC70,
    start=0x35DC70,
    end=0x35DC8E,
    scripts=[
        subroutine_0x35DC70,
    ],
)
