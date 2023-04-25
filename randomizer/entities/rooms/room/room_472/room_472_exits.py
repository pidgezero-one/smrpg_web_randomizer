"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=2,
        y=95,
        z=5,
        f=EdgeDirection.SOUTHEAST,
        length=3,
        height=7,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
        show_message=False,
        dst_x=14,
        dst_y=97,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHWEST,
        x_bit_7=False,
    ),
    RoomExit(
        x=15,
        y=121,
        z=5,
        f=EdgeDirection.SOUTHEAST,
        length=3,
        height=7,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R471_FACTORY_GROUNDS_AREA_02,
        show_message=False,
        dst_x=4,
        dst_y=32,
        dst_z=5,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False,
    ),
]
