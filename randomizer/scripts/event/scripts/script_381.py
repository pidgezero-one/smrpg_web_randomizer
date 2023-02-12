# E0381_MUSHROOM_KINGDOM_OCCUPIED_TOADSTOOLS_ROOM_ANTECHAMBER_FIGHT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7044_6, ["EVENT_256_ret_0"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_0,
            R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM,
            ["EVENT_256_ret_0"],
        ),
        SetBit(TEMP_7044_6),
        SetBit(TEMP_7043_5),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASWalkToXYCoords(x=12, y=95),
                ASShiftSoutheastPixels(8),
                ASFaceNorthwest(),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ],
        ),
        ActionQueueSync(target=NPC_0, subscript=[ASFaceSoutheast()]),
        ActionQueueSync(target=NPC_1, subscript=[ASFaceNorthwest()]),
        RememberLastObject(),
        Pause(30),
        ClearBit(TEMP_7043_5),
        SetSyncActionScript(NPC_0, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
        RememberLastObject(),
        SetBit(TEMP_7043_5),
        Pause(30),
        ClearBit(TEMP_7043_5),
        SetSyncActionScript(NPC_1, A0103_MK_THRONE_HENCHMAN_BOUNCE_BOSS_FIGHT_START),
        ActionQueueAsync(target=MARIO, subscript=[ASPause(30), ASFaceSoutheast()]),
        SetBit(TEMP_7043_5),
        Pause(30),
        RememberLastObject(),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASClearSolidityBits(bit_4=True),
                ASSetSolidityBits(cant_pass_walls=True),
                ASSetWalkingSpeed(NORMAL),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\xc0\x06`\xff")),
                ASShiftSoutheastPixels(11),
                ASSetWalkingSpeed(SLOW),
                ASShiftSoutheastPixels(4),
                ASBPL262728(),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASClearSolidityBits(bit_4=True),
                ASSetSolidityBits(cant_pass_walls=True),
                ASSetWalkingSpeed(NORMAL),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\xc0\x06`\xff")),
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
                ASShiftNorthwestPixels(11),
                ASSetWalkingSpeed(SLOW),
                ASShiftNorthwestPixels(4),
                ASBPL262728(),
            ],
        ),
        RememberLastObject(),
        RunEventAsSubroutine(E1186_HENCHMAN_BATTLE_PACK_SELECTOR),
        SetBit(TEMP_704A_2),
        RunEventAsSubroutine(E1011_POST_MINES_BOSS_CHECK_IF_WON),
        RemoveObjectFromSpecificLevel(
            NPC_0, R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM
        ),
        RemoveObjectFromSpecificLevel(
            NPC_1, R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM
        ),
        RemoveObjectFromCurrentLevel(NPC_0),
        RemoveObjectFromCurrentLevel(NPC_1),
        JmpIfObjectNotInSpecificLevel(
            NPC_1,
            R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM,
            ["EVENT_381_jmp_if_object_in_level_45"],
        ),
        FadeInFromBlack(sync=False),
        Return(),
        JmpIfObjectInSpecificLevel(
            NPC_4,
            R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
            ["EVENT_257_fade_in_from_black_async_0"],
            identifier="EVENT_381_jmp_if_object_in_level_45",
        ),
        ActionQueueSync(target=MARIO, subscript=[ASFaceSouth()]),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASShiftNortheastPixels(8),
                ASFaceNorthwest(),
            ],
        ),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[ASSetWalkingSpeed(NORMAL), ASShiftNortheastPixels(8)],
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM,
            mod_id=0,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM,
            mod_id=0,
        ),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASWalk1StepNortheast(),
                ASVisibilityOff(),
                ASDb(bytearray(b"\xfd\xf2")),
            ],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[ASPause(10), ASFaceEast(), ASPause(30), ASFaceSouth()],
        ),
        RememberLastObject(),
        Return(),
    ]
)
