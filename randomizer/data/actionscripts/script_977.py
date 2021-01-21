from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_977_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x704b, 7, 'ACTION_977_set_sprite_sequence_3']
    },
    {
        "identifier": 'ACTION_977_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_977_jmp_2',
        "command": 'jmp',
        "args": ['ACTION_977_set_priority_4']
    },
    {
        "identifier": 'ACTION_977_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_977_set_priority_4',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_977_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x704b, 7]
    },
    {
        "identifier": 'ACTION_977_ret_6',
        "command": 'ret'
    }
]
