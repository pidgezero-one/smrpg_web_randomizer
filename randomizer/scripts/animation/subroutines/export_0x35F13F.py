from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35F13F,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35F13F import (
    script as subroutine_0x35F13F,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F13F,
    start=0x35F13F,
    end=0x35F1BD,
    scripts=[
        subroutine_0x35F13F,
    ],
)
