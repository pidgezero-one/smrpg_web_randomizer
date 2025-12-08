# pylint: disable=C0301

"""E1358_CURTAIN_GAME_BEGINS_NPCS_WALK_INTO_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RemoveObjectFromSpecificLevel(
            NPC_6, R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM
        ),
        RemoveObjectFromSpecificLevel(NPC_3, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM),
        RemoveObjectFromSpecificLevel(
            NPC_8, R037_BOOSTER_TOWER_4F_3LEVEL_ROOM_WJUMPING_SPOOKUMS
        ),
        RemoveObjectFromSpecificLevel(NPC_4, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM),
        RemoveObjectFromSpecificLevel(
            NPC_0, R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM
        ),
        MoveScriptToBackgroundThread2(),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=9, y=18, z=0, direction=EAST),
                ASSetPriority(3),
                ASClearSolidityBits(cant_pass_walls=True),
                ASSetWalkingSpeed(SLOW),
                ASSetSequenceSpeed(NORMAL),
                ASFaceSouthwest(),
                ASVisibilityOn(),
                ASWalkSouthwestSteps(3),
                ASWalkNorthwestSteps(2),
                ASFaceNortheast(),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASPause(70),
                ASTransferToXYZF(x=9, y=18, z=0, direction=EAST),
                ASSetPriority(2),
                ASClearSolidityBits(cant_pass_walls=True),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(FAST),
                ASFaceSouthwest(),
                ASVisibilityOn(),
                ASWalkSouthwestSteps(7),
                ASWalkNorthwestSteps(5),
                ASFaceNortheast(),
                ASSetPriority(3),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASPause(70),
                ASPause(40),
                ASTransferToXYZF(x=9, y=18, z=0, direction=EAST),
                ASSetPriority(2),
                ASClearSolidityBits(cant_pass_walls=True),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(FAST),
                ASFaceSouthwest(),
                ASVisibilityOn(),
                ASWalkSouthwestSteps(7),
                ASWalkNorthwestSteps(3),
                ASFaceNortheast(),
                ASSetPriority(3),
            ]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASPause(70),
                ASPause(40),
                ASPause(120),
                ASTransferToXYZF(x=9, y=18, z=0, direction=EAST),
                ASSetPriority(2),
                ASClearSolidityBits(cant_pass_walls=True),
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASFaceSouthwest(),
                ASVisibilityOn(),
                ASWalkSouthwestSteps(7),
                ASWalkNorthwestSteps(1),
                ASFaceNortheast(),
                ASSetPriority(3),
            ]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASFaceSouthwest(),
                ASFixedFCoordOn(),
                ASWalkSouthwestSteps(1),
                ASWalkNorthwestSteps(1),
                ASSetAllSpeeds(NORMAL),
                ASPause(30),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
                ASPause(30),
                ASResetProperties(),
            ]),
        ActionQueueAsync(
            target=NPC_0, subscript=[ASFixedFCoordOff(), ASFaceNorthwest()]
        ),
        Jmp(["EVENT_1365_play_music_default_volume_0"], identifier="EVENT_1358_jmp_66"),
    ]
)
