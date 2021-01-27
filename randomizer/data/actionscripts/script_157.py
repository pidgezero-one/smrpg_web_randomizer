from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_157_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_157_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'ACTION_157_set_sprite_sequence_3']
    },
    {
        "identifier": 'ACTION_157_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._050_WATER_DROPLET, 4]
    },
    {
        "identifier": 'ACTION_157_set_sprite_sequence_3',
        "command": 'set_sprite_sequence',
        "args": [10, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_157_pause_4',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'ACTION_157_visibility_off_5',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_157_ret_6',
        "command": 'ret'
    }
]
