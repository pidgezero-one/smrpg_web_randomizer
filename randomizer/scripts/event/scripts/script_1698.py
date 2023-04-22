# pylint: disable=C0301

"""E1698_BANDITS_WAY_4_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(target=NPC_8, subscript=[ASShadowOff()]),
        ActionQueueSync(target=NPC_9, subscript=[ASShadowOff()]),
        ActionQueueAsync(
            target=MARIO, subscript=[ASObjectMemorySetBit(arg_1=0x0B, bits=[3])]
        ),
        SetVarToConst(TEMP_70AB, 22),
        StartLoopNTimes(3),
        SummonObjectToSpecificLevel(MEM_70AB, R078_BANDITS_WAY_AREA_04),
        SetSyncActionScript(MEM_70AB, A0474_BANDITS_WAY_2_CHEST_ROOM_CHEST),
        Pause(1),
        PauseActionScript(MEM_70AB),
        Inc(TEMP_70AB),
        EndLoop(),
        ActionQueueSync(target=NPC_6, subscript=[ASShiftZDownPixels(2)]),
        ActionQueueAsync(target=NPC_7, subscript=[ASShiftZDownPixels(2)]),
        SetVarToConst(TEMP_702C, 26),
        SetVarToConst(TEMP_70A9, 26),
        SetVarToConst(TEMP_70AA, 27),
        ActionQueueAsync(
            target=MEM_70A9,
            subscript=[
                ASBPL262728(),
                ASDb(bytearray(b"\xfd$\x11\x12")),
                ASCopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_702A),
            ],
        ),
        PauseActionScript(NPC_9),
        SetSyncActionScript(MEM_70AA, A0479_BANDITS_WAY_CHEST_PLATFORMS_ON_MOUNT),
        Pause(2),
        SetSyncActionScript(NPC_9, A0653_SLOW_ROTATING_PLATFORM),
        RunBackgroundEvent(
            event_id=E1699_BANDITS_WAY_4_LOADER_BACKGROUND, return_on_level_exit=True
        ),
        JmpIfBitClear(
            BANDITS_WAY_CUTSCENE_4_VIEWED, ["EVENT_1698_action_queue_async_31"]
        ),
        ResumeActionScript(NPC_2),
        ResumeActionScript(NPC_3),
        ResumeActionScript(NPC_4),
        ResumeActionScript(NPC_5),
        RunEventAsSubroutine(E0759_BANDITS_WAY_AREA_04_SHUFFLED_NPC_ANIMATION_LOADER),
        RunEventAsSubroutine(E0014_STANDARD_ROOM_LOADER),
        Pause(3),
        PauseActionScript(NPC_7),
        Return(),
        ActionQueueAsync(
            target=NPC_6,
            subscript=[ASSetSolidityBits(cant_pass_npcs=True, bit_7=True)],
            identifier="EVENT_1698_action_queue_async_31",
        ),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASWalkNortheastSteps(5),
                ASShiftNorthSteps(4),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[ASWalkNortheastSteps(2), ASWalk1StepNorth(), ASFaceNortheast()],
        ),
        SetBit(BANDITS_WAY_CUTSCENE_4_VIEWED),
        RunEventAsSubroutine(E0759_BANDITS_WAY_AREA_04_SHUFFLED_NPC_ANIMATION_LOADER),
        RunEventAsSubroutine(E0014_STANDARD_ROOM_LOADER),
        PauseActionScript(NPC_6),
        ActionQueueSync(
            target=NPC_12,
            subscript=[
                ASShadowOff(),
                ASVisibilityOn(),
                ASSequenceLoopingOn(),
                ASWalkNortheastPixels(1),
                ASFixedFCoordOn(),
                ASWalkSouthPixels(8),
                ASFixedFCoordOff(),
                ASFaceNortheast(),
            ],
        ),
        Pause(80),
        StartLoopNTimes(1),
        PauseActionScript(NPC_7),
        ActionQueueAsync(
            target=NPC_12,
            subscript=[
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASJumpToHeight(108),
                ASPause(27),
            ],
        ),
        ResumeActionScript(NPC_7),
        Pause(80),
        EndLoop(),
        PauseActionScript(NPC_7),
        ActionQueueAsync(
            target=NPC_12,
            subscript=[
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASJumpToHeight(108),
                ASFixedFCoordOn(),
                ASSetAllSpeeds(FAST),
                ASWalkEastPixels(4),
                ASShadowOn(),
                ASWalkEastPixels(
                    2,
                    identifier="EVENT_1698_action_queue_async_46_SUBSCRIPT_shift_east_pixels_6",
                ),
                ASJmpIfObjectInAir(
                    NPC_12,
                    ["EVENT_1698_action_queue_async_46_SUBSCRIPT_shift_east_pixels_6"],
                ),
                ASFixedFCoordOff(),
            ],
        ),
        Jmp(["EVENT_1698_action_queue_async_49"]),
        ActionQueueAsync(
            target=NPC_12,
            subscript=[
                ASPause(20),
                ASFaceSoutheast(),
                ASPause(8),
                ASFaceSouthwest(),
                ASPause(20),
                ASWalkSouthwestSteps(3),
                ASSetSequenceSpeed(NORMAL),
            ],
        ),
        ActionQueueAsync(
            target=NPC_12,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASFaceSoutheast(),
                ASPause(30),
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASJumpToHeight(112),
                ASFixedFCoordOn(),
                ASWalkEastSteps(4),
                ASVisibilityOff(),
            ],
            identifier="EVENT_1698_action_queue_async_49",
        ),
        ActionQueueSync(
            target=NPC_6,
            subscript=[ASClearSolidityBits(cant_pass_npcs=True, bit_7=True)],
        ),
        ResumeActionScript(NPC_2),
        ResumeActionScript(NPC_3),
        ResumeActionScript(NPC_4),
        ResumeActionScript(NPC_5),
        Return(),
    ]
)
