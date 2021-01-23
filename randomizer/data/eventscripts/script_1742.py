from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1742_stop_background_event_0',
        "command": 'stop_background_event',
        "args": [0x701c]
    },
    {
        "identifier": 'EVENT_1742_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_1742_enable_controls_until_return_2',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1742_jmp_fork_mario_on_object_3',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_1742_set_short_18', 'EVENT_1742_action_queue_sync_7']
    },
    {
        "identifier": 'EVENT_1742_set_7000_to_object_coord_4',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, [], CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_1742_mem_compare_val_5',
        "command": 'mem_compare_val',
        "args": [256]
    },
    {
        "identifier": 'EVENT_1742_jmp_if_comparison_result_is_greater_or_equal_6',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_1742_set_short_18']
    },
    {
        "identifier": 'EVENT_1742_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1742_action_queue_sync_7_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_1742_action_queue_sync_7_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1742_resume_action_script_8',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_1742_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1742_action_queue_async_9_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_9_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_9_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_9_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [7, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_9_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [112]
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_9_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_9_SUBSCRIPT_floating_on_6',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_9_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_9_SUBSCRIPT_fixed_f_coord_off_8',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_9_SUBSCRIPT_reset_properties_9',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_9_SUBSCRIPT_face_northwest_10',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_9_SUBSCRIPT_fixed_f_coord_on_11',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_9_SUBSCRIPT_set_vram_priority_12',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_9_SUBSCRIPT_set_solidity_bits_13',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1742_enable_controls_until_return_10',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1742_mem_compare_11',
        "command": 'mem_compare',
        "args": [0x7024, 0]
    },
    {
        "identifier": 'EVENT_1742_jmp_if_loaded_memory_is_below_0_12',
        "command": 'jmp_if_loaded_memory_is_below_0',
        "args": ['EVENT_1742_resume_background_event_16']
    },
    {
        "identifier": 'EVENT_1742_set_short_13',
        "command": 'set_short',
        "args": [0x701c, 0x0002]
    },
    {
        "identifier": 'EVENT_1742_run_background_event_with_pause_return_on_exit_14',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [3505, 0x701c, [12, 13]]
    },
    {
        "identifier": 'EVENT_1742_ret_15',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1742_resume_background_event_16',
        "command": 'resume_background_event',
        "args": [0x701c]
    },
    {
        "identifier": 'EVENT_1742_ret_17',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1742_set_short_18',
        "command": 'set_short',
        "args": [0x7028, 0x0024]
    },
    {
        "identifier": 'EVENT_1742_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1742_action_queue_sync_19_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_1742_action_queue_sync_19_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1742_resume_action_script_20',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70A8]
    },
    {
        "identifier": 'EVENT_1742_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_set_short_mem_1',
                "command": 'set_short_mem',
                "args": [0x700c, 0x7024]
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_add_short_mem_2',
                "command": 'add_short_mem',
                "args": [0x700c, 0x7028]
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_mem_compare_val_3',
                "command": 'mem_compare_val',
                "args": [64]
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_jmp_if_loaded_memory_is_above_or_equal_0_4',
                "command": 'jmp_if_loaded_memory_is_above_or_equal_0',
                "args": ['EVENT_1742_action_queue_async_21_SUBSCRIPT_set_short_mem_6']
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_jmp_5',
                "command": 'jmp',
                "args": ['EVENT_1742_action_queue_async_21_SUBSCRIPT_set_8']
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_set_short_mem_6',
                "command": 'set_short_mem',
                "args": [0x700c, 0x7028]
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_jmp_7',
                "command": 'jmp',
                "args": ['EVENT_1742_action_queue_async_21_SUBSCRIPT_set_animation_speed_15']
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_set_8',
                "command": 'set',
                "args": [0x700c, 64]
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_dec_short_mem_9',
                "command": 'dec_short_mem',
                "args": [0x700c, 0x7024]
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_jmp_if_700C_not_equals_short_10',
                "command": 'jmp_if_700C_not_equals_short',
                "args": [0, 'EVENT_1742_action_queue_async_21_SUBSCRIPT_set_animation_speed_15']
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_floating_off_11',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_jump_to_height_silent_12',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_floating_on_13',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_jmp_14',
                "command": 'jmp',
                "args": ['EVENT_1742_action_queue_async_21_SUBSCRIPT_set_solidity_bits_23']
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_set_animation_speed_15',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_floating_off_16',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_jump_to_height_silent_17',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_floating_on_18',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_load_mem_19',
                "command": 'load_mem',
                "args": [0x700c]
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_shift_northwest_pixels_20',
                "command": 'shift_northwest_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_inc_short_21',
                "command": 'inc_short',
                "args": [0x7024]
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_end_loop_22',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1742_action_queue_async_21_SUBSCRIPT_set_solidity_bits_23',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1742_enable_controls_until_return_22',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1742_mem_compare_23',
        "command": 'mem_compare',
        "args": [0x7024, 0]
    },
    {
        "identifier": 'EVENT_1742_jmp_if_loaded_memory_is_above_or_equal_0_24',
        "command": 'jmp_if_loaded_memory_is_above_or_equal_0',
        "args": ['EVENT_1742_resume_background_event_16']
    },
    {
        "identifier": 'EVENT_1742_set_short_25',
        "command": 'set_short',
        "args": [0x701c, 0x00b4]
    },
    {
        "identifier": 'EVENT_1742_run_background_event_with_pause_return_on_exit_26',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [3505, 0x701c, [12, 13]]
    },
    {
        "identifier": 'EVENT_1742_ret_27',
        "command": 'ret'
    }
]
