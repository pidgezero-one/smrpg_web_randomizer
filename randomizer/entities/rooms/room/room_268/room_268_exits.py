"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=9,
        y=27,
        z=1,
        f=EdgeDirection.SOUTHWEST,
        length=6,
        height=3,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN,
        show_message=False,
        dst_x=26,
        dst_y=53,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False,
    ),
]
