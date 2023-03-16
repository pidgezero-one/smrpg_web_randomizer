"""BE0085_FEAR_ROULETTE"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    header=["command_0x3a6d49, command_0x3a6d5a"],
    script=[
        RunSubroutine(["command_0x3a7531"]),
        ClearAMEM8Bit(0x60),
        SetAMEM16BitToConst(0x60, 11),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x3A8AC0),
        RunSubroutine(["command_0x3a771e"]),
        Db(bytearray(b"\xe2")),
        RunSubroutine(["command_0x3a7531"], identifier="command_0x3a6d49"),
        ClearAMEM8Bit(0x60),
        SetAMEM16BitToConst(0x60, 11),
        ObjectQueueAtOffsetAndIndex(index=2, target_address=0x3A8AC0),
        RunSubroutine(["command_0x3a771e"]),
        Db(bytearray(b"\xe2")),
        RunSubroutine(["command_0x3a7531"], identifier="command_0x3a6d5a"),
        ClearAMEM8Bit(0x60),
        SetAMEM16BitToConst(0x60, 11),
        ObjectQueueAtOffsetAndIndex(index=4, target_address=0x3A8AC0),
        RunSubroutine(["command_0x3a771e"]),
        Db(bytearray(b"\xe2")),
    ],
)
