from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_42_0X350DED,
)
from .contents.subroutine_0x42 import script as subroutine_0x42

bank = AnimationScriptBank(
    name=BEHAVIOUR_42_0X350DED,
    start=0x350DED,
    end=0x350E37,
    scripts=[
        subroutine_0x42,
    ],
)
