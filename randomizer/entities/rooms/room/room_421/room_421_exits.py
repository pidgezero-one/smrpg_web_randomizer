"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=8,
        y=72,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=5,
        height=3,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM,
        show_message=False,
        dst_x=16,
        dst_y=117,
        dst_z=4,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False),
]
