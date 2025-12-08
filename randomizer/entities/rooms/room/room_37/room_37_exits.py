"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=13,
        y=34,
        z=10,
        f=EdgeDirection.SOUTHEAST,
        length=4,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM,
        show_message=False,
        dst_x=16,
        dst_y=123,
        dst_z=0,
        dst_z_half=False,
        dst_f=NORTHWEST,
        x_bit_7=False),
    RoomExit(
        x=11,
        y=50,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R042_BOOSTER_TOWER_3F_AREA_02_NES_MARIO_ROOM,
        show_message=False,
        dst_x=25,
        dst_y=67,
        dst_z=4,
        dst_z_half=False,
        dst_f=SOUTHWEST,
        x_bit_7=False),
]
