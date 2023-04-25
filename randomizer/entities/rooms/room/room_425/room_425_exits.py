"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=16,
        y=118,
        z=4,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE,
        show_message=False,
        dst_x=8,
        dst_y=76,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False,
    ),
    RoomExit(
        x=27,
        y=111,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R423_BELOME_TEMPLE_AREA_06_BELOMES_FORTUNE_ROOM_WELEVATING_PLATFORM,
        show_message=False,
        dst_x=16,
        dst_y=20,
        dst_z=2,
        dst_z_half=False,
        dst_f=NORTHEAST,
        x_bit_7=False,
    ),
]
