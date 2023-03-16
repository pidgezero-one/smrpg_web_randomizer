from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35A4FB,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35A4FB import (
    script as subroutine_0x35A4FB,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35A4FB,
    start=0x35A4FB,
    end=0x35A69F,
    scripts=[
        subroutine_0x35A4FB,
    ],
)
