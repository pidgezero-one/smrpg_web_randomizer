"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=17,
        y=120,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY,
        show_message=False,
        dst_x=20,
        dst_y=69,
        dst_z=5,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False),
]
