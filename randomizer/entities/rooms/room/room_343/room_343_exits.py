"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=6,
        y=95,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=1,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R346_NIMBUS_LAND_INN_BEDROOM,
        show_message=False,
        dst_x=12,
        dst_y=80,
        dst_z=0,
        dst_z_half=True,
        dst_f=SOUTHEAST,
        x_bit_7=False,
    ),
]
