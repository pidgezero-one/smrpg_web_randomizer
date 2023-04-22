"""FryingPan animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        ClearAMEM16Bit(0x60),
        JmpIfAMEM8BitEqualsConst(0x62, 1, ["command_0x35f0ee"]),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x35F391),
        Pause1Frame(),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0011_TOADSTOOL_FRYING_PAN_ATTACK,
            sequence=0,
            store_to_vram=True,
        ),
        ReturnSubroutine(),
        ObjectQueueAtOffsetAndIndex(
            index=2, target_address=0x35F391, identifier="command_0x35f0ee"
        ),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=3),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0011_TOADSTOOL_FRYING_PAN_ATTACK,
            sequence=1,
            store_to_vram=True,
        ),
        PauseScriptUntilSpriteSequenceDone(),
        ReturnSubroutine(),
    ]
)
