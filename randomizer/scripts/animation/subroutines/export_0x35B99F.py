from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35B99F,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35B99F import (
    script as subroutine_0x35B99F,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35B99F,
    start=0x35B99F,
    end=0x35B9A7,
    scripts=[
        subroutine_0x35B99F,
    ],
)
