"""Hammer animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        ClearAMEM16Bit(0x60),
        JmpIfAMEM8BitEqualsConst(0x62, 1, ["command_0x35ed84"]),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x35F137),
        Pause1Frame(),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0005_MARIO_HAMMER_ATTACK_UP_RIGHT,
            sequence=0,
            store_to_vram=True),
        ReturnSubroutine(),
        ObjectQueueAtOffsetAndIndex(
            index=2, target_address=0x35F137, identifier="command_0x35ed84"
        ),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=3),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0005_MARIO_HAMMER_ATTACK_UP_RIGHT,
            sequence=1,
            store_to_vram=True),
        PauseScriptUntilSpriteSequenceDone(),
        ReturnSubroutine(),
    ]
)
