"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=15,
        y=57,
        z=5,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM,
        show_message=False,
        dst_x=22,
        dst_y=48,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False,
    ),
    RoomExit(
        x=2,
        y=31,
        z=5,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R471_FACTORY_GROUNDS_AREA_02,
        show_message=False,
        dst_x=15,
        dst_y=55,
        dst_z=5,
        dst_z_half=False,
        dst_f=NORTHWEST,
        x_bit_7=False,
    ),
]
