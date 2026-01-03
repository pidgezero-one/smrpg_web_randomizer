
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_382_action_queue_async_0',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_async_0_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_382_action_queue_async_0_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_382_action_queue_async_0_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_382_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 7, 'EVENT_382_jmp_if_bit_clear_70']
    },
    {
        "identifier": 'EVENT_382_jmp_if_object_not_in_level_2',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.NPC_4, Rooms._325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL, 'EVENT_382_jmp_if_object_in_level_5']
    },
    {
        "identifier": 'EVENT_382_fade_in_from_black_async_3',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_382_ret_4',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_382_jmp_if_object_in_level_5',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_1, Rooms._327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, 'EVENT_257_fade_in_from_black_async_0']
    },
    {
        "identifier": 'EVENT_382_jmp_if_bit_set_6',
        "command": 'jmp_if_bit_set',
        "args": [0x7082, 5, 'EVENT_382_action_queue_async_75']
    },
    {
        "identifier": 'EVENT_382_pause_action_script_7',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_1]
    },
    {
        "identifier": 'EVENT_382_pause_action_script_8',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_382_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_sync_9_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_sync_10_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_async_11_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [3, 67, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_382_fade_in_from_black_sync_12',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_382_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_async_13_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_382_action_queue_async_13_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_pause_script_until_effect_done_14',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_382_run_dialog_15',
        "command": 'run_dialog',
        "args": [663, AreaObjects.NPC_3, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_382_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_async_16_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_async_17_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_async_18_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_382_action_queue_async_18_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_382_action_queue_async_18_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_382_action_queue_async_18_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_sync_19_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 99]
    },
    {
        "identifier": 'EVENT_382_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_async_21_SUBSCRIPT_face_east_0',
                "command": 'face_east'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_remember_last_object_22',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_382_run_dialog_23',
        "command": 'run_dialog',
        "args": [664, AreaObjects.NPC_3, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_382_pause_action_script_24',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_382_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_sync_25_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_382_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_async_26_SUBSCRIPT_walk_1_step_northwest_0',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_382_action_queue_async_26_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_async_27_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_run_dialog_28',
        "command": 'run_dialog',
        "args": [662, AreaObjects.NPC_3, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_382_pause_29',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_382_set_action_script_async_30',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_382_pause_31',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_382_action_queue_sync_32',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_sync_32_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_382_action_queue_sync_32_SUBSCRIPT_walk_1_step_northwest_1',
                "command": 'walk_1_step_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_sync_33_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_382_action_queue_sync_33_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_async_34_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_382_action_queue_async_34_SUBSCRIPT_face_east_1',
                "command": 'face_east'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_run_dialog_35',
        "command": 'run_dialog',
        "args": [659, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_382_remember_last_object_36',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_382_set_action_script_sync_37',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 99]
    },
    {
        "identifier": 'EVENT_382_pause_38',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_382_run_dialog_39',
        "command": 'run_dialog',
        "args": [665, AreaObjects.NPC_4, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_382_pause_action_script_40',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_382_set_41',
        "command": 'set',
        "args": [0x70a9, 23]
    },
    {
        "identifier": 'EVENT_382_run_event_as_subroutine_42',
        "command": 'run_event_as_subroutine',
        "args": [278]
    },
    {
        "identifier": 'EVENT_382_action_queue_sync_43',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_sync_43_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_382_action_queue_sync_43_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_382_action_queue_sync_43_SUBSCRIPT_face_northwest_2',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_action_queue_async_44',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_async_44_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_remember_last_object_45',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_382_run_dialog_46',
        "command": 'run_dialog',
        "args": [666, AreaObjects.NPC_3, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_382_jmp_if_dialog_option_b_47',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_382_pause_78']
    },
    {
        "identifier": 'EVENT_382_pause_48',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_382_set_action_script_async_49',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_382_pause_50',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_382_set_action_script_sync_51',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 99]
    },
    {
        "identifier": 'EVENT_382_run_dialog_52',
        "command": 'run_dialog',
        "args": [698, AreaObjects.NPC_3, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_382_pause_action_script_53',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_3]
    },
    {
        "identifier": 'EVENT_382_set_54',
        "command": 'set',
        "args": [0x70a9, 23]
    },
    {
        "identifier": 'EVENT_382_run_event_as_subroutine_55',
        "command": 'run_event_as_subroutine',
        "args": [278]
    },
    {
        "identifier": 'EVENT_382_action_queue_sync_56',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_sync_56_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_382_action_queue_sync_56_SUBSCRIPT_floating_on_1',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_382_action_queue_sync_56_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_382_action_queue_sync_56_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_382_action_queue_sync_56_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_382_action_queue_sync_56_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_382_action_queue_sync_56_SUBSCRIPT_face_northwest_6',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_action_queue_sync_57',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_sync_57_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_382_action_queue_sync_57_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_382_action_queue_sync_57_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_382_action_queue_sync_57_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_action_queue_sync_58',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_sync_58_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_382_action_queue_sync_58_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_382_action_queue_sync_58_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_382_action_queue_sync_58_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_action_queue_sync_59',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_sync_59_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_382_action_queue_sync_59_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_382_action_queue_sync_59_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [120]
            },
            {
                "identifier": 'EVENT_382_action_queue_sync_59_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_remember_last_object_60',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_382_run_dialog_61',
        "command": 'run_dialog',
        "args": [699, AreaObjects.NPC_3, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_382_play_sound_62',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6]
    },
    {
        "identifier": 'EVENT_382_set_63',
        "command": 'set',
        "args": [0x70a7, 115]
    },
    {
        "identifier": 'EVENT_382_run_dialog_64',
        "command": 'run_dialog',
        "args": [524, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]]
    },
    {
        "identifier": 'EVENT_382_put_inventory_65',
        "command": 'put_inventory',
        "args": [items.FlowerTab]
    },
    {
        "identifier": 'EVENT_382_remember_last_object_66',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_382_action_queue_async_67',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_async_67_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_382_action_queue_async_67_SUBSCRIPT_face_south_1',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_set_bit_68',
        "command": 'set_bit',
        "args": [0x7082, 5]
    },
    {
        "identifier": 'EVENT_382_ret_69',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_382_jmp_if_bit_clear_70',
        "command": 'jmp_if_bit_clear',
        "args": [0x7082, 5, 'EVENT_382_run_event_as_subroutine_72']
    },
    {
        "identifier": 'EVENT_382_action_queue_async_71',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_async_71_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 63, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_382_action_queue_async_71_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_run_event_as_subroutine_72',
        "command": 'run_event_as_subroutine',
        "args": [81]
    },
    {
        "identifier": 'EVENT_382_ret_73',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_382_jmp_if_object_in_level_74',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_1, Rooms._327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, 'EVENT_257_fade_in_from_black_async_0']
    },
    {
        "identifier": 'EVENT_382_action_queue_async_75',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_async_75_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 63, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_382_action_queue_async_75_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_fade_in_from_black_async_76',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_382_ret_77',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_382_pause_78',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_382_action_queue_async_79',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_382_action_queue_async_79_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_382_run_dialog_80',
        "command": 'run_dialog',
        "args": [701, AreaObjects.NPC_3, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_382_set_bit_81',
        "command": 'set_bit',
        "args": [0x7082, 5]
    },
    {
        "identifier": 'EVENT_382_ret_82',
        "command": 'ret'
    }
]
