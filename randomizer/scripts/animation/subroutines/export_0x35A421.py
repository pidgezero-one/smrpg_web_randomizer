from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35A421,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35A421 import (
    script as subroutine_0x35A421,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35A421,
    start=0x35A421,
    end=0x35A48E,
    scripts=[
        subroutine_0x35A421,
    ],
)
