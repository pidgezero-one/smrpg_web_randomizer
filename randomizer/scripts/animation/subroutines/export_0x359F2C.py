from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X359F2C,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x359F2C import (
    script as subroutine_0x359F2C,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X359F2C,
    start=0x359F2C,
    end=0x35A0A4,
    scripts=[
        subroutine_0x359F2C,
    ],
)
