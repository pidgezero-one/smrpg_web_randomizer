"""Ally spell exports"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    ALLY_SPELLS)
from randomizer.types.spells.ids import ALLY_SPELL_POINTER_TABLE_START
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
from .contents.script_16 import script as script_16
from .contents.script_17 import script as script_17
from .contents.script_18 import script as script_18
from .contents.script_19 import script as script_19
from .contents.script_20 import script as script_20
from .contents.script_21 import script as script_21
from .contents.script_22 import script as script_22
from .contents.script_23 import script as script_23
from .contents.script_24 import script as script_24
from .contents.script_25 import script as script_25
from .contents.script_26 import script as script_26

bank = AnimationScriptBank(
    name=ALLY_SPELLS,
    start=0x35C9C8,
    end=0x35CAAB,
    pointer_table_start=ALLY_SPELL_POINTER_TABLE_START,
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
        script_16,
        script_17,
        script_18,
        script_19,
        script_20,
        script_21,
        script_22,
        script_23,
        script_24,
        script_25,
        script_26,
    ])
