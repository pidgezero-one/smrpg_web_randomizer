from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X355DBA,
)
from .contents.subroutine_0x355DBA import script as subroutine_0x355DBA

bank = AnimationScriptBank(
    name=SUBROUTINES_0X355DBA,
    start=0x355DBA,
    end=0x355E00,
    scripts=[
        subroutine_0x355DBA,
    ],
)
