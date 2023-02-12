# E1694_TEMPLE_ELEVATOR

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMPLE_ELEVATOR_DIRECTION, ["EVENT_1694_set_7016_to_object_xyz_3"]),
        JmpIfBitSet(TEMP_7044_0, ["EVENT_1694_set_7016_to_object_xyz_3"]),
        Return(),
        Set7016701BToObjectXYZ(
            MEM_70A8, identifier="EVENT_1694_set_7016_to_object_xyz_3"
        ),
        AddConstToVar(X_COORD_2, 48),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(height=48, silent=True),
                ASPause(3),
                ASTransferTo70167018(),
                ASClearSolidityBits(cant_pass_walls=True),
                ASShadowOff(),
                ASSetWalkingSpeed(NORMAL),
                ASFaceSouth(),
                ASSetPriority(2),
            ],
        ),
        JmpToSubroutine(["EVENT_1694_play_sound_18"]),
        JmpIfBitSet(TEMPLE_ELEVATOR_DIRECTION, ["EVENT_1694_action_queue_async_13"]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASFixedFCoordOff(),
                ASFaceSoutheast(),
                ASFixedFCoordOn(),
                ASShiftSouthSteps(16),
            ],
        ),
        JmpToSubroutine(["EVENT_1694_stop_sound_24"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASObjectMemoryModifyBits(arg_1=0x09, set_flags=[5], clear_bits=[4, 6]),
                ASFixedFCoordOff(),
                ASSetWalkingSpeed(FAST),
                ASSetSolidityBits(cant_pass_walls=True),
                ASShadowOn(),
                ASWalk1StepSoutheast(),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        SetBit(TEMPLE_ELEVATOR_DIRECTION),
        Return(),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASFixedFCoordOff(),
                ASFaceSoutheast(),
                ASFixedFCoordOn(),
                ASShiftNorthSteps(16),
            ],
            identifier="EVENT_1694_action_queue_async_13",
        ),
        JmpToSubroutine(["EVENT_1694_stop_sound_24"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASObjectMemoryModifyBits(arg_1=0x09, set_flags=[5], clear_bits=[4, 6]),
                ASFixedFCoordOff(),
                ASSetWalkingSpeed(FAST),
                ASSetSolidityBits(cant_pass_walls=True),
                ASShadowOn(),
                ASWalk1StepNorthwest(),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        ClearBit(TEMPLE_ELEVATOR_DIRECTION),
        Return(),
        PlaySound(
            sound=SO009_GREEN_SWITCH, channel=6, identifier="EVENT_1694_play_sound_18"
        ),
        ActionQueueSync(target=NPC_0, subscript=[ASSetPriority(2)]),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftNorthPixels(4),
                ASShiftSouthPixels(8),
                ASShiftNorthPixels(4),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        Pause(8),
        PlaySound(sound=SO048_MINECART_START, channel=6),
        Return(),
        StopSound(identifier="EVENT_1694_stop_sound_24"),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASObjectMemoryModifyBits(arg_1=0x09, set_flags=[5], clear_bits=[4, 6])
            ],
        ),
        Pause(4),
        PlaySound(sound=SO113_OPEN_CHAMBER_DOOR, channel=6),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftNorthPixels(4),
                ASShiftSouthPixels(8),
                ASShiftNorthPixels(4),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        Return(),
    ]
)
