from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_243_set_sprite_sequence_0',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_243_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_243_shift_southwest_pixels_2',
        "command": 'shift_southwest_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_243_shift_northeast_pixels_3',
        "command": 'shift_northeast_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_243_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'ACTION_243_reset_properties_6']
    },
    {
        "identifier": 'ACTION_243_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_243_shift_southwest_pixels_2']
    },
    {
        "identifier": 'ACTION_243_reset_properties_6',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_243_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_243_ret_8',
        "command": 'ret'
    }
]
