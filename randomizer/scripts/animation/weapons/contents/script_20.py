# HurlyGloves

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        ClearAMEM16Bit(0x60),
        JmpIfAMEM8BitEqualsConst(0x62, 1, ["command_0x35ef38"]),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x35F5E4),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0017_BOWSER_SWING_BALL_CHAIN, sequence=1, store_to_vram=True
        ),
        ReturnSubroutine(),
        ClearAMEM16Bit(0x6E, identifier="command_0x35ef38"),
        ObjectQueueAtOffsetAndIndex(index=2, target_address=0x35F5E4),
        PauseScriptUntilAMEMBitsSet(0x6E, [0]),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0017_BOWSER_SWING_BALL_CHAIN, sequence=1, store_to_vram=True
        ),
        PauseScriptUntilSpriteSequenceDone(),
        PauseScriptUntilAMEMBitsSet(0x6F, [0]),
        ReturnSubroutine(),
    ]
)
