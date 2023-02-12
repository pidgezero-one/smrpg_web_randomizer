from randomizer.entities.rooms.exit_imports import *

exits = [
    MapExit(
        x=5,
        y=16,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=7,
        nw_se_edge_active = True,
        ne_sw_edge_active = False,
        byte_2_bit_2 = True,
        destination = OW19_FOREST_MAZE,
        show_message = False,
        byte_2_bit_1 = False,
        byte_2_bit_0 = False,
    ),
]
