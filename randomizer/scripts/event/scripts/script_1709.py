# pylint: disable=C0301

"""E1709_BANDITS_WAY_5_LOADER_BACKGROUND_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(TEMP_7030, 100),
        SetVarToConst(TEMP_7032, 0),
        StartLoopNTimes(239, identifier="EVENT_1709_start_loop_n_times_2"),
        Pause(1),
        JmpIfBitSet(TEMP_7044_4, ["EVENT_1709_jmp_to_subroutine_17"]),
        JmpIfBitSet(TEMP_7044_5, ["EVENT_1709_jmp_to_subroutine_22"]),
        EndLoop(),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASPlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASJumpToHeight(108),
                ASPause(27),
            ]),
        JmpToSubroutine(["EVENT_1709_enable_controls_until_return_43"]),
        StopEmbeddedActionScript(NPC_5),
        StopEmbeddedActionScript(NPC_6),
        StopEmbeddedActionScript(NPC_7),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        ClearBit(TEMP_7044_4, identifier="EVENT_1709_clear_bit_13"),
        ClearBit(TEMP_7044_5),
        RunEventAsSubroutine(E1707_BANDITS_WAY_5_LOADER_BACKGROUND),
        Jmp(["EVENT_1709_start_loop_n_times_2"]),
        JmpToSubroutine(
            ["EVENT_1709_enable_controls_until_return_43"],
            identifier="EVENT_1709_jmp_to_subroutine_17"),
        JmpToSubroutine(["EVENT_1709_action_queue_async_52"]),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        PlaySound(sound=SO011_WHOOSH_AWAY, channel=6),
        Jmp(["EVENT_1709_clear_bit_13"]),
        JmpToSubroutine(
            ["EVENT_1709_enable_controls_until_return_43"],
            identifier="EVENT_1709_jmp_to_subroutine_22"),
        Inc(TEMP_7032),
        JmpIfVarEqualsConst(TEMP_7032, 3, ["EVENT_1709_run_event_at_return_33"]),
        JmpToSubroutine(["EVENT_1709_action_queue_async_55"]),
        CopyVarToVar(from_var=TEMP_7030, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=TEMP_7030, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 65486),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7030),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        PlaySound(sound=SO011_WHOOSH_AWAY, channel=6),
        Jmp(["EVENT_1709_clear_bit_13"]),
        RunEventAtReturn(
            E1710_BANDITS_WAY_5_LOADER_BACKGROUND_BOSS_FIGHT,
            identifier="EVENT_1709_run_event_at_return_33"),
        Return(),
        EnableControlsUntilReturn(
            [], identifier="EVENT_1709_enable_controls_until_return_43"
        ),
        SetVarToConst(TEMP_70AB, 25),
        StartLoopNTimes(2),
        PauseActionScript(MEM_70AB),
        JmpIfObjectInCurrentLevel(MEM_70AB, ["EVENT_1709_inc_49"]),
        StartSyncEmbeddedActionScript(
            target=MEM_70AB,
            prefix=0xF1,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetAllSpeeds(FASTER),
                ASWalkSouthwestSteps(3),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASVisibilityOff(),
            ]),
        Inc(TEMP_70AB, identifier="EVENT_1709_inc_49"),
        EndLoop(),
        Return(),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASJumpToHeight(108),
                ASPause(27),
                ASFaceMario(),
            ],
            identifier="EVENT_1709_action_queue_async_52"),
        ActionQueueAsync(target=MARIO, subscript=[ASFaceSouthwest7D()]),
        Return(),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASSetAllSpeeds(VERY_FAST),
                ASPlaySound(sound=SO030_SURPRISED_MONSTER, channel=4),
                ASStartLoopNTimes(3),
                ASShiftZUpPixels(8),
                ASShiftZDownPixels(8),
                ASEndLoop(),
                ASPause(10),
                ASStopSound(),
                ASFaceMario(),
                ASPause(10),
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASJumpToHeight(108),
                ASPause(27),
                ASSetWalkingSpeed(VERY_FAST),
                ASSetSequenceSpeed(NORMAL),
                ASFixedFCoordOn(),
                ASWalk1StepSouth(),
            ],
            identifier="EVENT_1709_action_queue_async_55"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASClearSolidityBits(cant_pass_walls=True),
                ASDb(bytearray(b"\xc8\x1c")),
                ASAddConstToVar(X_COORD_2, 256),
                ASAddConstToVar(Y_COORD_2, 128),
                ASDb(bytearray(b"\xfd\xc7")),
                ASDb(bytearray(b"\x98")),
                ASFaceNorthwest(),
                ASSetWalkingSpeed(NORMAL),
                ASSetSolidityBits(cant_pass_walls=True),
            ]),
        ActionQueueAsync(
            target=NPC_8, subscript=[ASFixedFCoordOff(), ASFaceSoutheast()]
        ),
        Return(),
    ]
)
