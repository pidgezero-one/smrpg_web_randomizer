"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=16,
        y=69,
        z=2,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R012_MARRYMORE_INN_SUITE_ROOM,
        show_message=False,
        dst_x=3,
        dst_y=21,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False),
    RoomExit(
        x=12,
        y=74,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=1,
        nw_se_edge_active=True,
        ne_sw_edge_active=True,
        byte_2_bit_2=False,
        destination=R006_MARRYMORE_INN_2F,
        show_message=False,
        dst_x=13,
        dst_y=42,
        dst_z=2,
        dst_z_half=True,
        dst_f=SOUTHWEST,
        x_bit_7=False),
]
