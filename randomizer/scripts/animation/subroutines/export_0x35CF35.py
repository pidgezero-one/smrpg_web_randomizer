from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35CF35,
)
from .contents.subroutine_0x35CF35 import script as subroutine_0x35CF35

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35CF35,
    start=0x35CF35,
    end=0x35D186,
    scripts=[
        subroutine_0x35CF35,
    ],
)
