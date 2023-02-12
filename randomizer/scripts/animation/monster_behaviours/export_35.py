from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_35_0X350CDC,
)
from .contents.subroutine_0x35 import script as subroutine_0x35

bank = AnimationScriptBank(
    name=BEHAVIOUR_35_0X350CDC,
    start=0x350CDC,
    end=0x350CF1,
    scripts=[
        subroutine_0x35,
    ],
)
