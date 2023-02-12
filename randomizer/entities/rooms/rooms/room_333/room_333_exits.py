from randomizer.entities.rooms.exit_imports import *

exits = [
    MapExit(
        x=1,
        y=25,
        z=0,
        f=EdgeDirection.SOUTHWEST,
        length=2,
        height=0,
        nw_se_edge_active = True,
        ne_sw_edge_active = False,
        byte_2_bit_2 = False,
        destination = OW14_KERO_SEWERS,
        show_message = False,
        byte_2_bit_1 = False,
        byte_2_bit_0 = False,
    ),
]
