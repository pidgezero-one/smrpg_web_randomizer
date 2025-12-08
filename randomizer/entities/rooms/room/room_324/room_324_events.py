"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E2078_MONSTRO_SAVE_BOX,
        x=22,
        y=89,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False),
    Event(
        event=E2074_ENTER_MONSTRO_SEALED_ROOM,
        x=12,
        y=61,
        z=4,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False),
]
