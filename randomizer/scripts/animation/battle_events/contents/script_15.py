"""BE0015_CROCO_STEALS_ITEMS_YOU_WANT_THEM_BACK"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[
        RunSubroutine(["command_0x3a7531"]),
        SetAMEM8BitTo7E1x(0x60, 0x7EE00A),
        JmpIfAMEMBitsClear(0x60, [1], ["command_0x3a6250"]),
        SpriteQueue(
            field_object=0, destinations=["queuestart_0x3aa845"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=1,
            destinations=["queuestart_0x3aa886"],
            character_slot=True,
            bit_4=True),
        RunSubroutine(["command_0x3a7729"]),
        ClearAMEM8Bit(0x60),
        SetAMEM16BitToConst(0x60, 5),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x3A8AC0),
        Jmp(["command_0x3a628a"]),
        SetAMEM8BitTo7E1x(0x60, 0x7EE00A, identifier="command_0x3a6250"),
        JmpIfAMEMBitsClear(0x60, [0], ["command_0x3a6273"]),
        SpriteQueue(
            field_object=0, destinations=["queuestart_0x3aa6a7"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=1,
            destinations=["queuestart_0x3aa886"],
            character_slot=True,
            bit_4=True),
        RunSubroutine(["command_0x3a7729"]),
        ClearAMEM8Bit(0x60),
        SetAMEM16BitToConst(0x60, 5),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x3A8AC0),
        Jmp(["command_0x3a628a"]),
        SpriteQueue(
            field_object=0,
            destinations=["queuestart_0x3aa845"],
            bit_2=True,
            bit_4=True,
            identifier="command_0x3a6273"),
        SpriteQueue(
            field_object=0,
            destinations=["queuestart_0x3aa886"],
            character_slot=True,
            bit_4=True),
        RunSubroutine(["command_0x3a7729"]),
        ClearAMEM8Bit(0x60),
        SetAMEM16BitToConst(0x60, 5),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x3A8AC0),
        RunSubroutine(["command_0x3a771e"], identifier="command_0x3a628a"),
        Jmp(["command_0x3a7550"]),
    ]
)
