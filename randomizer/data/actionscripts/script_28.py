from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_28_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD]]
    },
    {
        "identifier": 'ACTION_28_fixed_f_coord_on_1',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_28_shift_northeast_pixels_2',
        "command": 'shift_northeast_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_28_pause_3',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'ACTION_28_shift_southwest_pixels_4',
        "command": 'shift_southwest_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_28_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_28_shift_northeast_pixels_2']
    }
]
