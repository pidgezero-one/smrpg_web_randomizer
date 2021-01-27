from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_7_object_memory_set_bit_0',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_7_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_7_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_7_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_7_db_4',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_7_db_5',
        "command": 'db',
        "args": [0x25, 0xc0, 0x03, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_7_pause_6',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_7_bpl_26_27_28_7',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_7_set_sprite_sequence_8',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_7_pause_9',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_7_set_sprite_sequence_10',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_7_db_11',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_7_db_12',
        "command": 'db',
        "args": [0x25, 0x40, 0x00, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_7_pause_13',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_7_bpl_26_27_28_14',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_7_set_sprite_sequence_15',
        "command": 'set_sprite_sequence',
        "args": [4, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_7_sequence_looping_off_16',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_7_ret_17',
        "command": 'ret'
    }
]
