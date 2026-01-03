
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2606_freeze_camera_0',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2606_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2606_action_queue_sync_1_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [5, 20]
            }
        ]
    },
    {
        "identifier": 'EVENT_2606_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2606_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2606_action_queue_sync_2_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_2606_action_queue_sync_2_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2606_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2606_action_queue_sync_3_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [10, 47]
            },
            {
                "identifier": 'EVENT_2606_action_queue_sync_3_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2606_run_dialog_4',
        "command": 'run_dialog',
        "args": [3248, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2606_stop_embedded_action_script_5',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_2606_stop_embedded_action_script_6',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.SCREEN_FOCUS]
    },
    {
        "identifier": 'EVENT_2606_summon_to_current_level_at_marios_coords_7',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_2606_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2606_action_queue_async_8_SUBSCRIPT_walk_1_step_north_0',
                "command": 'walk_1_step_north'
            },
            {
                "identifier": 'EVENT_2606_action_queue_async_8_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2606_action_queue_async_8_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [8, 1, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2606_run_dialog_9',
        "command": 'run_dialog',
        "args": [3249, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2606_pause_script_resume_on_next_dialog_page_a_FD61_10',
        "command": 'pause_script_resume_on_next_dialog_page_a_FD61'
    },
    {
        "identifier": 'EVENT_2606_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2606_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [5, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2606_unsync_dialog_12',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_2606_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2606_action_queue_async_13_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2606_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2606_action_queue_async_13_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_2606_action_queue_async_13_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2606_action_queue_async_13_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2606_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2606_action_queue_sync_14_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_2606_action_queue_sync_14_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2606_run_dialog_15',
        "command": 'run_dialog',
        "args": [3252, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2606_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2606_action_queue_async_16_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2606_action_queue_async_16_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2606_action_queue_async_16_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [17, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2606_run_dialog_17',
        "command": 'run_dialog',
        "args": [3253, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2606_pause_script_resume_on_next_dialog_page_a_FD61_18',
        "command": 'pause_script_resume_on_next_dialog_page_a_FD61'
    },
    {
        "identifier": 'EVENT_2606_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2606_action_queue_sync_19_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2606_pause_script_resume_on_next_dialog_page_a_FD61_20',
        "command": 'pause_script_resume_on_next_dialog_page_a_FD61'
    },
    {
        "identifier": 'EVENT_2606_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2606_action_queue_async_21_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2606_action_queue_async_21_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2606_unsync_dialog_22',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_2606_pause_23',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2606_action_queue_sync_24',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2606_action_queue_sync_24_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2606_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2606_action_queue_sync_25_SUBSCRIPT_shift_northwest_pixels_0',
                "command": 'shift_northwest_pixels',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_2606_run_dialog_26',
        "command": 'run_dialog',
        "args": [3250, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2606_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2606_action_queue_sync_27_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2606_action_queue_sync_27_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2606_action_queue_sync_27_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2606_action_queue_async_28',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2606_action_queue_async_28_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2606_action_queue_async_28_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2606_action_queue_async_28_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2606_start_battle_29',
        "command": 'start_battle',
        "args": [0x0096, 48]
    },
    {
        "identifier": 'EVENT_2606_jmp_if_bit_clear_30',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_2606_remove_from_current_level_32']
    },
    {
        "identifier": 'EVENT_2606_reset_and_choose_game_31',
        "command": 'reset_and_choose_game'
    },
    {
        "identifier": 'EVENT_2606_remove_from_current_level_32',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_2606_remove_from_current_level_33',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_2606_remove_from_level_34',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._469_FACTORY_GROUNDS_AREA_01]
    },
    {
        "identifier": 'EVENT_2606_remove_from_level_35',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._469_FACTORY_GROUNDS_AREA_01]
    },
    {
        "identifier": 'EVENT_2606_action_queue_async_36',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2606_action_queue_async_36_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2606_action_queue_async_36_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2606_action_queue_async_36_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2606_fade_in_from_black_async_37',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2606_action_queue_sync_38',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2606_action_queue_sync_38_SUBSCRIPT_shift_southeast_pixels_0',
                "command": 'shift_southeast_pixels',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_2606_pause_39',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2606_run_dialog_40',
        "command": 'run_dialog',
        "args": [3251, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2606_start_battle_41',
        "command": 'start_battle',
        "args": [0x0092, 48]
    },
    {
        "identifier": 'EVENT_2606_jmp_if_bit_clear_42',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_2606_restore_all_hp_44']
    },
    {
        "identifier": 'EVENT_2606_reset_and_choose_game_43',
        "command": 'reset_and_choose_game'
    },
    {
        "identifier": 'EVENT_2606_restore_all_hp_44',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_2606_restore_all_fp_45',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_2606_remove_from_current_level_46',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_2606_remove_from_level_47',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_9, Rooms._469_FACTORY_GROUNDS_AREA_01]
    },
    {
        "identifier": 'EVENT_2606_enter_area_48',
        "command": 'enter_area',
        "args": [Rooms._406_FACTORY_GROUNDS_AREA_01_WITH_TOAD, RadialDirections.NORTHWEST, 10, 47, 5, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2606_ret_49',
        "command": 'ret'
    }
]
