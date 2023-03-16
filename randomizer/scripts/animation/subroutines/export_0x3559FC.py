from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3559FC,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3559FC import (
    script as subroutine_0x3559FC,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3559FC,
    start=0x3559FC,
    end=0x355AD8,
    scripts=[
        subroutine_0x3559FC,
    ],
)
