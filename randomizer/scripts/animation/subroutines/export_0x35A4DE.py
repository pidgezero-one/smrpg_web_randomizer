from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35A4DE,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35A4DE import (
    script as subroutine_0x35A4DE,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35A4DE,
    start=0x35A4DE,
    end=0x35A4E6,
    scripts=[
        subroutine_0x35A4DE,
    ],
)
