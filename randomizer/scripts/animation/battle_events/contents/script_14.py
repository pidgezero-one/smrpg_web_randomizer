"""BE0014_SET_7EE00A_TO_PARTY_SIZE_AT_START_OF_FIGHT"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[RunSubroutine(["command_0x3a69a6"]), Jmp(["command_0x3a7550"])]
)
