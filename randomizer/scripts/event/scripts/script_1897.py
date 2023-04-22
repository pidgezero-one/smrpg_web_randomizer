# pylint: disable=C0301

"""E1897_ABYSS_UPPER_MACHINE_YARID_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(ABYSS_TWO_CHEST_ROOM_DIRECTIONAL_BIT),
        JmpIfBitSet(UNKNOWN_DIRECTIONAL_BIT_2, ["EVENT_1897_action_queue_sync_3"]),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R474_SMITHY_FACTORY_AREA_15_FALLING_YARIDOVICHS,
            mod_id=0,
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkNorthwestPixels(4),
                ASWalkSouthPixels(8),
                ASFaceSouthwest(),
                ASSetSolidityBits(bit_7=True),
            ],
            identifier="EVENT_1897_action_queue_sync_3",
        ),
        JmpIfBitSet(
            ABYSS_FINAL_ROOM_TRAMPOLINE, ["EVENT_1897_fade_in_from_black_sync_7"]
        ),
        FadeInFromBlack(sync=False),
        Return(),
        FadeInFromBlack(sync=True, identifier="EVENT_1897_fade_in_from_black_sync_7"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASClearSolidityBits(cant_pass_walls=True),
                ASTransferXYZFSteps(x=0, y=255, z=30, direction=NORTHEAST),
                ASJumpToHeight(height=112, silent=True),
                ASWalk1StepSouth(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASPause(
                    1, identifier="EVENT_1897_action_queue_async_8_SUBSCRIPT_pause_7"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_1897_action_queue_async_8_SUBSCRIPT_pause_7"]
                ),
                ASPlaySound(sound=SO058_INSERT, channel=4),
            ],
        ),
        ClearBit(ABYSS_FINAL_ROOM_TRAMPOLINE),
        Return(),
    ]
)
