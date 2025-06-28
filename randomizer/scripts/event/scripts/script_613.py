# pylint: disable=C0301

"""E0613_MARRYMORE_SUITE_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASTransferXYZFPixels(x=0, y=248, z=0, direction=EAST),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
            ],
        ),
        JmpIfBitSet(BELLHOP_CALLED, ["EVENT_613_action_queue_async_34"]),
        JmpIfBitSet(TEMP_7042_4, ["EVENT_257_fade_in_from_black_async_0"]),
        JmpIfBitSet(TEMP_7042_3, ["EVENT_613_action_queue_async_6"]),
        ActionQueueAsync(
            target=NPC_0, subscript=[ASTransferToXYZF(x=4, y=19, z=0, direction=EAST)]
        ),
        Jmp(["EVENT_613_jmp_if_bit_set_7"]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=4, y=20, z=0, direction=EAST),
                ASFaceSouthwest(),
            ],
            identifier="EVENT_613_action_queue_async_6",
        ),
        JmpIfBitSet(
            TEMP_7042_3,
            ["EVENT_257_fade_in_from_black_async_0"],
            identifier="EVENT_613_jmp_if_bit_set_7",
        ),
        SetSyncActionScript(NPC_0, A0320_BELLHOP_SET_POSITION),
        FadeInFromBlack(sync=False),
        UnsyncActionScript(NPC_0),
        CopyVarToVar(from_var=MARRYMORE_SUITE_LEGAL_COUNT, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 1, ["EVENT_613_set_action_script_async_20"]
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASSetWalkingSpeed(SLOW),
                ASWalkSouthwestSteps(2),
                ASSetSequenceSpeed(SLOW),
            ],
        ),
        Jmp(["EVENT_613_set_action_script_sync_30"]),
        SetAsyncActionScript(
            MARIO, A0670_NOD_YES, identifier="EVENT_613_set_action_script_async_20"
        ),
        Pause(10),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASWalkSouthwestSteps(1),
                ASWalkNorthwestSteps(3),
                ASSetSequenceSpeed(SLOW),
                ASFaceSoutheast(),
            ],
        ),
        ActionQueueSync(target=MARIO, subscript=[ASPause(60), ASFaceNorth()]),
        RememberLastObject(),
        ActionQueueSync(target=MARIO, subscript=[ASPause(48), ASFaceNortheast()]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASWalkSoutheastSteps(3),
                ASWalkSouthwestSteps(1),
                ASSetSequenceSpeed(SLOW),
            ],
        ),
        Pause(10),
        SetSyncActionScript(
            NPC_0,
            A0321_BELLHOP_FACE_PLAYER,
            identifier="EVENT_613_set_action_script_sync_30",
        ),
        SetBit(BELLHOP_UNKNOWN),
        SetBit(TEMP_7042_3),
        Return(),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[ASTransferToXYZF(x=5, y=21, z=0, direction=EAST)],
            identifier="EVENT_613_action_queue_async_34",
        ),
        SetSyncActionScript(NPC_0, A0978_RANDOMLY_FACE_SOUTHWEST),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
