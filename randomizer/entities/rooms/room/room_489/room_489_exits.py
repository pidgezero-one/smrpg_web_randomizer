"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=1,
        y=46,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=1,
        nw_se_edge_active=True,
        ne_sw_edge_active=True,
        byte_2_bit_2=False,
        destination=R488_MUSHROOM_KINGDOM_JUMPING_KIDS_HOUSE_1F,
        show_message=False,
        dst_x=3,
        dst_y=20,
        dst_z=2,
        dst_z_half=True,
        dst_f=SOUTHWEST,
        x_bit_7=False),
]
