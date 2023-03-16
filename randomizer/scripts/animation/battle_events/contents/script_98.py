"""BE0098_SMITHY_IS_DEFEATED"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[
        RunSubroutine(["command_0x3a7531"]),
        FadeCurrentMusicToVolume(speed=3, volume=0),
        SpriteQueue(
            field_object=1, destinations=["queuestart_0x3ae382"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=2, destinations=["queuestart_0x3ae39b"], bit_2=True, bit_4=True
        ),
        Pause1Frame(),
        Pause1Frame(),
        Pause1Frame(),
        Pause1Frame(),
        Pause1Frame(),
        Pause1Frame(),
        Pause1Frame(),
        Pause1Frame(),
        Pause1Frame(),
        Pause1Frame(),
        Pause1Frame(),
        Pause1Frame(),
        Pause1Frame(),
        Pause1Frame(),
        Pause1Frame(),
        Pause1Frame(),
        RunSubroutine(["command_0x3a7729"]),
        SetAMEM16BitToConst(0x60, 12),
        ObjectQueueAtOffsetAndIndex(index=44, target_address=0x3A8AC0),
        ObjectQueueAtOffsetAndIndex(index=46, target_address=0x3A8AC0),
        RunSubroutine(["command_0x3a773f"]),
        ObjectQueueAtOffsetAndIndex(index=54, target_address=0x3A8AC0),
        RunSubroutine(["command_0x3a771e"]),
        Jmp(["command_0x3a7550"]),
    ]
)
