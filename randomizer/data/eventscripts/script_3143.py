from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3143_freeze_camera_0',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3143_set_7000_to_70A0_short_mem_1',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70aa]
    },
    {
        "identifier": 'EVENT_3143_set_7000_short_mem_to_7000_2',
        "command": 'set_7000_short_mem_to_7000',
        "args": [0x7034]
    },
    {
        "identifier": 'EVENT_3143_enable_controls_until_return_3',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.X, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_3143_start_embedded_action_script_sync_F1_4',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3143_start_embedded_action_script_sync_F1_4_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3143_start_embedded_action_script_sync_F1_4_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0xc8, 0x92]
            },
            {
                "identifier": 'EVENT_3143_start_embedded_action_script_sync_F1_4_SUBSCRIPT_add_short_2',
                "command": 'add_short',
                "args": [0x7016, 0xfffc]
            },
            {
                "identifier": 'EVENT_3143_start_embedded_action_script_sync_F1_4_SUBSCRIPT_add_short_3',
                "command": 'add_short',
                "args": [0x7018, 0xfff2]
            },
            {
                "identifier": 'EVENT_3143_start_embedded_action_script_sync_F1_4_SUBSCRIPT_run_away_shift_4',
                "command": 'run_away_shift'
            }
        ]
    },
    {
        "identifier": 'EVENT_3143_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3143_action_queue_sync_5_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3143_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70AA],
        "subscript": [
            {
                "identifier": 'EVENT_3143_action_queue_sync_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3143_jmp_if_mario_in_air_7',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3143_set_7000_to_pressed_button_11']
    },
    {
        "identifier": 'EVENT_3143_set_7000_to_tapped_button_8',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_3143_jmp_if_7000_all_bits_clear_9',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_3143_set_7000_to_pressed_button_11']
    },
    {
        "identifier": 'EVENT_3143_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3143_action_queue_sync_10_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x9c, 0x04]
            },
            {
                "identifier": 'EVENT_3143_action_queue_sync_10_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [108]
            }
        ]
    },
    {
        "identifier": 'EVENT_3143_set_7000_to_pressed_button_11',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_3143_mem_7000_and_const_12',
        "command": 'mem_7000_and_const',
        "args": [0x000f]
    },
    {
        "identifier": 'EVENT_3143_jmp_if_7000_equals_short_13',
        "command": 'jmp_if_7000_equals_short',
        "args": [1, 'EVENT_3143_set_short_23']
    },
    {
        "identifier": 'EVENT_3143_jmp_if_7000_equals_short_14',
        "command": 'jmp_if_7000_equals_short',
        "args": [5, 'EVENT_3143_set_short_25']
    },
    {
        "identifier": 'EVENT_3143_jmp_if_7000_equals_short_15',
        "command": 'jmp_if_7000_equals_short',
        "args": [4, 'EVENT_3143_set_short_27']
    },
    {
        "identifier": 'EVENT_3143_jmp_if_7000_equals_short_16',
        "command": 'jmp_if_7000_equals_short',
        "args": [6, 'EVENT_3143_set_short_29']
    },
    {
        "identifier": 'EVENT_3143_jmp_if_7000_equals_short_17',
        "command": 'jmp_if_7000_equals_short',
        "args": [2, 'EVENT_3143_set_short_31']
    },
    {
        "identifier": 'EVENT_3143_jmp_if_7000_equals_short_18',
        "command": 'jmp_if_7000_equals_short',
        "args": [10, 'EVENT_3143_set_short_33']
    },
    {
        "identifier": 'EVENT_3143_jmp_if_7000_equals_short_19',
        "command": 'jmp_if_7000_equals_short',
        "args": [8, 'EVENT_3143_set_short_35']
    },
    {
        "identifier": 'EVENT_3143_jmp_if_7000_equals_short_20',
        "command": 'jmp_if_7000_equals_short',
        "args": [9, 'EVENT_3143_set_short_37']
    },
    {
        "identifier": 'EVENT_3143_set_7000_short_mem_to_7000_short_mem_21',
        "command": 'set_7000_short_mem_to_7000_short_mem',
        "args": [0x7032, 0x700c]
    },
    {
        "identifier": 'EVENT_3143_jmp_22',
        "command": 'jmp',
        "args": ['EVENT_3143_set_7000_short_mem_to_7000_short_mem_38']
    },
    {
        "identifier": 'EVENT_3143_set_short_23',
        "command": 'set_short',
        "args": [0x700c, 0x0000]
    },
    {
        "identifier": 'EVENT_3143_jmp_24',
        "command": 'jmp',
        "args": ['EVENT_3143_set_7000_short_mem_to_7000_short_mem_38']
    },
    {
        "identifier": 'EVENT_3143_set_short_25',
        "command": 'set_short',
        "args": [0x700c, 0x0001]
    },
    {
        "identifier": 'EVENT_3143_jmp_26',
        "command": 'jmp',
        "args": ['EVENT_3143_set_7000_short_mem_to_7000_short_mem_38']
    },
    {
        "identifier": 'EVENT_3143_set_short_27',
        "command": 'set_short',
        "args": [0x700c, 0x0002]
    },
    {
        "identifier": 'EVENT_3143_jmp_28',
        "command": 'jmp',
        "args": ['EVENT_3143_set_7000_short_mem_to_7000_short_mem_38']
    },
    {
        "identifier": 'EVENT_3143_set_short_29',
        "command": 'set_short',
        "args": [0x700c, 0x0003]
    },
    {
        "identifier": 'EVENT_3143_jmp_30',
        "command": 'jmp',
        "args": ['EVENT_3143_set_7000_short_mem_to_7000_short_mem_38']
    },
    {
        "identifier": 'EVENT_3143_set_short_31',
        "command": 'set_short',
        "args": [0x700c, 0x0004]
    },
    {
        "identifier": 'EVENT_3143_jmp_32',
        "command": 'jmp',
        "args": ['EVENT_3143_set_7000_short_mem_to_7000_short_mem_38']
    },
    {
        "identifier": 'EVENT_3143_set_short_33',
        "command": 'set_short',
        "args": [0x700c, 0x0005]
    },
    {
        "identifier": 'EVENT_3143_jmp_34',
        "command": 'jmp',
        "args": ['EVENT_3143_set_7000_short_mem_to_7000_short_mem_38']
    },
    {
        "identifier": 'EVENT_3143_set_short_35',
        "command": 'set_short',
        "args": [0x700c, 0x0006]
    },
    {
        "identifier": 'EVENT_3143_jmp_36',
        "command": 'jmp',
        "args": ['EVENT_3143_set_7000_short_mem_to_7000_short_mem_38']
    },
    {
        "identifier": 'EVENT_3143_set_short_37',
        "command": 'set_short',
        "args": [0x700c, 0x0007]
    },
    {
        "identifier": 'EVENT_3143_set_7000_short_mem_to_7000_short_mem_38',
        "command": 'set_7000_short_mem_to_7000_short_mem',
        "args": [0x700c, 0x7032]
    },
    {
        "identifier": 'EVENT_3143_clear_bit_39',
        "command": 'clear_bit',
        "args": [0x7043, 4]
    },
    {
        "identifier": 'EVENT_3143_set_7016_to_object_xyz_40',
        "command": 'set_7016_to_object_xyz',
        "args": [AreaObjects.MEM_70AA]
    },
    {
        "identifier": 'EVENT_3143_start_embedded_action_script_sync_F1_41',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3143_start_embedded_action_script_sync_F1_41_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3143_start_embedded_action_script_sync_F1_41_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3143_start_embedded_action_script_sync_F1_41_SUBSCRIPT_sequence_playback_off_2',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_3143_start_embedded_action_script_sync_F1_41_SUBSCRIPT_shadow_off_3',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_3143_start_embedded_action_script_sync_F1_41_SUBSCRIPT_face_east_7C_4',
                "command": 'face_east_7C'
            },
            {
                "identifier": 'EVENT_3143_start_embedded_action_script_sync_F1_41_SUBSCRIPT_add_short_5',
                "command": 'add_short',
                "args": [0x7016, 0x0030]
            },
            {
                "identifier": 'EVENT_3143_start_embedded_action_script_sync_F1_41_SUBSCRIPT_run_away_transfer_6',
                "command": 'run_away_transfer'
            }
        ]
    },
    {
        "identifier": 'EVENT_3143_pause_42',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3143_jmp_if_bit_set_43',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_3143_set_7000_to_70A0_short_mem_1']
    },
    {
        "identifier": 'EVENT_3143_action_queue_sync_44',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3143_action_queue_sync_44_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._051_MOVING_YELLOW_SWITCH, 4]
            },
            {
                "identifier": 'EVENT_3143_action_queue_sync_44_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3143_set_short_45',
        "command": 'set_short',
        "args": [0x7034, 0x0000]
    },
    {
        "identifier": 'EVENT_3143_enable_controls_until_return_46',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_3143_start_loop_n_times_47',
        "command": 'start_loop_n_times',
        "args": [47]
    },
    {
        "identifier": 'EVENT_3143_jmp_if_mario_in_air_48',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3143_enable_controls_until_return_54']
    },
    {
        "identifier": 'EVENT_3143_pause_49',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3143_end_loop_50',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_3143_jmp_if_mario_in_air_51',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_3143_enable_controls_until_return_54']
    },
    {
        "identifier": 'EVENT_3143_action_queue_sync_52',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3143_action_queue_sync_52_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._051_MOVING_YELLOW_SWITCH, 4]
            },
            {
                "identifier": 'EVENT_3143_action_queue_sync_52_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3143_jmp_53',
        "command": 'jmp',
        "args": ['EVENT_3143_set_7000_to_70A0_short_mem_1']
    },
    {
        "identifier": 'EVENT_3143_enable_controls_until_return_54',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_3143_set_7000_to_70A0_short_mem_55',
        "command": 'set_7000_to_70A0_short_mem',
        "args": [0x70ae]
    },
    {
        "identifier": 'EVENT_3143_set_70A0_short_mem_to_7000_56',
        "command": 'set_70A0_short_mem_to_7000',
        "args": [0x70aa]
    },
    {
        "identifier": 'EVENT_3143_enable_trigger_57',
        "command": 'enable_trigger',
        "args": [AreaObjects.MEM_70AA]
    },
    {
        "identifier": 'EVENT_3143_unfreeze_camera_58',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_3143_start_embedded_action_script_sync_F1_59',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3143_start_embedded_action_script_sync_F1_59_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3143_start_embedded_action_script_sync_F1_60',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.MEM_70AA],
        "subscript": [
            {
                "identifier": 'EVENT_3143_start_embedded_action_script_sync_F1_60_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3143_start_embedded_action_script_sync_F1_60_SUBSCRIPT_object_memory_clear_bit_1',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3143_set_61',
        "command": 'set',
        "args": [0x70aa, 0]
    },
    {
        "identifier": 'EVENT_3143_action_queue_async_62',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3143_action_queue_async_62_SUBSCRIPT_sequence_playback_on_0',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_3143_action_queue_async_62_SUBSCRIPT_object_memory_modify_bits_1',
                "command": 'object_memory_modify_bits',
                "args": [0x09, [5], [4, 6]]
            },
            {
                "identifier": 'EVENT_3143_action_queue_async_62_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3143_action_queue_async_62_SUBSCRIPT_shadow_on_3',
                "command": 'shadow_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3143_ret_63',
        "command": 'ret'
    }
]
