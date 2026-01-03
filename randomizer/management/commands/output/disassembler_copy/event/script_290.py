
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_290_set_bit_0',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_290_set_7010_to_object_xyz_1',
        "command": 'set_7010_to_object_xyz',
        "args": [0x80]
    },
    {
        "identifier": 'EVENT_290_mem_compare_2',
        "command": 'mem_compare',
        "args": [0x7014, 5]
    },
    {
        "identifier": 'EVENT_290_jmp_if_comparison_result_is_greater_or_equal_3',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_338_run_dialog_9']
    },
    {
        "identifier": 'EVENT_290_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_async_4_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_290_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_290_jmp_if_bit_clear_98']
    },
    {
        "identifier": 'EVENT_290_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 7, 'EVENT_290_jmp_if_bit_clear_62']
    },
    {
        "identifier": 'EVENT_290_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 3, 'EVENT_290_jmp_if_bit_set_13']
    },
    {
        "identifier": 'EVENT_290_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 6, 'EVENT_290_set_bit_21']
    },
    {
        "identifier": 'EVENT_290_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 0, 'EVENT_290_jmp_if_bit_set_13']
    },
    {
        "identifier": 'EVENT_290_set_bit_10',
        "command": 'set_bit',
        "args": [0x7081, 0]
    },
    {
        "identifier": 'EVENT_290_run_dialog_11',
        "command": 'run_dialog',
        "args": [542, AreaObjects.NPC_1, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_290_jmp_12',
        "command": 'jmp',
        "args": ['EVENT_290_run_dialog_15']
    },
    {
        "identifier": 'EVENT_290_jmp_if_bit_set_13',
        "command": 'jmp_if_bit_set',
        "args": [0x7081, 5, 'EVENT_290_run_dialog_19']
    },
    {
        "identifier": 'EVENT_290_run_dialog_14',
        "command": 'run_dialog',
        "args": [543, AreaObjects.NPC_1, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_290_run_dialog_15',
        "command": 'run_dialog',
        "args": [544, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_290_open_shop_16',
        "command": 'open_shop',
        "args": [Shops._00_MUSHROOM_KINGDOM]
    },
    {
        "identifier": 'EVENT_290_fade_in_from_black_async_17',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_290_ret_18',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_290_run_dialog_19',
        "command": 'run_dialog',
        "args": [610, AreaObjects.NPC_1, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_290_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_290_run_dialog_15']
    },
    {
        "identifier": 'EVENT_290_set_bit_21',
        "command": 'set_bit',
        "args": [0x7082, 3]
    },
    {
        "identifier": 'EVENT_290_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_async_22_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_290_action_queue_async_22_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [14, 20]
            },
            {
                "identifier": 'EVENT_290_action_queue_async_22_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_290_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_async_23_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_290_action_queue_async_23_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [14, 20, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_290_action_queue_async_23_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_290_action_queue_async_23_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_290_action_queue_async_23_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_290_action_queue_async_23_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_290_pause_24',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_290_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_sync_25_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_25_SUBSCRIPT_add_z_coord_1_step_1',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_25_SUBSCRIPT_dec_z_coord_1_step_2',
                "command": 'dec_z_coord_1_step'
            }
        ]
    },
    {
        "identifier": 'EVENT_290_run_dialog_26',
        "command": 'run_dialog',
        "args": [611, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_290_remember_last_object_27',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_290_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_sync_28_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_28_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_28_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_28_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_28_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_290_run_dialog_29',
        "command": 'run_dialog',
        "args": [612, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_290_run_dialog_30',
        "command": 'run_dialog',
        "args": [613, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_290_action_queue_sync_31',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_sync_31_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_31_SUBSCRIPT_floating_on_1',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_31_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_31_SUBSCRIPT_walk_1_step_northeast_3',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_31_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_31_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_290_pause_32',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_290_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_sync_33_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_33_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_290_run_dialog_34',
        "command": 'run_dialog',
        "args": [614, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_290_pause_script_resume_on_next_dialog_page_a_35',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_290_action_queue_async_36',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_async_36_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_290_action_queue_async_36_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_290_unsync_dialog_37',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_290_action_queue_sync_38',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_sync_38_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_38_SUBSCRIPT_add_z_coord_1_step_1',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_38_SUBSCRIPT_dec_z_coord_1_step_2',
                "command": 'dec_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_38_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_38_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_290_run_dialog_39',
        "command": 'run_dialog',
        "args": [615, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_290_remember_last_object_40',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_290_action_queue_sync_41',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_sync_41_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_41_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_41_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_41_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_41_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_41_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_41_SUBSCRIPT_reset_properties_6',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_41_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_290_run_dialog_42',
        "command": 'run_dialog',
        "args": [616, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_290_remember_last_object_43',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_290_action_queue_async_44',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_async_44_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_290_action_queue_sync_45',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_sync_45_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_45_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_45_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_45_SUBSCRIPT_add_z_coord_1_step_3',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_45_SUBSCRIPT_dec_z_coord_1_step_4',
                "command": 'dec_z_coord_1_step'
            }
        ]
    },
    {
        "identifier": 'EVENT_290_run_dialog_46',
        "command": 'run_dialog',
        "args": [617, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_290_remember_last_object_47',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_290_action_queue_async_48',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_async_48_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'shift_northwest_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_290_action_queue_async_48_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [8, 54, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_290_pause_49',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_290_set_7000_to_tapped_button_50',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_290_jmp_if_7000_any_bits_set_51',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0, 1, 2, 3], 'EVENT_290_action_queue_sync_53']
    },
    {
        "identifier": 'EVENT_290_jmp_52',
        "command": 'jmp',
        "args": ['EVENT_290_pause_49']
    },
    {
        "identifier": 'EVENT_290_action_queue_sync_53',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_sync_53_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_53_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_53_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_290_run_dialog_54',
        "command": 'run_dialog',
        "args": [618, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_290_remember_last_object_55',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_290_set_56',
        "command": 'set',
        "args": [0x70a7, 102]
    },
    {
        "identifier": 'EVENT_290_play_sound_57',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_290_run_dialog_58',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_290_put_inventory_59',
        "command": 'put_inventory',
        "args": [items.PickMeUp]
    },
    {
        "identifier": 'EVENT_290_set_action_script_sync_60',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_290_ret_61',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_290_jmp_if_bit_clear_62',
        "command": 'jmp_if_bit_clear',
        "args": [0x7082, 0, 'EVENT_290_run_dialog_104']
    },
    {
        "identifier": 'EVENT_290_jmp_if_bit_set_63',
        "command": 'jmp_if_bit_set',
        "args": [0x7083, 4, 'EVENT_290_jmp_if_bit_set_13']
    },
    {
        "identifier": 'EVENT_290_action_queue_sync_64',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_sync_64_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_290_action_queue_async_65',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_async_65_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_290_action_queue_async_65_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [14, 20]
            },
            {
                "identifier": 'EVENT_290_action_queue_async_65_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_290_action_queue_async_66',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_async_66_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_290_action_queue_async_66_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [14, 20, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_290_action_queue_async_66_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_290_action_queue_async_66_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_290_action_queue_async_66_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_290_action_queue_async_66_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_290_pause_67',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_290_action_queue_sync_68',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_sync_68_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_68_SUBSCRIPT_add_z_coord_1_step_1',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_68_SUBSCRIPT_dec_z_coord_1_step_2',
                "command": 'dec_z_coord_1_step'
            }
        ]
    },
    {
        "identifier": 'EVENT_290_run_dialog_69',
        "command": 'run_dialog',
        "args": [611, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_290_remember_last_object_70',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_290_action_queue_sync_71',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_sync_71_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, 1, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_71_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [38]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_71_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_290_run_dialog_72',
        "command": 'run_dialog',
        "args": [683, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_290_run_dialog_73',
        "command": 'run_dialog',
        "args": [684, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_290_action_queue_async_74',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_async_74_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_290_action_queue_async_74_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_290_action_queue_async_74_SUBSCRIPT_floating_on_2',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_290_action_queue_async_74_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_290_action_queue_async_74_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_290_action_queue_async_74_SUBSCRIPT_walk_1_step_southwest_5',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_290_action_queue_async_74_SUBSCRIPT_shift_southwest_pixels_6',
                "command": 'shift_southwest_pixels',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_290_unsync_dialog_75',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_290_run_dialog_76',
        "command": 'run_dialog',
        "args": [685, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_290_play_sound_77',
        "command": 'play_sound',
        "args": [Sounds._027_FOUND_AN_ITEM, 6]
    },
    {
        "identifier": 'EVENT_290_set_78',
        "command": 'set',
        "args": [0x70a7, 130]
    },
    {
        "identifier": 'EVENT_290_run_dialog_79',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_290_run_dialog_80',
        "command": 'run_dialog',
        "args": [686, AreaObjects.NPC_0, [_0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_290_action_queue_async_81',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_async_81_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_290_action_queue_async_81_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_290_action_queue_async_81_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_290_unsync_dialog_82',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_290_run_event_as_subroutine_83',
        "command": 'run_event_as_subroutine',
        "args": [272]
    },
    {
        "identifier": 'EVENT_290_action_queue_sync_84',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_sync_84_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_84_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_84_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_84_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_84_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_290_action_queue_sync_85',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_sync_85_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_290_action_queue_sync_85_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_290_remember_last_object_86',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_290_run_dialog_87',
        "command": 'run_dialog',
        "args": [728, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_290_pause_88',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_290_set_89',
        "command": 'set',
        "args": [0x70ae, 20]
    },
    {
        "identifier": 'EVENT_290_set_action_script_async_90',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_290_pause_91',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_290_action_queue_async_92',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_async_92_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_290_action_queue_async_92_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_290_action_queue_async_92_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_290_set_bit_93',
        "command": 'set_bit',
        "args": [0x7083, 4]
    },
    {
        "identifier": 'EVENT_290_remove_one_from_inventory_94',
        "command": 'remove_one_from_inventory',
        "args": [items.RareFrogCoin]
    },
    {
        "identifier": 'EVENT_290_put_inventory_95',
        "command": 'put_inventory',
        "args": [items.CricketPie]
    },
    {
        "identifier": 'EVENT_290_action_queue_async_96',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_290_action_queue_async_96_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_290_action_queue_async_96_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_290_ret_97',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_290_jmp_if_bit_clear_98',
        "command": 'jmp_if_bit_clear',
        "args": [0x7083, 4, 'EVENT_290_jmp_if_bit_clear_62']
    },
    {
        "identifier": 'EVENT_290_run_dialog_99',
        "command": 'run_dialog',
        "args": [2241, AreaObjects.NPC_1, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_290_run_dialog_100',
        "command": 'run_dialog',
        "args": [544, AreaObjects.NPC_1, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_290_open_shop_101',
        "command": 'open_shop',
        "args": [Shops._00_MUSHROOM_KINGDOM]
    },
    {
        "identifier": 'EVENT_290_fade_in_from_black_async_102',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_290_ret_103',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_290_run_dialog_104',
        "command": 'run_dialog',
        "args": [687, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_290_ret_105',
        "command": 'ret'
    }
]
