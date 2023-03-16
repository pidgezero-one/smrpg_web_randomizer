from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A7EE5,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A7EE5 import (
    script as subroutine_0x3A7EE5,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A7EE5,
    start=0x3A7EE5,
    end=0x3A7EFE,
    scripts=[
        subroutine_0x3A7EE5,
    ],
)
