from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E3350_KEEP_ALL_DOOR_PATHS_EXIT_TO_REWARD_ROOM,
        x=20,
        y=16,
        z=1,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active = True,
        ne_sw_edge_active = False,
        byte_8_bit_4 = False,
    ),
    Event(
        event=E1935_KEEP_ROTATING_ROOM_EXIT_TO_PREVIOUS,
        x=6,
        y=48,
        z=1,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active = True,
        ne_sw_edge_active = False,
        byte_8_bit_4 = False,
    ),
]
