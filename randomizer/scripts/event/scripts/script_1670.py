# E1670_LANDS_END_2_SUMMON_INVISIBLE_PLATFORM

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E1840_PLATFORM_SUBROUTINE),
        JmpIfBitSet(TEMP_7043_1, ["EVENT_1670_ret_7"]),
        JmpIfMarioOnAnObjectOrNot(["EVENT_1670_ret_3", "EVENT_1670_play_sound_4"]),
        Return(identifier="EVENT_1670_ret_3"),
        PlaySound(sound=SO014_FLOWER, channel=6, identifier="EVENT_1670_play_sound_4"),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASVisibilityOn(),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFixedFCoordOn(),
                ASShiftNortheastPixels(4),
            ],
        ),
        SetBit(TEMP_7043_1),
        Return(identifier="EVENT_1670_ret_7"),
    ]
)
