from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_940_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._121_AXEM_RANGER_TELEPORT, 4]
    },
    {
        "identifier": 'ACTION_940_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 0, 'ACTION_940_set_sprite_sequence_5']
    },
    {
        "identifier": 'ACTION_940_set_sprite_sequence_2',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_940_pause_3',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_940_ret_4',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_940_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_940_pause_6',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_940_ret_7',
        "command": 'ret'
    }
]
