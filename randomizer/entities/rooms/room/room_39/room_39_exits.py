"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=16,
        y=125,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R037_BOOSTER_TOWER_4F_3LEVEL_ROOM_WJUMPING_SPOOKUMS,
        show_message=False,
        dst_x=14,
        dst_y=35,
        dst_z=10,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False,
    ),
    RoomExit(
        x=11,
        y=127,
        z=5,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R201_BOOSTER_TOWER_6F_AREA_01_SMALL_ROOM_WSAVE_POINT,
        show_message=False,
        dst_x=29,
        dst_y=117,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False,
    ),
]
