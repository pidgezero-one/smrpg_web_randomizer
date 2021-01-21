from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_680_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_680_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_680_pause_2',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_680_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [21, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_680_pause_4',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_680_reset_properties_5',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_680_pause_6',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_680_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'ACTION_680_ret_11']
    },
    {
        "identifier": 'ACTION_680_jmp_if_mario_in_air_8',
        "command": 'jmp_if_mario_in_air',
        "args": ['ACTION_680_pause_6']
    },
    {
        "identifier": 'ACTION_680_pause_9',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_680_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_680_pause_2']
    },
    {
        "identifier": 'ACTION_680_ret_11',
        "command": 'ret'
    }
]
