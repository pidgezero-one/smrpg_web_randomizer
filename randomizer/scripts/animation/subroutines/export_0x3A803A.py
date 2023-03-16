from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A803A,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A803A import (
    script as subroutine_0x3A803A,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A803A,
    start=0x3A803A,
    end=0x3A804A,
    scripts=[
        subroutine_0x3A803A,
    ],
)
