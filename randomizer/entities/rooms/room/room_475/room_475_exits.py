"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=20,
        y=122,
        z=9,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R442_SMITHY_FACTORY_AREA_11_CONVEYOR_BELTS_SPAWNING_DRILL_BITS_AND_MACKS,
        show_message=False,
        dst_x=15,
        dst_y=63,
        dst_z=2,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False),
    RoomExit(
        x=30,
        y=68,
        z=12,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R473_SMITHY_FACTORY_AREA_13_BOWYERS_FALLING_DOWN_CONVEYOR_BELTS,
        show_message=False,
        dst_x=1,
        dst_y=113,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False),
]
