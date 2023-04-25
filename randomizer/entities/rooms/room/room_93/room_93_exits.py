"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=16,
        y=67,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE,
        show_message=False,
        dst_x=13,
        dst_y=26,
        dst_z=4,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False,
    ),
    RoomExit(
        x=16,
        y=59,
        z=1,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=2,
        nw_se_edge_active=True,
        ne_sw_edge_active=True,
        byte_2_bit_2=False,
        destination=R097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F,
        show_message=False,
        dst_x=17,
        dst_y=91,
        dst_z=1,
        dst_z_half=True,
        dst_f=NORTHWEST,
        x_bit_7=False,
    ),
]
