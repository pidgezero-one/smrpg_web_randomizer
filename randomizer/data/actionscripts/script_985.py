from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_985_pause_0',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'ACTION_985_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_985_pause_2',
        "command": 'pause',
        "args": [48]
    },
    {
        "identifier": 'ACTION_985_reset_properties_3',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_985_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_985_shift_northeast_steps_5',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_985_set_bit_6',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_985_pause_7',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_985_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_985_pause_9',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_985_shift_southwest_steps_10',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_985_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_985_jmp_12',
        "command": 'jmp',
        "args": ['ACTION_985_pause_0']
    }
]
