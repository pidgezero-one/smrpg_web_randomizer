# pylint: disable=C0301

"""E1650_MOLEVILLE_LIBERATED_EXTERIOR_LOADER_CONTD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StopMusic(),
        Pause(1),
        EnterArea(
            room_id=R338_MOLEVILLE_DYNA_AND_MITES_HOUSE,
            face_direction=SOUTHWEST,
            x=4,
            y=41,
            z=0,
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASShadowOff(),
                ASTransferXYZFSteps(x=0, y=0, z=20, direction=EAST),
            ],
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSequenceLoopingOn(),
                ASTransferToXYZF(x=3, y=38, z=0, direction=EAST),
                ASFaceSouthwest(),
                ASVisibilityOn(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASTransferToXYZF(x=2, y=38, z=0, direction=EAST),
                ASFaceSoutheast(),
                ASVisibilityOn(),
                ASSequenceLoopingOn(),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(SLOW),
            ],
        ),
        FadeInFromBlack(sync=False),
        SetAsyncActionScript(NPC_1, A0650_BLUE_CLOUD_MOVEMENT),
        FadeOutSoundToVolume(duration=0, volume=64),
        PlaySoundBalance(sound=SO019_LONG_FALL, balance=32),
        Pause(60),
        FadeOutSoundToVolume(duration=0, volume=127),
        PlaySound(sound=SO021_RUMBLING, channel=6),
        ActionQueueSync(target=NPC_0, subscript=[ASPause(8), ASFaceSoutheast()]),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSouthPixels(4),
                ASStartLoopNTimes(5),
                ASWalkNorthPixels(8),
                ASWalkSouthPixels(8),
                ASEndLoop(),
                ASWalkNorthPixels(4),
                ASSetWalkingSpeed(FASTER),
                ASWalkSouthPixels(3),
                ASStartLoopNTimes(8),
                ASWalkNorthPixels(6),
                ASWalkSouthPixels(6),
                ASEndLoop(),
                ASWalkNorthPixels(3),
                ASSetWalkingSpeed(FAST),
                ASWalkSouthPixels(2),
                ASStartLoopNTimes(10),
                ASWalkNorthPixels(4),
                ASWalkSouthPixels(4),
                ASEndLoop(),
                ASWalkNorthPixels(2),
            ],
        ),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASTransferToXYZF(x=4, y=41, z=20, direction=EAST),
                ASSetSpriteSequence(index=7, is_sequence=True, looping=True),
                ASVisibilityOn(),
                ASShadowOn(),
                ASSetVRAMPriority(PRIORITY_3),
                ASJumpToHeight(0),
                ASPause(
                    1, identifier="EVENT_1650_action_queue_sync_16_SUBSCRIPT_pause_6"
                ),
                ASJmpIfObjectInAir(
                    NPC_3, ["EVENT_1650_action_queue_sync_16_SUBSCRIPT_pause_6"]
                ),
                ASJumpToHeight(104),
                ASSetAllSpeeds(NORMAL),
                ASWalkSouthwestSteps(5),
                ASVisibilityOff(),
            ],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPause(4),
                ASSetSpriteSequence(
                    index=8, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASShadowOn(),
                ASFloatingOn(),
                ASJumpToHeight(height=0, silent=True),
                ASPause(
                    1, identifier="EVENT_1650_action_queue_sync_17_SUBSCRIPT_pause_5"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_1650_action_queue_sync_17_SUBSCRIPT_pause_5"]
                ),
                ASJumpToHeight(height=104, silent=True),
                ASWalk1StepNorth(),
                ASPause(
                    1, identifier="EVENT_1650_action_queue_sync_17_SUBSCRIPT_pause_9"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_1650_action_queue_sync_17_SUBSCRIPT_pause_9"]
                ),
                ASFaceSouthwest(),
                ASSetSequenceSpeed(VERY_FAST),
                ASSetSpriteSequence(index=8, is_sequence=True, looping=True),
                ASPause(60),
                ASResetProperties(),
                ASSetAllSpeeds(NORMAL),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetSolidityBits(cant_pass_walls=True),
                ASPause(12),
                ASTransferToXYZF(x=5, y=40, z=20, direction=EAST),
                ASVisibilityOn(),
                ASFloatingOn(),
                ASJumpToHeight(0),
                ASWalk1StepNortheast(),
                ASSetAllSpeeds(NORMAL),
                ASPause(
                    1, identifier="EVENT_1650_action_queue_sync_18_SUBSCRIPT_pause_8"
                ),
                ASJmpIfObjectInAir(
                    NPC_2, ["EVENT_1650_action_queue_sync_18_SUBSCRIPT_pause_8"]
                ),
                ASJumpToHeight(133),
                ASWalk1StepNortheast(),
                ASPause(
                    1, identifier="EVENT_1650_action_queue_sync_18_SUBSCRIPT_pause_12"
                ),
                ASJmpIfObjectInAir(
                    NPC_2, ["EVENT_1650_action_queue_sync_18_SUBSCRIPT_pause_12"]
                ),
                ASJumpToHeight(125),
                ASWalkSoutheastSteps(2),
                ASPause(
                    1, identifier="EVENT_1650_action_queue_sync_18_SUBSCRIPT_pause_16"
                ),
                ASJmpIfObjectInAir(
                    NPC_2, ["EVENT_1650_action_queue_sync_18_SUBSCRIPT_pause_16"]
                ),
                ASJumpToHeight(116),
                ASWalkSouthwestSteps(2),
                ASClearSolidityBits(cant_pass_walls=True),
            ],
        ),
        Pause(20),
        SetVarToConst(TEMP_7034, 2),
        SetVarToConst(X_COORD_1, 2304),
        SetVarToConst(Y_COORD_1, 5376),
        SetVarToConst(Z_COORD_1, 256),
        StartLoopNTimes(23),
        Pause(1, identifier="EVENT_1650_pause_25"),
        CreatePacketAt7010(
            packet=P032_BLUE_CLOUD, destinations=["EVENT_1650_pause_25"]
        ),
        Pause(4),
        AddConstToVar(TEMP_7034, 3),
        AddConstToVar(Z_COORD_1, 112),
        EndLoop(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetAllSpeeds(SLOW),
                ASWalk1StepSouthwest(),
                ASFaceEast(),
                ASSetAllSpeeds(NORMAL),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetAllSpeeds(NORMAL),
                ASWalkNorthwestSteps(2),
                ASFaceSouthwest(),
                ASSetSequenceSpeed(SLOW),
                ASSequenceLoopingOn(),
            ],
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetAllSpeeds(FAST),
                ASWalkSoutheastSteps(3),
                ASFaceNortheast(),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(SLOW),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ],
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFixedFCoordOn(),
                ASSetAllSpeeds(FAST),
                ASWalkEastSteps(2),
                ASFixedFCoordOff(),
                ASWalk1StepSoutheast(),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(SLOW),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ],
        ),
        SetAsyncActionScript(NPC_2, A0650_BLUE_CLOUD_MOVEMENT),
        PauseScriptUntilEffectDone(),
        SetBit(OPTIONAL_MINECART_CLEARED),
        SetBit(TEMP_7042_1),
        SetSyncActionScript(NPC_0, A0160_SEQUENCE_LOOPING_ON),
        SetSyncActionScript(NPC_1, A0160_SEQUENCE_LOOPING_ON),
        SetSyncActionScript(NPC_2, A0160_SEQUENCE_LOOPING_ON),
        Return(),
    ]
)
