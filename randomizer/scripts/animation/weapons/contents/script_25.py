"""WarFan animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        ClearAMEM16Bit(0x60),
        JmpIfAMEM8BitEqualsConst(0x62, 1, ["command_0x35efd4"]),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x35F43F),
        Pause1Frame(),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0010_TOADSTOOL_SLAP_ATTACK, sequence=3, store_to_vram=True
        ),
        ReturnSubroutine(),
        ClearAMEM8Bit(0x6F, identifier="command_0x35efd4"),
        ObjectQueueAtOffsetAndIndex(index=2, target_address=0x35F43F),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=3),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0010_TOADSTOOL_SLAP_ATTACK, sequence=4, store_to_vram=True
        ),
        PauseScriptUntilSpriteSequenceDone(),
        PauseScriptUntilAMEMBitsSet(0x6F, [0]),
        ReturnSubroutine(),
    ]
)
