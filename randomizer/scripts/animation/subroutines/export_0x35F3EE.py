from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35F3EE,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35F3EE import (
    script as subroutine_0x35F3EE,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F3EE,
    start=0x35F3EE,
    end=0x35F43E,
    scripts=[
        subroutine_0x35F3EE,
    ],
)
