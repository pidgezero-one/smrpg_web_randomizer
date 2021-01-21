from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_775_set_700C_to_pressed_button_0',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_775_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x700c, 20, 'ACTION_775_set_short_11']
    },
    {
        "identifier": 'ACTION_775_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._105_SURPRISE, 4]
    },
    {
        "identifier": 'ACTION_775_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_775_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_775_jump_to_height_silent_5',
        "command": 'jump_to_height_silent',
        "args": [112]
    },
    {
        "identifier": 'ACTION_775_shift_southwest_pixels_6',
        "command": 'shift_southwest_pixels',
        "args": [1]
    },
    {
        "identifier": 'ACTION_775_shift_west_pixels_7',
        "command": 'shift_west_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_775_jmp_if_mario_in_air_8',
        "command": 'jmp_if_mario_in_air',
        "args": ['ACTION_775_shift_west_pixels_7']
    },
    {
        "identifier": 'ACTION_775_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._084_SMOKED, 4]
    },
    {
        "identifier": 'ACTION_775_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_775_jump_to_height_silent_5']
    },
    {
        "identifier": 'ACTION_775_set_short_11',
        "command": 'set_short',
        "args": [0x7034, 0xffff]
    },
    {
        "identifier": 'ACTION_775_db_12',
        "command": 'db',
        "args": [0xc7, 0x00]
    },
    {
        "identifier": 'ACTION_775_create_packet_at_7010_coords_jmp_if_null_13',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._032_BLUE_CLOUD, 'ACTION_775_pause_14']
    },
    {
        "identifier": 'ACTION_775_pause_14',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'ACTION_775_jmp_15',
        "command": 'jmp',
        "args": ['ACTION_775_set_short_11']
    }
]
