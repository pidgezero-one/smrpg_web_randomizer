from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35549D,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35549D import (
    script as subroutine_0x35549D,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35549D,
    start=0x35549D,
    end=0x35554D,
    scripts=[
        subroutine_0x35549D,
    ],
)
