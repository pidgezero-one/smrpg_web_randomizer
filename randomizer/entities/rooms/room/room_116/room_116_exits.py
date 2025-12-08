"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=25,
        y=59,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL,
        show_message=False,
        dst_x=3,
        dst_y=21,
        dst_z=2,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False),
]
