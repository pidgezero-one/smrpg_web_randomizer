"""Monster entrance animation exports"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    MONSTER_ENTRANCES,
)
from .contents.script_0 import script as script_0
from .contents.script_1 import script as script_1
from .contents.script_2 import script as script_2
from .contents.script_3 import script as script_3
from .contents.script_4 import script as script_4
from .contents.script_5 import script as script_5
from .contents.script_6 import script as script_6
from .contents.script_7 import script as script_7
from .contents.script_8 import script as script_8
from .contents.script_9 import script as script_9
from .contents.script_10 import script as script_10
from .contents.script_11 import script as script_11
from .contents.script_12 import script as script_12
from .contents.script_13 import script as script_13
from .contents.script_14 import script as script_14
from .contents.script_15 import script as script_15

bank = AnimationScriptBank(
    name=MONSTER_ENTRANCES,
    start=0x352148,
    end=0x3523C3,
    pointer_table_start=0x352128,
    scripts=[
        script_0,
        script_1,
        script_2,
        script_3,
        script_4,
        script_5,
        script_6,
        script_7,
        script_8,
        script_9,
        script_10,
        script_11,
        script_12,
        script_13,
        script_14,
        script_15,
    ],
)
