from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35617C,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35617C import (
    script as subroutine_0x35617C,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35617C,
    start=0x35617C,
    end=0x3561AC,
    scripts=[
        subroutine_0x35617C,
    ],
)
