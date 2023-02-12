# E1685_TEMPLE_FORTUNE_HEAD_1

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(BELOME_FORTUNE_1, ["EVENT_1685_ret_45"]),
        Set7000ToTappedButton(),
        JmpIf7000AllBitsClear(destinations=["EVENT_1685_ret_45"]),
        ActionQueueSync(target=MARIO, subscript=[ASJumpToHeight(64)]),
        JmpIfBitSet(BELOME_HEAD_1, ["EVENT_1685_ret_45"]),
        Pause(1, identifier="EVENT_1685_pause_5"),
        JmpIfMarioInAir(["EVENT_1685_pause_5"]),
        PlaySound(sound=SO154_BIG_SQUISH, channel=6),
        Pause(2),
        Store02To0248(),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM,
            mod_id=32,
        ),
        Store00To0248(),
        Pause(1),
        SetBit(BELOME_HEAD_1),
        JmpIfVarNotEqualsConst(
            SECONDARY_TEMP_7024, 0, ["EVENT_1685_jmp_if_var_not_equals_const_20"]
        ),
        SetVarToConst(SECONDARY_TEMP_7024, 1),
        CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 16),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AC),
        Jmp(["EVENT_1685_set_7000_to_7000_short_mem_39"]),
        JmpIfVarNotEqualsConst(
            TEMP_7026,
            0,
            ["EVENT_1685_set_7000_to_70A0_short_mem_26"],
            identifier="EVENT_1685_jmp_if_var_not_equals_const_20",
        ),
        SetVarToConst(TEMP_7026, 4),
        CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 16),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AC),
        Jmp(["EVENT_1685_set_7000_to_7000_short_mem_39"]),
        CopyVarToVar(
            from_var=TEMP_70AC,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_1685_set_7000_to_70A0_short_mem_26",
        ),
        AddConstToVar(PRIMARY_TEMP_7000, 16),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AC),
        SetVarToConst(TEMP_70AB, 24, identifier="EVENT_1685_set_29"),
        RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASFixedFCoordOff(),
                ASFaceSouthwest(),
                ASVisibilityOn(),
                ASFixedFCoordOn(),
                ASShiftSouthPixels(4),
                ASFloatingOn(),
                ASJumpToHeight(0),
                ASPause(
                    1, identifier="EVENT_1685_action_queue_sync_31_SUBSCRIPT_pause_8"
                ),
                ASJmpIfObjectInAir(
                    NPC_0, ["EVENT_1685_action_queue_sync_31_SUBSCRIPT_pause_8"]
                ),
                ASPlaySound(sound=SO109_BIG_SHELL_HIT, channel=4),
                ASShiftNorthPixels(8),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASFixedFCoordOff(),
                ASFaceSouthwest(),
                ASVisibilityOn(),
                ASFixedFCoordOn(),
                ASShiftSouthPixels(4),
                ASFloatingOn(),
                ASJumpToHeight(0),
                ASPause(
                    1, identifier="EVENT_1685_action_queue_sync_32_SUBSCRIPT_pause_8"
                ),
                ASJmpIfObjectInAir(
                    NPC_1, ["EVENT_1685_action_queue_sync_32_SUBSCRIPT_pause_8"]
                ),
                ASPlaySound(sound=SO109_BIG_SHELL_HIT, channel=4),
                ASShiftNorthPixels(8),
            ],
        ),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASIncPaletteRowBy(1),
                ASVisibilityOn(),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASFloatingOn(),
                ASJumpToHeight(0),
            ],
        ),
        SetVarToConst(TEMP_70AB, 0),
        RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
        SetBit(UNKNOWN_BELOME_TEMPLE),
        SetBit(UNKNOWN_BELOME_FORTUNE),
        ClearBit(HAS_A_PRIZE_FORTUNE),
        CopyVarToVar(
            from_var=SECONDARY_TEMP_7024,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_1685_set_7000_to_7000_short_mem_39",
        ),
        AddVarTo7000(TEMP_7026),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7028),
        CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
        Mem7000OrVar(TEMP_7028),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AC),
        Return(identifier="EVENT_1685_ret_45"),
    ]
)
