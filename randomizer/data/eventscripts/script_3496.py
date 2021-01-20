from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3496_set_short_mem_0',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x7034, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_pause_2',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_jmp_if_bit_clear_3',
        "command": 'jmp_if_bit_clear',
        "args": [0x707b, 5, 'EVENT_3496_pause_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_pause_4',
        "command": 'pause',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_pause_action_script_5',
        "command": 'pause_action_script',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_pause_action_script_6',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3496_action_queue_sync_7_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3496_action_queue_sync_7_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3496_action_queue_sync_7_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3496_action_queue_sync_7_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3496_action_queue_sync_7_SUBSCRIPT_shift_north_pixels_4',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3496_action_queue_sync_7_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3496_action_queue_sync_7_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3496_action_queue_sync_7_SUBSCRIPT_jmp_if_var_equals_short_7',
                "command": 'jmp_if_var_equals_short',
                "args": [0x7034, 0, 'EVENT_3496_action_queue_sync_8']
            },
            {
                "identifier": 'EVENT_3496_action_queue_sync_7_SUBSCRIPT_play_sound_8',
                "command": 'play_sound',
                "args": [Sounds._055_LOSE_COINS_COIN_FOUNTAIN, 6]
            }
        ]
    },
    {
        "identifier": 'EVENT_3496_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3496_action_queue_sync_8_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._065_THWOMP_STOMP, 4]
            },
            {
                "identifier": 'EVENT_3496_action_queue_sync_8_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3496_action_queue_sync_8_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [144]
            }
        ]
    },
    {
        "identifier": 'EVENT_3496_set_short_9',
        "command": 'set_short',
        "args": [0x700c, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_start_loop_n_times_10',
        "command": 'start_loop_n_times',
        "args": [7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_set_short_mem_11',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_jmp_if_var_equals_short_12',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_3496_pause_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_create_packet_at_object_coords_jmp_if_null_13',
        "command": 'create_packet_at_object_coords_jmp_if_null',
        "args": [NPCPackets._017_SMALL_COIN_NOT_MOVING, AreaObjects.MARIO, 'EVENT_3496_pause_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_dec_short_14',
        "command": 'dec_short',
        "args": [0x702a],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_pause_15',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_add_short_16',
        "command": 'add_short',
        "args": [0x700c, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_end_loop_17',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_pause_18',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_jmp_if_mario_in_air_19',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3496_pause_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3496_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=3, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_3496_action_queue_async_20_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3496_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3496_resume_action_script_21',
        "command": 'resume_action_script',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_resume_action_script_22',
        "command": 'resume_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_clear_bit_23',
        "command": 'clear_bit',
        "args": [0x707b, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_set_bit_24',
        "command": 'set_bit',
        "args": [0x7078, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3496_ret_25',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
