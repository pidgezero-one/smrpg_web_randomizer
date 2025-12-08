"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=1,
        y=122,
        z=4,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM,
        show_message=False,
        dst_x=19,
        dst_y=23,
        dst_z=4,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False),
    RoomExit(
        x=14,
        y=95,
        z=4,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM,
        show_message=False,
        dst_x=19,
        dst_y=67,
        dst_z=4,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False),
]
