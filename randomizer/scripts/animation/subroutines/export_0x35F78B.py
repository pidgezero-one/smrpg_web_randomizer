from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35F78B,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35F78B import (
    script as subroutine_0x35F78B,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F78B,
    start=0x35F78B,
    end=0x35F816,
    scripts=[
        subroutine_0x35F78B,
    ],
)
