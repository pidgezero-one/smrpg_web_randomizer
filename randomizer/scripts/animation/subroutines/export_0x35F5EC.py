from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35F5EC,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35F5EC import (
    script as subroutine_0x35F5EC,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35F5EC,
    start=0x35F5EC,
    end=0x35F729,
    scripts=[
        subroutine_0x35F5EC,
    ],
)
