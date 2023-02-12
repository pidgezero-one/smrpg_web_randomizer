# E3214_SHIP_1ST_BOSS

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(SHIP_MIDBOSS_COMPLETED, ["EVENT_3214_fade_out_to_black_async_200"]),
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        SetBit(TEMP_707C_5),
        ClearBit(TEMP_707C_6),
        ClearBit(TEMP_707C_7),
        RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
        RestoreAllHP(),
        RestoreAllFP(),
        SetBit(SHIP_MIDBOSS_COMPLETED),
        EnterArea(
            room_id=R173_SUNKEN_SHIP_POSTKC_AREA_01_SMALL_ROOM_WTRAMPOLINE,
            face_direction=NORTHEAST,
            x=3,
            y=89,
            z=8,
            run_entrance_event=True,
        ),
        ClearBit(DIRECTIONAL_7049_0),
        ActionQueueSync(
            target=MARIO, subscript=[ASJumpToHeight(height=0, silent=True)]
        ),
        Pause(20),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        Return(),
        FadeOutToBlack(sync=False, identifier="EVENT_3214_fade_out_to_black_async_200"),
        SetBit(DIRECTIONAL_7049_0),
        EnableControls([]),
        EnterArea(
            room_id=R173_SUNKEN_SHIP_POSTKC_AREA_01_SMALL_ROOM_WTRAMPOLINE,
            face_direction=SOUTH,
            x=2,
            y=92,
            z=8,
            run_entrance_event=True,
        ),
        ActionQueueSync(
            target=MARIO, subscript=[ASJumpToHeight(height=0, silent=True)]
        ),
        Return(),
    ]
)
