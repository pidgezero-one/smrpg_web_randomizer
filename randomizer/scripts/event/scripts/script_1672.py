# pylint: disable=C0301

"""E1672_LANDS_END_2_SUMMON_INVISIBLE_PLATFORM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E1840_PLATFORM_SUBROUTINE),
        JmpIfBitSet(TEMP_7043_2, ["EVENT_1672_jmp_fork_mario_on_object_8"]),
        JmpIfMarioOnAnObjectOrNot(["EVENT_1672_ret_3", "EVENT_1672_play_sound_4"]),
        Return(identifier="EVENT_1672_ret_3"),
        PlaySound(sound=SO014_FLOWER, channel=6, identifier="EVENT_1672_play_sound_4"),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASVisibilityOn(),
                ASFixedFCoordOn(),
                ASShiftZUpPixels(12),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ]),
        SetBit(TEMP_7043_2),
        Return(),
        JmpIfMarioOnAnObjectOrNot(
            ["EVENT_1672_jmp_if_bit_set_10", "EVENT_1672_ret_3"],
            identifier="EVENT_1672_jmp_fork_mario_on_object_8"),
        Jmp(["EVENT_1672_ret_3"]),
        JmpIfBitSet(
            TEMP_7043_4, ["EVENT_1672_ret_3"], identifier="EVENT_1672_jmp_if_bit_set_10"
        ),
        SetBit(TEMP_7043_4),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FASTER),
                ASShiftNorthSteps(3),
                ASSetWalkingSpeed(NORMAL),
            ]),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASWalk1StepSoutheast(),
                ASWalkNortheastSteps(4),
                ASWalkSouthwestSteps(4),
                ASWalk1StepNorthwest(),
            ]),
        Return(),
    ]
)
