# pylint: disable=C0301

"""E3280_SHIP_LOWER_HENCHMAN_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(SHIP_PRE_BOSS_BATTLE_1_CLEARED, ["EVENT_3280_jmp_to_event_83"]),
        SetSyncActionScript(NPC_4, A0015_DO_NOTHING),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[ASTransferXYZFSteps(x=0, y=0, z=25, direction=NORTHEAST)]),
        RunEventAsSubroutine(
            E0803_SHIP_1ST_PREBOSS_BATTLE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        ActionQueueSync(target=NPC_0, subscript=[ASPause(20), ASFaceSouthwest()]),
        ActionQueueSync(target=NPC_1, subscript=[ASPause(3), ASFaceSouthwest()]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[ASPause(8), ASFaceMario(), ASWalk1StepSouth(), ASFaceMario()]),
        ActionQueueSync(target=NPC_3, subscript=[ASFaceMario()]),
        ActionQueueAsync(
            target=SCREEN_FOCUS, subscript=[ASWalk1StepNortheast(), ASWalk1StepNorth()]
        ),
        JmpIfBitSet(
            UNKNOWN_FIRST_PRE_BOSS_SUNKEN_SHIP_ROOM_7058_5,
            ["EVENT_3280_action_queue_sync_10"]),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASSetWalkingSpeed(SLOW),
                ASShiftZUpSteps(3),
                ASShiftZUpPixels(8),
                ASSetWalkingSpeed(NORMAL),
            ],
            identifier="EVENT_3280_action_queue_sync_10"),
        ActionQueueSync(
            target=NPC_0, subscript=[ASWalkToXYCoords(x=3, y=125), ASFaceMario()]
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASWalkToXYCoords(x=4, y=122),
                ASFaceMario(),
                ASWalkToXYCoords(x=3, y=123),
            ]),
        ActionQueueSync(
            target=NPC_2, subscript=[ASWalkToXYCoords(x=2, y=123), ASFaceMario()]
        ),
        ActionQueueSync(
            target=NPC_3, subscript=[ASWalkToXYCoords(x=3, y=122), ASFaceMario()]
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(40),
                ASTurnClockwise45DegreesNTimes(255),
                ASPause(2),
                ASTurnClockwise45DegreesNTimes(255),
                ASPause(12),
                ASTurnClockwise45DegreesNTimes(1),
                ASPause(2),
                ASTurnClockwise45DegreesNTimes(1),
                ASPause(2),
                ASTurnClockwise45DegreesNTimes(1),
                ASPause(2),
                ASTurnClockwise45DegreesNTimes(1),
                ASPause(12),
                ASTurnClockwise45DegreesNTimes(255),
                ASPause(2),
                ASTurnClockwise45DegreesNTimes(255),
            ]),
        SetSyncActionScript(NPC_4, A0014_FLOATING_CHEST),
        JmpIfBitSet(
            UNKNOWN_FIRST_PRE_BOSS_SUNKEN_SHIP_ROOM_7058_5,
            ["EVENT_3280_start_battle_23"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[ASPause(4), ASFaceNorth(), ASPause(2), ASFaceNorthwest()]),
        ActionQueueSync(
            target=NPC_2, subscript=[ASJumpToHeight(height=48, silent=True)]
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPause(4),
                ASFaceNorth(),
                ASPause(2),
                ASFaceNortheast(),
                ASPause(2),
                ASFaceEast(),
                ASPause(2),
                ASFaceSoutheast(),
            ]),
        ActionQueueSync(
            target=NPC_0, subscript=[ASJumpToHeight(height=48, silent=True)]
        ),
        RunEventAsSubroutine(
            E1186_HENCHMAN_BATTLE_PACK_SELECTOR, identifier="EVENT_3280_start_battle_23"
        ),
        SetBit(TEMP_707C_5),
        ClearBit(TEMP_707C_6),
        ClearBit(TEMP_707C_7),
        RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
        JmpIfBitSet(RUN_AWAY, ["EVENT_3280_set_bit_84"]),
        FadeInFromBlack(sync=False),
        ActionQueueSync(target=MARIO, subscript=[ASFaceNortheast()]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[ASFixedFCoordOn(), ASWalk1StepNortheast(), ASFixedFCoordOff()]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[ASFixedFCoordOn(), ASWalk1StepSoutheast(), ASFixedFCoordOff()]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[ASFixedFCoordOn(), ASWalk1StepNorthwest(), ASFixedFCoordOff()]),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASFaceSoutheast(),
                ASFixedFCoordOn(),
                ASWalk1StepNorthwest(),
                ASFixedFCoordOff(),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASJumpToHeight(height=48, silent=True),
                ASJumpToHeight(height=48, silent=True),
            ]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFaceNorth(),
                ASFaceNorthwest(),
                ASFaceNorth(),
                ASFaceNortheast(),
            ]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetAllSpeeds(VERY_FAST),
                ASSequenceLoopingOn(),
                ASJumpToHeight(height=64, silent=True),
                ASPlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASWalkNortheastSteps(13),
                ASVisibilityOff(),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASFixedFCoordOn(),
                ASWalk1StepNortheast(),
                ASFixedFCoordOff(),
                ASSetAllSpeeds(VERY_FAST),
                ASSequenceLoopingOn(),
                ASJumpToHeight(height=64, silent=True),
                ASPlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASWalk1StepSoutheast(),
                ASWalkNortheastSteps(11),
                ASVisibilityOff(),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetAllSpeeds(VERY_FAST),
                ASJumpToHeight(height=48, silent=True),
                ASPause(20),
                ASPlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASWalkNortheastSteps(3),
                ASWalkSoutheastSteps(4),
                ASWalkNortheastSteps(11),
                ASVisibilityOff(),
            ]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASSetAllSpeeds(VERY_FAST),
                ASJumpToHeight(height=48, silent=True),
                ASPause(20),
                ASPlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASWalkNortheastSteps(3),
                ASWalkSoutheastSteps(3),
                ASWalkNortheastSteps(10),
                ASVisibilityOff(),
            ]),
        RemoveObjectFromSpecificLevel(
            NPC_0, R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL
        ),
        RemoveObjectFromSpecificLevel(
            NPC_1, R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL
        ),
        RemoveObjectFromSpecificLevel(
            NPC_2, R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL
        ),
        RemoveObjectFromSpecificLevel(
            NPC_3, R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL
        ),
        SetBit(SHIP_PRE_BOSS_BATTLE_1_CLEARED),
        ClearBit(UNKNOWN_FIRST_PRE_BOSS_SUNKEN_SHIP_ROOM_7058_5),
        Return(),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3280_jmp_to_event_83"),
        SetBit(
            UNKNOWN_FIRST_PRE_BOSS_SUNKEN_SHIP_ROOM_7058_5,
            identifier="EVENT_3280_set_bit_84"),
        RunEventAtReturn(E3306_SHIP_LOWER_HENCHMAN_ROOM_LOADER_CONTINUED),
        Return(),
    ]
)
