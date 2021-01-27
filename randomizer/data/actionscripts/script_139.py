from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_139_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._047_SNOOZE, 6]
    },
    {
        "identifier": 'ACTION_139_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [27, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_139_pause_2',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_139_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [28, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_139_pause_4',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_139_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [29, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_139_pause_6',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_139_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_139_play_sound_0']
    }
]
