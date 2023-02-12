from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35DC93,
)
from .contents.subroutine_0x35DC93 import script as subroutine_0x35DC93

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35DC93,
    start=0x35DC93,
    end=0x35DCB1,
    scripts=[
        subroutine_0x35DC93,
    ],
)
