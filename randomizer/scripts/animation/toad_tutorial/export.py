from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    TOAD_TUTORIAL,
)
from .contents.script_0 import script as script_0

bank = AnimationScriptBank(
    name=TOAD_TUTORIAL,
    start=0x02F4BF,
    end=0x02F50D,
    scripts=[
        script_0,
    ],
)
