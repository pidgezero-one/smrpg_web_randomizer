"""Exit list import"""

from randomizer.entities.rooms.exit_imports import *

exits = [
    MapExit(
        x=11,
        y=13,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=True,
        destination=OW20_PIPE_VAULT,
        show_message=False,
        byte_2_bit_1=False,
        byte_2_bit_0=False,
    ),
    MapExit(
        x=20,
        y=31,
        z=0,
        f=EdgeDirection.SOUTHEAST,
        length=2,
        height=0,
        nw_se_edge_active=True,
        ne_sw_edge_active=False,
        byte_2_bit_2=True,
        destination=OW20_PIPE_VAULT,
        show_message=False,
        byte_2_bit_1=False,
        byte_2_bit_0=False,
    ),
]
