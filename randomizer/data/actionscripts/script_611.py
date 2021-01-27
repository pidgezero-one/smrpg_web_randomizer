from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_611_visibility_off_0',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_611_object_memory_set_bit_1',
        "command": 'object_memory_set_bit',
        "args": [0x0d, [6]]
    },
    {
        "identifier": 'ACTION_611_set_priority_2',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_611_set_3',
        "command": 'set',
        "args": [0x70ae, 21]
    },
    {
        "identifier": 'ACTION_611_set_object_memory_bits_4',
        "command": 'set_object_memory_bits',
        "args": [0x0e, [0]]
    },
    {
        "identifier": 'ACTION_611_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_611_jmp_if_var_not_equals_byte_6',
        "command": 'jmp_if_var_not_equals_byte',
        "args": [0x70ae, 21, 'ACTION_611_visibility_off_0']
    },
    {
        "identifier": 'ACTION_611_visibility_on_7',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_611_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_611_sequence_looping_on_9',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_611_shift_southeast_pixels_10',
        "command": 'shift_southeast_pixels',
        "args": [18]
    },
    {
        "identifier": 'ACTION_611_shift_z_down_steps_11',
        "command": 'shift_z_down_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_611_face_mario_12',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_611_pause_13',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_611_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_611_face_mario_12']
    }
]
