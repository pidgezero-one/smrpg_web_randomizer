"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=16,
        y=8,
        z=3,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R361_VOLCANO_AREA_09,
        show_message=False,
        dst_x=28,
        dst_y=125,
        dst_z=1,
        dst_z_half=False,
        dst_f=NORTHWEST,
        x_bit_7=False),
    RoomExit(
        x=17,
        y=25,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R362_VOLCANO_AREA_07_STOMPING_CORKPEDITE,
        show_message=False,
        dst_x=2,
        dst_y=25,
        dst_z=5,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False),
]
