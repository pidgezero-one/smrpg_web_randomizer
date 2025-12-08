"""BE0007_COUNTDOWN_RUNS_SCHEDULE_1_00_3_00_5_00_6_00_7_00"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[
        RunSubroutine(["command_0x3a7531"]),
        ClearAMEM8Bit(0x60),
        SetAMEM16BitToConst(0x60, 3),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x3A8AC0),
        ObjectQueueAtOffsetAndIndex(index=4, target_address=0x3A8AC0),
        Pause1Frame(),
        SpriteQueue(
            field_object=0,
            destinations=["queuestart_0x3ab97e"],
            character_slot=True,
            bit_4=True),
        SpriteQueue(
            field_object=1,
            destinations=["queuestart_0x3ab97e"],
            character_slot=True,
            bit_4=True),
        SpriteQueue(
            field_object=2,
            destinations=["queuestart_0x3ab97e"],
            character_slot=True,
            bit_4=True),
        Db(bytearray(b"\x18\x00\x80")),
        RunSubroutine(["command_0x3a773f"]),
        RunSubroutine(["command_0x3a755e"]),
        Db(bytearray(b"[\x01\x00")),
        Jmp(["command_0x3a7550"]),
    ]
)
