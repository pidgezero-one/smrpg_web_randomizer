from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A72CE,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A72CE import (
    script as subroutine_0x3A72CE,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A72CE,
    start=0x3A72CE,
    end=0x3A7327,
    scripts=[
        subroutine_0x3A72CE,
    ],
)
