from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3601_set_short_0',
        "command": 'set_short',
        "args": [0x703e, 0x0003],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_set_action_script_sync_1',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 288],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 289],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_unsync_action_script_3',
        "command": 'unsync_action_script',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_apply_solidity_mod_4',
        "command": 'apply_solidity_mod',
        "args": [Rooms._034_YOSTER_ISLE, 2, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_apply_solidity_mod_5',
        "command": 'apply_solidity_mod',
        "args": [Rooms._034_YOSTER_ISLE, 4, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_apply_solidity_mod_6',
        "command": 'apply_solidity_mod',
        "args": [Rooms._034_YOSTER_ISLE, 6, [_0x6BFlags.PERMANENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3601_action_queue_async_7_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3601_pause_8',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_pause_script_until_effect_done_9',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_run_dialog_10',
        "command": 'run_dialog',
        "args": [944, AreaObjects.NPC_9, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_pause_11',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_set_action_script_async_12',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_pause_13',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_freeze_camera_14',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_3601_action_queue_sync_15_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3601_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3601_action_queue_async_16_SUBSCRIPT_shift_southeast_steps_0',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3601_action_queue_async_16_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3601_action_queue_async_16_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [13, 84]
            },
            {
                "identifier": 'EVENT_3601_action_queue_async_16_SUBSCRIPT_face_northwest_3',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3601_run_background_event_17',
        "command": 'run_background_event',
        "args": [465, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_pause_18',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_jmp_if_audio_memory_equals_19',
        "command": 'jmp_if_audio_memory_equals',
        "args": [3, 'EVENT_3601_pause_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3601_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3601_set_action_script_sync_21',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.SCREEN_FOCUS, 801],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_set_action_script_async_22',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 636],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_pause_23',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3601_action_queue_async_24_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3601_action_queue_async_24_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3601_action_queue_async_24_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3601_action_queue_async_24_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3601_action_queue_async_24_SUBSCRIPT_face_west_4',
                "command": 'face_west',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3601_pause_25',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_set_short_mem_26',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7014],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_mem_compare_27',
        "command": 'mem_compare',
        "args": [0x7000, 17],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_jmp_if_comparison_result_is_lesser_28',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3601_set_action_script_async_29'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_set_action_script_async_29',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 798],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_set_action_script_sync_30',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.SCREEN_FOCUS, 801],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3601_action_queue_async_31_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3601_action_queue_async_31_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3601_action_queue_async_31_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3601_action_queue_async_31_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3601_action_queue_async_31_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3601_action_queue_async_31_SUBSCRIPT_fixed_f_coord_off_5',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3601_action_queue_async_31_SUBSCRIPT_face_west_6',
                "command": 'face_west',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3601_pause_32',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_set_short_mem_33',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7014],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_mem_compare_34',
        "command": 'mem_compare',
        "args": [0x7000, 12],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_jmp_if_comparison_result_is_lesser_35',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3601_set_action_script_async_37'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_jmp_36',
        "command": 'jmp',
        "args": ['EVENT_3601_pause_32'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_set_action_script_async_37',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 798],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_set_action_script_sync_38',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.SCREEN_FOCUS, 801],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_action_queue_async_39',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3601_action_queue_async_39_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3601_action_queue_async_39_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3601_action_queue_async_39_SUBSCRIPT_sequence_looping_on_2',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3601_action_queue_async_39_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3601_action_queue_async_39_SUBSCRIPT_sequence_looping_off_4',
                "command": 'sequence_looping_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3601_action_queue_async_39_SUBSCRIPT_fixed_f_coord_off_5',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3601_action_queue_async_39_SUBSCRIPT_face_west_6',
                "command": 'face_west',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3601_pause_40',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_set_short_mem_41',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7014],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_mem_compare_42',
        "command": 'mem_compare',
        "args": [0x7000, 8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_jmp_if_comparison_result_is_lesser_43',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_3601_set_action_script_async_44'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_set_action_script_async_44',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 802],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_pause_45',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_jmp_if_var_equals_short_46',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7014, 0, 'EVENT_3601_clear_bit_48'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_jmp_47',
        "command": 'jmp',
        "args": ['EVENT_3601_pause_45'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_clear_bit_48',
        "command": 'clear_bit',
        "args": [0x7085, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_jmp_if_bit_set_49',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 7, 'EVENT_3600_jmp_if_bit_clear_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_jmp_if_bit_set_50',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 6, 'EVENT_3600_jmp_if_bit_clear_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_jmp_if_bit_set_51',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'EVENT_3600_jmp_if_bit_clear_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_start_embedded_action_script_async_52',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3601_start_embedded_action_script_async_52_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3601_unsync_action_script_53',
        "command": 'unsync_action_script',
        "args": [AreaObjects.NPC_9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_start_embedded_action_script_async_54',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3601_start_embedded_action_script_async_54_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3601_set_action_script_sync_55',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 677],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_set_action_script_sync_56',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 677],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3601_jmp_57',
        "command": 'jmp',
        "args": ['EVENT_3600_action_queue_sync_21'],
        "subscript": []
    }
]
