"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=3,
        y=110,
        z=2,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R359_VOLCANO_AREA_02,
        show_message=False,
        dst_x=28,
        dst_y=43,
        dst_z=1,
        dst_z_half=False,
        dst_f=NORTHWEST,
        x_bit_7=False),
]
