from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35F1C4,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35F1C4 import (
    script as subroutine_0x35F1C4,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F1C4,
    start=0x35F1C4,
    end=0x35F214,
    scripts=[
        subroutine_0x35F1C4,
    ],
)
