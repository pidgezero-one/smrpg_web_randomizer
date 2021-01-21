from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_615_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x709f, 0, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_615_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 3, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_615_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 0, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_615_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 1, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_615_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7042, 5, 'EVENT_615_run_dialog_49']
    },
    {
        "identifier": 'EVENT_615_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_615_action_queue_async_5_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [16]
            },
            {
                "identifier": 'EVENT_615_action_queue_async_5_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._005_BLOCK_SWITCH, 6]
            }
        ]
    },
    {
        "identifier": 'EVENT_615_palette_set_6',
        "command": 'palette_set',
        "args": [89, 7]
    },
    {
        "identifier": 'EVENT_615_pause_7',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_615_fade_out_music_to_volume_8',
        "command": 'fade_out_music_to_volume',
        "args": [2, 0]
    },
    {
        "identifier": 'EVENT_615_circle_mask_static_9',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 18, 3]
    },
    {
        "identifier": 'EVENT_615_pause_10',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_615_play_sound_11',
        "command": 'play_sound',
        "args": [Sounds._054_GOODNIGHT, 6]
    },
    {
        "identifier": 'EVENT_615_pause_12',
        "command": 'pause',
        "args": [50]
    },
    {
        "identifier": 'EVENT_615_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_615_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [30, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_615_pause_14',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_615_circle_mask_static_15',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 0, 1]
    },
    {
        "identifier": 'EVENT_615_pause_script_until_effect_done_16',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_615_set_bit_17',
        "command": 'set_bit',
        "args": [0x7049, 5]
    },
    {
        "identifier": 'EVENT_615_enter_area_18',
        "command": 'enter_area',
        "args": [Rooms._012_MARRYMORE_INN_SUITE_ROOM, RadialDirections.SOUTH, 8, 13, 1, []]
    },
    {
        "identifier": 'EVENT_615_apply_tile_mod_19',
        "command": 'apply_tile_mod',
        "args": [Rooms._012_MARRYMORE_INN_SUITE_ROOM, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_615_restore_all_hp_20',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_615_restore_all_fp_21',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_615_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_615_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_615_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_615_action_queue_async_23_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 248, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_615_action_queue_async_23_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_615_pause_24',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'EVENT_615_play_sound_25',
        "command": 'play_sound',
        "args": [Sounds._015_NIGHT_CRICKETS, 6]
    },
    {
        "identifier": 'EVENT_615_pause_26',
        "command": 'pause',
        "args": [46]
    },
    {
        "identifier": 'EVENT_615_play_sound_27',
        "command": 'play_sound',
        "args": [Sounds._015_NIGHT_CRICKETS, 6]
    },
    {
        "identifier": 'EVENT_615_pause_28',
        "command": 'pause',
        "args": [23]
    },
    {
        "identifier": 'EVENT_615_play_sound_29',
        "command": 'play_sound',
        "args": [Sounds._015_NIGHT_CRICKETS, 6]
    },
    {
        "identifier": 'EVENT_615_pause_30',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_615_play_sound_31',
        "command": 'play_sound',
        "args": [Sounds._015_NIGHT_CRICKETS, 6]
    },
    {
        "identifier": 'EVENT_615_stop_sound_32',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_615_pause_33',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_615_fade_out_music_to_volume_34',
        "command": 'fade_out_music_to_volume',
        "args": [2, 96]
    },
    {
        "identifier": 'EVENT_615_circle_mask_static_35',
        "command": 'circle_mask_static',
        "args": [AreaObjects.MARIO, 255, 3]
    },
    {
        "identifier": 'EVENT_615_pause_script_until_effect_done_36',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_615_fade_out_music_to_volume_37',
        "command": 'fade_out_music_to_volume',
        "args": [2, 96]
    },
    {
        "identifier": 'EVENT_615_play_sound_38',
        "command": 'play_sound',
        "args": [Sounds._047_SNOOZE, 6]
    },
    {
        "identifier": 'EVENT_615_pause_39',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_615_stop_sound_40',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_615_action_queue_async_41',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_615_action_queue_async_41_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_615_run_event_as_subroutine_42',
        "command": 'run_event_as_subroutine',
        "args": [286]
    },
    {
        "identifier": 'EVENT_615_apply_tile_mod_43',
        "command": 'apply_tile_mod',
        "args": [Rooms._012_MARRYMORE_INN_SUITE_ROOM, 0, []]
    },
    {
        "identifier": 'EVENT_615_pause_action_script_44',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_615_action_queue_async_45',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_615_action_queue_async_45_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_615_action_queue_async_45_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_615_action_queue_async_45_SUBSCRIPT_walk_1_step_south_2',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_615_action_queue_async_45_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_615_action_queue_async_45_SUBSCRIPT_jmp_if_mario_in_air_4',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_615_action_queue_async_45_SUBSCRIPT_pause_3']
            },
            {
                "identifier": 'EVENT_615_action_queue_async_45_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._058_INSERT, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_615_clear_bit_46',
        "command": 'clear_bit',
        "args": [0x7049, 5]
    },
    {
        "identifier": 'EVENT_615_set_bit_47',
        "command": 'set_bit',
        "args": [0x7042, 5]
    },
    {
        "identifier": 'EVENT_615_ret_48',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_615_run_dialog_49',
        "command": 'run_dialog',
        "args": [990, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_615_run_dialog_50',
        "command": 'run_dialog',
        "args": [991, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_615_jmp_if_dialog_option_b_51',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_615_clear_bit_46']
    },
    {
        "identifier": 'EVENT_615_set_bit_52',
        "command": 'set_bit',
        "args": [0x7042, 6]
    },
    {
        "identifier": 'EVENT_615_set_short_mem_53',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac]
    },
    {
        "identifier": 'EVENT_615_jmp_if_var_equals_short_54',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 199, 'EVENT_615_set_bit_58']
    },
    {
        "identifier": 'EVENT_615_add_55',
        "command": 'add',
        "args": [0x70ac, 0x01]
    },
    {
        "identifier": 'EVENT_615_set_short_mem_56',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac]
    },
    {
        "identifier": 'EVENT_615_jmp_57',
        "command": 'jmp',
        "args": ['EVENT_615_action_queue_async_5']
    },
    {
        "identifier": 'EVENT_615_set_bit_58',
        "command": 'set_bit',
        "args": [0x709f, 6]
    },
    {
        "identifier": 'EVENT_615_set_59',
        "command": 'set',
        "args": [0x70ac, 199]
    },
    {
        "identifier": 'EVENT_615_jmp_60',
        "command": 'jmp',
        "args": ['EVENT_615_action_queue_async_5']
    }
]
