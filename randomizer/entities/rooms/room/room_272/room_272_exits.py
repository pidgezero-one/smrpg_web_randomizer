"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=2,
        y=22,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R282_MOLEVILLE_MINES_AREA_10_SMALL_ROOM_WMINECART_TRACKS,
        show_message=False,
        dst_x=24,
        dst_y=117,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False),
    RoomExit(
        x=10,
        y=12,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM,
        show_message=False,
        dst_x=19,
        dst_y=31,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False),
]
