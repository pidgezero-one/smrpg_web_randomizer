from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35D75F,
)
from .contents.subroutine_0x35D75F import script as subroutine_0x35D75F

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35D75F,
    start=0x35D75F,
    end=0x35DAD8,
    scripts=[
        subroutine_0x35D75F,
    ],
)
