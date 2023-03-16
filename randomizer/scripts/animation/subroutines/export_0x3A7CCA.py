from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A7CCA,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A7CCA import (
    script as subroutine_0x3A7CCA,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A7CCA,
    start=0x3A7CCA,
    end=0x3A7CD1,
    scripts=[
        subroutine_0x3A7CCA,
    ],
)
