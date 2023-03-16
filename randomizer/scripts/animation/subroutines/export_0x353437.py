from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X353437,
)
from randomizer.scripts.animation.subroutines.contents.subroutine_0x353437 import (
    script as subroutine_0x353437,
)

bank = AnimationScriptBank(
    name=SUBROUTINES_0X353437,
    start=0x353437,
    end=0x353705,
    scripts=[
        subroutine_0x353437,
    ],
)
