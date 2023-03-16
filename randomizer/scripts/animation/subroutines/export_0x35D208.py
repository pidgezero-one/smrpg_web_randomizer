from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35D208,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35D208 import (
    script as subroutine_0x35D208,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35D208,
    start=0x35D208,
    end=0x35D2D4,
    scripts=[
        subroutine_0x35D208,
    ],
)
