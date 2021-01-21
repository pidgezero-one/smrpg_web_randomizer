from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_624_set_object_memory_bits_0',
        "command": 'set_object_memory_bits',
        "args": [0x0b, bits=[1]]
    },
    {
        "identifier": 'ACTION_624_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_624_shift_northeast_pixels_2',
        "command": 'shift_northeast_pixels',
        "args": [12]
    },
    {
        "identifier": 'ACTION_624_visibility_on_3',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_624_shift_northeast_pixels_4',
        "command": 'shift_northeast_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_624_shift_northeast_steps_5',
        "command": 'shift_northeast_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_624_shift_northeast_pixels_6',
        "command": 'shift_northeast_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_624_walk_1_step_northwest_7',
        "command": 'walk_1_step_northwest'
    },
    {
        "identifier": 'ACTION_624_set_animation_speed_8',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_624_set_bit_9',
        "command": 'set_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'ACTION_624_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'ACTION_624_ret_11',
        "command": 'ret'
    }
]
