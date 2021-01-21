from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_981_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_981_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_981_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_981_transfer_xyzf_pixels_3',
        "command": 'transfer_xyzf_pixels',
        "args": [251, 254, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_981_jmp_if_random_above_128_4',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_979_set_sprite_sequence_4']
    },
    {
        "identifier": 'ACTION_981_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_980_pause_4']
    }
]
