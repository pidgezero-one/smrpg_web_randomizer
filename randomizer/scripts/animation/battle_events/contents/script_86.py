"""BE0086_SMELTER_POURS_MOLTEN_LIQUID_SMITHY_WELDS"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[
        RunSubroutine(["command_0x3a7531"]),
        FadeOutScreen(duration=1),
        PauseScriptUntil(condition=FADE_4BPP_COMPLETE),
        SpriteQueue(
            field_object=1, destinations=["queuestart_0x3ae12b"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=0, destinations=["queuestart_0x3ae154"], bit_2=True, bit_4=True
        ),
        ClearAMEM8Bit(0x60),
        SetAMEM16BitToConst(0x60, 12),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x3A8AC0),
        RunSubroutine(["command_0x3a7760"]),
        SetAMEM8BitTo7E1x(0x60, 0x7EE00E),
        JmpIfAMEMBitsSet(0x60, [0], ["command_0x3a6d9e"]),
        SpriteQueue(
            field_object=2, destinations=["queuestart_0x3ae1b4"], bit_2=True, bit_4=True
        ),
        Jmp(["command_0x3a6da3"]),
        SpriteQueue(
            field_object=3,
            destinations=["queuestart_0x3ae1e1"],
            bit_2=True,
            bit_4=True,
            identifier="command_0x3a6d9e",
        ),
        RunSubroutine(["command_0x3a771e"], identifier="command_0x3a6da3"),
        Jmp(["command_0x3a7550"]),
    ]
)
