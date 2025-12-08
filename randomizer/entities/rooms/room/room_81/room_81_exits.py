"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=13,
        y=14,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R079_ROSE_WAY_MAIN_AREA,
        show_message=False,
        dst_x=23,
        dst_y=65,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHWEST,
        x_bit_7=False),
    RoomExit(
        x=26,
        y=49,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED,
        show_message=False,
        dst_x=22,
        dst_y=106,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False),
]
