
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1119_freeze_camera_0',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_1_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [14, 58, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_1_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_1_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_1_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_1_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_2_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [13, 56, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_2_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_2_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_2_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_2_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_3_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [13, 57, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_3_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_3_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_3_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_3_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_4_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [14, 59, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_4_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_4_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_4_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_4_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_5_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [15, 60, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_5_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_5_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_5_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_5_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_6_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [12, 63, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_6_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_6_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 147]
    },
    {
        "identifier": 'EVENT_1119_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 147]
    },
    {
        "identifier": 'EVENT_1119_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 147]
    },
    {
        "identifier": 'EVENT_1119_set_action_script_sync_10',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 147]
    },
    {
        "identifier": 'EVENT_1119_set_action_script_sync_11',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 147]
    },
    {
        "identifier": 'EVENT_1119_fade_in_from_black_async_12',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_13_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_13_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_13_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_13_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_13_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_13_SUBSCRIPT_shift_northeast_pixels_5',
                "command": 'shift_northeast_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_pause_14',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_15_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_15_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_pause_16',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1119_unfreeze_camera_17',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_1119_run_dialog_18',
        "command": 'run_dialog',
        "args": [2850, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1119_pause_script_resume_on_next_dialog_page_a_FD61_19',
        "command": 'pause_script_resume_on_next_dialog_page_a_FD61'
    },
    {
        "identifier": 'EVENT_1119_pause_script_resume_on_next_dialog_page_a_FD61_20',
        "command": 'pause_script_resume_on_next_dialog_page_a_FD61'
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_21_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [85]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_21_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_unsync_dialog_22',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_1119_close_dialog_23',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1119_pause_24',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1119_run_dialog_25',
        "command": 'run_dialog',
        "args": [2851, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1119_run_dialog_26',
        "command": 'run_dialog',
        "args": [2852, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1119_pause_27',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1119_jmp_if_dialog_option_b_28',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1119_jmp_if_var_equals_byte_30']
    },
    {
        "identifier": 'EVENT_1119_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_1118_pause_0']
    },
    {
        "identifier": 'EVENT_1119_jmp_if_var_equals_byte_30',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70bc, 1, 'EVENT_1119_pause_54']
    },
    {
        "identifier": 'EVENT_1119_jmp_if_var_equals_byte_31',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70bc, 2, 'EVENT_1119_pause_76']
    },
    {
        "identifier": 'EVENT_1119_jmp_if_var_equals_byte_32',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70bc, 3, 'EVENT_1119_pause_76']
    },
    {
        "identifier": 'EVENT_1119_pause_33',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1119_run_dialog_34',
        "command": 'run_dialog',
        "args": [2853, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_35',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_35_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_36',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_36_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_36_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_pause_37',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_38',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_38_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_38_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_38_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_39',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_39_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_39_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_39_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_39_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [17]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_39_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_39_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_apply_tile_mod_40',
        "command": 'apply_tile_mod',
        "args": [Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1119_pause_41',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1119_run_dialog_42',
        "command": 'run_dialog',
        "args": [2854, AreaObjects.NPC_13, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1119_pause_43',
        "command": 'pause',
        "args": [100]
    },
    {
        "identifier": 'EVENT_1119_apply_tile_mod_44',
        "command": 'apply_tile_mod',
        "args": [Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, 33, []]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_45',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_45_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_45_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_45_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_46',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_46_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 40, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_46_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_46_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_46_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_46_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_46_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_46_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [17]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_46_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_46_SUBSCRIPT_face_southwest_8',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_pause_47',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_48',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_48_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_49',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_49_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_set_50',
        "command": 'set',
        "args": [0x70bc, 1]
    },
    {
        "identifier": 'EVENT_1119_pause_51',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1119_run_dialog_52',
        "command": 'run_dialog',
        "args": [2855, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1119_jmp_53',
        "command": 'jmp',
        "args": ['EVENT_1119_run_dialog_26']
    },
    {
        "identifier": 'EVENT_1119_pause_54',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_55',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_55_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_56',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_56_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_56_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_pause_57',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_58',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_58_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_58_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_58_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_59',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_59_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_59_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_59_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_59_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [17]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_59_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_59_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_60',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_60_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_60_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_60_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_60_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [18]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_60_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_60_SUBSCRIPT_visibility_off_5',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_apply_tile_mod_61',
        "command": 'apply_tile_mod',
        "args": [Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1119_pause_62',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1119_run_dialog_63',
        "command": 'run_dialog',
        "args": [2856, AreaObjects.NPC_13, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1119_pause_64',
        "command": 'pause',
        "args": [100]
    },
    {
        "identifier": 'EVENT_1119_apply_tile_mod_65',
        "command": 'apply_tile_mod',
        "args": [Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, 33, []]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_66',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_66_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_66_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_66_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_67',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_67_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 40, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_67_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_67_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_67_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_67_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_67_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_67_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [18]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_67_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_67_SUBSCRIPT_face_southwest_8',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_68',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_68_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_68_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [5, 40, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_68_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_68_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_68_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_68_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_68_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_68_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [17]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_68_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_68_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_pause_69',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_70',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_70_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_71',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_71_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_set_72',
        "command": 'set',
        "args": [0x70bc, 2]
    },
    {
        "identifier": 'EVENT_1119_pause_73',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1119_run_dialog_74',
        "command": 'run_dialog',
        "args": [2855, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1119_jmp_75',
        "command": 'jmp',
        "args": ['EVENT_1119_run_dialog_26']
    },
    {
        "identifier": 'EVENT_1119_pause_76',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_77',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_77_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_78',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_78_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_78_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_pause_79',
        "command": 'pause',
        "args": [15]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_80',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_80_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_80_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_80_SUBSCRIPT_shift_northwest_steps_2',
                "command": 'shift_northwest_steps',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_81',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_81_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_81_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_81_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_81_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [17]
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_82',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_82_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_82_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_82_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_82_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [17]
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_83',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_83_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_83_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_83_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_83_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [18]
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_84',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_84_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_84_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_84_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_84_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [18]
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_apply_tile_mod_85',
        "command": 'apply_tile_mod',
        "args": [Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, 33, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_86',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_86_SUBSCRIPT_shift_northeast_steps_0',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_86_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_87',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_87_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_87_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_87_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_88',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_88_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_88_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_88_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_89',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_89_SUBSCRIPT_shift_northwest_steps_0',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_89_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_89_SUBSCRIPT_visibility_off_2',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_pause_90',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1119_jmp_if_var_equals_byte_91',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70bc, 3, 'EVENT_1119_run_dialog_95']
    },
    {
        "identifier": 'EVENT_1119_run_dialog_92',
        "command": 'run_dialog',
        "args": [2857, AreaObjects.NPC_13, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1119_pause_93',
        "command": 'pause',
        "args": [100]
    },
    {
        "identifier": 'EVENT_1119_jmp_94',
        "command": 'jmp',
        "args": ['EVENT_1119_apply_tile_mod_97']
    },
    {
        "identifier": 'EVENT_1119_run_dialog_95',
        "command": 'run_dialog',
        "args": [2858, AreaObjects.NPC_13, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1119_pause_96',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1119_apply_tile_mod_97',
        "command": 'apply_tile_mod',
        "args": [Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, 33, []]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_98',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_98_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_98_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_98_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [15]
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_99',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_99_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 40, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_99_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_99_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_99_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_99_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_99_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_99_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [21]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_99_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_99_SUBSCRIPT_face_southwest_8',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_100',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_100_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_100_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [5, 40, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_100_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_100_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_100_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_100_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_100_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_100_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_100_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_100_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_sync_101',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_sync_101_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_101_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [5, 40, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_101_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_101_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_101_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_101_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_101_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_101_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [18]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_101_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_sync_101_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_102',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_102_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_102_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [5, 40, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_102_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_102_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_102_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_102_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_102_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_102_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [17]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_102_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1119_action_queue_async_102_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_pause_103',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_104',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_104_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_action_queue_async_105',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1119_action_queue_async_105_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1119_set_106',
        "command": 'set',
        "args": [0x70bc, 3]
    },
    {
        "identifier": 'EVENT_1119_pause_107',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1119_run_dialog_108',
        "command": 'run_dialog',
        "args": [2855, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1119_jmp_109',
        "command": 'jmp',
        "args": ['EVENT_1119_run_dialog_26']
    }
]
