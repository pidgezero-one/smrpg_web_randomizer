"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=30,
        y=16,
        z=3,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R358_VOLCANO_AREA_11,
        show_message=False,
        dst_x=19,
        dst_y=125,
        dst_z=1,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False),
    RoomExit(
        x=19,
        y=38,
        z=3,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R361_VOLCANO_AREA_09,
        show_message=False,
        dst_x=30,
        dst_y=94,
        dst_z=1,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False),
]
