from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_593_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7063, 6, 'EVENT_257_fade_in_from_black_async_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_jmp_1',
        "command": 'jmp',
        "args": ['EVENT_593_pause_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_palette_set_2',
        "command": 'palette_set',
        "args": [81, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_palette_set_3',
        "command": 'palette_set',
        "args": [82, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_palette_set_4',
        "command": 'palette_set',
        "args": [83, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_5',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_fade_out_music_to_volume_6',
        "command": 'fade_out_music_to_volume',
        "args": [0, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_start_battle_7',
        "command": 'start_battle',
        "args": [0x008c, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_set_bit_8',
        "command": 'set_bit',
        "args": [0x704a, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_run_event_as_subroutine_9',
        "command": 'run_event_as_subroutine',
        "args": [1011],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_10',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remove_from_level_11',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remove_from_level_12',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remove_from_level_13',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remove_from_level_14',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remove_from_level_15',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_set_bit_16',
        "command": 'set_bit',
        "args": [0x7056, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_restore_all_hp_17',
        "command": 'restore_all_hp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_restore_all_fp_18',
        "command": 'restore_all_fp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_jmp_19',
        "command": 'jmp',
        "args": ['EVENT_593_apply_tile_mod_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_20_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_20_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 8, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_async_21_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 19, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_21_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_apply_tile_mod_22',
        "command": 'apply_tile_mod',
        "args": [Rooms._271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_23',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_apply_tile_mod_24',
        "command": 'apply_tile_mod',
        "args": [Rooms._271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE, 1, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_25',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_apply_tile_mod_26',
        "command": 'apply_tile_mod',
        "args": [Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_27',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_apply_tile_mod_28',
        "command": 'apply_tile_mod',
        "args": [Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, 1, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_apply_solidity_mod_29',
        "command": 'apply_solidity_mod',
        "args": [Rooms._271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_apply_solidity_mod_30',
        "command": 'apply_solidity_mod',
        "args": [Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_jmp_31',
        "command": 'jmp',
        "args": ['EVENT_593_fade_in_music_150'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_32',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_async_33',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_async_33_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [21, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_33_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_33_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [18, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_33_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_34',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_34_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_store_02_to_0248_35',
        "command": 'store_02_to_0248',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_fade_in_from_colour_duration_36',
        "command": 'fade_in_from_colour_duration',
        "args": [90, Colours.WHITE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_37',
        "command": 'pause',
        "args": [40],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_async_38',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_async_38_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_38_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_script_until_effect_done_39',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_store_00_to_0248_40',
        "command": 'store_00_to_0248',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_41',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [22, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [22, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [18, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [21, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [18, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_end_loop_20',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_face_southeast_22',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_41_SUBSCRIPT_reset_properties_23',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_42',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_43',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_43_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_44',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_run_dialog_45',
        "command": 'run_dialog',
        "args": [960, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remember_last_object_46',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_47',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_48',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_48_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_48_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_48_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_48_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [24, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_48_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_48_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_48_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_48_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_48_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_48_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [19, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_48_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_48_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [22, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_48_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_48_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_48_SUBSCRIPT_end_loop_14',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_48_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_48_SUBSCRIPT_face_northwest_16',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_48_SUBSCRIPT_reset_properties_17',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_49',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_50',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_50_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_51',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_run_dialog_52',
        "command": 'run_dialog',
        "args": [961, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_53',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_play_sound_54',
        "command": 'play_sound',
        "args": [Sounds._021_RUMBLING, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_55',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_55_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_55_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_55_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_55_SUBSCRIPT_shift_z_down_pixels_3',
                "command": 'shift_z_down_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_55_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_55_SUBSCRIPT_shift_z_down_pixels_5',
                "command": 'shift_z_down_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_async_56',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_async_56_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_56_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_56_SUBSCRIPT_shift_west_steps_2',
                "command": 'shift_west_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_57',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_face_north_2',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [134]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_fixed_f_coord_on_9',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_sequence_looping_on_10',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_shift_southeast_pixels_12',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_sequence_looping_off_13',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_reset_properties_14',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_sequence_looping_on_16',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_shift_northwest_pixels_17',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_sequence_looping_off_18',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_fixed_f_coord_off_19',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [74]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_set_sprite_sequence_21',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_58',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [22, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_walk_1_step_southeast_9',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_shift_southeast_pixels_10',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_face_northwest_12',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_reset_properties_13',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_shift_northwest_pixels_14',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [21, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_reset_properties_17',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_set_animation_speed_18',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_face_northeast_19',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_face_southeast_21',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_set_sprite_sequence_23',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_reset_properties_25',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_pause_26',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_pause_27',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_set_sprite_sequence_28',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_59',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_59_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [23, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_60',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_60_SUBSCRIPT_floating_on_0',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_60_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_60_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 6]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_61',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_61_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_61_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_62',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_62_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_62_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_63',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_63_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_63_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_remember_last_object_64',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_65',
        "command": 'pause',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_66',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_66_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_67',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_67_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_run_dialog_68',
        "command": 'run_dialog',
        "args": [962, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remember_last_object_69',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_unsync_dialog_70',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_71',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_72',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_72_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_72_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_72_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_72_SUBSCRIPT_walk_1_step_west_3',
                "command": 'walk_1_step_west',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_72_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_72_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_72_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [17, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_async_73',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_async_73_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_73_SUBSCRIPT_face_south_1',
                "command": 'face_south',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_async_73_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_73_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_async_73_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_73_SUBSCRIPT_face_west_5',
                "command": 'face_west',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_async_73_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_73_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_async_73_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_73_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [11, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_run_dialog_74',
        "command": 'run_dialog',
        "args": [963, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_75',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_async_76',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_async_76_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_set_action_script_async_77',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_78',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_79',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_79_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_79_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_80',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_80_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_80_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_80_SUBSCRIPT_walk_1_step_northwest_2',
                "command": 'walk_1_step_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_80_SUBSCRIPT_shift_northwest_pixels_3',
                "command": 'shift_northwest_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_81',
        "command": 'pause',
        "args": [12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remember_last_object_82',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_set_action_script_sync_83',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_84',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_84_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_84_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_84_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_84_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_async_85',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_async_85_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_85_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_85_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_85_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_85_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_85_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_85_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_85_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_85_SUBSCRIPT_face_northeast_8',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_async_85_SUBSCRIPT_reset_properties_9',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_async_86',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_async_86_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_86_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_db_87',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x99, 0x07, 0xff],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_script_until_effect_done_88',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_set_action_script_sync_89',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 294],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_90',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_action_script_91',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_92',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_92_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_92_SUBSCRIPT_walk_1_step_south_1',
                "command": 'walk_1_step_south',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_92_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_92_SUBSCRIPT_walk_1_step_south_3',
                "command": 'walk_1_step_south',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_93',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_93_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_93_SUBSCRIPT_set_object_memory_bits_1',
                "command": 'set_object_memory_bits',
                "args": [0x0e, bits=[0]]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_94',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_95',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_95_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_95_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_96',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_96_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_96_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_96_SUBSCRIPT_face_south_2',
                "command": 'face_south',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_97',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_97_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_97_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_98',
        "command": 'pause',
        "args": [6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_play_music_default_volume_99',
        "command": 'play_music_default_volume',
        "args": [Music._23_GOT_A_STAR_PIECE_PART_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remember_last_object_100',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_101',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_set_action_script_sync_102',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 295],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_103',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_103_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_103_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_103_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_103_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_103_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_103_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_103_SUBSCRIPT_transfer_to_object_xy_6',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.NPC_9]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_103_SUBSCRIPT_transfer_xyzf_pixels_7',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 16, RadialDirections.SOUTHEAST]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_103_SUBSCRIPT_visibility_on_8',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_103_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_103_SUBSCRIPT_shift_z_down_pixels_10',
                "command": 'shift_z_down_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_103_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_103_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_103_SUBSCRIPT_shift_z_down_pixels_13',
                "command": 'shift_z_down_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_103_SUBSCRIPT_visibility_off_14',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_104',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_set_action_script_sync_105',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 296],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_106',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_106_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_106_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_106_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_106_SUBSCRIPT_transfer_to_object_xy_3',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.NPC_9]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_106_SUBSCRIPT_transfer_xyzf_pixels_4',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 16, RadialDirections.SOUTHEAST]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_106_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_106_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_106_SUBSCRIPT_shift_z_down_pixels_7',
                "command": 'shift_z_down_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_106_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_106_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_106_SUBSCRIPT_shift_z_down_pixels_10',
                "command": 'shift_z_down_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_106_SUBSCRIPT_visibility_off_11',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_palette_set_morphs_107',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 86, 12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_108',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_set_action_script_sync_109',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 297],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_110',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_110_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [24, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_110_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_110_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_110_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_110_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_110_SUBSCRIPT_transfer_to_object_xy_5',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.NPC_9]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_110_SUBSCRIPT_transfer_xyzf_steps_6',
                "command": 'transfer_xyzf_steps',
                "args": [0, 0, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_110_SUBSCRIPT_visibility_on_7',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_110_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_110_SUBSCRIPT_shift_z_down_pixels_9',
                "command": 'shift_z_down_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_110_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_110_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_110_SUBSCRIPT_shift_z_down_pixels_12',
                "command": 'shift_z_down_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_110_SUBSCRIPT_visibility_off_13',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_palette_set_morphs_111',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 84, 8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_112',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_palette_set_morphs_113',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 85, 13],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remember_last_object_114',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_short_115',
        "command": 'pause_short',
        "args": [370],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_action_script_116',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_start_embedded_action_script_async_117',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_start_embedded_action_script_async_117_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_593_start_embedded_action_script_async_117_SUBSCRIPT_floating_off_1',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_593_start_embedded_action_script_async_117_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_start_embedded_action_script_async_117_SUBSCRIPT_shift_west_pixels_3',
                "command": 'shift_west_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_start_embedded_action_script_async_117_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_db_118',
        "command": 'db',
        "args": [0xfd, 0x8c, 0x32, 0x0a, 0x30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_set_action_script_sync_119',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_120',
        "command": 'pause',
        "args": [180],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_action_script_121',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_122',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_122_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_122_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_122_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_122_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_122_SUBSCRIPT_add_z_coord_1_step_4',
                "command": 'add_z_coord_1_step',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_122_SUBSCRIPT_shift_z_up_pixels_5',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_122_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_122_SUBSCRIPT_shift_z_up_pixels_7',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_122_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_122_SUBSCRIPT_shift_z_up_pixels_9',
                "command": 'shift_z_up_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_122_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_122_SUBSCRIPT_shift_z_up_pixels_11',
                "command": 'shift_z_up_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_122_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_122_SUBSCRIPT_shift_z_up_pixels_13',
                "command": 'shift_z_up_pixels',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_123',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_123_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_123_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_123_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [5, 29, 14, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_123_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [2, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_123_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_123_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_123_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_123_SUBSCRIPT_shift_z_up_pixels_7',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_123_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_123_SUBSCRIPT_shift_z_up_pixels_9',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_123_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_123_SUBSCRIPT_visibility_off_11',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_remember_last_object_124',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_async_125',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_async_125_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_125_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_125_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_125_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_125_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_125_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_126',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_action_script_127',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_freeze_camera_128',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_129',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_129_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [131]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_129_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_129_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_129_SUBSCRIPT_set_object_memory_bits_3',
                "command": 'set_object_memory_bits',
                "args": [0x0e, bits=[2, 3]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_129_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_129_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_130',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_set_priority_3',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x25, 0x00, 0x04, 0xf0, 0xff]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_shift_south_steps_7',
                "command": 'shift_south_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_shift_south_pixels_8',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_floating_off_9',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_bpl_26_27_28_10',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_shift_southwest_pixels_13',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=1, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_shift_southwest_pixels_16',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_set_sprite_sequence_17',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_shift_southwest_pixels_18',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_shift_southwest_pixels_20',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_130_SUBSCRIPT_set_sprite_sequence_21',
                "command": 'set_sprite_sequence',
                "args": [31, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_131',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_131_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_131_SUBSCRIPT_shift_west_pixels_1',
                "command": 'shift_west_pixels',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_132',
        "command": 'pause',
        "args": [86],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_play_music_default_volume_133',
        "command": 'play_music_default_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remember_last_object_134',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_unfreeze_camera_135',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_async_136',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_async_136_SUBSCRIPT_floating_on_0',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_async_136_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_137',
        "command": 'pause',
        "args": [240],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_138',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_138_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_138_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_138_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_138_SUBSCRIPT_shift_z_up_steps_3',
                "command": 'shift_z_up_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_138_SUBSCRIPT_shift_z_up_pixels_4',
                "command": 'shift_z_up_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_139',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_139_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [34]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_139_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_139_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_139_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_139_SUBSCRIPT_add_z_coord_1_step_4',
                "command": 'add_z_coord_1_step',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_140',
        "command": 'pause',
        "args": [160],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_db_141',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x00, 0x0a, 0xce],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remember_last_object_142',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_set_action_script_sync_143',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_144',
        "command": 'pause',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_action_script_145',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_146',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_146_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_146_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_146_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_147',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_147_SUBSCRIPT_transfer_to_object_xy_0',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.NPC_9]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_147_SUBSCRIPT_transfer_xyzf_steps_1',
                "command": 'transfer_xyzf_steps',
                "args": [0, 0, 5, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_147_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_147_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_147_SUBSCRIPT_shift_z_up_steps_4',
                "command": 'shift_z_up_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_remember_last_object_148',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_run_star_piece_sequence_149',
        "command": 'run_star_piece_sequence',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_fade_in_music_150',
        "command": 'fade_in_music',
        "args": [Music._33_MOLEVILLE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remove_from_current_level_151',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remove_from_current_level_152',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remove_from_current_level_153',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remove_from_current_level_154',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remove_from_level_155',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_9, Rooms._271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remove_from_level_156',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remove_from_level_157',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remove_from_level_158',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_jmp_159',
        "command": 'jmp',
        "args": ['EVENT_593_set_bit_165'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_db_160',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x72, 0x00, 0x00],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_161',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_161_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 21, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_161_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_162',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_162_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_162_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_162_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_162_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [7, 20, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_163',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_163_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 20, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_163_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_593_remember_last_object_164',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_set_bit_165',
        "command": 'set_bit',
        "args": [0x7049, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_jmp_166',
        "command": 'jmp',
        "args": ['EVENT_593_action_queue_sync_172'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_run_event_as_subroutine_167',
        "command": 'run_event_as_subroutine',
        "args": [276],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_fade_in_from_black_async_168',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_169',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_run_dialog_170',
        "command": 'run_dialog',
        "args": [3212, AreaObjects.NPC_4, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_pause_171',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_172',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_172_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_172_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_172_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_172_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_173',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_173_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_173_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_173_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_173_SUBSCRIPT_walk_1_step_southeast_3',
                "command": 'walk_1_step_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_173_SUBSCRIPT_shift_northeast_pixels_4',
                "command": 'shift_northeast_pixels',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_fade_in_from_black_async_174',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_stop_sound_175',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_stop_sound_176',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_stop_sound_177',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_stop_sound_178',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_stop_sound_179',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_stop_sound_180',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_stop_sound_181',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_stop_sound_182',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_stop_sound_183',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_stop_sound_184',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remove_from_level_185',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_remove_from_level_186',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_apply_tile_mod_187',
        "command": 'apply_tile_mod',
        "args": [Rooms._276_MOLEVILLE_MINES_AREA_01_ENTRANCE, 0, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_apply_solidity_mod_188',
        "command": 'apply_solidity_mod',
        "args": [Rooms._276_MOLEVILLE_MINES_AREA_01_ENTRANCE, 0, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_set_bit_189',
        "command": 'set_bit',
        "args": [0x7063, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_store_01_to_0248_190',
        "command": 'store_01_to_0248',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_set_short_191',
        "command": 'set_short',
        "args": [0x700a, 0x00ce],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_jmp_to_event_192',
        "command": 'jmp_to_event',
        "args": [720],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_stop_sound_193',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_593_ret_194',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
