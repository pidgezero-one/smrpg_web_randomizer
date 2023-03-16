from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A82AA,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x3A82AA import (
    script as subroutine_0x3A82AA,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3A82AA,
    start=0x3A82AA,
    end=0x3A82C7,
    scripts=[
        subroutine_0x3A82AA,
    ],
)
