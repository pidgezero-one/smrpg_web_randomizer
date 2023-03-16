from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A7868,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A7868 import (
    script as subroutine_0x3A7868,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A7868,
    start=0x3A7868,
    end=0x3A7885,
    scripts=[
        subroutine_0x3A7868,
    ],
)
