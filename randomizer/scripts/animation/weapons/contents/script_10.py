# Cymbals

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        ClearAMEM16Bit(0x60),
        JmpIfAMEM8BitEqualsConst(0x62, 1, ["command_0x35ee0f"]),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x35F783),
        Pause1Frame(),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0023_MALLOW_SWING_STICK, sequence=2, store_to_vram=True
        ),
        ReturnSubroutine(),
        ObjectQueueAtOffsetAndIndex(
            index=2, target_address=0x35F783, identifier="command_0x35ee0f"
        ),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=2),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0023_MALLOW_SWING_STICK, sequence=3, store_to_vram=True
        ),
        PauseScriptUntilSpriteSequenceDone(),
        ReturnSubroutine(),
    ]
)
