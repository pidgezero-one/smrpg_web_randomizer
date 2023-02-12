# SuperSlap

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        ClearAMEM16Bit(0x60),
        JmpIfAMEM8BitEqualsConst(0x62, 1, ["command_0x35f054"]),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0010_TOADSTOOL_SLAP_ATTACK, sequence=0, store_to_vram=True
        ),
        ObjectQueueAtOffsetAndIndex(index=4, target_address=0x35F35F),
        ReturnSubroutine(),
        ObjectQueueAtOffsetAndIndex(
            index=6, target_address=0x35F35F, identifier="command_0x35f054"
        ),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0010_TOADSTOOL_SLAP_ATTACK, sequence=2, store_to_vram=True
        ),
        PauseScriptUntilSpriteSequenceDone(),
        ResetObjectMappingMemory(),
        ReturnSubroutine(),
    ]
)
