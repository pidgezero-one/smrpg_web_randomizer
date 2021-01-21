from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3688_set_7010_to_object_xyz_0',
        "command": 'set_7010_to_object_xyz',
        "args": [0x80]
    },
    {
        "identifier": 'EVENT_3688_mem_compare_1',
        "command": 'mem_compare',
        "args": [0x7014, 2]
    },
    {
        "identifier": 'EVENT_3688_jmp_if_comparison_result_is_greater_or_equal_2',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3688_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._143_METRONOME_UPBEAT_DING, 6]
    },
    {
        "identifier": 'EVENT_3688_pause_4',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_3688_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._143_METRONOME_UPBEAT_DING, 6]
    },
    {
        "identifier": 'EVENT_3688_pause_6',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'EVENT_3688_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._143_METRONOME_UPBEAT_DING, 6]
    },
    {
        "identifier": 'EVENT_3688_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 5, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3688_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x709f, 0, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3688_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x709f, 1, 'EVENT_3584_ret_0']
    },
    {
        "identifier": 'EVENT_3688_set_bit_11',
        "command": 'set_bit',
        "args": [0x709f, 0]
    },
    {
        "identifier": 'EVENT_3688_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3688_action_queue_sync_12_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3688_action_queue_sync_12_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3688_action_queue_sync_12_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [6, 22]
            },
            {
                "identifier": 'EVENT_3688_action_queue_sync_12_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3688_action_queue_sync_12_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3688_pause_13',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_3688_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3688_action_queue_async_14_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_14_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_14_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [3, 23, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_14_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_14_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_14_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_14_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_14_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_14_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_14_SUBSCRIPT_set_solidity_bits_9',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3688_pause_15',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3688_run_dialog_16',
        "command": 'run_dialog',
        "args": [3846, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3688_jmp_if_dialog_option_b_17',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_3688_close_dialog_34']
    },
    {
        "identifier": 'EVENT_3688_run_dialog_18',
        "command": 'run_dialog',
        "args": [3847, AreaObjects.NPC_14, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3688_jmp_if_dialog_option_b_or_c_19',
        "command": 'jmp_if_dialog_option_b_or_c',
        "args": ['EVENT_3688_set_short_41', 'EVENT_3688_close_dialog_34']
    },
    {
        "identifier": 'EVENT_3688_set_short_20',
        "command": 'set_short',
        "args": [0x7024, 0x000a]
    },
    {
        "identifier": 'EVENT_3688_run_event_as_subroutine_21',
        "command": 'run_event_as_subroutine',
        "args": [274]
    },
    {
        "identifier": 'EVENT_3688_jmp_if_bit_set_22',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 3, 'EVENT_3688_run_dialog_52']
    },
    {
        "identifier": 'EVENT_3688_run_dialog_23',
        "command": 'run_dialog',
        "args": [3849, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3688_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3688_action_queue_async_24_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_24_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_24_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_24_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_24_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_24_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_24_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_24_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_24_SUBSCRIPT_shift_southeast_steps_8',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_24_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3688_pause_25',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3688_run_dialog_26',
        "command": 'run_dialog',
        "args": [3850, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3688_set_27',
        "command": 'set',
        "args": [0x70a7, 102]
    },
    {
        "identifier": 'EVENT_3688_set_28',
        "command": 'set',
        "args": [0x7000, 10]
    },
    {
        "identifier": 'EVENT_3688_set_short_mem_29',
        "command": 'set_short_mem',
        "args": [0x703a, 0x7000]
    },
    {
        "identifier": 'EVENT_3688_set_30',
        "command": 'set',
        "args": [0x7000, 3852]
    },
    {
        "identifier": 'EVENT_3688_run_event_as_subroutine_31',
        "command": 'run_event_as_subroutine',
        "args": [3827]
    },
    {
        "identifier": 'EVENT_3688_set_short_mem_32',
        "command": 'set_short_mem',
        "args": [0x7000, 0x703a]
    },
    {
        "identifier": 'EVENT_3688_dec_coins_33',
        "command": 'dec_coins'
    },
    {
        "identifier": 'EVENT_3688_close_dialog_34',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_3688_pause_35',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_3688_run_dialog_36',
        "command": 'run_dialog',
        "args": [3851, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3688_action_queue_async_37',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3688_action_queue_async_37_SUBSCRIPT_object_memory_clear_bit_0',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3688_set_action_script_sync_38',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 978]
    },
    {
        "identifier": 'EVENT_3688_set_action_script_sync_39',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_3688_ret_40',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3688_set_short_41',
        "command": 'set_short',
        "args": [0x7024, 0x0096]
    },
    {
        "identifier": 'EVENT_3688_run_event_as_subroutine_42',
        "command": 'run_event_as_subroutine',
        "args": [274]
    },
    {
        "identifier": 'EVENT_3688_jmp_if_bit_set_43',
        "command": 'jmp_if_bit_set',
        "args": [0x7049, 3, 'EVENT_3688_run_dialog_52']
    },
    {
        "identifier": 'EVENT_3688_run_dialog_44',
        "command": 'run_dialog',
        "args": [3849, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3688_action_queue_async_45',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3688_action_queue_async_45_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_45_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_45_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_45_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_45_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [90]
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_45_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_45_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_45_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_45_SUBSCRIPT_shift_southeast_steps_8',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3688_action_queue_async_45_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3688_pause_46',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3688_run_dialog_47',
        "command": 'run_dialog',
        "args": [3850, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3688_set_48',
        "command": 'set',
        "args": [0x70a7, 108]
    },
    {
        "identifier": 'EVENT_3688_set_49',
        "command": 'set',
        "args": [0x7000, 150]
    },
    {
        "identifier": 'EVENT_3688_set_short_mem_50',
        "command": 'set_short_mem',
        "args": [0x703a, 0x7000]
    },
    {
        "identifier": 'EVENT_3688_jmp_51',
        "command": 'jmp',
        "args": ['EVENT_3688_set_30']
    },
    {
        "identifier": 'EVENT_3688_run_dialog_52',
        "command": 'run_dialog',
        "args": [3853, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_3688_jmp_53',
        "command": 'jmp',
        "args": ['EVENT_3688_close_dialog_34']
    }
]
