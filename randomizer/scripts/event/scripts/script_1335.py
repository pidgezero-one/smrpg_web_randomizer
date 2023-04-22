# pylint: disable=C0301

"""E1335_PORTRAIT_GAME_4"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_5, ["EVENT_1335_ret_54"]),
        JmpIfVarEqualsConst(
            SECONDARY_TEMP_7024, 5, ["EVENT_1335_remove_from_current_level_10"]
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=47,
        ),
        Pause(5),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=49,
        ),
        PlaySound(sound=SO088_WRONG_SIGNAL, channel=6),
        Pause(30),
        StartBattleAtBattlefield(46, BF12_BOOSTER_TOWER),
        FadeInFromBlack(sync=False),
        Jmp(["EVENT_1338_pause_0"]),
        RemoveObjectFromCurrentLevel(
            NPC_3, identifier="EVENT_1335_remove_from_current_level_10"
        ),
        ActionQueueAsync(
            target=NPC_6,
            subscript=[
                ASShiftToXYCoords(x=18, y=25),
                ASWalkNorthwestPixels(5),
                ASVisibilityOn(),
                ASFaceSoutheast(),
                ASSetPriority(0),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
            ],
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=47,
        ),
        Pause(5),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=49,
        ),
        Pause(10),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceNortheast(),
                ASFixedFCoordOn(),
                ASSetAllSpeeds(FAST),
                ASWalkToXYCoords(x=17, y=27),
                ASFixedFCoordOff(),
            ],
        ),
        Pause(30),
        ActionQueueAsync(
            target=NPC_6,
            subscript=[
                ASFaceSouthwest(),
                ASPause(30),
                ASSetSequenceSpeed(SLOW),
                ASSetSpriteSequence(index=6, is_mold=True, looping=True),
            ],
        ),
        Pause(10),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASVisibilityOn(),
                ASPlaySound(sound=SO078_CLICK, channel=6),
                ASSetWalkingSpeed(NORMAL),
                ASJumpToHeight(21),
                ASFloatingOn(),
                ASWalkSouthwestSteps(1),
            ],
        ),
        ActionQueueAsync(target=NPC_6, subscript=[ASResetProperties()]),
        Pause(30),
        PlaySound(sound=SO106_OFF_BALANCE, channel=6),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=47,
        ),
        Pause(5),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=48,
        ),
        Pause(5),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=47,
        ),
        Pause(5),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=48,
        ),
        Pause(5),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=47,
        ),
        Pause(5),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=48,
        ),
        Pause(5),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=47,
        ),
        Pause(5),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=48,
        ),
        Pause(5),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=47,
        ),
        Pause(5),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=48,
        ),
        Pause(30),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetAllSpeeds(NORMAL),
                ASWalkNortheastPixels(8),
                ASPause(15),
                ASSetSpriteSequence(
                    index=10, sprite_offset=2, is_sequence=True, looping=False
                ),
                ASPause(45),
            ],
        ),
        ActionQueueAsync(target=NPC_7, subscript=[ASPause(8), ASVisibilityOff()]),
        RunEventAsSubroutine(E0241_FREESTANDING_1_GRANT),
        ActionQueueAsync(target=MARIO, subscript=[ASResetProperties()]),
        SetBit(PORTRAIT_GAME_COMPLETED),
        Return(identifier="EVENT_1335_ret_54"),
    ]
)
