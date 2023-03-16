from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35D191,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x35D191 import (
    script as subroutine_0x35D191,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35D191,
    start=0x35D191,
    end=0x35D1FD,
    scripts=[
        subroutine_0x35D191,
    ],
)
