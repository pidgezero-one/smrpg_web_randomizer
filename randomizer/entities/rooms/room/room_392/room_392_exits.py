"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=21,
        y=79,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R394_VOLCANO_POSTCD_AREA_05,
        show_message=False,
        dst_x=27,
        dst_y=57,
        dst_z=22,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False,
    ),
    RoomExit(
        x=17,
        y=56,
        z=7,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
        show_message=False,
        dst_x=21,
        dst_y=120,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False,
    ),
]
