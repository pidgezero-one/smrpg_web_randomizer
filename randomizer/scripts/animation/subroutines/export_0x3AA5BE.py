from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3AA5BE,
)
from .contents.subroutine_0x3AA5BE import script as subroutine_0x3AA5BE

bank = AnimationScriptBank(
    name=SUBROUTINES_0X3AA5BE,
    start=0x3AA5BE,
    end=0x3AA655,
    scripts=[
        subroutine_0x3AA5BE,
    ],
)
