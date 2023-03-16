from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35FD4C,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35FD4C import (
    script as subroutine_0x35FD4C,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35FD4C,
    start=0x35FD4C,
    end=0x35FD8F,
    scripts=[
        subroutine_0x35FD4C,
    ],
)
