from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3540CA,
)
from .contents.subroutine_0x3540CA import script as subroutine_0x3540CA

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3540CA,
    start=0x3540CA,
    end=0x3542BE,
    scripts=[
        subroutine_0x3540CA,
    ],
)
