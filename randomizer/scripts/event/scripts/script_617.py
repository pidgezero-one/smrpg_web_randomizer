# pylint: disable=C0301

"""E0617_MARIO_AS_BELLHOP_MAIN_EVENT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToObjectCoord(target_npc=NPC_5, coord=COORD_Y, pixel=True, bit_7=True),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 63, ["EVENT_617_enable_controls_until_return_3"]
        ),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalk1StepNortheast(),
                ASFaceNorthwest(),
            ]),
        EnableControlsUntilReturn(
            [], identifier="EVENT_617_enable_controls_until_return_3"
        ),
        Pause(60),
        JmpIfRandom1of2(["EVENT_617_action_queue_async_17"]),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASTransferToXYZF(x=6, y=64, z=0, direction=EAST),
                ASSetSequenceSpeed(NORMAL),
                ASSetWalkingSpeed(SLOW),
                ASWalkNorthwestSteps(4),
                ASSetSequenceSpeed(SLOW),
            ]),
        SetVarToConst(TEMP_70A9, 27),
        SetVarToConst(TEMP_70B8, 1),
        Jmp(["EVENT_617_pause_20"]),
        ActionQueueAsync(
            target=NPC_6,
            subscript=[
                ASTransferToXYZF(x=6, y=64, z=0, direction=EAST),
                ASVisibilityOn(),
                ASSetSequenceSpeed(NORMAL),
                ASSetWalkingSpeed(SLOW),
                ASWalkNorthwestSteps(4),
                ASSetSequenceSpeed(SLOW),
            ],
            identifier="EVENT_617_action_queue_async_17"),
        SetVarToConst(TEMP_70A9, 26),
        SetVarToConst(TEMP_70B8, 3),
        Pause(120, identifier="EVENT_617_pause_20"),
        ActionQueueAsync(target=NPC_1, subscript=[ASFaceNortheast()]),
        Pause(10),
        RunDialog(
            dialog_id=DI1005_PLAYER_ESCORTS_GUEST,
            above_object=NPC_1,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Pause(10),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSequenceLoopingOff(),
                ASSetSequenceSpeed(NORMAL),
                ASFaceSouth(),
            ]),
        ClearBit(TEMP_7042_4),
        ClearBit(TEMP_7042_5),
        ClearBit(TEMP_7042_6),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        CopyVarToVar(from_var=TEMP_70B8, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 2, ["EVENT_617_set_action_script_sync_43"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 3, ["EVENT_617_set_action_script_sync_46"]
        ),
        SetSyncActionScript(NPC_7, A0321_BELLHOP_FACE_PLAYER),
        Return(),
        SetSyncActionScript(
            NPC_8,
            A0321_BELLHOP_FACE_PLAYER,
            identifier="EVENT_617_set_action_script_sync_43"),
        SetSyncActionScript(NPC_9, A0321_BELLHOP_FACE_PLAYER),
        Return(),
        SetSyncActionScript(
            NPC_6,
            A0321_BELLHOP_FACE_PLAYER,
            identifier="EVENT_617_set_action_script_sync_46"),
        Return(),
    ]
)
