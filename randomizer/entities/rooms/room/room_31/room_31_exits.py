"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=6,
        y=89,
        z=3,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=2,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R021_MUSHROOM_KINGDOM_CASTLE_BRANCH_ROOM_TO_VAULTGUEST_ROOM,
        show_message=False,
        dst_x=13,
        dst_y=69,
        dst_z=1,
        dst_z_half=True,
        dst_f=NORTHEAST,
        x_bit_7=False,
    ),
]
