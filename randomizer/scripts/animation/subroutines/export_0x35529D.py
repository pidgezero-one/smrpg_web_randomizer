from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35529D,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35529D import (
    script as subroutine_0x35529D,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35529D,
    start=0x35529D,
    end=0x3552C4,
    scripts=[
        subroutine_0x35529D,
    ],
)
