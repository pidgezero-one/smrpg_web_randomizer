"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=2,
        y=71,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R364_VOLCANO_AREA_14,
        show_message=False,
        dst_x=1,
        dst_y=109,
        dst_z=3,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False),
    RoomExit(
        x=2,
        y=66,
        z=5,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R390_VOLCANO_AREA_16_ERUPTING_STUMPET,
        show_message=False,
        dst_x=13,
        dst_y=27,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHWEST,
        x_bit_7=False),
]
