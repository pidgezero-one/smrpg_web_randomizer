from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_798_jmp_if_random_above_66_0',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_799_set_animation_speed_0']
    },
    {
        "identifier": 'ACTION_798_set_sprite_sequence_1',
        "command": 'set_sprite_sequence',
        "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_798_jump_to_height_silent_2',
        "command": 'jump_to_height_silent',
        "args": [80]
    },
    {
        "identifier": 'ACTION_798_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_798_jmp_if_mario_in_air_4',
        "command": 'jmp_if_mario_in_air',
        "args": ['ACTION_798_pause_3']
    },
    {
        "identifier": 'ACTION_798_jump_to_height_silent_5',
        "command": 'jump_to_height_silent',
        "args": [80]
    },
    {
        "identifier": 'ACTION_798_pause_6',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_798_jmp_if_mario_in_air_7',
        "command": 'jmp_if_mario_in_air',
        "args": ['ACTION_798_pause_6']
    },
    {
        "identifier": 'ACTION_798_jump_to_height_silent_8',
        "command": 'jump_to_height_silent',
        "args": [80]
    },
    {
        "identifier": 'ACTION_798_pause_9',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_798_jmp_if_mario_in_air_10',
        "command": 'jmp_if_mario_in_air',
        "args": ['ACTION_798_pause_9']
    },
    {
        "identifier": 'ACTION_798_reset_properties_11',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_798_face_northwest_12',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_798_ret_13',
        "command": 'ret'
    }
]
