# E0593_MINES_BOSS_ROOM_LOADER_AFTER_DEFEAT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(
            POST_MINES_LEVEL_MODS_COMPLETED, ["EVENT_257_fade_in_from_black_async_0"]
        ),
        Pause(2),
        FadeOutMusicToVolume(duration=0, volume=1),
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        RemoveObjectFromSpecificLevel(
            NPC_0, R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE
        ),
        RemoveObjectFromSpecificLevel(
            NPC_4, R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE
        ),
        RemoveObjectFromSpecificLevel(
            NPC_5, R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE
        ),
        RemoveObjectFromSpecificLevel(
            NPC_6, R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE
        ),
        SetBit(MINES_BOSS_2_DEFEATED),
        RestoreAllHP(),
        RestoreAllFP(),
        FadeInFromBlack(sync=False),
        RunEventAsSubroutine(E0201_UNLOCK_FOREST_IF_GATED_BY_MOLEVILLE_CHARACTER),
        RunEventAsSubroutine(E0198_UNLOCK_TOWER_IF_GATED_BY_MOLEVILLE),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE,
            mod_id=0,
        ),
        Pause(1),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE,
            mod_id=1,
        ),
        Pause(1),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
            mod_id=0,
        ),
        Pause(1),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
            mod_id=1,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE,
            mod_id=0,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
            mod_id=0,
        ),
        FadeInMusic(M33_MOLEVILLE),
        SetBit(TEMP_7049_6),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R276_MOLEVILLE_MINES_AREA_01_ENTRANCE, mod_id=0
        ),
        ApplySolidityModToLevel(
            permanent=True, room_id=R276_MOLEVILLE_MINES_AREA_01_ENTRANCE, mod_id=0
        ),
        SetBit(POST_MINES_LEVEL_MODS_COMPLETED),
        Store01To0248(),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        Return(),
    ]
)
