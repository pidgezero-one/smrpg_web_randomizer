from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X352DC0,
)
from .contents.subroutine_0x352DC0 import script as subroutine_0x352DC0

bank = AnimationScriptBank(
    name=SUBROUTINES_0X352DC0,
    start=0x352DC0,
    end=0x352DC7,
    scripts=[
        subroutine_0x352DC0,
    ],
)
