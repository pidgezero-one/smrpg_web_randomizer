from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35C604,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35C604 import (
    script as subroutine_0x35C604,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35C604,
    start=0x35C604,
    end=0x35C685,
    scripts=[
        subroutine_0x35C604,
    ],
)
