"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=14,
        y=99,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=3,
        height=7,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R472_FACTORY_GROUNDS_AREA_03,
        show_message=False,
        dst_x=4,
        dst_y=96,
        dst_z=5,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False),
]
