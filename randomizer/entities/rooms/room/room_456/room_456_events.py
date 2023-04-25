"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E3350_KEEP_ALL_DOOR_PATHS_EXIT_TO_REWARD_ROOM,
        x=25,
        y=103,
        z=16,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
    Event(
        event=E1946_KEEP_DONKEY_ROOM_EXIT_TO_PREVIOUS,
        x=22,
        y=124,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
]
