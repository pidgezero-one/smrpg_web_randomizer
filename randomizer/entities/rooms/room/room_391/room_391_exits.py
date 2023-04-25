"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=11,
        y=54,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R365_VOLCANO_POSTCD_AREA_03,
        show_message=False,
        dst_x=15,
        dst_y=16,
        dst_z=6,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False,
    ),
    RoomExit(
        x=13,
        y=43,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R394_VOLCANO_POSTCD_AREA_05,
        show_message=False,
        dst_x=26,
        dst_y=123,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False,
    ),
]
