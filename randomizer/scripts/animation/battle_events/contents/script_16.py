"""BE0016_CROCO_RETURNS_ITEMS_ENOUGH_HERE_S_YOUR_JUNK"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[
        RunSubroutine(["command_0x3a7531"]),
        SpriteQueue(
            field_object=0, destinations=["queuestart_0x3aa892"], bit_2=True, bit_4=True
        ),
        RunSubroutine(["command_0x3a7729"]),
        ClearAMEM8Bit(0x60),
        SetAMEM16BitToConst(0x60, 5),
        ObjectQueueAtOffsetAndIndex(index=2, target_address=0x3A8AC0),
        RunSubroutine(["command_0x3a771e"]),
        Jmp(["command_0x3a7550"]),
    ]
)
