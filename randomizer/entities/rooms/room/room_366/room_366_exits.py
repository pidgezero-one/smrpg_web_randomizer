"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=12,
        y=67,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R386_VOLCANO_AREA_12_ERUPTING_STUMPET,
        show_message=False,
        dst_x=19,
        dst_y=123,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False),
    RoomExit(
        x=15,
        y=71,
        z=5,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R386_VOLCANO_AREA_12_ERUPTING_STUMPET,
        show_message=False,
        dst_x=20,
        dst_y=110,
        dst_z=4,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False),
]
