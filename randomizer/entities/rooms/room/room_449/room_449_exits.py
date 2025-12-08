"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=4,
        y=78,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM,
        show_message=False,
        dst_x=27,
        dst_y=99,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False),
    RoomExit(
        x=28,
        y=30,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM,
        show_message=False,
        dst_x=2,
        dst_y=66,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False),
]
