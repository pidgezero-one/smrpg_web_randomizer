"""Event tile list import"""

from randomizer.entities.rooms.event_imports import *

events = [
    Event(
        event=E3626_NIMBUS_SHOP_CHEST_CAMERA_SHIFT,
        x=13,
        y=16,
        z=3,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False),
    Event(
        event=E3694_NIMBUS_SHOP_EXIT,
        x=17,
        y=26,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_8_bit_4=False),
]
