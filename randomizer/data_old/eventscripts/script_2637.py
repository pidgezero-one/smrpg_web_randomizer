
from randomizer.helpers.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2637_action_queue_sync_9',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_1, True],
        "subscript": [
            {
                "identifier": 'EVENT_2637_action_queue_sync_9_SUBSCRIPT_sequence_looping_off_0',
                "command": 'sequence_looping_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2637_action_queue_async_10',
        "command": 'action_queue',
        'args': [AreaObjects.MARIO, False],
        "subscript": [
            {
                "identifier": 'EVENT_2637_action_queue_async_10_SUBSCRIPT_overwrite_solidity_0',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2637_action_queue_async_10_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [4, 16]
            },
            {
                "identifier": 'EVENT_2637_action_queue_async_10_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2637_run_dialog_12',
        "command": 'run_dialog',
        "args": [3304, AreaObjects.BOWSER, [_0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2637_set_7000_to_pressed_button_13',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_2637_pause_14',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_15',
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 1, 'EVENT_2637_close_dialog_18']
    },
    {
        "identifier": 'EVENT_2637_jmp_if_7000_equals_short_16',
        "command": 'jmp_if_var_equals_const',
        'args': [0x7000, 2, 'EVENT_2637_close_dialog_18_']
    },
    {
        "identifier": 'EVENT_2637_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_2637_set_7000_to_pressed_button_13']
    },
    {
        "identifier": 'EVENT_2637_close_dialog_18',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_2637_pause_20',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2637_action_queue_sync_21',
        "command": 'action_queue',
        'args': [AreaObjects.MARIO, True],
        "subscript": [
            {
                "identifier": 'EVENT_2637_action_queue_sync_21_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [11, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2637_jmp_if_random_above_128_22',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2637_action_queue_sync_26']
    },
    {
        "identifier": 'EVENT_2637_action_queue_sync_23',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_1, True],
        "subscript": [
            {
                "identifier": 'EVENT_2637_action_queue_sync_23_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2637_pause_20_',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2637_await_a_1',
        "command": 'run_event_as_subroutine',
        "args": [2646]
    },
    {
        "identifier": 'EVENT_2637_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_2637_play_sound_40']
    },
    {
        "identifier": 'EVENT_2637_action_queue_sync_26',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_1, True],
        "subscript": [
            {
                "identifier": 'EVENT_2637_action_queue_sync_26_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2637_pause_20__',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2637_await_a_2',
        "command": 'run_event_as_subroutine',
        "args": [2646]
    },
    {
        "identifier": 'EVENT_2637_jmp_28',
        "command": 'jmp',
        "args": ['EVENT_2637_play_sound_49']
    },
    {
        "identifier": 'EVENT_2637_close_dialog_18_',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_2637_pause_31',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2637_action_queue_sync_32',
        "command": 'action_queue',
        'args': [AreaObjects.MARIO, True],
        "subscript": [
            {
                "identifier": 'EVENT_2637_action_queue_sync_32_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2637_jmp_if_random_above_128_33',
        "command": 'jmp_if_random_above_128',
        "args": ['EVENT_2637_action_queue_sync_37']
    },
    {
        "identifier": 'EVENT_2637_action_queue_sync_34',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_1, True],
        "subscript": [
            {
                "identifier": 'EVENT_2637_action_queue_sync_34_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2637_pause_20_____',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2637_await_a_2___',
        "command": 'run_event_as_subroutine',
        "args": [2646]
    },
    {
        "identifier": 'EVENT_2637_jmp_36',
        "command": 'jmp',
        "args": ['EVENT_2637_play_sound_49']
    },
    {
        "identifier": 'EVENT_2637_action_queue_sync_37',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_1, True],
        "subscript": [
            {
                "identifier": 'EVENT_2637_action_queue_sync_37_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2637_pause_20____',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2637_await_a_2__',
        "command": 'run_event_as_subroutine',
        "args": [2646]
    },
    {
        "identifier": 'EVENT_2637_jmp_39',
        "command": 'jmp',
        "args": ['EVENT_2637_play_sound_40']
    },
    {
        "identifier": 'EVENT_2637_play_sound_40',
        "command": 'play_sound',
        "args": [Sounds._088_WRONG_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_2637_set_action_script_async_42',
        "command": 'set_action_script',
        'args': [AreaObjects.MARIO, False, 395]
    },
    {
        "identifier": 'EVENT_2637_action_queue_sync_43',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_1, True],
        "subscript": [
            {
                "identifier": 'EVENT_2637_action_queue_sync_43_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2637_action_queue_sync_43_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2637_run_dialog_44',
        "command": 'jmp',
        "args": ['EVENT_2637_run_dialog_79']
    },
    {
        "identifier": 'EVENT_2637_play_sound_49',
        "command": 'play_sound',
        "args": [Sounds._087_CORRECT_SIGNAL, 6]
    },
    {
        "identifier": 'EVENT_2637_pause_20______',
        "command": 'pause',
        "args": [25]
    },
    {
        "identifier": 'EVENT_2637_set_action_script_async_51',
        "command": 'set_action_script',
        'args': [AreaObjects.MARIO, False, 395]
    },
    {
        "identifier": 'EVENT_2637_action_queue_sync_52',
        "command": 'action_queue',
        'args': [AreaObjects.NPC_1, True],
        "subscript": [
            {
                "identifier": 'EVENT_2637_action_queue_sync_52_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2637_action_queue_sync_52_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2637_jmp_if_bit_set_53',
        "command": 'jmp_if_bit_set',
        "args": [0x7059, 0, 'EVENT_2637_set_var_to_random_grant']
    },
    {
        "identifier": 'EVENT_2637_inc_54',
        "command": 'inc',
        "args": [0x70ef]
    },
    {
        "identifier": 'EVENT_2637_store_win_count_for_dialog',
        "command": 'copy_var_to_var',
        'args': [0x70EF, 0x7000]
    },
    {
        "identifier": 'EVENT_2637_check_wins',
        "command": 'run_event_as_subroutine',
        "args": [2650]
    },
    {
        "identifier": 'EVENT_2637_jmp_if_comparison_result_is_greater_or_equal_189',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2637_run_dialog_135']
    },
    {
        "identifier": 'EVENT_2637_set_var_to_random_grant',
        "command": 'run_event_as_subroutine',
        "args": [2649]
    },
    {
        "identifier": 'EVENT_2637_jmp_tier1',
        "command": 'jmp',
        "args": [ 'EVENT_2637_run_dialog_79']
    },
    {
        "identifier": 'EVENT_2637_run_dialog_135',
        "command": 'run_dialog',
        "args": [3308, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2637_set_win_bit',
        "command": 'set_bit',
        "args": [0x7059, 0]
    },
    {
        "identifier": 'EVENT_2637_set_final_grant',
        "command": 'run_event_as_subroutine',
        "args": [178]
    },
    {
        "identifier": 'EVENT_2637_run_dialog_79',
        "command": 'run_dialog',
        "args": [3310, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2637_jmp_if_dialog_option_b_80',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2637_pause_138']
    },
    {
        "identifier": 'EVENT_2637_pause_81',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2637_set_action_script_async_82',
        "command": 'set_action_script',
        'args': [AreaObjects.MARIO, False, 670]
    },
    {
        "identifier": 'EVENT_2637_jmp_83',
        "command": 'jmp',
        "args": ['EVENT_2637_action_queue_sync_9']
    },
    {
        "identifier": 'EVENT_2637_pause_138',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_2637_set_action_script_async_139',
        "command": 'set_action_script',
        'args': [AreaObjects.MARIO, False, 671]
    },
    {
        "identifier": 'EVENT_2637_ret_141',
        "command": 'ret'
    }
]
