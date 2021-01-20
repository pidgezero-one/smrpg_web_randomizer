from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1710_jmp_to_subroutine_0',
        "command": 'jmp_to_subroutine',
        "args": [0x396c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 467],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 467],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 467],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 467],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_jmp_to_subroutine_5',
        "command": 'jmp_to_subroutine',
        "args": [0x399b],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_1710_start_battle_19'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_run_dialog_7',
        "command": 'run_dialog',
        "args": [1067, AreaObjects.NPC_8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_summon_to_current_level_at_marios_coords_8',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_1710_action_queue_async_9_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_9_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_9_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_9_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_9_SUBSCRIPT_walk_1_step_northeast_4',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_9_SUBSCRIPT_face_southeast_5',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1710_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1710_action_queue_sync_10_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_10_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_10_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_10_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_10_SUBSCRIPT_add_z_coord_1_step_4',
                "command": 'add_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_10_SUBSCRIPT_dec_z_coord_1_step_5',
                "command": 'dec_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_10_SUBSCRIPT_end_loop_6',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1710_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_1710_action_queue_async_11_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._020_LIGHTING_BOLT, 4]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_11_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_11_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_11_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1710_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1710_action_queue_sync_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_12_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_12_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_12_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_12_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_12_SUBSCRIPT_face_southeast_5',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_12_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_12_SUBSCRIPT_face_southwest_7',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_12_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_12_SUBSCRIPT_face_northwest_9',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_12_SUBSCRIPT_end_loop_10',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1710_run_dialog_13',
        "command": 'run_dialog',
        "args": [1061, AreaObjects.NPC_8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1710_action_queue_async_14_SUBSCRIPT_walk_1_step_southwest_0',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_14_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1710_pause_15',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_run_dialog_16',
        "command": 'run_dialog',
        "args": [1062, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1710_action_queue_sync_17_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_17_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_17_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_17_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_17_SUBSCRIPT_walk_1_step_northeast_4',
                "command": 'walk_1_step_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1710_pause_18',
        "command": 'pause',
        "args": [23],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_start_battle_19',
        "command": 'start_battle',
        "args": [0x00a3, 9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_set_bit_20',
        "command": 'set_bit',
        "args": [0x707c, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_clear_bit_21',
        "command": 'clear_bit',
        "args": [0x707c, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_clear_bit_22',
        "command": 'clear_bit',
        "args": [0x707c, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_run_event_as_subroutine_23',
        "command": 'run_event_as_subroutine',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_remove_from_current_level_24',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_remove_from_current_level_25',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_remove_from_current_level_26',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_remove_from_current_level_27',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_remove_from_current_level_28',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_remove_from_current_level_29',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_remove_from_current_level_30',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_remove_from_current_level_31',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_remove_from_level_32',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_8, Rooms._206_BANDITS_WAY_AREA_05],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_restore_all_hp_33',
        "command": 'restore_all_hp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_restore_all_fp_34',
        "command": 'restore_all_fp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_fade_in_from_black_async_35',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_jmp_36',
        "command": 'jmp',
        "args": ['EVENT_1710_action_queue_async_40'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_put_inventory_37',
        "command": 'put_inventory',
        "args": [0x70a7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_run_dialog_38',
        "command": 'run_dialog',
        "args": [1070, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_action_queue_async_39',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_1710_action_queue_async_39_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_39_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1710_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1710_action_queue_async_40_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_40_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [6, 88]
            }
        ]
    },
    {
        "identifier": 'EVENT_1710_play_sound_41',
        "command": 'play_sound',
        "args": [Sounds._019_LONG_FALL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_pause_42',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_action_queue_async_43',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_1710_action_queue_async_43_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_43_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_43_SUBSCRIPT_shadow_on_2',
                "command": 'shadow_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_43_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_43_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_43_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x1d, 0x9d]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_43_SUBSCRIPT_shadow_off_6',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_43_SUBSCRIPT_set_solidity_bits_7',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1710_action_queue_sync_44',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1710_action_queue_sync_44_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 6]
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_44_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_44_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_44_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_44_SUBSCRIPT_shift_north_pixels_4',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_44_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1710_action_queue_sync_44_SUBSCRIPT_shift_north_pixels_6',
                "command": 'shift_north_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_1710_action_queue_async_45',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_1710_action_queue_async_45_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_45_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.LOOPING_OFF]]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_45_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_45_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 6]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_45_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [55]
            }
        ]
    },
    {
        "identifier": 'EVENT_1710_action_queue_async_46',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1710_action_queue_async_46_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_46_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0xc8, 0x80]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_46_SUBSCRIPT_add_short_2',
                "command": 'add_short',
                "args": [0x7016, 0xfffc]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_46_SUBSCRIPT_add_short_3',
                "command": 'add_short',
                "args": [0x7018, 0xfff0]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_46_SUBSCRIPT_run_away_shift_4',
                "command": 'run_away_shift',
                "args": []
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_46_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_46_SUBSCRIPT_jmp_6',
                "command": 'jmp',
                "args": ['EVENT_1710_set_bit_47']
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_46_SUBSCRIPT_shift_south_steps_7',
                "command": 'shift_south_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1710_action_queue_async_46_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1710_set_bit_47',
        "command": 'set_bit',
        "args": [0x7081, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_set_bit_48',
        "command": 'set_bit',
        "args": [0x704d, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_set_short_49',
        "command": 'set_short',
        "args": [0x700a, 0x00c9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_jmp_to_event_50',
        "command": 'jmp_to_event',
        "args": [720],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1710_ret_51',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
