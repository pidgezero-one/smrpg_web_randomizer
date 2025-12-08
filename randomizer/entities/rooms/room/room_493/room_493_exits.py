"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=4,
        y=83,
        z=1,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=1,
        nw_se_edge_active=True,
        ne_sw_edge_active=True,
        byte_2_bit_2=False,
        destination=R052_MUSHROOM_KINGDOM_INN_2F,
        show_message=False,
        dst_x=1,
        dst_y=121,
        dst_z=1,
        dst_z_half=True,
        dst_f=NORTHEAST,
        x_bit_7=False),
]
