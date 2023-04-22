# pylint: disable=C0301

"""E2606_FACTORY_1ST_BOSS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FreezeCamera(),
        ActionQueueSync(target=SCREEN_FOCUS, subscript=[ASWalkToXYCoords(x=5, y=20)]),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASSetWalkingSpeed(SLOW),
                ASWalk1StepNortheast(),
                ASWalkNortheastPixels(8),
            ],
        ),
        ActionQueueSync(
            target=MARIO, subscript=[ASWalkToXYCoords(x=10, y=47), ASFaceNorthwest()]
        ),
        StopEmbeddedActionScript(NPC_9),
        StopEmbeddedActionScript(SCREEN_FOCUS),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASSetSpriteSequence(
                    index=0, is_mold=True, is_sequence=True, looping=True
                ),
                ASWalk1StepSouthwest(),
                ASWalkSouthwestPixels(4),
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
            ],
        ),
        ActionQueueSync(target=NPC_8, subscript=[ASWalkNorthwestPixels(12)]),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASWalkSoutheastSteps(4),
            ],
        ),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASWalkSoutheastSteps(4),
            ],
        ),
        RunEventAsSubroutine(E1186_HENCHMAN_BATTLE_PACK_SELECTOR),
        JmpIfBitClear(GAME_OVER, ["EVENT_2606_remove_from_current_level_28"]),
        ResetAndChooseGame(),
        RemoveObjectFromCurrentLevel(
            NPC_6, identifier="EVENT_2606_remove_from_current_level_28"
        ),
        RemoveObjectFromCurrentLevel(NPC_7),
        RemoveObjectFromSpecificLevel(NPC_6, R469_FACTORY_GROUNDS_AREA_01),
        RemoveObjectFromSpecificLevel(NPC_7, R469_FACTORY_GROUNDS_AREA_01),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASSetSpriteSequence(
                    index=2, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASWalkNorthwestPixels(1),
                ASSetSpriteSequence(
                    index=0, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ],
        ),
        FadeInFromBlack(sync=False),
        ActionQueueSync(target=NPC_8, subscript=[ASWalkSoutheastPixels(12)]),
        Pause(16),
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        JmpIfBitClear(GAME_OVER, ["EVENT_2606_restore_all_hp_41"]),
        ResetAndChooseGame(),
        RestoreAllHP(identifier="EVENT_2606_restore_all_hp_41"),
        RestoreAllFP(),
        RemoveObjectFromCurrentLevel(NPC_8),
        RemoveObjectFromSpecificLevel(NPC_8, R469_FACTORY_GROUNDS_AREA_01),
        SetBit(INNER_FACTORY_ROOM_1_COMPLETED),
        EnterArea(
            room_id=R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
            face_direction=NORTHWEST,
            x=9,
            y=43,
            z=5,
            run_entrance_event=True,
        ),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        Return(),
    ]
)
