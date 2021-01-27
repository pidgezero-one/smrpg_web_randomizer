from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_639_set_700C_to_70A0_short_mem_0',
        "command": 'set_700C_to_70A0_short_mem',
        "args": [0x70b8]
    },
    {
        "identifier": 'ACTION_639_set_7000_short_mem_to_700C_1',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7016]
    },
    {
        "identifier": 'ACTION_639_set_700C_to_70A0_short_mem_2',
        "command": 'set_700C_to_70A0_short_mem',
        "args": [0x70b9]
    },
    {
        "identifier": 'ACTION_639_set_7000_short_mem_to_700C_3',
        "command": 'set_7000_short_mem_to_700C',
        "args": [0x7018]
    },
    {
        "identifier": 'ACTION_639_set_short_4',
        "command": 'set_short',
        "args": [0x701a, 0x0020]
    },
    {
        "identifier": 'ACTION_639_db_5',
        "command": 'db',
        "args": [0x9a]
    },
    {
        "identifier": 'ACTION_639_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'ACTION_639_transfer_xyzf_pixels_9']
    },
    {
        "identifier": 'ACTION_639_transfer_xyzf_pixels_7',
        "command": 'transfer_xyzf_pixels',
        "args": [212, 6, 30, RadialDirections.NORTHEAST]
    },
    {
        "identifier": 'ACTION_639_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_639_visibility_on_10']
    },
    {
        "identifier": 'ACTION_639_transfer_xyzf_pixels_9',
        "command": 'transfer_xyzf_pixels',
        "args": [244, 14, 30, RadialDirections.NORTHEAST]
    },
    {
        "identifier": 'ACTION_639_visibility_on_10',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_639_jmp_11',
        "command": 'jmp',
        "args": ['ACTION_638_set_bit_4']
    }
]
