"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=3,
        y=21,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
        show_message=False,
        dst_x=5,
        dst_y=40,
        dst_z=1,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False,
    ),
]
