from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X352C67,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x352C67 import (
    script as subroutine_0x352C67,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X352C67,
    start=0x352C67,
    end=0x352C78,
    scripts=[
        subroutine_0x352C67,
    ],
)
