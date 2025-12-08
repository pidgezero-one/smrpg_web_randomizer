# pylint: disable=C0301

"""E1364_CURTAIN_ROOM_EXIT_TO_BALCONY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(CURTAIN_MINIGAME_COMPLETED, ["EVENT_1364_check_fast_travel"]),
        JmpIfBitSet(TOWER_BOSS_1_DEFEATED, ["EVENT_1364_check_fast_travel"]),
        SetVarToConst(TEMP_7026, 0),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=2),
        FreezeCamera(),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=3),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASBounceToXYWithHeight(x=0, y=3, height=0),
            ]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASShiftToXYCoords(x=3, y=26),
                ASSetWalkingSpeed(FASTEST),
                ASWalkNorthwestPixels(8),
                ASSetSpriteSequence(
                    index=3, sprite_offset=3, is_sequence=True, looping=True
                ),
            ]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASResetProperties(),
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASPause(15),
                ASFaceNortheast(),
                ASPause(15),
                ASWalkNortheastSteps(3),
                ASWalkNortheastPixels(8),
                ASPause(7),
                ASSetSpriteSequence(
                    index=10, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(7),
                ASSetSpriteSequence(
                    index=11, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(15),
                ASSetSpriteSequence(index=9, is_mold=True, looping=True),
                ASPause(7),
                ASSetSpriteSequence(index=8, is_mold=True, looping=True),
                ASPause(30),
                ASResetProperties(),
                ASFaceNorthwest(),
                ASPause(20),
                ASSetPriority(3),
                ASClearSolidityBits(cant_pass_walls=True),
                ASWalkNorthwestSteps(3),
                ASWalkNorthwestPixels(7),
            ]),
        Pause(20),
        PlaySound(sound=SO090_CURTAIN, channel=6),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=37),
        Pause(2),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=38),
        Pause(2),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=39),
        Pause(2),
        Pause(15),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASWalkNorthwestPixels(20),
                ASSetPriority(2),
                ASPause(15),
                ASFaceSoutheast(),
                ASPause(10),
                ASSetSolidityBits(cant_pass_walls=True),
                ASSetAllSpeeds(NORMAL),
            ]),
        PlaySound(sound=SO090_CURTAIN, channel=6),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=38),
        Pause(2),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=37),
        Pause(2),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            mod_id=36),
        Pause(2),
        JmpToEvent(E1358_CURTAIN_GAME_BEGINS_NPCS_WALK_INTO_ROOM),
        JmpIfBitSet(
            TOWER_BOSS_2_DEFEATED,
            ["EVENT_1364_check_if_should_be_locked"],
            identifier="EVENT_1364_check_fast_travel"),
        EnterArea(
            room_id=R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
            face_direction=NORTHEAST,
            x=4,
            y=19,
            z=0,
            run_entrance_event=True,
            identifier="EVENT_1364_enter_area_0"),
        Return(),
        JmpIfBitSet(
            FAST_TRAVEL_ENABLED,
            ["EVENT_1364_enter_area_0"],
            identifier="EVENT_1364_check_if_should_be_locked"),
        Return(),
    ]
)
