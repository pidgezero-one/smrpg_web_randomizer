"""Toad tutorial exports"""

from randomizer.types.battle_animation_scripts.types import AnimationScriptBank
from randomizer.types.battle_animation_scripts.ids import (
    TOAD_TUTORIAL)
from .contents.script_0 import script as script_0

bank = AnimationScriptBank(
    name=TOAD_TUTORIAL,
    start=0x02F4BF,
    end=0x02F50D,
    scripts=[
        script_0,
    ])
