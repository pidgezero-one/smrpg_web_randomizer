"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=1,
        y=24,
        z=5,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=1,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R356_VOLCANO_AREA_08,
        show_message=False,
        dst_x=17,
        dst_y=23,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHWEST,
        x_bit_7=False),
    RoomExit(
        x=6,
        y=27,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R385_VOLCANO_AREA_06,
        show_message=False,
        dst_x=26,
        dst_y=83,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False),
]
