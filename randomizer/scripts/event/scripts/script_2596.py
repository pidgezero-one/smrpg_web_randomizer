# pylint: disable=C0301

"""E2596_ABYSS_1ST_BOSS_FIGHT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(ABYSS_BOSS_1_DEFEATED, ["EVENT_2596_ret_42"]),
        Pause(16),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASStartLoopNTimes(1),
                ASSetSpriteSequence(
                    index=0, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASPause(16),
                ASSetSpriteSequence(
                    index=0,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPause(16),
                ASEndLoop(),
            ],
        ),
        ActionQueueAsync(
            target=MARIO, subscript=[ASResetProperties(), ASFaceNortheast()]
        ),
        ActionQueueAsync(target=SCREEN_FOCUS, subscript=[ASWalkToXYCoords(x=4, y=69)]),
        Pause(30),
        SetSyncActionScript(MARIO, A0861_ABYSS_1ST_BOSS_FIGHT_SHOCKED),
        SetSyncActionScript(SCREEN_FOCUS, A0862_ABYSS_1ST_BOSS_FIGHT_CAMERA),
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        SetSyncActionScript(MARIO, A0015_DO_NOTHING),
        SetSyncActionScript(SCREEN_FOCUS, A0015_DO_NOTHING),
        JmpIfBitClear(GAME_OVER, ["EVENT_2596_restore_all_hp_38"]),
        ResetAndChooseGame(),
        RestoreAllHP(identifier="EVENT_2596_restore_all_hp_38"),
        RestoreAllFP(),
        SetBit(ABYSS_BOSS_1_DEFEATED),
        SetBit(GAMEBOY_KID_PURCHASE_COMPLETE),
        EnterArea(
            room_id=R433_SMITHY_FACTORY_AREA_01_____DUMMY,
            face_direction=NORTHEAST,
            x=7,
            y=106,
            z=10,
            run_entrance_event=True,
        ),
        Return(identifier="EVENT_2596_ret_42"),
    ]
)
