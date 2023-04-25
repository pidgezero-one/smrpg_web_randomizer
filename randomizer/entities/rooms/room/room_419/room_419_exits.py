"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=4,
        y=111,
        z=6,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R417_GARDENERS_HOUSE_OUTSIDE,
        show_message=False,
        dst_x=6,
        dst_y=99,
        dst_z=2,
        dst_z_half=False,
        dst_f=SOUTH,
        x_bit_7=False,
    ),
    RoomExit(
        x=4,
        y=112,
        z=6,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R417_GARDENERS_HOUSE_OUTSIDE,
        show_message=False,
        dst_x=6,
        dst_y=99,
        dst_z=2,
        dst_z_half=False,
        dst_f=SOUTH,
        x_bit_7=False,
    ),
]
