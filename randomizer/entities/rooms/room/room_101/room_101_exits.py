"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    MapExit(
        x=14,
        y=91,
        z=6,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=True,
        destination=OW25_BOOSTER_PASS,
        show_message=False,
        byte_2_bit_1=False,
        byte_2_bit_0=False),
    RoomExit(
        x=1,
        y=122,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R100_BOOSTER_PASS_AREA_01,
        show_message=True,
        dst_x=19,
        dst_y=26,
        dst_z=8,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False),
]
