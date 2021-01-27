from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_559_set_vram_priority_0',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_559_set_priority_1',
        "command": 'set_priority',
        "args": [1]
    },
    {
        "identifier": 'ACTION_559_shift_south_pixels_2',
        "command": 'shift_south_pixels',
        "args": [6]
    },
    {
        "identifier": 'ACTION_559_shift_southwest_pixels_3',
        "command": 'shift_southwest_pixels',
        "args": [6]
    },
    {
        "identifier": 'ACTION_559_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_559_ret_5',
        "command": 'ret'
    }
]
