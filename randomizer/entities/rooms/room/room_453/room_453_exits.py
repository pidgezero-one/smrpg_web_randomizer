"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=11,
        y=30,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R479_BOWSERS_KEEP_2ND_TIME_AREA_04_THRONE_ROOM,
        show_message=False,
        dst_x=12,
        dst_y=47,
        dst_z=0,
        dst_z_half=True,
        dst_f=SOUTHWEST,
        x_bit_7=False,
    ),
    RoomExit(
        x=28,
        y=18,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=3,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R452_BOWSERS_KEEP_AREA_06_SAVE_POINT_WCROCO_SHOP,
        show_message=False,
        dst_x=9,
        dst_y=93,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False,
    ),
]
