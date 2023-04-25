"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=13,
        y=36,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R473_SMITHY_FACTORY_AREA_13_BOWYERS_FALLING_DOWN_CONVEYOR_BELTS,
        show_message=False,
        dst_x=10,
        dst_y=54,
        dst_z=15,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False,
    ),
    RoomExit(
        x=16,
        y=27,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R474_SMITHY_FACTORY_AREA_15_FALLING_YARIDOVICHS,
        show_message=False,
        dst_x=18,
        dst_y=39,
        dst_z=8,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False,
    ),
]
