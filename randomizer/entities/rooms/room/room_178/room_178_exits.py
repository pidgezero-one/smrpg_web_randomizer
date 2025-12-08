"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=9,
        y=90,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM,
        show_message=False,
        dst_x=11,
        dst_y=124,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHWEST,
        x_bit_7=False),
    RoomExit(
        x=14,
        y=82,
        z=6,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R181_SUNKEN_SHIP_POSTKC_AREA_03_ALLEY_RATS_ON_CANNONS,
        show_message=False,
        dst_x=31,
        dst_y=64,
        dst_z=5,
        dst_z_half=False,
        dst_f=NORTHWEST,
        x_bit_7=False),
]
