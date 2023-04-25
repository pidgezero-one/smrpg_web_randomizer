"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=1,
        y=17,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R016_MARIOS_PAD,
        show_message=False,
        dst_x=12,
        dst_y=34,
        dst_z=1,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False,
    ),
]
