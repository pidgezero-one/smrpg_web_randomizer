# pylint: disable=C0301

"""E3781_BEAN_VALLEY_EAST_VINE_ROOM_EXIT_TO_NIMBUS_MEZZANINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfMarioInAir(["EVENT_3584_ret_0"]),
        EnterArea(
            room_id=R369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE,
            face_direction=NORTHEAST,
            x=24,
            y=25,
            z=0),
        Db(bytearray(b"\xfdI")),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(132),
                ASWalkNortheastSteps(2),
                ASWalkNortheastPixels(20),
                ASSetWalkingSpeed(NORMAL),
            ]),
        FadeInFromBlack(sync=False),
        Pause(1, identifier="EVENT_3781_pause_7"),
        JmpIfMarioInAir(["EVENT_3781_pause_7"]),
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, OW49_NIMBUS_LAND),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3781_ret_12"]),
        RunEventAsSubroutine(E3912_NIMBUS_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_3781_ret_12"),
    ]
)
