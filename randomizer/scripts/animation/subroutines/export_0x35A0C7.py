from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35A0C7,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35A0C7 import (
    script as subroutine_0x35A0C7,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35A0C7,
    start=0x35A0C7,
    end=0x35A2FF,
    scripts=[
        subroutine_0x35A0C7,
    ],
)
