"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=16,
        y=18,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R084_ROSE_TOWN_OUTSIDE,
        show_message=False,
        dst_x=16,
        dst_y=56,
        dst_z=1,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False),
]
