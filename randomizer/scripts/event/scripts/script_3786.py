# pylint: disable=C0301

"""E3786_BEAN_VALLEY_WEST_VINE_ROOM_EXIT_TO_UPPER_CHEST_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfMarioInAir(["EVENT_3584_ret_0"]),
        EnterArea(
            room_id=R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND,
            face_direction=NORTHEAST,
            x=17,
            y=104,
            z=6),
        Db(bytearray(b"\xfdI")),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASClearSolidityBits(cant_pass_walls=True),
                ASJumpToHeight(128),
                ASWalkNortheastPixels(8),
                ASFloatingOn(),
                ASWalk1StepNortheast(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASWalk1StepNortheast(),
            ]),
        FadeInFromBlack(sync=False),
        Pause(1, identifier="EVENT_3786_pause_5"),
        JmpIfMarioInAir(["EVENT_3786_pause_5"]),
        Return(),
    ]
)
