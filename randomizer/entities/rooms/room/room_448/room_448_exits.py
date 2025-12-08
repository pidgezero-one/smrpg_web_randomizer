"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=5,
        y=40,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM,
        show_message=False,
        dst_x=23,
        dst_y=105,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False),
]
