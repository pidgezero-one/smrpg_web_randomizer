"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=28,
        y=127,
        z=1,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R356_VOLCANO_AREA_08,
        show_message=False,
        dst_x=17,
        dst_y=8,
        dst_z=3,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False),
    RoomExit(
        x=30,
        y=93,
        z=1,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R383_VOLCANO_AREA_10_JUMPING_PYROSPHERES,
        show_message=False,
        dst_x=19,
        dst_y=37,
        dst_z=3,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False),
]
