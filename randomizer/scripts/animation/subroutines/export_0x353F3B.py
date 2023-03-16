from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X353F3B,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x353F3B import (
    script as subroutine_0x353F3B,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X353F3B,
    start=0x353F3B,
    end=0x353F6A,
    scripts=[
        subroutine_0x353F3B,
    ],
)
