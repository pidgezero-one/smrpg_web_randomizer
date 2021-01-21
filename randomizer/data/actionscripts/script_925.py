from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_925_set_priority_0',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_925_set_700C_to_current_level_1',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_925_jmp_if_var_equals_short_2',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 79, 'ACTION_925_set_priority_4']
    },
    {
        "identifier": 'ACTION_925_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_925_set_priority_4',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_925_shift_south_pixels_5',
        "command": 'shift_south_pixels',
        "args": [3]
    },
    {
        "identifier": 'ACTION_925_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_925_ret_7',
        "command": 'ret'
    }
]
