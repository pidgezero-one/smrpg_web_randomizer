"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=13,
        y=29,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R363_VOLCANO_AREA_15_STOMPING_CORKPEDITE,
        show_message=False,
        dst_x=3,
        dst_y=67,
        dst_z=5,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False,
    ),
    RoomExit(
        x=22,
        y=1,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R367_VOLCANO_AREA_17_LEADS_TO_HINOPIOS_SHOP,
        show_message=False,
        dst_x=13,
        dst_y=123,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False,
    ),
]
