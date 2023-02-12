# E0382_MUSHROOM_KINGDOM_OCCUPIED_TOADSTOOLS_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_7,
            subscript=[ASSetWalkingSpeed(FASTEST), ASShiftSouthwestPixels(4)],
        ),
        ActionQueueAsync(
            target=NPC_6,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASShiftNorthPixels(2),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
            ],
        ),
        JmpIfBitSet(TEMP_7044_7, ["EVENT_382_jmp_if_bit_clear_79"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_4,
            R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
            ["EVENT_382_jmp_if_object_in_level_5"],
        ),
        FadeInFromBlack(sync=False),
        Return(),
        JmpIfObjectInSpecificLevel(
            NPC_1,
            R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM,
            ["EVENT_257_fade_in_from_black_async_0"],
            identifier="EVENT_382_jmp_if_object_in_level_5",
        ),
        JmpIfBitSet(
            OCCUPIED_MUSHROOM_KINGDOM_TOAD_RESCUED, ["EVENT_382_action_queue_async_84"]
        ),
        PauseActionScript(NPC_1),
        PauseActionScript(NPC_2),
        ActionQueueSync(target=NPC_2, subscript=[ASFaceSoutheast()]),
        ActionQueueSync(target=NPC_1, subscript=[ASFaceNorthwest()]),
        ActionQueueAsync(
            target=NPC_3, subscript=[ASTransferToXYZF(x=3, y=67, z=0, direction=EAST)]
        ),
        FadeInFromBlack(sync=True),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[ASSetWalkingSpeed(VERY_SLOW), ASWalk1StepNortheast()],
        ),
        PauseScriptUntilEffectDone(),
        ActionQueueAsync(target=NPC_3, subscript=[ASFaceNorthwest()]),
        ActionQueueAsync(target=MARIO, subscript=[ASFaceNorthwest()]),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASWalk1StepNortheast(),
                ASShiftSoutheastSteps(3),
                ASFaceSouthwest(),
            ],
        ),
        ActionQueueSync(target=NPC_3, subscript=[ASFaceNortheast()]),
        SetSyncActionScript(NPC_3, A0099_LOOPED_JUMPING),
        ActionQueueAsync(target=MARIO, subscript=[ASFaceEast()]),
        RememberLastObject(),
        PauseActionScript(NPC_3),
        ActionQueueSync(
            target=NPC_3, subscript=[ASJumpToHeight(height=0, silent=True)]
        ),
        ActionQueueAsync(
            target=NPC_2, subscript=[ASWalk1StepNorthwest(), ASFaceSouthwest()]
        ),
        ActionQueueAsync(target=MARIO, subscript=[ASFaceNortheast()]),
        Pause(1),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        Pause(1),
        ActionQueueSync(
            target=NPC_1, subscript=[ASSetWalkingSpeed(FAST), ASWalk1StepNorthwest()]
        ),
        ActionQueueSync(target=NPC_3, subscript=[ASPause(10), ASFaceSoutheast()]),
        ActionQueueAsync(target=MARIO, subscript=[ASPause(10), ASFaceEast()]),
        RememberLastObject(),
        SetSyncActionScript(NPC_3, A0099_LOOPED_JUMPING),
        Pause(10),
        PauseActionScript(NPC_3),
        SetVarToConst(TEMP_70A9, 23),
        RunEventAsSubroutine(E0278_UNKNOWN),
        ActionQueueSync(
            target=NPC_3,
            subscript=[ASSetAllSpeeds(FAST), ASWalk1StepSouthwest(), ASFaceNorthwest()],
        ),
        ActionQueueAsync(target=MARIO, subscript=[ASFaceSoutheast()]),
        RememberLastObject(),
        SetSyncActionScript(NPC_3, A0099_LOOPED_JUMPING),
        Pause(10),
        PauseActionScript(NPC_3),
        SetVarToConst(TEMP_70A9, 23),
        RunEventAsSubroutine(E0278_UNKNOWN),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASShiftNortheastSteps(7),
                ASShiftSoutheastSteps(3),
                ASShiftNorthwestSteps(3),
                ASShiftSouthwestSteps(7),
                ASFaceNorthwest(),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[ASPause(30), ASFaceNortheast(), ASPause(120), ASFaceNorthwest()],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[ASPause(30), ASFaceNortheast(), ASPause(120), ASFaceSouthwest()],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[ASPause(30), ASFaceNortheast(), ASPause(120), ASFaceSoutheast()],
        ),
        RememberLastObject(),
        RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
        ActionQueueAsync(target=MARIO, subscript=[ASPause(30), ASFaceSouth()]),
        SetBit(OCCUPIED_MUSHROOM_KINGDOM_TOAD_RESCUED),
        Return(),
        JmpIfBitClear(
            OCCUPIED_MUSHROOM_KINGDOM_TOAD_RESCUED,
            ["EVENT_382_run_event_as_subroutine_81"],
            identifier="EVENT_382_jmp_if_bit_clear_79",
        ),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASTransferToXYZF(x=4, y=63, z=0, direction=EAST),
                ASFaceSouthwest(),
            ],
        ),
        RunEventAsSubroutine(
            E0081_MARIO_LANDS_SUBROUTINE,
            identifier="EVENT_382_run_event_as_subroutine_81",
        ),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_382_ret_82"]),
        RunEventAsSubroutine(E3889_MUSHROOM_KINGDOM_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_382_ret_82"),
        JmpIfObjectInSpecificLevel(
            NPC_1,
            R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM,
            ["EVENT_257_fade_in_from_black_async_0"],
        ),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASTransferToXYZF(x=4, y=63, z=0, direction=EAST),
                ASFaceSouthwest(),
            ],
            identifier="EVENT_382_action_queue_async_84",
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
