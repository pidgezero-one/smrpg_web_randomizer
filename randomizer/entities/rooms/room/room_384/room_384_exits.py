"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=19,
        y=56,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R360_VOLCANO_AREA_04_BUNCH_OF_STEPS,
        show_message=False,
        dst_x=30,
        dst_y=67,
        dst_z=4,
        dst_z_half=False,
        dst_f=NORTHWEST,
        x_bit_7=False,
    ),
    RoomExit(
        x=31,
        y=54,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R385_VOLCANO_AREA_06,
        show_message=False,
        dst_x=18,
        dst_y=79,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False,
    ),
]
