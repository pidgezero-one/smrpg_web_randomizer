from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2114_fade_out_music_to_volume_0',
        "command": 'fade_out_music_to_volume',
        "args": [0, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_play_music_default_volume_1',
        "command": 'play_music_default_volume',
        "args": [Music._01_DODOS_COMING],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_stop_music_2',
        "command": 'stop_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_run_dialog_3',
        "command": 'run_dialog',
        "args": [3360, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_4',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_enable_controls_until_return_5',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_6',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_7',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_play_sound_8',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_9',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_enable_controls_until_return_10',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_11',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_play_music_default_volume_12',
        "command": 'play_music_default_volume',
        "args": [Music._01_DODOS_COMING],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_13',
        "command": 'pause',
        "args": [143],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_14',
        "command": 'pause',
        "args": [235],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_15',
        "command": 'pause',
        "args": [118],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2114_action_queue_async_16_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [2, 56]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_16_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_16_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_16_SUBSCRIPT_sequence_playback_off_3',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_16_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_16_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_16_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [31]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_16_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_16_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [31]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_16_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_16_SUBSCRIPT_sequence_playback_on_10',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_16_SUBSCRIPT_sequence_looping_on_11',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_16_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_16_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [66]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_16_SUBSCRIPT_sequence_looping_off_14',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_16_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_16_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [17]
            }
        ]
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_17',
        "command": 'jmp_to_subroutine',
        "args": [0x7b0d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_18',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_19',
        "command": 'jmp_to_subroutine',
        "args": [0x7b1e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_20',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_21',
        "command": 'jmp_to_subroutine',
        "args": [0x7b0d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_22',
        "command": 'jmp_to_subroutine',
        "args": [0x7b51],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_23',
        "command": 'jmp_to_subroutine',
        "args": [0x79ef],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_24',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_25',
        "command": 'jmp_to_subroutine',
        "args": [0x7b0d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_26',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_27',
        "command": 'jmp_to_subroutine',
        "args": [0x7b1e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_28',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_29',
        "command": 'jmp_to_subroutine',
        "args": [0x7b0d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_30',
        "command": 'jmp_to_subroutine',
        "args": [0x7b51],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_31',
        "command": 'jmp_to_subroutine',
        "args": [0x79fd],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_32',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_33',
        "command": 'jmp_to_subroutine',
        "args": [0x7b0d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_34',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_35',
        "command": 'jmp_to_subroutine',
        "args": [0x7b1e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_36',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_37',
        "command": 'jmp_to_subroutine',
        "args": [0x7b0d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2114_action_queue_async_38_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_38_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2114_set_short_39',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_clear_bit_40',
        "command": 'clear_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_start_loop_n_times_41',
        "command": 'start_loop_n_times',
        "args": [18],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_42',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_7000_to_tapped_button_43',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_if_7000_all_bits_clear_44',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_2114_end_loop_46'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_bit_45',
        "command": 'set_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_end_loop_46',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_if_bit_set_47',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 7, 'EVENT_2120_stop_music_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2114_action_queue_sync_48_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_sync_48_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_sync_48_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_sync_48_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_sync_48_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2114_action_queue_sync_48_SUBSCRIPT_sequence_looping_off_5',
                "command": 'sequence_looping_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2114_clear_bit_49',
        "command": 'clear_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_short_50',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_start_loop_n_times_51',
        "command": 'start_loop_n_times',
        "args": [22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_52',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_7000_to_tapped_button_53',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_if_7000_all_bits_clear_54',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_2114_end_loop_56'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_bit_55',
        "command": 'set_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_end_loop_56',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_if_bit_clear_57',
        "command": 'jmp_if_bit_clear',
        "args": [0x708a, 7, 'EVENT_2121_stop_music_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_short_58',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_59',
        "command": 'pause',
        "args": [17],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_60',
        "command": 'jmp_to_subroutine',
        "args": [0x7b0d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_61',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_62',
        "command": 'jmp_to_subroutine',
        "args": [0x7b1e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_63',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_64',
        "command": 'jmp_to_subroutine',
        "args": [0x7b0d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_65',
        "command": 'pause',
        "args": [74],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_action_queue_async_66',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [25]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [36]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_sequence_looping_on_12',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_start_loop_n_times_13',
                "command": 'start_loop_n_times',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_end_loop_18',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [50]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_set_sprite_sequence_21',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_66_SUBSCRIPT_sequence_looping_off_22',
                "command": 'sequence_looping_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2114_pause_67',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_short_68',
        "command": 'set_short',
        "args": [0x7024, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_short_69',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_clear_bit_70',
        "command": 'clear_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_start_loop_n_times_71',
        "command": 'start_loop_n_times',
        "args": [17],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_72',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_7000_to_tapped_button_73',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_if_7000_all_bits_clear_74',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_2114_end_loop_76'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_bit_75',
        "command": 'set_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_end_loop_76',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_if_bit_set_77',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 7, 'EVENT_2120_stop_music_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_add_short_78',
        "command": 'add_short',
        "args": [0x7024, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_if_var_not_equals_short_79',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7024, 7, 'EVENT_2114_set_short_69'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_action_queue_async_80',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2114_action_queue_async_80_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_80_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2114_pause_81',
        "command": 'pause',
        "args": [18],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_82',
        "command": 'jmp_to_subroutine',
        "args": [0x7b0d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_83',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_84',
        "command": 'jmp_to_subroutine',
        "args": [0x7b1e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_85',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_86',
        "command": 'jmp_to_subroutine',
        "args": [0x7b0d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_87',
        "command": 'jmp_to_subroutine',
        "args": [0x7b51],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_88',
        "command": 'jmp_to_subroutine',
        "args": [0x7a0b],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_89',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_90',
        "command": 'jmp_to_subroutine',
        "args": [0x7b2f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_91',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_92',
        "command": 'jmp_to_subroutine',
        "args": [0x7b40],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_93',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_94',
        "command": 'jmp_to_subroutine',
        "args": [0x7b2f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_action_queue_async_95',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2114_action_queue_async_95_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_95_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2114_set_short_96',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_clear_bit_97',
        "command": 'clear_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_start_loop_n_times_98',
        "command": 'start_loop_n_times',
        "args": [18],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_99',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_7000_to_tapped_button_100',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_if_7000_all_bits_clear_101',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_2114_end_loop_103'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_bit_102',
        "command": 'set_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_end_loop_103',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_if_bit_set_104',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 7, 'EVENT_2120_stop_music_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_action_queue_sync_105',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2114_action_queue_sync_105_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_sync_105_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_sync_105_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_sync_105_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_sync_105_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2114_action_queue_sync_105_SUBSCRIPT_sequence_looping_off_5',
                "command": 'sequence_looping_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2114_clear_bit_106',
        "command": 'clear_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_short_107',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_start_loop_n_times_108',
        "command": 'start_loop_n_times',
        "args": [22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_109',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_7000_to_tapped_button_110',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_if_7000_all_bits_clear_111',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_2114_end_loop_113'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_bit_112',
        "command": 'set_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_end_loop_113',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_if_bit_clear_114',
        "command": 'jmp_if_bit_clear',
        "args": [0x708a, 7, 'EVENT_2121_stop_music_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_short_115',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_116',
        "command": 'pause',
        "args": [18],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_117',
        "command": 'jmp_to_subroutine',
        "args": [0x7b40],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_118',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_119',
        "command": 'jmp_to_subroutine',
        "args": [0x7b2f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_120',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_121',
        "command": 'jmp_to_subroutine',
        "args": [0x7b40],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_122',
        "command": 'jmp_to_subroutine',
        "args": [0x7b51],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_123',
        "command": 'jmp_to_subroutine',
        "args": [0x79fd],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_action_queue_async_124',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2114_action_queue_async_124_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_124_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [23]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_124_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_124_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_124_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_124_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_124_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_124_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_124_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_124_SUBSCRIPT_shift_southeast_steps_9',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_124_SUBSCRIPT_ret_10',
                "command": 'ret',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2114_action_queue_async_125',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2114_action_queue_async_125_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_125_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2114_set_short_126',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_clear_bit_127',
        "command": 'clear_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_start_loop_n_times_128',
        "command": 'start_loop_n_times',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_129',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_7000_to_tapped_button_130',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_if_7000_all_bits_clear_131',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_2114_end_loop_133'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_bit_132',
        "command": 'set_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_end_loop_133',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_if_bit_set_134',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 7, 'EVENT_2120_stop_music_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_action_queue_sync_135',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2114_action_queue_sync_135_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_sync_135_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_sync_135_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_sync_135_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_sync_135_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2114_action_queue_sync_135_SUBSCRIPT_sequence_looping_off_5',
                "command": 'sequence_looping_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2114_clear_bit_136',
        "command": 'clear_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_short_137',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_start_loop_n_times_138',
        "command": 'start_loop_n_times',
        "args": [22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_139',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_7000_to_tapped_button_140',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_if_7000_all_bits_clear_141',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_2114_end_loop_143'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_bit_142',
        "command": 'set_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_end_loop_143',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_if_bit_clear_144',
        "command": 'jmp_if_bit_clear',
        "args": [0x708a, 7, 'EVENT_2121_stop_music_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_short_145',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_146',
        "command": 'pause',
        "args": [17],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_147',
        "command": 'jmp_to_subroutine',
        "args": [0x7b0d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_148',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_149',
        "command": 'jmp_to_subroutine',
        "args": [0x7b1e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_150',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_151',
        "command": 'jmp_to_subroutine',
        "args": [0x7b0d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_152',
        "command": 'jmp_to_subroutine',
        "args": [0x7b51],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_153',
        "command": 'jmp_to_subroutine',
        "args": [0x7a0b],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_154',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_155',
        "command": 'jmp_to_subroutine',
        "args": [0x7b2f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_156',
        "command": 'pause',
        "args": [13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_157',
        "command": 'jmp_to_subroutine',
        "args": [0x7b40],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_158',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_to_subroutine_159',
        "command": 'jmp_to_subroutine',
        "args": [0x7b2f],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_action_queue_async_160',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_sequence_playback_on_1',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [9]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_sequence_playback_off_8',
                "command": 'sequence_playback_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_sequence_looping_off_10',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_face_northwest_11',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_sequence_playback_on_16',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_shift_northwest_steps_19',
                "command": 'shift_northwest_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_set_animation_speed_20',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_set_animation_speed_21',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_shift_northwest_steps_22',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_visibility_off_23',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_sequence_looping_off_24',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_pause_25',
                "command": 'pause',
                "args": [9]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_clear_solidity_bits_26',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_pause_27',
                "command": 'pause',
                "args": [38]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_shirt_to_xy_coords_28',
                "command": 'shirt_to_xy_coords',
                "args": [127, 66]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_visibility_on_29',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_set_sprite_sequence_30',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_shift_southeast_steps_31',
                "command": 'shift_southeast_steps',
                "args": [14]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_pause_32',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_shirt_to_xy_coords_33',
                "command": 'shirt_to_xy_coords',
                "args": [11, 75]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_shift_southwest_pixels_34',
                "command": 'shift_southwest_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_set_sprite_sequence_35',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_face_northwest_36',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_visibility_on_37',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_shift_northwest_steps_38',
                "command": 'shift_northwest_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_face_southwest_39',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_set_sprite_sequence_40',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_160_SUBSCRIPT_sequence_looping_off_41',
                "command": 'sequence_looping_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2114_pause_161',
        "command": 'pause',
        "args": [25],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_action_queue_sync_162',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2114_action_queue_sync_162_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_sync_162_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_sync_162_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_sync_162_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_sync_162_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2114_action_queue_sync_162_SUBSCRIPT_sequence_looping_off_5',
                "command": 'sequence_looping_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2114_clear_bit_163',
        "command": 'clear_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_short_164',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_start_loop_n_times_165',
        "command": 'start_loop_n_times',
        "args": [22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_166',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_7000_to_tapped_button_167',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_if_7000_all_bits_clear_168',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_2114_end_loop_170'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_bit_169',
        "command": 'set_bit',
        "args": [0x708a, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_end_loop_170',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_jmp_if_bit_clear_171',
        "command": 'jmp_if_bit_clear',
        "args": [0x708a, 7, 'EVENT_2120_stop_music_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_short_172',
        "command": 'set_short',
        "args": [0x7000, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_173',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_enable_controls_until_return_174',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_clear_bit_175',
        "command": 'clear_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_clear_bit_176',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_action_queue_async_177',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2114_action_queue_async_177_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_177_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_177_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_177_SUBSCRIPT_sequence_looping_off_3',
                "command": 'sequence_looping_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2114_pause_178',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_action_queue_async_179',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2114_action_queue_async_179_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_179_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_179_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_179_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_179_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [11]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_179_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2114_pause_180',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_play_sound_181',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_pause_182',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_action_queue_async_183',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2114_action_queue_async_183_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_183_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_183_SUBSCRIPT_face_south_2',
                "command": 'face_south',
                "args": []
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_183_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=2, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2114_action_queue_async_183_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [60]
            }
        ]
    },
    {
        "identifier": 'EVENT_2114_set_action_script_async_184',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_set_bit_185',
        "command": 'set_bit',
        "args": [0x7092, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_remove_from_level_186',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_unfreeze_camera_187',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2114_ret_188',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
