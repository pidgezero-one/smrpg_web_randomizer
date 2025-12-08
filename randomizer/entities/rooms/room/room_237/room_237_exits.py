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
        destination=R221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS,
        show_message=False,
        dst_x=28,
        dst_y=80,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False),
    RoomExit(
        x=16,
        y=26,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=3,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER,
        show_message=False,
        dst_x=21,
        dst_y=57,
        dst_z=7,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False),
]
