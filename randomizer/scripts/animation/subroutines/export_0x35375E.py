from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35375E,
)
from .contents.subroutine_0x35375E import script as subroutine_0x35375E

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35375E,
    start=0x35375E,
    end=0x353963,
    scripts=[
        subroutine_0x35375E,
    ],
)
