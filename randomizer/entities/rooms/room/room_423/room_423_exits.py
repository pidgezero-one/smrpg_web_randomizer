"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=15,
        y=21,
        z=2,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM,
        show_message=False,
        dst_x=27,
        dst_y=112,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False,
    ),
]
