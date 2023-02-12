from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X35AD5C,
)
from .contents.subroutine_0x35AD5C import script as subroutine_0x35AD5C

bank = AnimationScriptBank(
    name=SUBROUTINES_0X35AD5C,
    start=0x35AD5C,
    end=0x35B019,
    scripts=[
        subroutine_0x35AD5C,
    ],
)
