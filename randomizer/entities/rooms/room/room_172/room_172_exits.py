"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=7,
        y=66,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY,
        show_message=False,
        dst_x=21,
        dst_y=75,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False),
]
