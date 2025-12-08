# pylint: disable=C0301

"""E3223_SHIP_TROOPA_PUZZLE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1, identifier="EVENT_3223_pause_0"),
        JmpIfBitSet(TEMP_7044_7, ["EVENT_3223_play_sound_12"]),
        JmpIfBitClear(TEMP_7043_0, ["EVENT_3223_pause_0"]),
        SetSyncActionScript(NPC_3, A0338_SHIP_TRAMPOLINE_PUZZLE_SCROLL),
        JmpIfBitSet(SHIP_TROOPA_PRIZE, ["EVENT_3223_ret_11"]),
        SetVarToConst(X_COORD_1, 15),
        SetVarToConst(Y_COORD_1, 117),
        SetVarToConst(Z_COORD_1, 15),
        Db(bytearray(b"\xfd\xc4")),
        Pause(1, identifier="EVENT_3223_pause_9"),
        JmpToEvent(E3384_SHIP_TROOPA_PRIZE_PACKET_GRANT),
        Return(identifier="EVENT_3223_ret_11"),
        PlaySound(
            sound=SO022_CLOSE_DOOR, channel=6, identifier="EVENT_3223_play_sound_12"
        ),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASStartLoopNTimes(7),
                ASWalkSouthPixels(2),
                ASWalkNorthPixels(2),
                ASEndLoop(),
            ]),
        Return(),
    ]
)
