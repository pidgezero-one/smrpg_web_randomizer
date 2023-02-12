# E1370_CURTAIN_GAME_SUCCESS_FAILURE_GENERAL

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(30),
        PlaySound(
            sound=SO088_WRONG_SIGNAL, channel=4, identifier="EVENT_1370_play_sound____"
        ),
        JmpIfVarEqualsConst(TEMP_7026, 2, ["EVENT_1369_pause_0"]),
        Pause(30),
        ActionQueueAsync(target=MARIO, subscript=[ASResetProperties()]),
        PlaySound(sound=SO090_CURTAIN, channel=6),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=32,
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=36,
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=40,
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=44,
        ),
        MoveScriptToBackgroundThread2(),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASFixedFCoordOff(),
                ASResetProperties(),
                ASSetAllSpeeds(VERY_FAST),
                ASBounceToXYWithHeight(x=5, y=19, height=0),
                ASFaceSouthwest(),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASFixedFCoordOff(),
                ASResetProperties(),
                ASSetAllSpeeds(VERY_FAST),
                ASBounceToXYWithHeight(x=3, y=20, height=0),
                ASFaceNortheast(),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASFixedFCoordOff(),
                ASResetProperties(),
                ASSetAllSpeeds(VERY_FAST),
                ASBounceToXYWithHeight(x=4, y=22, height=0),
                ASFaceNortheast(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASFixedFCoordOff(),
                ASResetProperties(),
                ASSetAllSpeeds(VERY_FAST),
                ASBounceToXYWithHeight(x=5, y=24, height=0),
                ASFaceNortheast(),
            ],
        ),
        Pause(20),
        Inc(TEMP_7026),
        Jmp(["EVENT_1358_jmp_66"]),
    ]
)
