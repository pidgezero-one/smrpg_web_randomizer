from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3508_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_async_0_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x0b, [3]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_set_short_1',
        "command": 'set_short',
        "args": [0x7024, 0x0000]
    },
    {
        "identifier": 'EVENT_3508_set_short_2',
        "command": 'set_short',
        "args": [0x7034, 0x0010]
    },
    {
        "identifier": 'EVENT_3508_set_short_3',
        "command": 'set_short',
        "args": [0x7026, 0x0001]
    },
    {
        "identifier": 'EVENT_3508_set_random_4',
        "command": 'set_random',
        "args": [0x702c, 6]
    },
    {
        "identifier": 'EVENT_3508_add_short_5',
        "command": 'add_short',
        "args": [0x702c, 0x01]
    },
    {
        "identifier": 'EVENT_3508_set_6',
        "command": 'set',
        "args": [0x70af, 3]
    },
    {
        "identifier": 'EVENT_3508_freeze_camera_7',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3508_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_sync_8_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 67, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.LAYER_3],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_sync_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_9_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [18]
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3508_jmp_if_bit_clear_11',
        "command": 'jmp_if_bit_clear',
        "args": [0x7086, 4, 'EVENT_3507_set_0']
    },
    {
        "identifier": 'EVENT_3508_jmp_if_bit_clear_12',
        "command": 'jmp_if_bit_clear',
        "args": [0x7086, 3, 'EVENT_3507_set_0']
    },
    {
        "identifier": 'EVENT_3508_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x704e, 1, 'EVENT_3507_set_0']
    },
    {
        "identifier": 'EVENT_3508_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_async_14_SUBSCRIPT_shadow_on_0',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_14_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_14_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_14_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_14_SUBSCRIPT_shift_z_down_pixels_5',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_14_SUBSCRIPT_shift_northwest_steps_6',
                "command": 'shift_northwest_steps',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_3508_set_17']
    },
    {
        "identifier": 'EVENT_3508_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_async_16_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_16_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_16_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_16_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_16_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_set_17',
        "command": 'set',
        "args": [0x70ae, 3]
    },
    {
        "identifier": 'EVENT_3508_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 707]
    },
    {
        "identifier": 'EVENT_3508_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 707]
    },
    {
        "identifier": 'EVENT_3508_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 707]
    },
    {
        "identifier": 'EVENT_3508_pause_21',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3508_freeze_all_npcs_until_return_22',
        "command": 'freeze_all_npcs_until_return'
    },
    {
        "identifier": 'EVENT_3508_palette_set_morphs_23',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 1]
    },
    {
        "identifier": 'EVENT_3508_palette_set_morphs_24',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 2]
    },
    {
        "identifier": 'EVENT_3508_palette_set_morphs_25',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 3]
    },
    {
        "identifier": 'EVENT_3508_palette_set_morphs_26',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 4]
    },
    {
        "identifier": 'EVENT_3508_palette_set_morphs_27',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 5]
    },
    {
        "identifier": 'EVENT_3508_palette_set_morphs_28',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 6]
    },
    {
        "identifier": 'EVENT_3508_palette_set_morphs_29',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 26, 7]
    },
    {
        "identifier": 'EVENT_3508_pause_30',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_3508_jmp_if_bit_set_31',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 2, 'EVENT_3508_play_sound_33']
    },
    {
        "identifier": 'EVENT_3508_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_async_32_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [11, 65, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_32_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_32_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_32_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_32_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_32_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_32_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [64]
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_play_sound_33',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_3508_run_dialog_34',
        "command": 'run_dialog',
        "args": [1191, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3508_jmp_if_dialog_option_b_35',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3508_run_dialog_duration_54']
    },
    {
        "identifier": 'EVENT_3508_run_dialog_36',
        "command": 'run_dialog',
        "args": [1183, AreaObjects.NPC_12, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3508_action_queue_async_37',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_async_37_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_37_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_37_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_37_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_37_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._003_MENU_SCROLL, 6]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_37_SUBSCRIPT_shift_northeast_pixels_5',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_37_SUBSCRIPT_end_loop_6',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_37_SUBSCRIPT_jump_to_height_7',
                "command": 'jump_to_height',
                "args": [107]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_37_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_37_SUBSCRIPT_start_loop_n_times_9',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_37_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._003_MENU_SCROLL, 6]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_37_SUBSCRIPT_shift_southwest_pixels_11',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_37_SUBSCRIPT_end_loop_12',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_37_SUBSCRIPT_start_loop_n_times_13',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_37_SUBSCRIPT_jump_to_height_14',
                "command": 'jump_to_height',
                "args": [107]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_37_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_37_SUBSCRIPT_end_loop_16',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_run_dialog_duration_38',
        "command": 'run_dialog_duration',
        "args": [1184, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3508_jmp_to_subroutine_39',
        "command": 'jmp_to_subroutine',
        "args": [0x74b8]
    },
    {
        "identifier": 'EVENT_3508_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_async_40_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [36]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_40_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._049_BIG_SHELL_HIT, 4]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_40_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_40_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_40_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [112]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_40_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_40_SUBSCRIPT_start_loop_n_times_6',
                "command": 'start_loop_n_times',
                "args": [15]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_40_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_40_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_40_SUBSCRIPT_visibility_on_9',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_40_SUBSCRIPT_shift_southeast_pixels_10',
                "command": 'shift_southeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_40_SUBSCRIPT_end_loop_11',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_40_SUBSCRIPT_reset_properties_12',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_40_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_40_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_40_SUBSCRIPT_shift_northwest_pixels_15',
                "command": 'shift_northwest_pixels',
                "args": [16]
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_action_queue_sync_41',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_sync_41_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_41_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._050_WATER_DROPLET, 4]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_41_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [56]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_41_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_41_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_41_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_41_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_41_SUBSCRIPT_shift_northwest_steps_7',
                "command": 'shift_northwest_steps',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_action_queue_async_42',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_async_42_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [84]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_42_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._049_BIG_SHELL_HIT, 4]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_42_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [112]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_42_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_42_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_42_SUBSCRIPT_start_loop_n_times_5',
                "command": 'start_loop_n_times',
                "args": [23]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_42_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_42_SUBSCRIPT_shift_southeast_pixels_7',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_42_SUBSCRIPT_visibility_on_8',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_42_SUBSCRIPT_shift_southeast_pixels_9',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_42_SUBSCRIPT_end_loop_10',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_42_SUBSCRIPT_reset_properties_11',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_42_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_42_SUBSCRIPT_transfer_to_xyzf_13',
                "command": 'transfer_to_xyzf',
                "args": [7, 59, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_action_queue_async_43',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_async_43_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_43_SUBSCRIPT_shift_xy_steps_1',
                "command": 'shift_xy_steps',
                "args": [3, 6]
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_run_dialog_duration_44',
        "command": 'run_dialog_duration',
        "args": [1185, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3508_action_queue_async_45',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_async_45_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_45_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_45_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_jmp_to_subroutine_46',
        "command": 'jmp_to_subroutine',
        "args": [0x74b8]
    },
    {
        "identifier": 'EVENT_3508_action_queue_async_47',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_async_47_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [17]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_47_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_47_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [23]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_47_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_47_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 4]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_47_SUBSCRIPT_floating_off_5',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_47_SUBSCRIPT_jump_to_height_silent_6',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_47_SUBSCRIPT_shift_northwest_pixels_7',
                "command": 'shift_northwest_pixels',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_47_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_47_SUBSCRIPT_transfer_to_xyzf_9',
                "command": 'transfer_to_xyzf',
                "args": [7, 59, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_run_dialog_duration_48',
        "command": 'run_dialog_duration',
        "args": [1192, DialogDurations.FOREVER, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3508_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_sync_49_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_49_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._050_WATER_DROPLET, 4]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_49_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [56]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_49_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_49_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_49_SUBSCRIPT_reset_properties_5',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_49_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_49_SUBSCRIPT_shift_northwest_steps_7',
                "command": 'shift_northwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_49_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_49_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_49_SUBSCRIPT_shift_southeast_steps_10',
                "command": 'shift_southeast_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_action_queue_async_50',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_async_50_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [72]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_50_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_50_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [23]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_50_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_50_SUBSCRIPT_play_sound_4',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 4]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_50_SUBSCRIPT_floating_off_5',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_50_SUBSCRIPT_jump_to_height_silent_6',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_50_SUBSCRIPT_shift_northwest_pixels_7',
                "command": 'shift_northwest_pixels',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_50_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_50_SUBSCRIPT_jmp_if_mario_in_air_9',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_3508_action_queue_async_50_SUBSCRIPT_pause_8']
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_50_SUBSCRIPT_jump_to_height_silent_10',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_50_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_action_queue_sync_51',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_sync_51_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._027_FOUND_AN_ITEM, 4]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_51_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_51_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_51_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_51_SUBSCRIPT_start_loop_n_times_4',
                "command": 'start_loop_n_times',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_51_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_51_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_51_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_51_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_51_SUBSCRIPT_end_loop_9',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_51_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [73]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_51_SUBSCRIPT_transfer_to_xyzf_11',
                "command": 'transfer_to_xyzf',
                "args": [6, 57, 5, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_51_SUBSCRIPT_visibility_on_12',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_51_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_sync_52_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [100]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_52_SUBSCRIPT_shift_xy_steps_1',
                "command": 'shift_xy_steps',
                "args": [254, 252]
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_action_queue_async_53',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_async_53_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [100]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_53_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [7, 59, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_53_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_run_dialog_duration_54',
        "command": 'run_dialog_duration',
        "args": [1187, DialogDurations.SHORT, [_0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_3508_play_sound_55',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_3508_fade_out_music_to_volume_56',
        "command": 'fade_out_music_to_volume',
        "args": [2, 0]
    },
    {
        "identifier": 'EVENT_3508_action_queue_async_57',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_async_57_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_57_SUBSCRIPT_shift_southeast_steps_1',
                "command": 'shift_southeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_57_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_palette_set_morphs_58',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 97, 1]
    },
    {
        "identifier": 'EVENT_3508_palette_set_morphs_59',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 98, 2]
    },
    {
        "identifier": 'EVENT_3508_palette_set_morphs_60',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 99, 3]
    },
    {
        "identifier": 'EVENT_3508_palette_set_morphs_61',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 100, 4]
    },
    {
        "identifier": 'EVENT_3508_palette_set_morphs_62',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 101, 5]
    },
    {
        "identifier": 'EVENT_3508_palette_set_morphs_63',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 102, 6]
    },
    {
        "identifier": 'EVENT_3508_palette_set_morphs_64',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 103, 7]
    },
    {
        "identifier": 'EVENT_3508_unfreeze_all_npcs_65',
        "command": 'unfreeze_all_npcs'
    },
    {
        "identifier": 'EVENT_3508_action_queue_async_66',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_async_66_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_async_66_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [9]
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_set_67',
        "command": 'set',
        "args": [0x70b2, 0]
    },
    {
        "identifier": 'EVENT_3508_run_background_event_68',
        "command": 'run_background_event',
        "args": [3500, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_3508_run_background_event_69',
        "command": 'run_background_event',
        "args": [3503, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_6]]
    },
    {
        "identifier": 'EVENT_3508_set_action_script_sync_70',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.LAYER_1, 704]
    },
    {
        "identifier": 'EVENT_3508_set_action_script_sync_71',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.LAYER_2, 655]
    },
    {
        "identifier": 'EVENT_3508_set_action_script_sync_72',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.LAYER_3, 705]
    },
    {
        "identifier": 'EVENT_3508_set_short_73',
        "command": 'set_short',
        "args": [0x701e, 0x0190]
    },
    {
        "identifier": 'EVENT_3508_run_background_event_with_pause_return_on_exit_74',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [1551, 0x701e, [12, 13]]
    },
    {
        "identifier": 'EVENT_3508_set_action_script_sync_75',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 352]
    },
    {
        "identifier": 'EVENT_3508_clear_bit_76',
        "command": 'clear_bit',
        "args": [0x707b, 4]
    },
    {
        "identifier": 'EVENT_3508_play_music_default_volume_77',
        "command": 'play_music_default_volume',
        "args": [Music._38_BOOSTER_HILL]
    },
    {
        "identifier": 'EVENT_3508_run_event_at_return_78',
        "command": 'run_event_at_return',
        "args": [3502]
    },
    {
        "identifier": 'EVENT_3508_ret_79',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3508_action_queue_sync_80',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_sync_80_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_80_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [5, 54, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_80_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_80_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_80_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_80_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_80_SUBSCRIPT_shift_southwest_pixels_6',
                "command": 'shift_southwest_pixels',
                "args": [36]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_80_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._049_BIG_SHELL_HIT, 4]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_80_SUBSCRIPT_visibility_on_8',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_80_SUBSCRIPT_jump_to_height_9',
                "command": 'jump_to_height',
                "args": [24]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_80_SUBSCRIPT_walk_1_step_southeast_10',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_80_SUBSCRIPT_set_700C_to_object_coord_11',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.DUMMY_0X07, Coords.X, CoordUnits.PIXEL]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_80_SUBSCRIPT_mem_compare_12',
                "command": 'mem_compare',
                "args": [0x700c, 5888]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_80_SUBSCRIPT_jmp_if_comparison_result_is_lesser_13',
                "command": 'jmp_if_comparison_result_is_lesser',
                "args": ['EVENT_3508_action_queue_sync_80_SUBSCRIPT_jump_to_height_9']
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_action_queue_sync_81',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3508_action_queue_sync_81_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_3508_action_queue_sync_81_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [112]
            }
        ]
    },
    {
        "identifier": 'EVENT_3508_ret_82',
        "command": 'ret'
    }
]
