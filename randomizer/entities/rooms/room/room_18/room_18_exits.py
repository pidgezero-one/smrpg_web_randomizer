"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=12,
        y=35,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=3,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R320_MUSHROOM_KINGDOM_CASTLE_ENTRANCE_TO_THRONE_ROOM,
        show_message=False,
        dst_x=28,
        dst_y=93,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False),
]
