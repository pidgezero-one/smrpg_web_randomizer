# pylint: disable=C0301

"""E0441_PIPE_VAULT_CHOMPWEED_ROOM_CHOMPWEEDS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfMarioInAir(["EVENT_256_ret_0"]),
        StoreCoinCountTo7000(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_441_action_queue_sync_10"]),
        SummonObjectToCurrentLevelAtMariosCoords(NPC_8),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASFloatingOff(),
                ASTransferXYZFPixels(x=0, y=0, z=24, direction=EAST),
                ASSetVarToRandom(PRIMARY_TEMP_700C, 8),
                ASFaceEast7C(),
                ASJumpToHeight(height=108, silent=True),
                ASSetWalkingSpeed(NORMAL),
                ASWalkFDirectionPixels(12),
                ASFloatingOn(),
                ASWalkFDirectionPixels(12),
                ASVisibilityOff(),
            ],
        ),
        SummonObjectToCurrentLevelAtMariosCoords(NPC_9),
        ActionQueueSync(
            target=NPC_9,
            subscript=[
                ASFloatingOff(),
                ASTransferXYZFPixels(x=0, y=0, z=24, direction=EAST),
                ASSetVarToRandom(PRIMARY_TEMP_700C, 8),
                ASFaceEast7C(),
                ASJumpToHeight(height=108, silent=True),
                ASSetWalkingSpeed(NORMAL),
                ASWalkFDirectionPixels(12),
                ASFloatingOn(),
                ASWalkFDirectionPixels(12),
                ASVisibilityOff(),
            ],
        ),
        PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=6),
        SetVarToConst(PRIMARY_TEMP_7000, 2),
        Dec7000FromCoins(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=8, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASJumpToHeight(height=108, silent=True),
                ASPause(15),
                ASResetProperties(),
            ],
            identifier="EVENT_441_action_queue_sync_10",
        ),
        Return(),
    ]
)
