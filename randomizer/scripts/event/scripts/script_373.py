# pylint: disable=C0301

"""E0373_MUSHROOM_KINGDOM_BOSS_FIGHT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(
            MUSHROOM_KINGDOM_LIBERATED, ["EVENT_375_play_music_default_volume_0"]
        ),
        Pause(1, identifier="EVENT_373_pause_1"),
        JmpIfMarioInAir(["EVENT_373_pause_1"]),
        JmpIfObjectInSpecificLevel(
            NPC_1,
            R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM,
            ["EVENT_373_start_battle_99"],
        ),
        Db(bytearray(b"\xc7\x80")),
        JmpIfVarNotEqualsConst(Z_COORD_2, 4, ["EVENT_256_ret_0"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASClearSolidityBits(cant_pass_walls=True),
                ASBounceToXYWithHeight(x=16, y=29, height=4),
                ASFaceNortheast(),
                ASSetSolidityBits(cant_pass_walls=True),
            ],
            identifier="EVENT_373_action_queue_sync_6",
        ),
        ActionQueueSync(target=SCREEN_FOCUS, subscript=[ASWalkToXYCoords(x=12, y=9)]),
        SetBit(TEMP_7043_5),
        Pause(30),
        ActionQueueAsync(target=NPC_4, subscript=[ASFaceSoutheast()]),
        Pause(10),
        ActionQueueAsync(target=NPC_5, subscript=[ASFaceSoutheast()]),
        Pause(10),
        ActionQueueAsync(target=NPC_6, subscript=[ASFaceNorthwest()]),
        Pause(10),
        ActionQueueAsync(target=NPC_7, subscript=[ASFaceNorthwest()]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceNortheast(),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ],
        ),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASPlaySound(sound=SO086_BIG_BOUNCE, channel=6),
                ASSetWalkingSpeed(SLOW),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\x00\n\xe0\xff")),
                ASWalk1StepSouthwest(),
                ASBPL262728(),
                ASTransferToXYZF(x=18, y=26, z=20, direction=EAST),
                ASPause(120),
                ASFloatingOn(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASWalkSouthwestPixels(3),
                ASSetWalkingSpeed(SLOW),
                ASWalkSouthwestPixels(13),
            ],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPause(30),
                ASSetSpriteSequence(
                    index=23,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASPause(150),
                ASSetSpriteSequence(
                    index=7,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASJumpToHeight(height=108, silent=True),
            ],
        ),
        PlaySound(sound=SO019_LONG_FALL, channel=6),
        Pause(180),
        SetBit(TEMP_7043_5),
        PauseActionScript(NPC_10),
        SetSyncActionScript(NPC_10, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
        SetSyncActionScript(NPC_4, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
        SetSyncActionScript(NPC_5, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
        SetSyncActionScript(NPC_6, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
        SetSyncActionScript(NPC_7, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
        JmpIfBitClear(UNUSED_7082_4, ["EVENT_373_action_queue_sync_32"]),
        SetSyncActionScript(NPC_8, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
        SetSyncActionScript(NPC_9, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
        Jmp(["EVENT_373_play_sound_34"]),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASFixedFCoordOn(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASSetWalkingSpeed(NORMAL),
                ASJumpToHeight(height=80, silent=True),
                ASFloatingOn(),
                ASWalkNorthwestPixels(8),
                ASSetWalkingSpeed(SLOW),
                ASWalkNorthwestPixels(8),
                ASFixedFCoordOff(),
            ],
            identifier="EVENT_373_action_queue_sync_32",
        ),
        ActionQueueSync(
            target=NPC_9,
            subscript=[
                ASFixedFCoordOn(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASSetWalkingSpeed(NORMAL),
                ASJumpToHeight(height=80, silent=True),
                ASFloatingOn(),
                ASWalkSoutheastPixels(8),
                ASSetWalkingSpeed(SLOW),
                ASWalkSoutheastPixels(8),
                ASFixedFCoordOff(),
            ],
        ),
        PlaySound(
            sound=SO021_RUMBLING, channel=6, identifier="EVENT_373_play_sound_34"
        ),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkSouthPixels(8),
                ASWalk1StepNorth(),
                ASWalkSouthPixels(12),
                ASWalkNorthPixels(8),
                ASWalkSouthPixels(6),
                ASWalkNorthPixels(4),
                ASStopSound(),
                ASWalkSouthPixels(3),
                ASWalkNorthPixels(1),
            ],
        ),
        Pause(60),
        ClearBit(TEMP_7043_5),
        SetSyncActionScript(NPC_10, A0113_HENCHMAN_BOUNCING_IN_PLACE),
        ActionQueueAsync(target=MARIO, subscript=[ASResetProperties()]),
        SetAsyncActionScript(NPC_3, A0636_54_VELOCITY_SINGLE_JUMP),
        PlaySound(sound=SO022_CLOSE_DOOR, channel=6),
        Pause(20),
        SetBit(TEMP_7043_5),
        ActionQueueSync(target=NPC_4, subscript=[ASPause(40), ASFaceNortheast()]),
        ActionQueueSync(target=NPC_5, subscript=[ASPause(40), ASFaceNortheast()]),
        ActionQueueSync(
            target=NPC_8, subscript=[ASPause(40), ASFixedFCoordOff(), ASFaceNortheast()]
        ),
        ActionQueueSync(
            target=NPC_9, subscript=[ASPause(40), ASFixedFCoordOff(), ASFaceNortheast()]
        ),
        ActionQueueSync(target=NPC_6, subscript=[ASPause(40), ASFaceNortheast()]),
        ActionQueueAsync(target=NPC_7, subscript=[ASPause(40), ASFaceNortheast()]),
        ClearBit(TEMP_7043_5),
        ActionQueueSync(target=NPC_4, subscript=[ASPause(80), ASFaceSoutheast()]),
        ActionQueueSync(target=NPC_5, subscript=[ASPause(80), ASFaceSoutheast()]),
        ActionQueueSync(
            target=NPC_8, subscript=[ASPause(80), ASFixedFCoordOff(), ASFaceSoutheast()]
        ),
        ActionQueueSync(
            target=NPC_9, subscript=[ASPause(80), ASFixedFCoordOff(), ASFaceNorthwest()]
        ),
        ActionQueueSync(target=NPC_6, subscript=[ASPause(80), ASFaceNorthwest()]),
        ActionQueueAsync(target=NPC_7, subscript=[ASPause(80), ASFaceNorthwest()]),
        Pause(10),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASFaceSoutheast(),
                ASPause(30),
                ASSetWalkingSpeed(NORMAL),
                ASSetSolidityBits(cant_pass_walls=True),
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
                ASJumpToHeight(height=72, silent=True),
                ASWalk1StepSoutheast(),
            ],
        ),
        SetVarToConst(TEMP_70A9, 24),
        RunEventAsSubroutine(E0278_UNKNOWN),
        ActionQueueAsync(target=MARIO, subscript=[ASFaceNorthwest()]),
        Pause(20),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASFaceSoutheast(),
                ASSetWalkingSpeed(NORMAL),
                ASSetSolidityBits(cant_pass_walls=True),
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
                ASJumpToHeight(height=80, silent=True),
                ASWalk1StepSoutheast(),
                ASWalkSoutheastPixels(4),
            ],
        ),
        SetVarToConst(TEMP_70A9, 25),
        RunEventAsSubroutine(E0278_UNKNOWN),
        ActionQueueAsync(
            target=NPC_5, subscript=[ASFixedFCoordOff(), ASFaceNortheast()]
        ),
        ActionQueueAsync(target=MARIO, subscript=[ASFaceSouthwest()]),
        Pause(20),
        ActionQueueAsync(
            target=NPC_6,
            subscript=[
                ASFaceNorthwest(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASSetWalkingSpeed(NORMAL),
                ASJumpToHeight(height=80, silent=True),
                ASWalk1StepNorthwest(),
                ASWalkNorthwestPixels(4),
            ],
        ),
        SetVarToConst(TEMP_70A9, 26),
        RunEventAsSubroutine(E0278_UNKNOWN),
        ActionQueueAsync(
            target=NPC_6, subscript=[ASFixedFCoordOff(), ASFaceNortheast()]
        ),
        ActionQueueAsync(target=MARIO, subscript=[ASPause(10), ASFaceSouth()]),
        Pause(20),
        RememberLastObject(),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASSetSolidityBits(cant_pass_walls=True),
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
                ASJumpToHeight(height=72, silent=True),
                ASWalk1StepNorthwest(),
            ],
        ),
        SetVarToConst(TEMP_70A9, 26),
        RunEventAsSubroutine(E0278_UNKNOWN),
        ActionQueueSync(target=MARIO, subscript=[ASPause(10), ASFaceSoutheast()]),
        Pause(20),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPause(10),
                ASFaceNortheast(),
                ASPause(10),
                ASSetSpriteSequence(
                    index=2,
                    sprite_offset=3,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
            ],
        ),
        PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
        Xor3105With01(),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASPause(20),
                ASSetSolidityBits(cant_pass_walls=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFloatingOff(),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\x00\x08\x84\xff")),
                ASSetWalkingSpeed(SLOW),
                ASWalk1StepSoutheast(),
                ASBPL262728(),
            ],
        ),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASPause(20),
                ASSetSolidityBits(cant_pass_walls=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFloatingOff(),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\x00\x08\x84\xff")),
                ASSetWalkingSpeed(SLOW),
                ASWalk1StepNortheast(),
                ASBPL262728(),
            ],
        ),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASPause(20),
                ASSetSolidityBits(cant_pass_walls=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFloatingOff(),
                ASSetPriority(3),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\x00\x08\x84\xff")),
                ASSetWalkingSpeed(SLOW),
                ASWalk1StepNortheast(),
                ASBPL262728(),
            ],
        ),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASPause(20),
                ASSetSolidityBits(cant_pass_walls=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFloatingOff(),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\x00\x08\x84\xff")),
                ASSetWalkingSpeed(SLOW),
                ASWalk1StepNorthwest(),
                ASBPL262728(),
            ],
        ),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASSetSolidityBits(cant_pass_walls=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFloatingOff(),
                ASPause(20),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%@\x08\x84\xff")),
                ASSetWalkingSpeed(SLOW),
                ASWalkSouthwestPixels(8),
                ASSetWalkingSpeed(NORMAL),
                ASWalk1StepSouthwest(),
                ASBPL262728(),
            ],
        ),
        PlaySound(sound=SO000_SILENCE, channel=6),
        RememberLastObject(),
        FadeOutMusicToVolume(duration=0, volume=1),
        RunEventAsSubroutine(
            E0354_BOSS_BATTLE_CONTAINER, identifier="EVENT_373_start_battle_99"
        ),
        ReturnFD(),
        RestoreAllHP(),
        RestoreAllFP(),
        RemoveObjectFromCurrentLevel(NPC_3),
        RemoveObjectFromCurrentLevel(NPC_4),
        RemoveObjectFromCurrentLevel(NPC_5),
        RemoveObjectFromCurrentLevel(NPC_6),
        RemoveObjectFromCurrentLevel(NPC_7),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromCurrentLevel(NPC_2),
        RemoveObjectFromSpecificLevel(
            NPC_8, R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM
        ),
        RemoveObjectFromSpecificLevel(
            NPC_9, R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM
        ),
        RemoveObjectFromCurrentLevel(NPC_8),
        RemoveObjectFromCurrentLevel(NPC_9),
        Pause(30),
        SetBit(TEMP_7049_2),
        RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        JmpToEvent(E0375_TALK_TO_CHANCELLOR_AFTER_MUSHROOM_KINGDOM_BOSS),
        Return(),
    ]
)
