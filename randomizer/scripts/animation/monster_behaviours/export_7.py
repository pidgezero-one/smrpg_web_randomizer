from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_7_0X350796,
)
from .contents.subroutine_0x7 import script as subroutine_0x7

bank = AnimationScriptBank(
    name=BEHAVIOUR_7_0X350796,
    start=0x350796,
    end=0x3507A1,
    scripts=[
        subroutine_0x7,
    ],
)
