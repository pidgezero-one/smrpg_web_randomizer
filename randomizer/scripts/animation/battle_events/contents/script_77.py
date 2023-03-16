"""BE0077_SCREEN_FLASHES_WHITE"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[
        RunSubroutine(["command_0x3a7531"]),
        Db(bytearray(b"\x18\x00\x80")),
        Db(bytearray(b"\xba\x01\x00\x00")),
        ScreenEffect(SEF0016_UNKNOWN),
        Jmp(["command_0x3a7550"]),
    ]
)
