"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=13,
        y=23,
        z=2,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
        show_message=False,
        dst_x=18,
        dst_y=112,
        dst_z=2,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False),
    RoomExit(
        x=21,
        y=24,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=1,
        nw_se_edge_active=True,
        ne_sw_edge_active=True,
        byte_2_bit_2=False,
        destination=R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT,
        show_message=False,
        dst_x=17,
        dst_y=40,
        dst_z=0,
        dst_z_half=True,
        dst_f=SOUTHEAST,
        x_bit_7=False),
]
