from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_82_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_82_visibility_on_1',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_82_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'ACTION_82_set_sprite_sequence_4']
    },
    {
        "identifier": 'ACTION_82_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._050_WATER_DROPLET, 4]
    },
    {
        "identifier": 'ACTION_82_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_82_pause_5',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_82_set_sprite_sequence_6',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_82_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_154_fixed_f_coord_on_0']
    },
    {
        "identifier": 'ACTION_82_ret_8',
        "command": 'ret'
    }
]
