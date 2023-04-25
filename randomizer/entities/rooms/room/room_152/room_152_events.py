"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E0633_MARRYMORE_CHAPEL_LOBBY_EXIT_TO_EXTERIOR,
        x=3,
        y=37,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=2,
        nw_se_edge_active=True,
        ne_sw_edge_active=True,
        byte_8_bit_4=False,
    ),
    Event(
        event=E0673_MARRYMORE_CHAPEL_LOBBY_EXIT_TO_ANTECHAMBER,
        x=7,
        y=25,
        z=4,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False,
    ),
]
