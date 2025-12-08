"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=3,
        y=67,
        z=5,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R477_BOWSERS_KEEP_2ND_TIME_AREA_02,
        show_message=False,
        dst_x=16,
        dst_y=69,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False),
    RoomExit(
        x=17,
        y=40,
        z=5,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R479_BOWSERS_KEEP_2ND_TIME_AREA_04_THRONE_ROOM,
        show_message=False,
        dst_x=2,
        dst_y=66,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False),
]
