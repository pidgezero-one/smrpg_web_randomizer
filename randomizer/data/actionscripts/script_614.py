from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_614_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_614_object_memory_set_bit_1',
        "command": 'object_memory_set_bit',
        "args": [0x0d, [6]]
    },
    {
        "identifier": 'ACTION_614_set_priority_2',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_614_set_object_memory_bits_3',
        "command": 'set_object_memory_bits',
        "args": [0x0e, [2]]
    },
    {
        "identifier": 'ACTION_614_pause_4',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_614_jmp_if_var_not_equals_byte_5',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70ae, 24, 'ACTION_614_visibility_off_0']
    },
    {
        "identifier": 'ACTION_614_visibility_on_6',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_614_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_614_sequence_looping_on_8',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_614_shift_southeast_pixels_9',
        "command": 'shift_southeast_pixels',
        "args": [18]
    },
    {
        "identifier": 'ACTION_614_shift_z_down_steps_10',
        "command": 'shift_z_down_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_614_face_mario_11',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_614_pause_12',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_614_jmp_13',
        "command": 'jmp',
        "args": ['ACTION_614_face_mario_11']
    }
]
