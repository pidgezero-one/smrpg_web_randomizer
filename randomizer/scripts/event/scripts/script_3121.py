# pylint: disable=C0301

"""E3121_SEWER_BOSS_FIGHT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        JmpIfBitClear(GAME_OVER, ["EVENT_3121_set_bit_103"]),
        ResetAndChooseGame(),
        SetBit(TEMP_707C_5, identifier="EVENT_3121_set_bit_103"),
        ClearBit(TEMP_707C_6),
        ClearBit(TEMP_707C_7),
        Pause(10),
        SetBit(SEWER_BOSS_DEFEATED),
        RestoreAllHP(),
        RestoreAllFP(),
        RemoveObjectFromCurrentLevel(MARIO),
        SetBit(UNKNOWN_MIDAS_RIVER_704D_6),
        ClearBit(BUCKET_WARP_BIT),
        Pause(1),
        EnterArea(
            room_id=R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS,
            face_direction=SOUTH,
            x=12,
            y=108,
            z=11,
        ),
        RunEventAsSubroutine(E0014_STANDARD_ROOM_LOADER),
        ActionQueueAsync(
            target=MARIO, subscript=[ASJumpToHeight(height=144, silent=True)]
        ),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        Return(),
    ]
)
