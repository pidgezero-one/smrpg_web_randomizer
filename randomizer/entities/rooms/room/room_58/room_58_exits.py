"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=19,
        y=43,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER,
        show_message=False,
        dst_x=12,
        dst_y=101,
        dst_z=2,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False),
    RoomExit(
        x=27,
        y=27,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES,
        show_message=False,
        dst_x=3,
        dst_y=49,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False),
]
