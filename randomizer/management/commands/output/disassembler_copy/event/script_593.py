
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_593_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7063, 6, 'EVENT_257_fade_in_from_black_async_0']
    },
    {
        "identifier": 'EVENT_593_palette_set_1',
        "command": 'palette_set',
        "args": [81, 1, [3]]
    },
    {
        "identifier": 'EVENT_593_palette_set_2',
        "command": 'palette_set',
        "args": [82, 1, [2, 3]]
    },
    {
        "identifier": 'EVENT_593_palette_set_3',
        "command": 'palette_set',
        "args": [83, 1, [0, 2, 3]]
    },
    {
        "identifier": 'EVENT_593_pause_4',
        "command": 'pause',
        "args": [2]
    },
    {
        "identifier": 'EVENT_593_fade_out_music_to_volume_5',
        "command": 'fade_out_music_to_volume',
        "args": [0, 1]
    },
    {
        "identifier": 'EVENT_593_start_battle_6',
        "command": 'start_battle',
        "args": [0x008c, 5]
    },
    {
        "identifier": 'EVENT_593_set_bit_7',
        "command": 'set_bit',
        "args": [0x704a, 2]
    },
    {
        "identifier": 'EVENT_593_run_event_as_subroutine_8',
        "command": 'run_event_as_subroutine',
        "args": [1011]
    },
    {
        "identifier": 'EVENT_593_play_music_current_volume_9',
        "command": 'play_music_current_volume',
        "args": [Music._23_GOT_A_STAR_PIECE_PART_1]
    },
    {
        "identifier": 'EVENT_593_pause_10',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_593_stop_music_FDA2_11',
        "command": 'stop_music_FDA2'
    },
    {
        "identifier": 'EVENT_593_remove_from_level_12',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE]
    },
    {
        "identifier": 'EVENT_593_remove_from_level_13',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE]
    },
    {
        "identifier": 'EVENT_593_remove_from_level_14',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE]
    },
    {
        "identifier": 'EVENT_593_remove_from_level_15',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE]
    },
    {
        "identifier": 'EVENT_593_remove_from_level_16',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE]
    },
    {
        "identifier": 'EVENT_593_set_bit_17',
        "command": 'set_bit',
        "args": [0x7056, 3]
    },
    {
        "identifier": 'EVENT_593_restore_all_hp_18',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_593_restore_all_fp_19',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_20_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
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
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_apply_tile_mod_22',
        "command": 'apply_tile_mod',
        "args": [Rooms._271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_593_pause_23',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_593_apply_tile_mod_24',
        "command": 'apply_tile_mod',
        "args": [Rooms._271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_593_pause_25',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_593_apply_tile_mod_26',
        "command": 'apply_tile_mod',
        "args": [Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_593_pause_27',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_593_apply_tile_mod_28',
        "command": 'apply_tile_mod',
        "args": [Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, 1, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_593_apply_solidity_mod_29',
        "command": 'apply_solidity_mod',
        "args": [Rooms._271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_593_apply_solidity_mod_30',
        "command": 'apply_solidity_mod',
        "args": [Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_593_pause_31',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_593_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_async_32_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [21, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_32_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_32_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [18, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_32_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_33_SUBSCRIPT_shadow_on_0',
                "command": 'shadow_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_store_02_to_0248_34',
        "command": 'store_02_to_0248'
    },
    {
        "identifier": 'EVENT_593_fade_in_from_colour_duration_35',
        "command": 'fade_in_from_colour_duration',
        "args": [90, Colours.WHITE]
    },
    {
        "identifier": 'EVENT_593_pause_36',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'EVENT_593_action_queue_async_37',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_async_37_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_37_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_script_until_effect_done_38',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_593_store_00_to_0248_39',
        "command": 'store_00_to_0248'
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_40',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [22, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [23, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_set_sprite_sequence_8',
                "command": 'set_sprite_sequence',
                "args": [22, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [3, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [18, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [21, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [18, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [3, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_end_loop_20',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_face_southeast_22',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_40_SUBSCRIPT_reset_properties_23',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_41',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_42',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_42_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_43',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_593_run_dialog_44',
        "command": 'run_dialog',
        "args": [960, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_593_remember_last_object_45',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_593_pause_46',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_47',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_47_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_47_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [23, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_47_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_47_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [24, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_47_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_47_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [23, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_47_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_47_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [3, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_47_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_47_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [19, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_47_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_47_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [22, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_47_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_47_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [19, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_47_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_47_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [3, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_47_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_47_SUBSCRIPT_end_loop_17',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_47_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_47_SUBSCRIPT_face_northwest_19',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_47_SUBSCRIPT_reset_properties_20',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_48',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_49_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_50',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_593_run_dialog_51',
        "command": 'run_dialog',
        "args": [961, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_593_pause_52',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_593_play_sound_53',
        "command": 'play_sound',
        "args": [Sounds._021_RUMBLING, 6]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_54',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_54_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_54_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_54_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_54_SUBSCRIPT_shift_z_down_pixels_3',
                "command": 'shift_z_down_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_54_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_54_SUBSCRIPT_shift_z_down_pixels_5',
                "command": 'shift_z_down_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_async_55',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_async_55_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_55_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_55_SUBSCRIPT_shift_west_steps_2',
                "command": 'shift_west_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_56',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_face_north_2',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [23, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [134]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_fixed_f_coord_on_9',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_sequence_looping_on_10',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_shift_southeast_pixels_12',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_sequence_looping_off_13',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_reset_properties_14',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_sequence_looping_on_16',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_shift_northwest_pixels_17',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_sequence_looping_off_18',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_fixed_f_coord_off_19',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [74]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_56_SUBSCRIPT_set_sprite_sequence_21',
                "command": 'set_sprite_sequence',
                "args": [23, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_57',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [22, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [23, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_walk_1_step_southeast_9',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_shift_southeast_pixels_10',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_face_northwest_12',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_reset_properties_13',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_shift_northwest_pixels_14',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [21, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_reset_properties_17',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_set_animation_speed_18',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_face_northeast_19',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_face_southeast_21',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_set_sprite_sequence_23',
                "command": 'set_sprite_sequence',
                "args": [14, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_pause_24',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_reset_properties_25',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_pause_26',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_face_northwest_27',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_pause_28',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_57_SUBSCRIPT_set_sprite_sequence_29',
                "command": 'set_sprite_sequence',
                "args": [23, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_58',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_58_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [23, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_59',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_59_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_59_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_59_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_59_SUBSCRIPT_shift_z_down_pixels_3',
                "command": 'shift_z_down_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_remember_last_object_60',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_593_pause_61',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_62',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_62_SUBSCRIPT_floating_on_0',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_62_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_62_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._022_CLOSE_DOOR, 6]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_63',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_63_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_63_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_64',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_64_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_64_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_65',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_65_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_65_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_remember_last_object_66',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_593_pause_67',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_68',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_68_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_69',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_69_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_run_dialog_70',
        "command": 'run_dialog',
        "args": [962, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_593_remember_last_object_71',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_593_unsync_dialog_72',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_593_pause_73',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_74',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_74_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_74_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_74_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_74_SUBSCRIPT_walk_1_step_west_3',
                "command": 'walk_1_step_west'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_74_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_74_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_74_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [17, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_async_75',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_async_75_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_75_SUBSCRIPT_face_south_1',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_593_action_queue_async_75_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_75_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_593_action_queue_async_75_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_75_SUBSCRIPT_face_west_5',
                "command": 'face_west'
            },
            {
                "identifier": 'EVENT_593_action_queue_async_75_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_75_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_593_action_queue_async_75_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_75_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [11, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_run_dialog_76',
        "command": 'run_dialog',
        "args": [963, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_593_pause_77',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_593_action_queue_async_78',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_async_78_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_set_action_script_async_79',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_593_pause_80',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_81',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_81_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_81_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_82',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_82_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_82_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_82_SUBSCRIPT_walk_1_step_northwest_2',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_82_SUBSCRIPT_shift_northwest_pixels_3',
                "command": 'shift_northwest_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_83',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'EVENT_593_remember_last_object_84',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_593_set_action_script_sync_85',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 120]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_86',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_86_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_86_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_86_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_86_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_async_87',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_async_87_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_87_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_87_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_87_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [64]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_87_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_87_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [9, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_87_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_87_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_87_SUBSCRIPT_face_northeast_8',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_593_action_queue_async_87_SUBSCRIPT_reset_properties_9',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_async_88',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_async_88_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_88_SUBSCRIPT_shadow_on_1',
                "command": 'shadow_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_db_89',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x99, 0x07, 0xff]
    },
    {
        "identifier": 'EVENT_593_pause_script_until_effect_done_90',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_593_set_action_script_sync_91',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 294]
    },
    {
        "identifier": 'EVENT_593_pause_92',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_593_pause_action_script_93',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_94',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_94_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_94_SUBSCRIPT_walk_1_step_south_1',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_94_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_94_SUBSCRIPT_walk_1_step_south_3',
                "command": 'walk_1_step_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_95',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_95_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_95_SUBSCRIPT_set_object_memory_bits_1',
                "command": 'set_object_memory_bits',
                "args": [0x0e, [0]]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_96',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_97',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_97_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_97_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_98',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_98_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_98_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_98_SUBSCRIPT_face_south_2',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_99',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_99_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_99_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_100',
        "command": 'pause',
        "args": [6]
    },
    {
        "identifier": 'EVENT_593_play_music_default_volume_101',
        "command": 'play_music_default_volume',
        "args": [Music._23_GOT_A_STAR_PIECE_PART_1]
    },
    {
        "identifier": 'EVENT_593_remember_last_object_102',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_593_pause_103',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'EVENT_593_set_action_script_sync_104',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 295]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_105',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_105_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_105_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_105_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_105_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_105_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_105_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_105_SUBSCRIPT_transfer_to_object_xy_6',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.NPC_9]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_105_SUBSCRIPT_transfer_xyzf_pixels_7',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 16, RadialDirections.SOUTHEAST]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_105_SUBSCRIPT_visibility_on_8',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_105_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_105_SUBSCRIPT_shift_z_down_pixels_10',
                "command": 'shift_z_down_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_105_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_105_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_105_SUBSCRIPT_shift_z_down_pixels_13',
                "command": 'shift_z_down_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_105_SUBSCRIPT_visibility_off_14',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_106',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_593_set_action_script_sync_107',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 296]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_108',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_108_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_108_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_108_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_108_SUBSCRIPT_transfer_to_object_xy_3',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.NPC_9]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_108_SUBSCRIPT_transfer_xyzf_pixels_4',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 16, RadialDirections.SOUTHEAST]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_108_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_108_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_108_SUBSCRIPT_shift_z_down_pixels_7',
                "command": 'shift_z_down_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_108_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_108_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_108_SUBSCRIPT_shift_z_down_pixels_10',
                "command": 'shift_z_down_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_108_SUBSCRIPT_visibility_off_11',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_palette_set_morphs_109',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 86, 12]
    },
    {
        "identifier": 'EVENT_593_pause_110',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_593_set_action_script_sync_111',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 297]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_112',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_112_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [24, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_112_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_112_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_112_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_112_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_112_SUBSCRIPT_transfer_to_object_xy_5',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.NPC_9]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_112_SUBSCRIPT_transfer_xyzf_steps_6',
                "command": 'transfer_xyzf_steps',
                "args": [0, 0, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_112_SUBSCRIPT_visibility_on_7',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_112_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_112_SUBSCRIPT_shift_z_down_pixels_9',
                "command": 'shift_z_down_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_112_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_112_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_112_SUBSCRIPT_shift_z_down_pixels_12',
                "command": 'shift_z_down_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_112_SUBSCRIPT_visibility_off_13',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_palette_set_morphs_113',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 84, 8]
    },
    {
        "identifier": 'EVENT_593_pause_114',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_593_palette_set_morphs_115',
        "command": 'palette_set_morphs',
        "args": [PaletteSetTypes.FADE_TO, 10, 85, 13]
    },
    {
        "identifier": 'EVENT_593_remember_last_object_116',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_593_pause_short_117',
        "command": 'pause_short',
        "args": [370]
    },
    {
        "identifier": 'EVENT_593_pause_action_script_118',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_593_start_embedded_action_script_async_F1_119',
        "command": 'start_embedded_action_script_async_F1',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_start_embedded_action_script_async_F1_119_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_593_start_embedded_action_script_async_F1_119_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_593_start_embedded_action_script_async_F1_119_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_start_embedded_action_script_async_F1_119_SUBSCRIPT_shift_west_pixels_3',
                "command": 'shift_west_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_start_embedded_action_script_async_F1_119_SUBSCRIPT_shift_southwest_pixels_4',
                "command": 'shift_southwest_pixels',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_db_120',
        "command": 'db',
        "args": [0xfd, 0x8c, 0x32, 0x0a, 0x30]
    },
    {
        "identifier": 'EVENT_593_set_action_script_sync_121',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 120]
    },
    {
        "identifier": 'EVENT_593_pause_122',
        "command": 'pause',
        "args": [180]
    },
    {
        "identifier": 'EVENT_593_pause_action_script_123',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_124',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_124_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_124_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_124_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_124_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_124_SUBSCRIPT_add_z_coord_1_step_4',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_124_SUBSCRIPT_shift_z_up_pixels_5',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_124_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_124_SUBSCRIPT_shift_z_up_pixels_7',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_124_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_124_SUBSCRIPT_shift_z_up_pixels_9',
                "command": 'shift_z_up_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_124_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_124_SUBSCRIPT_shift_z_up_pixels_11',
                "command": 'shift_z_up_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_124_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_124_SUBSCRIPT_shift_z_up_pixels_13',
                "command": 'shift_z_up_pixels',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_125',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_125_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_125_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_125_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [5, 29, 14, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_125_SUBSCRIPT_transfer_xyzf_pixels_3',
                "command": 'transfer_xyzf_pixels',
                "args": [2, 0, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_125_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_125_SUBSCRIPT_visibility_on_5',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_125_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_125_SUBSCRIPT_shift_z_up_pixels_7',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_125_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_125_SUBSCRIPT_shift_z_up_pixels_9',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_125_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_125_SUBSCRIPT_visibility_off_11',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_remember_last_object_126',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_593_action_queue_async_127',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_async_127_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_127_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_127_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_127_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_127_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_593_action_queue_async_127_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_128',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_593_pause_action_script_129',
        "command": 'pause_action_script',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_593_freeze_camera_130',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_131',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_131_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [131]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_131_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_131_SUBSCRIPT_shift_z_down_pixels_2',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_131_SUBSCRIPT_set_object_memory_bits_3',
                "command": 'set_object_memory_bits',
                "args": [0x0e, [2, 3]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_131_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_131_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_132',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_set_priority_3',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x25, 0x00, 0x04, 0xf0, 0xff]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_shift_south_steps_7',
                "command": 'shift_south_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_shift_south_pixels_8',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_floating_off_9',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_bpl_26_27_28_10',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [3, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_set_animation_speed_12',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_shift_southwest_pixels_13',
                "command": 'shift_southwest_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [2, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_shift_southwest_pixels_16',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_set_sprite_sequence_17',
                "command": 'set_sprite_sequence',
                "args": [2, 3, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_shift_southwest_pixels_18',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_set_sprite_sequence_19',
                "command": 'set_sprite_sequence',
                "args": [2, 3, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_shift_southwest_pixels_20',
                "command": 'shift_southwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_132_SUBSCRIPT_set_sprite_sequence_21',
                "command": 'set_sprite_sequence',
                "args": [31, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_133',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_133_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_133_SUBSCRIPT_shift_west_pixels_1',
                "command": 'shift_west_pixels',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_134',
        "command": 'pause',
        "args": [86]
    },
    {
        "identifier": 'EVENT_593_play_music_default_volume_135',
        "command": 'play_music_default_volume',
        "args": [Music._24_GOT_A_STAR_PIECE_PART_2]
    },
    {
        "identifier": 'EVENT_593_remember_last_object_136',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_593_unfreeze_camera_137',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_593_action_queue_async_138',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_async_138_SUBSCRIPT_floating_on_0',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_593_action_queue_async_138_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_139',
        "command": 'pause',
        "args": [240]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_140',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_140_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_140_SUBSCRIPT_shift_z_up_steps_1',
                "command": 'shift_z_up_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_140_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_140_SUBSCRIPT_shift_z_up_steps_3',
                "command": 'shift_z_up_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_140_SUBSCRIPT_shift_z_up_pixels_4',
                "command": 'shift_z_up_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_141',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_141_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [34]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_141_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_141_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_141_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_141_SUBSCRIPT_add_z_coord_1_step_4',
                "command": 'add_z_coord_1_step'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_pause_142',
        "command": 'pause',
        "args": [160]
    },
    {
        "identifier": 'EVENT_593_db_143',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x00, 0x0a, 0xce]
    },
    {
        "identifier": 'EVENT_593_remember_last_object_144',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_593_set_action_script_sync_145',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 120]
    },
    {
        "identifier": 'EVENT_593_pause_146',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'EVENT_593_pause_action_script_147',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_148',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_148_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_148_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_148_SUBSCRIPT_shift_z_up_steps_2',
                "command": 'shift_z_up_steps',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_149',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_149_SUBSCRIPT_transfer_to_object_xy_0',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.NPC_9]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_149_SUBSCRIPT_transfer_xyzf_steps_1',
                "command": 'transfer_xyzf_steps',
                "args": [0, 0, 5, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_149_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_149_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_149_SUBSCRIPT_shift_z_up_steps_4',
                "command": 'shift_z_up_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_remember_last_object_150',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_593_run_star_piece_sequence_151',
        "command": 'run_star_piece_sequence',
        "args": [3]
    },
    {
        "identifier": 'EVENT_593_fade_in_music_152',
        "command": 'fade_in_music',
        "args": [Music._33_MOLEVILLE]
    },
    {
        "identifier": 'EVENT_593_remove_from_current_level_153',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_593_remove_from_current_level_154',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_593_remove_from_current_level_155',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_593_remove_from_current_level_156',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_593_remove_from_level_157',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_9, Rooms._271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    },
    {
        "identifier": 'EVENT_593_remove_from_level_158',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    },
    {
        "identifier": 'EVENT_593_remove_from_level_159',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    },
    {
        "identifier": 'EVENT_593_remove_from_level_160',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    },
    {
        "identifier": 'EVENT_593_db_161',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x72, 0x00, 0x00]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_162',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_162_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 21, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_162_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_163',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_163_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_163_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_163_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_163_SUBSCRIPT_transfer_to_xyzf_3',
                "command": 'transfer_to_xyzf',
                "args": [7, 20, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_164',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_164_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 20, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_164_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_remember_last_object_165',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_593_set_bit_166',
        "command": 'set_bit',
        "args": [0x7049, 6]
    },
    {
        "identifier": 'EVENT_593_run_event_as_subroutine_167',
        "command": 'run_event_as_subroutine',
        "args": [276]
    },
    {
        "identifier": 'EVENT_593_fade_in_from_black_async_168',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_593_pause_169',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_593_run_dialog_170',
        "command": 'run_dialog',
        "args": [3212, AreaObjects.NPC_4, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_593_pause_171',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_172',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_172_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_172_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_172_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_172_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_action_queue_sync_173',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_sync_173_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_173_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_173_SUBSCRIPT_walk_1_step_southeast_2',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_173_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_593_action_queue_sync_173_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_set_action_script_sync_174',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_593_action_queue_async_175',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_593_action_queue_async_175_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_593_remove_from_level_176',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    },
    {
        "identifier": 'EVENT_593_remove_from_level_177',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    },
    {
        "identifier": 'EVENT_593_apply_tile_mod_178',
        "command": 'apply_tile_mod',
        "args": [Rooms._276_MOLEVILLE_MINES_AREA_01_ENTRANCE, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_593_apply_solidity_mod_179',
        "command": 'apply_solidity_mod',
        "args": [Rooms._276_MOLEVILLE_MINES_AREA_01_ENTRANCE, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_593_set_bit_180',
        "command": 'set_bit',
        "args": [0x7063, 6]
    },
    {
        "identifier": 'EVENT_593_store_01_to_0248_181',
        "command": 'store_01_to_0248'
    },
    {
        "identifier": 'EVENT_593_ret_182',
        "command": 'ret'
    }
]
