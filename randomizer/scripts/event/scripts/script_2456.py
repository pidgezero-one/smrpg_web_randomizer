# E2456_AWAKEN_SLEEPING_WIGGLER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(DIRECTIONAL_7046_7, ["EVENT_2456_ret_23"]),
        JmpIfBitSet(UNKNOWN_7047_3, ["EVENT_2456_ret_23"]),
        ClearBit(DIRECTIONAL_7046_7),
        ClearBit(DIRECTIONAL_7046_5),
        ClearBit(DIRECTIONAL_7046_6),
        SetBit(UNKNOWN_7047_3),
        SetBit(DIRECTIONAL_7047_0),
        SetBit(UNKNOWN_7047_4),
        FreezeCamera(),
        RemoveObjectFromCurrentLevel(NPC_10),
        RemoveObjectFromSpecificLevel(
            NPC_10, R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS
        ),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASWalkToXYCoords(x=0, y=59),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        SetSyncActionScript(MARIO, A0485_PLAYER_SHOCKED_WHEN_WIGGLER_WAKES_UP),
        SetSyncActionScript(SCREEN_FOCUS, A0392_SLEEPING_WIGGLER_CAMERA),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASShiftSoutheastPixels(8),
                ASStartLoopNTimes(6),
                ASSetSpriteSequence(
                    index=24,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASShiftSouthPixels(5),
                ASPlaySound(sound=SO021_RUMBLING, channel=6),
                ASPause(8),
                ASSetSpriteSequence(
                    index=25,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASShiftNorthPixels(5),
                ASPlaySound(sound=SO021_RUMBLING, channel=6),
                ASPause(8),
                ASEndLoop(),
                ASSetSpriteSequence(
                    index=26,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPlaySound(sound=SO021_RUMBLING, channel=6),
                ASPause(8),
                ASSetSpriteSequence(
                    index=27,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASSetBit(TEMP_7043_0),
                ASPlaySound(sound=SO021_RUMBLING, channel=6),
                ASPause(8),
                ASSetSpriteSequence(
                    index=29,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPlaySound(sound=SO021_RUMBLING, channel=6),
                ASPause(3),
                ASShiftNorthwestPixels(6),
                ASSetSpriteSequence(
                    index=30,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPlaySound(sound=SO021_RUMBLING, channel=6),
                ASPause(3),
                ASSetSpriteSequence(
                    index=31,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPlaySound(sound=SO021_RUMBLING, channel=6),
            ],
        ),
        Pause(8),
        FadeOutToBlack(sync=False, duration=24),
        RemoveObjectFromSpecificLevel(
            NPC_1, R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS
        ),
        ApplySolidityModToLevel(
            permanent=True, room_id=R225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, mod_id=0
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA,
            mod_id=0,
        ),
        ApplySolidityModToLevel(
            permanent=True, room_id=R234_FOREST_MAZE_SECRET, mod_id=0
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS,
            mod_id=0,
        ),
        EnterArea(
            room_id=R225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA,
            face_direction=SOUTH,
            x=4,
            y=74,
            z=0,
            run_entrance_event=True,
        ),
        Return(identifier="EVENT_2456_ret_23"),
    ]
)
