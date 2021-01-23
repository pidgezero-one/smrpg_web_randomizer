from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1709_set_short_0',
        "command": 'set_short',
        "args": [0x7030, 0x0064]
    },
    {
        "identifier": 'EVENT_1709_set_short_1',
        "command": 'set_short',
        "args": [0x7032, 0x0000]
    },
    {
        "identifier": 'EVENT_1709_start_loop_n_times_2',
        "command": 'start_loop_n_times',
        "args": [239]
    },
    {
        "identifier": 'EVENT_1709_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1709_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'EVENT_1709_jmp_to_subroutine_17']
    },
    {
        "identifier": 'EVENT_1709_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'EVENT_1709_jmp_to_subroutine_22']
    },
    {
        "identifier": 'EVENT_1709_end_loop_6',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1709_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1709_action_queue_async_7_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_7_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_7_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_7_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [27]
            }
        ]
    },
    {
        "identifier": 'EVENT_1709_jmp_to_subroutine_8',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1709_enable_controls_until_return_43']
    },
    {
        "identifier": 'EVENT_1709_stop_embedded_action_script_9',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_5]
    },
    {
        "identifier": 'EVENT_1709_stop_embedded_action_script_10',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_6]
    },
    {
        "identifier": 'EVENT_1709_stop_embedded_action_script_11',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_1709_enable_controls_until_return_12',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1709_clear_bit_13',
        "command": 'clear_bit',
        "args": [0x7044, 4]
    },
    {
        "identifier": 'EVENT_1709_clear_bit_14',
        "command": 'clear_bit',
        "args": [0x7044, 5]
    },
    {
        "identifier": 'EVENT_1709_run_event_as_subroutine_15',
        "command": 'run_event_as_subroutine',
        "args": [1707]
    },
    {
        "identifier": 'EVENT_1709_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_1709_start_loop_n_times_2']
    },
    {
        "identifier": 'EVENT_1709_jmp_to_subroutine_17',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1709_enable_controls_until_return_43']
    },
    {
        "identifier": 'EVENT_1709_jmp_to_subroutine_18',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1709_action_queue_async_52']
    },
    {
        "identifier": 'EVENT_1709_enable_controls_until_return_19',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1709_play_sound_20',
        "command": 'play_sound',
        "args": [Sounds._011_WHOOSH_AWAY, 6]
    },
    {
        "identifier": 'EVENT_1709_jmp_21',
        "command": 'jmp',
        "args": ['EVENT_1709_clear_bit_13']
    },
    {
        "identifier": 'EVENT_1709_jmp_to_subroutine_22',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1709_enable_controls_until_return_43']
    },
    {
        "identifier": 'EVENT_1709_inc_short_23',
        "command": 'inc_short',
        "args": [0x7032]
    },
    {
        "identifier": 'EVENT_1709_jmp_if_var_equals_short_24',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7032, 3, 'EVENT_1709_run_event_at_return_33']
    },
    {
        "identifier": 'EVENT_1709_jmp_to_subroutine_25',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_1709_action_queue_async_55']
    },
    {
        "identifier": 'EVENT_1709_set_short_mem_26',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7030]
    },
    {
        "identifier": 'EVENT_1709_set_short_mem_27',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7030]
    },
    {
        "identifier": 'EVENT_1709_add_28',
        "command": 'add',
        "args": [0x7000, 65486]
    },
    {
        "identifier": 'EVENT_1709_set_short_mem_29',
        "command": 'set_short_mem',
        "args": [0x7030, 0x7000]
    },
    {
        "identifier": 'EVENT_1709_enable_controls_until_return_30',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1709_play_sound_31',
        "command": 'play_sound',
        "args": [Sounds._011_WHOOSH_AWAY, 6]
    },
    {
        "identifier": 'EVENT_1709_jmp_32',
        "command": 'jmp',
        "args": ['EVENT_1709_clear_bit_13']
    },
    {
        "identifier": 'EVENT_1709_run_event_at_return_33',
        "command": 'run_event_at_return',
        "args": [1710]
    },
    {
        "identifier": 'EVENT_1709_stop_sound_34',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1709_stop_sound_35',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1709_stop_sound_36',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1709_stop_sound_37',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1709_stop_sound_38',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1709_stop_sound_39',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1709_stop_sound_40',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1709_stop_sound_41',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_1709_ret_42',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1709_enable_controls_until_return_43',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1709_set_44',
        "command": 'set',
        "args": [0x70ab, 25]
    },
    {
        "identifier": 'EVENT_1709_start_loop_n_times_45',
        "command": 'start_loop_n_times',
        "args": [2]
    },
    {
        "identifier": 'EVENT_1709_pause_action_script_46',
        "command": 'pause_action_script',
        "args": [AreaObjects.MEM_70AB]
    },
    {
        "identifier": 'EVENT_1709_jmp_if_present_in_current_level_47',
        "command": 'jmp_if_present_in_current_level',
        "args": [AreaObjects.MEM_70AB, 'EVENT_1709_inc_49']
    },
    {
        "identifier": 'EVENT_1709_start_embedded_action_script_sync_F1_48',
        "command": 'start_embedded_action_script_sync_F1',
        "args": [AreaObjects.MEM_70AB],
        "subscript": [
            {
                "identifier": 'EVENT_1709_start_embedded_action_script_sync_F1_48_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1709_start_embedded_action_script_sync_F1_48_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1709_start_embedded_action_script_sync_F1_48_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1709_start_embedded_action_script_sync_F1_48_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1709_start_embedded_action_script_sync_F1_48_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1709_inc_49',
        "command": 'inc',
        "args": [0x70ab]
    },
    {
        "identifier": 'EVENT_1709_end_loop_50',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1709_ret_51',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1709_action_queue_async_52',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1709_action_queue_async_52_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_52_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_52_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_52_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [27]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_52_SUBSCRIPT_face_mario_4',
                "command": 'face_mario'
            }
        ]
    },
    {
        "identifier": 'EVENT_1709_action_queue_async_53',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1709_action_queue_async_53_SUBSCRIPT_face_southwest_7D_0',
                "command": 'face_southwest_7D',
                "args": [0x1c]
            }
        ]
    },
    {
        "identifier": 'EVENT_1709_ret_54',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1709_action_queue_async_55',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1709_action_queue_async_55_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_55_SUBSCRIPT_play_sound_1',
                "command": 'play_sound',
                "args": [Sounds._030_SURPRISED_MONSTER, 4]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_55_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_55_SUBSCRIPT_shift_z_up_pixels_3',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_55_SUBSCRIPT_shift_z_down_pixels_4',
                "command": 'shift_z_down_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_55_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_55_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_55_SUBSCRIPT_stop_sound_7',
                "command": 'stop_sound'
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_55_SUBSCRIPT_face_mario_8',
                "command": 'face_mario'
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_55_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_55_SUBSCRIPT_play_sound_10',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_55_SUBSCRIPT_clear_solidity_bits_11',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_55_SUBSCRIPT_jump_to_height_12',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_55_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [27]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_55_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_55_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_55_SUBSCRIPT_fixed_f_coord_on_16',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_55_SUBSCRIPT_walk_1_step_south_17',
                "command": 'walk_1_step_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_1709_action_queue_async_56',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1709_action_queue_async_56_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_56_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_56_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0xc8, 0x1c]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_56_SUBSCRIPT_add_short_3',
                "command": 'add_short',
                "args": [0x7016, 0x0100]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_56_SUBSCRIPT_add_short_4',
                "command": 'add_short',
                "args": [0x7018, 0x0080]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_56_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0xfd, 0xc7]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_56_SUBSCRIPT_db_6',
                "command": 'db',
                "args": [0x98]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_56_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_56_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_56_SUBSCRIPT_set_solidity_bits_9',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1709_action_queue_async_57',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1709_action_queue_async_57_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1709_action_queue_async_57_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_1709_ret_58',
        "command": 'ret'
    }
]
