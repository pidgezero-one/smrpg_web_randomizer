# pylint: disable=C0301

"""E1544_SAND_WHIRLPOOL"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FreezeAllNPCsUntilReturn(),
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=PRIMARY_TEMP_700C),
        SetSyncActionScript(MARIO, A0781_PLAYER_SPINS_ON_FLOWER),
        Pause(1),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASInc(PRIMARY_TEMP_700C),
                ASFixedFCoordOff(),
                ASFaceEast7C(),
                ASFixedFCoordOn(),
            ],
            identifier="EVENT_1544_action_queue_sync_7",
        ),
        Pause(2),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_1544_action_queue_sync_7"]),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000, 2, ["EVENT_1544_action_queue_sync_7"]
        ),
        PixelateLayers(
            layers=[LAYER_L1, LAYER_L2, LAYER_L3], pixel_size=9, duration=70
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPlaySound(sound=SO112_DRAINING_WATER, channel=4),
                ASFixedFCoordOff(),
                ASSetVarToConst(PRIMARY_TEMP_700C, 2),
                ASStartLoopNTimes(15),
                ASInc(PRIMARY_TEMP_700C),
                ASFaceEast7C(),
                ASVisibilityOn(),
                ASWalkFDirectionPixels(1),
                ASVisibilityOff(),
                ASPause(1),
                ASEndLoop(),
            ],
        ),
        FadeOutToBlack(sync=False, duration=30),
        Return(),
    ]
)
