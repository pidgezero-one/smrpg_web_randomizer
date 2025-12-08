"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=1,
        y=126,
        z=10,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R220_SMITHY_FACTORY_AREA_02_WSAVE_POINT,
        show_message=False,
        dst_x=15,
        dst_y=56,
        dst_z=10,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False),
    RoomExit(
        x=20,
        y=106,
        z=10,
        f=EdgeDirection.SOUTHEAST,
        length=1,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R221_SMITHY_FACTORY_AREA_04_GREEN_SWITCH_WAMEBOIDS,
        show_message=False,
        dst_x=17,
        dst_y=99,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False),
]
