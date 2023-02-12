from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_36_0X350D22,
)
from .contents.subroutine_0x36 import script as subroutine_0x36

bank = AnimationScriptBank(
    name=BEHAVIOUR_36_0X350D22,
    start=0x350D22,
    end=0x350D35,
    scripts=[
        subroutine_0x36,
    ],
)
