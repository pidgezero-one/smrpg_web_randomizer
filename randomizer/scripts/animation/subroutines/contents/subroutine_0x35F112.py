# pylint: disable=C0301,C0103

"""referenced by weapons LuckyHammer"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=18,
    script=[
        ClearAMEM8Bit(0x6F, identifier="command_0x35f112"),
        ObjectQueueAtOffsetAndIndex(index=4, target_address=0x35F137),
        Pause1Frame(),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0002_MARIO_WALKING_UP_RIGHT, sequence=10, store_to_vram=True
        ),
        PauseScriptUntilAMEMBitsSet(0x6F, [0]),
        PauseScriptUntilSpriteSequenceDone(),
        ReturnSubroutine(),
    ],
)
