"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=9,
        y=48,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=1,
        nw_se_edge_active=True,
        ne_sw_edge_active=True,
        byte_2_bit_2=False,
        destination=R085_ROSE_TOWN_DURING_BOWYER_INN_1F,
        show_message=False,
        dst_x=7,
        dst_y=14,
        dst_z=0,
        dst_z_half=True,
        dst_f=SOUTHEAST,
        x_bit_7=False),
]
