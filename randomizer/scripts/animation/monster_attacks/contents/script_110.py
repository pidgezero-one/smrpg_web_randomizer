# SilverBullet

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        SetOMEM60To072C(),
        DisplayMessageAtOMEM60As(BATTLE_DIALOGUE),
        RunSubroutine(["command_0x353155"]),
        ClearAMEM16Bit(0x60),
        ClearAMEM8Bit(0x6F),
        ClearAMEM8Bit(0x6E),
        SetAMEM8BitToConst(0x6E, 1),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x35D2D5),
        PauseScriptUntilAMEMBitsSet(0x6F, [0]),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0506_JOHNNY,
            sequence=0,
            store_to_vram=True,
            looping=True,
            store_palette=True,
        ),
        ReturnSubroutine(),
    ]
)
