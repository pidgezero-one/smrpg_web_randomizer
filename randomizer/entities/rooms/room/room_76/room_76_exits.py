"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    MapExit(
        x=1,
        y=6,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=OW11_BANDITS_WAY,
        show_message=False,
        byte_2_bit_1=False,
        byte_2_bit_0=False,
    ),
    RoomExit(
        x=14,
        y=51,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R207_BANDITS_WAY_AREA_02,
        show_message=False,
        dst_x=2,
        dst_y=83,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False,
    ),
]
