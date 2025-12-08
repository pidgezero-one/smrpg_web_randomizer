"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=6,
        y=26,
        z=2,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R191_MUSHROOM_KINGDOM_OUTSIDE,
        show_message=False,
        dst_x=5,
        dst_y=92,
        dst_z=4,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False),
    RoomExit(
        x=3,
        y=19,
        z=3,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=1,
        nw_se_edge_active=True,
        ne_sw_edge_active=True,
        byte_2_bit_2=False,
        destination=R489_MUSHROOM_KINGDOM_JUMPING_KIDS_HOUSE_2F,
        show_message=False,
        dst_x=1,
        dst_y=45,
        dst_z=1,
        dst_z_half=True,
        dst_f=NORTHEAST,
        x_bit_7=False),
]
