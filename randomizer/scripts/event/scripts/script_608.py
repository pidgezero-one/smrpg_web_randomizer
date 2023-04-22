# pylint: disable=C0301

"""E0608_MARRYMORE_INN_3F_HALLWAY_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7042_0, ["EVENT_608_jmp_if_bit_set_4"]),
        JmpIfBitSet(TEMP_7042_4, ["EVENT_608_jmp_if_bit_set_4"]),
        FadeInFromBlack(sync=False),
        Return(),
        JmpIfBitSet(
            TEMP_7042_2,
            ["EVENT_608_action_queue_sync_8"],
            identifier="EVENT_608_jmp_if_bit_set_4",
        ),
        JmpIfBitSet(TEMP_7042_3, ["EVENT_608_action_queue_sync_8"]),
        JmpIfBitSet(TEMP_7042_4, ["EVENT_608_action_queue_sync_8"]),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASTransferToXYZF(x=15, y=71, z=4, direction=EAST),
                ASTransferXYZFPixels(x=0, y=4, z=0, direction=EAST),
            ],
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                )
            ],
            identifier="EVENT_608_action_queue_sync_8",
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                )
            ],
        ),
        ApplySolidityModToLevel(
            permanent=True, room_id=R011_MARRYMORE_INN_3F, mod_id=0
        ),
        JmpIfBitSet(BELLHOP_CALLED, ["EVENT_608_remove_from_current_level_22"]),
        FadeInFromBlack(sync=False),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
        JmpIfBitSet(TEMP_7042_2, ["EVENT_608_ret_21"]),
        JmpIfBitSet(TEMP_7042_4, ["EVENT_608_ret_21"]),
        SetBit(TEMP_7042_2),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R011_MARRYMORE_INN_3F, mod_id=0
        ),
        ApplySolidityModToLevel(
            permanent=True, room_id=R011_MARRYMORE_INN_3F, mod_id=1
        ),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASWalk1StepNortheast(),
                ASVisibilityOff(),
                ASTransferToXYZF(x=16, y=101, z=0, direction=EAST),
            ],
        ),
        Return(identifier="EVENT_608_ret_21"),
        RemoveObjectFromCurrentLevel(
            NPC_2, identifier="EVENT_608_remove_from_current_level_22"
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
