# pylint: disable=C0301

"""E0610_MARRYMORE_OCCUPIED_EXTERIOR_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, OW28_MARRYMORE),
        Set0158Bit7Offset(0x0158),
        ClearBit(TEMP_7042_0),
        ClearBit(TEMP_7042_1),
        ClearBit(TEMP_7042_2),
        ClearBit(TEMP_7042_3),
        ClearBit(TEMP_7042_4),
        ClearBit(TEMP_7042_5),
        ClearBit(TEMP_7042_6),
        ClearBit(TEMP_7042_7),
        SetVarToConst(TEMP_70AC, 0),
        SetVarToConst(TEMP_70B8, 0),
        ClearBit(TEMP_704C_0),
        ClearBit(GUEST_DROPPED_OFF),
        ClearBit(EMPLOYMENT_704C_2),
        ClearBit(EMPLOYMENT_704C_3),
        ClearBit(BELLHOP_CALLED),
        ClearBit(MARRYMORE_UNKNOWN_709F_6),
        FadeOutMusicToVolume(duration=1, volume=127),
        JmpIfBitSet(MARRYMORE_BACKDOOR_OPEN, ["EVENT_610_action_queue_sync_33"]),
        SetSyncActionScript(NPC_7, A0376_TURN_RANDOMLY_IN_PLACE),
        SetSyncActionScript(NPC_8, A0113_HENCHMAN_BOUNCING_IN_PLACE),
        SetSyncActionScript(NPC_0, A0376_TURN_RANDOMLY_IN_PLACE),
        SetSyncActionScript(NPC_1, A0376_TURN_RANDOMLY_IN_PLACE),
        SetSyncActionScript(NPC_2, A0098_WALK_RANDOM_DIRECTIONS_NO_SOLIDITY_CHANGE),
        SetSyncActionScript(NPC_3, A0376_TURN_RANDOMLY_IN_PLACE),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASTransferToXYZF(x=17, y=113, z=0, direction=EAST),
                ASShadowOff(),
            ]),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASTransferToXYZF(x=18, y=113, z=0, direction=EAST),
                ASShadowOff(),
            ]),
        Jmp(["EVENT_610_fade_in_from_black_async_42"]),
        ActionQueueSync(
            target=NPC_3,
            subscript=[ASTransferToXYZF(x=15, y=72, z=8, direction=EAST)],
            identifier="EVENT_610_action_queue_sync_33"),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=16, y=68, z=8, direction=EAST),
                ASFaceSouthwest(),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASTransferToXYZF(x=16, y=69, z=8, direction=EAST),
                ASFaceSouthwest(),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASTransferToXYZF(x=16, y=72, z=8, direction=EAST),
                ASFaceNorthwest(),
            ]),
        ActionQueueSync(target=NPC_7, subscript=[ASFaceSoutheast()]),
        RememberLastObject(),
        SetSyncActionScript(NPC_5, A0376_TURN_RANDOMLY_IN_PLACE),
        SetSyncActionScript(NPC_6, A0376_TURN_RANDOMLY_IN_PLACE),
        SetSyncActionScript(NPC_8, A0113_HENCHMAN_BOUNCING_IN_PLACE),
        FadeInFromBlack(sync=False, identifier="EVENT_610_fade_in_from_black_async_42"),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_610_ret_26"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_610_ret_26"]),
        RunEventAsSubroutine(E3902_MARRYMORE_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_610_ret_26"),
    ]
)
