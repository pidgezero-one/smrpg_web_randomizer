"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    MapExit(
        x=7,
        y=87,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=True,
        destination=OW52_YOSTER_ISLE,
        show_message=False,
        byte_2_bit_1=False,
        byte_2_bit_0=False),
    RoomExit(
        x=24,
        y=52,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R033_YOSTER_ISLE_ENTRANCE_FROM_PIPE_VAULT,
        show_message=False,
        dst_x=2,
        dst_y=24,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False),
]
