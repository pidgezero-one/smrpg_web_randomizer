from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1740_enable_controls_0',
        "command": 'enable_controls',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1740_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._151_GAME_INTRO_BOOSTER_HILL, RadialDirections.NORTHWEST, 7, 57, 0, []]
    },
    {
        "identifier": 'EVENT_1740_set_short_2',
        "command": 'set_short',
        "args": [0x7024, 0x0000]
    },
    {
        "identifier": 'EVENT_1740_set_short_3',
        "command": 'set_short',
        "args": [0x7026, 0x0001]
    },
    {
        "identifier": 'EVENT_1740_freeze_camera_4',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_1740_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1740_action_queue_async_5_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x0b, [3]]
            },
            {
                "identifier": 'EVENT_1740_action_queue_async_5_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [7, 58, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1740_action_queue_async_5_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1740_action_queue_async_5_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1740_action_queue_async_5_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1740_set_6',
        "command": 'set',
        "args": [0x70ae, 3]
    },
    {
        "identifier": 'EVENT_1740_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 772]
    },
    {
        "identifier": 'EVENT_1740_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 772]
    },
    {
        "identifier": 'EVENT_1740_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 772]
    },
    {
        "identifier": 'EVENT_1740_fade_in_from_black_sync_10',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_1740_run_background_event_11',
        "command": 'run_background_event',
        "args": [1743, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_1740_run_background_event_12',
        "command": 'run_background_event',
        "args": [1741, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_6]]
    },
    {
        "identifier": 'EVENT_1740_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.LAYER_1, 704]
    },
    {
        "identifier": 'EVENT_1740_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.LAYER_2, 655]
    },
    {
        "identifier": 'EVENT_1740_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.LAYER_3, 776]
    },
    {
        "identifier": 'EVENT_1740_set_short_16',
        "command": 'set_short',
        "args": [0x701e, 0x014a]
    },
    {
        "identifier": 'EVENT_1740_run_background_event_with_pause_return_on_exit_17',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [1744, 0x701e, [12, 13]]
    },
    {
        "identifier": 'EVENT_1740_move_script_to_background_thread_2_18',
        "command": 'move_script_to_background_thread_2'
    },
    {
        "identifier": 'EVENT_1740_pause_19',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1740_jmp_if_bit_set_20',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_1740_fade_out_to_black_async_duration_36']
    },
    {
        "identifier": 'EVENT_1740_pause_21',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1740_jmp_if_bit_set_22',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_1740_fade_out_to_black_async_duration_36']
    },
    {
        "identifier": 'EVENT_1740_jmp_if_bit_clear_23',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 5, 'EVENT_1740_pause_19']
    },
    {
        "identifier": 'EVENT_1740_mem_compare_24',
        "command": 'mem_compare',
        "args": [0x7024, 0]
    },
    {
        "identifier": 'EVENT_1740_jmp_if_loaded_memory_is_0_25',
        "command": 'jmp_if_loaded_memory_is_0',
        "args": ['EVENT_1740_clear_bit_34']
    },
    {
        "identifier": 'EVENT_1740_jmp_if_loaded_memory_is_above_or_equal_0_26',
        "command": 'jmp_if_loaded_memory_is_above_or_equal_0',
        "args": ['EVENT_1740_action_queue_async_32']
    },
    {
        "identifier": 'EVENT_1740_dec_short_27',
        "command": 'dec_short',
        "args": [0x7026]
    },
    {
        "identifier": 'EVENT_1740_jmp_if_var_not_equals_short_28',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7026, 0, 'EVENT_1740_pause_19']
    },
    {
        "identifier": 'EVENT_1740_action_queue_async_29',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1740_action_queue_async_29_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1740_action_queue_async_29_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1740_action_queue_async_29_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1740_action_queue_async_29_SUBSCRIPT_dec_short_3',
                "command": 'dec_short',
                "args": [0x7024]
            },
            {
                "identifier": 'EVENT_1740_action_queue_async_29_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1740_set_short_30',
        "command": 'set_short',
        "args": [0x7026, 0x0001]
    },
    {
        "identifier": 'EVENT_1740_jmp_31',
        "command": 'jmp',
        "args": ['EVENT_1740_jmp_if_bit_set_20']
    },
    {
        "identifier": 'EVENT_1740_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1740_action_queue_async_32_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1740_action_queue_async_32_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1740_action_queue_async_32_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1740_action_queue_async_32_SUBSCRIPT_inc_short_3',
                "command": 'inc_short',
                "args": [0x7024]
            },
            {
                "identifier": 'EVENT_1740_action_queue_async_32_SUBSCRIPT_set_solidity_bits_4',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1740_jmp_33',
        "command": 'jmp',
        "args": ['EVENT_1740_jmp_if_bit_set_20']
    },
    {
        "identifier": 'EVENT_1740_clear_bit_34',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_1740_jmp_35',
        "command": 'jmp',
        "args": ['EVENT_1740_pause_19']
    },
    {
        "identifier": 'EVENT_1740_fade_out_to_black_async_duration_36',
        "command": 'fade_out_to_black_async_duration',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1740_move_script_to_main_thread_37',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_1740_freeze_all_npcs_until_return_38',
        "command": 'freeze_all_npcs_until_return'
    },
    {
        "identifier": 'EVENT_1740_stop_all_background_events_39',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_1740_db_40',
        "command": 'db',
        "args": [0xfd, 0x44]
    },
    {
        "identifier": 'EVENT_1740_stop_background_event_41',
        "command": 'stop_background_event',
        "args": [0x701c]
    },
    {
        "identifier": 'EVENT_1740_stop_background_event_42',
        "command": 'stop_background_event',
        "args": [0x701e]
    },
    {
        "identifier": 'EVENT_1740_unfreeze_camera_43',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_1740_jmp_to_event_44',
        "command": 'jmp_to_event',
        "args": [1731]
    }
]
