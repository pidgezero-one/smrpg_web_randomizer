from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35A77D,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35A77D import (
    script as subroutine_0x35A77D,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35A77D,
    start=0x35A77D,
    end=0x35A97B,
    scripts=[
        subroutine_0x35A77D,
    ],
)
