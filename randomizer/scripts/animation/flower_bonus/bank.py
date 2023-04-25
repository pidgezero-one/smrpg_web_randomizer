"""Flower bonus exports"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    FLOWER_BONUS,
)
from .contents.script_0 import script as script_0
from .contents.script_1 import script as script_1
from .contents.script_2 import script as script_2
from .contents.script_3 import script as script_3
from .contents.script_4 import script as script_4
from .contents.script_5 import script as script_5

bank = AnimationScriptBank(
    name=FLOWER_BONUS,
    start=0x02F461,
    end=0x02F4A0,
    pointer_table_start=0x02F455,
    scripts=[
        script_0,
        script_1,
        script_2,
        script_3,
        script_4,
        script_5,
    ],
)
