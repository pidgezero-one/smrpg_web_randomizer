from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1685_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7050, 6, 'EVENT_1685_ret_45'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_set_7000_to_tapped_button_1',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_jmp_if_7000_all_bits_clear_2',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_1685_ret_45'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1685_action_queue_sync_3_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [64]
            }
        ]
    },
    {
        "identifier": 'EVENT_1685_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_1685_ret_45'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_pause_5',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_jmp_if_mario_in_air_6',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1685_pause_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._154_BIG_SQUISH, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_pause_8',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_store_02_to_0248_9',
        "command": 'store_02_to_0248',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_apply_tile_mod_10',
        "command": 'apply_tile_mod',
        "args": [Rooms._420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM, 32, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_store_00_to_0248_11',
        "command": 'store_00_to_0248',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_pause_12',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_set_bit_13',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_jmp_if_var_not_equals_short_14',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7024, 0, 'EVENT_1685_jmp_if_var_not_equals_short_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_set_short_15',
        "command": 'set_short',
        "args": [0x7024, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_set_short_mem_16',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_add_17',
        "command": 'add',
        "args": [0x7000, 16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_set_short_mem_18',
        "command": 'set_short_mem',
        "args": [0x70ac, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_jmp_19',
        "command": 'jmp',
        "args": ['EVENT_1685_set_short_mem_39'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_jmp_if_var_not_equals_short_20',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7026, 0, 'EVENT_1685_set_short_mem_26'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_set_short_21',
        "command": 'set_short',
        "args": [0x7026, 0x0004],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_set_short_mem_22',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_add_23',
        "command": 'add',
        "args": [0x7000, 16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_set_short_mem_24',
        "command": 'set_short_mem',
        "args": [0x70ac, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_1685_set_short_mem_39'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_set_short_mem_26',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_add_27',
        "command": 'add',
        "args": [0x7000, 16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_set_short_mem_28',
        "command": 'set_short_mem',
        "args": [0x70ac, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_set_29',
        "command": 'set',
        "args": [0x70ab, 24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_run_event_as_subroutine_30',
        "command": 'run_event_as_subroutine',
        "args": [1739],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_action_queue_sync_31',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1685_action_queue_sync_31_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_31_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_31_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_31_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_31_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_31_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_31_SUBSCRIPT_floating_on_6',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_31_SUBSCRIPT_jump_to_height_7',
                "command": 'jump_to_height',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_31_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_31_SUBSCRIPT_db_9',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x14, 0x69]
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_31_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._109_BIG_SHELL_HIT, 4]
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_31_SUBSCRIPT_shift_north_pixels_11',
                "command": 'shift_north_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_1685_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1685_action_queue_sync_32_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_32_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_32_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_32_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_32_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_32_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_32_SUBSCRIPT_floating_on_6',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_32_SUBSCRIPT_jump_to_height_7',
                "command": 'jump_to_height',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_32_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_32_SUBSCRIPT_db_9',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x15, 0x84]
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_32_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._109_BIG_SHELL_HIT, 4]
            },
            {
                "identifier": 'EVENT_1685_action_queue_sync_32_SUBSCRIPT_shift_north_pixels_11',
                "command": 'shift_north_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_1685_action_queue_async_33',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1685_action_queue_async_33_SUBSCRIPT_inc_palette_row_by_0',
                "command": 'inc_palette_row_by',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1685_action_queue_async_33_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1685_action_queue_async_33_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1685_action_queue_async_33_SUBSCRIPT_floating_on_3',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1685_action_queue_async_33_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_1685_set_34',
        "command": 'set',
        "args": [0x70ab, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_run_event_as_subroutine_35',
        "command": 'run_event_as_subroutine',
        "args": [1739],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_set_bit_36',
        "command": 'set_bit',
        "args": [0x7050, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_set_bit_37',
        "command": 'set_bit',
        "args": [0x7094, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_clear_bit_38',
        "command": 'clear_bit',
        "args": [0x704f, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_set_short_mem_39',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_add_short_mem_40',
        "command": 'add_short_mem',
        "args": [0x7000, 0x7026],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_set_short_mem_41',
        "command": 'set_short_mem',
        "args": [0x7028, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_set_short_mem_42',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_mem_7000_or_var_43',
        "command": 'mem_7000_or_var',
        "args": [0x7028],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_set_short_mem_44',
        "command": 'set_short_mem',
        "args": [0x70ac, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1685_ret_45',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
