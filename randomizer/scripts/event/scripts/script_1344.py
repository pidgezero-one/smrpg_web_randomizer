# pylint: disable=C0301

"""E1344_TOWER_HENCHMAN_2_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM,
            mod_id=32,
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM,
            mod_id=33,
        ),
        JmpIfBitClear(SPOOKUM_DIRECTION, ["EVENT_1344_pause_action_script_6"]),
        PlayMusicAtDefaultVolume(M32_AND_MY_NAMES_BOOSTER),
        ClearBit(SPOOKUM_DIRECTION),
        PauseActionScript(NPC_0, identifier="EVENT_1344_pause_action_script_6"),
        PauseActionScript(NPC_1),
        ActionQueueAsync(
            target=NPC_1, subscript=[ASWalkSouthwestPixels(6), ASFaceSoutheast()]
        ),
        RunEventAsSubroutine(E0798_TOWER_FIRST_RAIL_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
