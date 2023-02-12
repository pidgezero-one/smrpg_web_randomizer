# E2603_FACTORY_4TH_BOSS_FIGHT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(INNER_FACTORY_ROOM_4_COMPLETED, ["EVENT_2603_ret_72"]),
        SetBit(INNER_FACTORY_ROOM_4_COMPLETED),
        ActionQueueSync(target=MARIO, subscript=[ASFaceNorthwest()]),
        ActionQueueAsync(target=SCREEN_FOCUS, subscript=[ASWalkToXYCoords(x=5, y=75)]),
        Pause(16),
        ActionQueueAsync(
            target=NPC_12,
            subscript=[
                ASSequenceLoopingOff(),
                ASPause(16),
                ASFaceSoutheast(),
                ASShiftSoutheastSteps(2),
            ],
        ),
        Db(bytearray(b"\xfd\x8d")),
        ActionQueueAsync(
            target=NPC_12,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(FAST),
                ASWalk1StepSouthwest(),
                ASShiftSouthwestPixels(8),
                ASFaceSoutheast(),
            ],
        ),
        Db(bytearray(b"\xfd\x8d")),
        ActionQueueAsync(
            target=NPC_12,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASWalk1StepNortheast(),
                ASShiftNortheastPixels(10),
                ASShiftNorthwestSteps(2),
                ASFaceSoutheast(),
            ],
        ),
        Db(bytearray(b"\xfd\x8d")),
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        JmpIfBitClear(GAME_OVER, ["EVENT_2603_restore_all_hp_18"]),
        ResetAndChooseGame(),
        RestoreAllHP(identifier="EVENT_2603_restore_all_hp_18"),
        RestoreAllFP(),
        RemoveObjectFromCurrentLevel(NPC_0),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromCurrentLevel(NPC_2),
        RemoveObjectFromCurrentLevel(NPC_3),
        RemoveObjectFromCurrentLevel(NPC_4),
        RemoveObjectFromCurrentLevel(NPC_5),
        RemoveObjectFromCurrentLevel(NPC_6),
        RemoveObjectFromCurrentLevel(NPC_12),
        RemoveObjectFromSpecificLevel(
            NPC_0, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM
        ),
        RemoveObjectFromSpecificLevel(
            NPC_1, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM
        ),
        RemoveObjectFromSpecificLevel(
            NPC_2, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM
        ),
        RemoveObjectFromSpecificLevel(
            NPC_3, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM
        ),
        RemoveObjectFromSpecificLevel(
            NPC_4, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM
        ),
        RemoveObjectFromSpecificLevel(
            NPC_5, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM
        ),
        RemoveObjectFromSpecificLevel(
            NPC_6, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM
        ),
        RemoveObjectFromSpecificLevel(
            NPC_12, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASShiftToXYCoords(x=10, y=91),
                ASSetWalkingSpeed(FASTEST),
                ASShiftNorthPixels(8),
                ASFaceNorthwest(),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        RunEventAsSubroutine(E1969_CHECK_IF_STAR_PIECES_FOR_FACTORY_BOSS_COLLECTED),
        JmpIfComparisonResultIsLesser(["EVENT_2603_fade_in_from_black_async_39"]),
        SummonObjectToSpecificLevel(
            NPC_14, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM
        ),
        FadeInFromBlack(
            sync=False, identifier="EVENT_2603_fade_in_from_black_async_39"
        ),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        Return(identifier="EVENT_2603_ret_72"),
    ]
)
