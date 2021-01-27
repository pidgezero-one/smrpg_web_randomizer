from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_912_floating_off_0',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_912_visibility_off_1',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_912_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_912_pause_3',
        "command": 'pause',
        "args": [9]
    },
    {
        "identifier": 'ACTION_912_visibility_on_4',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_912_pause_5',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_912_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7064, 6, 'ACTION_912_pause_5']
    },
    {
        "identifier": 'ACTION_912_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'ACTION_912_pause_10']
    },
    {
        "identifier": 'ACTION_912_set_sprite_sequence_8',
        "command": 'set_sprite_sequence',
        "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_912_pause_9',
        "command": 'pause',
        "args": [18]
    },
    {
        "identifier": 'ACTION_912_pause_10',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_912_visibility_off_11',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_912_ret_12',
        "command": 'ret'
    }
]
