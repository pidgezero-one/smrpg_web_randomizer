"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=1,
        y=80,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R434_SMITHY_FACTORY_AREA_09_FALLING_AXEM_REDS_ON_CONVEYOR_BELTS,
        show_message=False,
        dst_x=14,
        dst_y=13,
        dst_z=5,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False),
    RoomExit(
        x=16,
        y=62,
        z=2,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS,
        show_message=False,
        dst_x=20,
        dst_y=121,
        dst_z=9,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False),
]
