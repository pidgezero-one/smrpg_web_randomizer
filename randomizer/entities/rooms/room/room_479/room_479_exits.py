"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=1,
        y=67,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R478_BOWSERS_KEEP_2ND_TIME_AREA_03_LAVA_ROOM_WBRIDGE,
        show_message=False,
        dst_x=16,
        dst_y=42,
        dst_z=5,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False),
    RoomExit(
        x=13,
        y=43,
        z=1,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM,
        show_message=False,
        dst_x=11,
        dst_y=29,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False),
]
