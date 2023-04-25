"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    MapExit(
        x=8,
        y=25,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=OW19_FOREST_MAZE,
        show_message=False,
        byte_2_bit_1=False,
        byte_2_bit_0=False,
    ),
    RoomExit(
        x=3,
        y=14,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R226_FOREST_MAZE_AREA_02,
        show_message=False,
        dst_x=25,
        dst_y=43,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHWEST,
        x_bit_7=False,
    ),
]
