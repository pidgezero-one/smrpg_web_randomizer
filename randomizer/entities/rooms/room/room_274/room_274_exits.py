"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=7,
        y=87,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE,
        show_message=False,
        dst_x=2,
        dst_y=57,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False),
    RoomExit(
        x=2,
        y=85,
        z=4,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R278_MOLEVILLE_MINES_AREA_03_LEADS_BACK_TO_AREA_1,
        show_message=False,
        dst_x=19,
        dst_y=93,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHWEST,
        x_bit_7=False),
]
