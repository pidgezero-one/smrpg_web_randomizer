# E1335_PORTRAIT_GAME_4

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
                ShiftToXYCoords(x=18, y=25),
                ShiftNorthwestPixels(5),
                VisibilityOn(),
                FaceSoutheast(),
                SetPriority(0),
                SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
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
                FaceNortheast(),
                FixedFCoordOn(),
                SetAllSpeeds(FAST),
                WalkToXYCoords(x=17, y=27),
                FixedFCoordOff(),
            ],
        ),
        Pause(30),
        ActionQueueAsync(
            target=NPC_6,
            subscript=[
                FaceSouthwest(),
                Pause(30),
                SetSequenceSpeed(SLOW),
                SetSpriteSequence(index=6, is_mold=True, looping=True),
            ],
        ),
        Pause(10),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                VisibilityOn(),
                PlaySound(sound=SO078_CLICK, channel=6),
                SetWalkingSpeed(NORMAL),
                JumpToHeight(21),
                FloatingOn(),
                ShiftSouthwestSteps(1),
            ],
        ),
        ActionQueueAsync(target=NPC_6, subscript=[ResetProperties()]),
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
                SetAllSpeeds(NORMAL),
                ShiftNortheastPixels(8),
                Pause(15),
                SetSpriteSequence(
                    index=10, sprite_offset=2, is_sequence=True, looping=False
                ),
                Pause(45),
            ],
        ),
        ActionQueueAsync(target=NPC_7, subscript=[Pause(8), VisibilityOff()]),
        RunEventAsSubroutine(E0241_FREESTANDING_1_GRANT),
        ActionQueueAsync(target=MARIO, subscript=[ResetProperties()]),
        SetBit(PORTRAIT_GAME_COMPLETED),
        Return(identifier="EVENT_1335_ret_54"),
    ]
)
