from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_8_object_memory_set_bit_0',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_8_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_8_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_8_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_8_db_4',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_8_db_5',
        "command": 'db',
        "args": [0x25, 0xc0, 0x03, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_8_pause_6',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_8_bpl_26_27_28_7',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_8_set_sprite_sequence_8',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_8_db_9',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_8_db_10',
        "command": 'db',
        "args": [0x25, 0x40, 0x00, 0x80, 0xff]
    },
    {
        "identifier": 'ACTION_8_pause_11',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_8_bpl_26_27_28_12',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_8_set_sprite_sequence_13',
        "command": 'set_sprite_sequence',
        "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_8_sequence_looping_off_14',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_8_pause_15',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_8_object_memory_clear_bit_16',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_8_ret_17',
        "command": 'ret'
    }
]
