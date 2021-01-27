from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_817_set_700C_to_current_level_0',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_817_jmp_if_700C_equals_short_1',
        "command": 'jmp_if_700C_equals_short',
        "args": [457, 'ACTION_817_set_sprite_sequence_6']
    },
    {
        "identifier": 'ACTION_817_set_priority_2',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_817_sequence_looping_off_3',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_817_fixed_f_coord_on_4',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_817_ret_5',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_817_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_817_sequence_looping_off_7',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_817_fixed_f_coord_on_8',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_817_ret_9',
        "command": 'ret'
    }
]
