"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=19,
        y=126,
        z=1,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R383_VOLCANO_AREA_10_JUMPING_PYROSPHERES,
        show_message=False,
        dst_x=29,
        dst_y=17,
        dst_z=3,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False,
    ),
    RoomExit(
        x=12,
        y=122,
        z=1,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R386_VOLCANO_AREA_12_ERUPTING_STUMPET,
        show_message=False,
        dst_x=27,
        dst_y=113,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False,
    ),
]
