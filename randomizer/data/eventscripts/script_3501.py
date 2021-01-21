from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3501_stop_background_event_0',
        "command": 'stop_background_event',
        "args": [0x701c]
    },
    {
        "identifier": 'EVENT_3501_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_3501_enable_controls_until_return_2',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_3501_jmp_fork_mario_on_object_3',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_3501_set_short_18', 'EVENT_3501_action_queue_sync_7']
    },
    {
        "identifier": 'EVENT_3501_set_7000_to_object_coord_4',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_3501_mem_compare_5',
        "command": 'mem_compare',
        "args": [0x7000, 256]
    },
    {
        "identifier": 'EVENT_3501_jmp_if_comparison_result_is_greater_or_equal_6',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3501_set_short_18']
    },
    {
        "identifier": 'EVENT_3501_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3501_action_queue_sync_7_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3501_action_queue_sync_7_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3501_resume_action_script_8',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3501_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._049_BIG_SHELL_HIT, 4]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [112]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [7, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_floating_on_7',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_start_loop_n_times_8',
                "command": 'start_loop_n_times',
                "args": [15]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_visibility_off_9',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_visibility_on_11',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_mem_compare_12',
                "command": 'mem_compare',
                "args": [0x7030, 65488]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_jmp_if_loaded_memory_is_above_or_equal_0_13',
                "command": 'jmp_if_loaded_memory_is_above_or_equal_0',
                "args": ['EVENT_3501_action_queue_async_9_SUBSCRIPT_pause_17']
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_shift_southeast_pixels_14',
                "command": 'shift_southeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_dec_short_15',
                "command": 'dec_short',
                "args": [0x7024]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_jmp_16',
                "command": 'jmp',
                "args": ['EVENT_3501_action_queue_async_9_SUBSCRIPT_end_loop_18']
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_end_loop_18',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_reset_properties_19',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_set_vram_priority_20',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_9_SUBSCRIPT_set_solidity_bits_21',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3501_enable_controls_until_return_10',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_3501_mem_compare_11',
        "command": 'mem_compare',
        "args": [0x7024, 0]
    },
    {
        "identifier": 'EVENT_3501_jmp_if_loaded_memory_is_below_0_12',
        "command": 'jmp_if_loaded_memory_is_below_0',
        "args": ['EVENT_3501_resume_background_event_16']
    },
    {
        "identifier": 'EVENT_3501_set_short_13',
        "command": 'set_short',
        "args": [0x701c, 0x0002]
    },
    {
        "identifier": 'EVENT_3501_run_background_event_with_pause_return_on_exit_14',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [3505, 0x701c, [12, 13]]
    },
    {
        "identifier": 'EVENT_3501_ret_15',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3501_resume_background_event_16',
        "command": 'resume_background_event',
        "args": [0x701c]
    },
    {
        "identifier": 'EVENT_3501_ret_17',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_3501_set_short_18',
        "command": 'set_short',
        "args": [0x7028, 0x0024]
    },
    {
        "identifier": 'EVENT_3501_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3501_action_queue_sync_19_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3501_action_queue_sync_19_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3501_resume_action_script_20',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_3501_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_set_short_mem_1',
                "command": 'set_short_mem',
                "args": [0x700c, 0x7024]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_add_short_mem_2',
                "command": 'add_short_mem',
                "args": [0x700c, 0x7028]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_mem_compare_3',
                "command": 'mem_compare',
                "args": [0x700c, 64]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_jmp_if_loaded_memory_is_above_or_equal_0_4',
                "command": 'jmp_if_loaded_memory_is_above_or_equal_0',
                "args": ['EVENT_3501_action_queue_async_21_SUBSCRIPT_set_short_mem_6']
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_jmp_5',
                "command": 'jmp',
                "args": ['EVENT_3501_action_queue_async_21_SUBSCRIPT_set_8']
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_set_short_mem_6',
                "command": 'set_short_mem',
                "args": [0x700c, 0x7028]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_jmp_7',
                "command": 'jmp',
                "args": ['EVENT_3501_action_queue_async_21_SUBSCRIPT_set_animation_speed_16']
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_set_8',
                "command": 'set',
                "args": [0x700c, 64]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_dec_short_mem_9',
                "command": 'dec_short_mem',
                "args": [0x700c, 0x7024]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_jmp_if_var_not_equals_short_10',
                "command": 'jmp_if_var_not_equals_short',
                "args": [0x700c, 0, 'EVENT_3501_action_queue_async_21_SUBSCRIPT_set_animation_speed_16']
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_play_sound_11',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 4]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_floating_off_12',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_jump_to_height_silent_13',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_floating_on_14',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_jmp_15',
                "command": 'jmp',
                "args": ['EVENT_3501_action_queue_async_21_SUBSCRIPT_set_solidity_bits_25']
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_set_animation_speed_16',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_play_sound_17',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 4]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_floating_off_18',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_jump_to_height_silent_19',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_floating_on_20',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_load_mem_21',
                "command": 'load_mem',
                "args": [0x700c]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_shift_northwest_pixels_22',
                "command": 'shift_northwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_add_short_23',
                "command": 'add_short',
                "args": [0x7024, 0x01]
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_end_loop_24',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3501_action_queue_async_21_SUBSCRIPT_set_solidity_bits_25',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3501_enable_controls_until_return_22',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_3501_mem_compare_23',
        "command": 'mem_compare',
        "args": [0x7024, 0]
    },
    {
        "identifier": 'EVENT_3501_jmp_if_loaded_memory_is_above_or_equal_0_24',
        "command": 'jmp_if_loaded_memory_is_above_or_equal_0',
        "args": ['EVENT_3501_resume_background_event_16']
    },
    {
        "identifier": 'EVENT_3501_set_short_25',
        "command": 'set_short',
        "args": [0x701c, 0x0078]
    },
    {
        "identifier": 'EVENT_3501_run_background_event_with_pause_return_on_exit_26',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [3505, 0x701c, [12, 13]]
    },
    {
        "identifier": 'EVENT_3501_ret_27',
        "command": 'ret'
    }
]
