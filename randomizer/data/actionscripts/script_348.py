from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_348_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_348_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_348_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_348_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_348_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 7, 'ACTION_348_pause_3']
    },
    {
        "identifier": 'ACTION_348_reset_properties_5',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_348_sequence_looping_off_6',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_348_ret_7',
        "command": 'ret'
    }
]
