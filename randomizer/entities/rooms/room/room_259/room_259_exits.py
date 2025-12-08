"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    RoomExit(
        x=28,
        y=116,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS,
        show_message=False,
        dst_x=2,
        dst_y=77,
        dst_z=9,
        dst_z_half=False,
        dst_f=NORTHWEST,
        x_bit_7=False),
    RoomExit(
        x=30,
        y=125,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=False,
        destination=R042_BOOSTER_TOWER_3F_AREA_02_NES_MARIO_ROOM,
        show_message=False,
        dst_x=20,
        dst_y=65,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False),
]
