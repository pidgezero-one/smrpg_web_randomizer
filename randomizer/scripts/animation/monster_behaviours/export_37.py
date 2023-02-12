from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    BEHAVIOUR_37_0X350D36,
)
from .contents.subroutine_0x37 import script as subroutine_0x37

bank = AnimationScriptBank(
    name=BEHAVIOUR_37_0X350D36,
    start=0x350D36,
    end=0x350D71,
    scripts=[
        subroutine_0x37,
    ],
)
