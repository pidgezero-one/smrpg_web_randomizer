from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_585_face_southeast_0',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_585_fixed_f_coord_on_1',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_585_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_585_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_585_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_585_shift_southwest_steps_5',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_585_shift_northeast_steps_6',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_585_shift_southwest_steps_7',
        "command": 'shift_southwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_585_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_585_shift_southwest_steps_5']
    }
]
