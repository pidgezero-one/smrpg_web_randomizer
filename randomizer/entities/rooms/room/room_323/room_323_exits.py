"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=26,
        y=98,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
        show_message=False,
        dst_x=9,
        dst_y=19,
        dst_z=2,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False,
    ),
    RoomExit(
        x=29,
        y=91,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM,
        show_message=False,
        dst_x=13,
        dst_y=35,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False,
    ),
]
