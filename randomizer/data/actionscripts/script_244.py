from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_244_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_244_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_244_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_244_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'ACTION_244_reset_properties_5']
    },
    {
        "identifier": 'ACTION_244_jmp_4',
        "command": 'jmp',
        "args": ['ACTION_244_pause_2']
    },
    {
        "identifier": 'ACTION_244_reset_properties_5',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_244_ret_6',
        "command": 'ret'
    }
]
