# E0701_PASTOR_MARIO

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7044_6, ["EVENT_256_ret_0"]),
        SetBit(TEMP_7044_6),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASFloatingOff(),
                ASBounceToXYWithHeight(x=23, y=70, height=2),
                ASShiftSoutheastPixels(8),
                ASFaceSouthwest(),
                ASShiftZUpPixels(4),
            ],
        ),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(index=6, is_sequence=True, looping=True),
                ASPause(60),
                ASSetSpriteSequence(
                    index=9, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASPause(30),
            ],
        ),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
    ]
)
