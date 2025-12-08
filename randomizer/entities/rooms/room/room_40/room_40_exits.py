"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
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
        destination=R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS,
        show_message=False,
        dst_x=11,
        dst_y=81,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False),
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
        destination=R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS,
        show_message=False,
        dst_x=21,
        dst_y=21,
        dst_z=0,
        dst_z_half=False,
        dst_f=SOUTHEAST,
        x_bit_7=False),
]
