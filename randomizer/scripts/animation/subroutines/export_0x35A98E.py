from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35A98E,
)
from .contents.subroutine_0x35A98E import script as subroutine_0x35A98E

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35A98E,
    start=0x35A98E,
    end=0x35ABAC,
    scripts=[
        subroutine_0x35A98E,
    ],
)
