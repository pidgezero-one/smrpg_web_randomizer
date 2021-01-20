from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3504_stop_background_event_0',
        "command": 'stop_background_event',
        "args": [timer_memory=0x701c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3504_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7043, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3504_enable_controls_until_return_2',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3504_jmp_fork_mario_on_object_3',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_3504_reset_coords_15', 'EVENT_3504_set_7000_to_object_coord_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3504_set_7000_to_object_coord_4',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3504_mem_compare_5',
        "command": 'mem_compare',
        "args": [0x7000, 288],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3504_jmp_if_comparison_result_is_greater_or_equal_6',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3504_reset_coords_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3504_disable_trigger_7',
        "command": 'disable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3504_resume_action_script_8',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3504_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3504_action_queue_async_9_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3504_action_queue_async_9_SUBSCRIPT_floating_off_1',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3504_action_queue_async_9_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._049_BIG_SHELL_HIT, 4]
            },
            {
                "identifier": 'EVENT_3504_action_queue_async_9_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [112]
            },
            {
                "identifier": 'EVENT_3504_action_queue_async_9_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3504_action_queue_async_9_SUBSCRIPT_floating_on_5',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3504_action_queue_async_9_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3504_action_queue_async_9_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_3504_action_queue_async_9_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3504_action_queue_async_9_SUBSCRIPT_visibility_on_9',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3504_action_queue_async_9_SUBSCRIPT_mem_compare_10',
                "command": 'mem_compare',
                "args": [0x7030, 65475]
            },
            {
                "identifier": 'EVENT_3504_action_queue_async_9_SUBSCRIPT_jmp_if_loaded_memory_is_above_or_equal_0_11',
                "command": 'jmp_if_loaded_memory_is_above_or_equal_0',
                "args": ['EVENT_3504_action_queue_async_9_SUBSCRIPT_pause_15']
            },
            {
                "identifier": 'EVENT_3504_action_queue_async_9_SUBSCRIPT_shift_southeast_pixels_12',
                "command": 'shift_southeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3504_action_queue_async_9_SUBSCRIPT_add_short_13',
                "command": 'add_short',
                "args": [0x7024, 0xfffe]
            },
            {
                "identifier": 'EVENT_3504_action_queue_async_9_SUBSCRIPT_jmp_14',
                "command": 'jmp',
                "args": ['EVENT_3504_action_queue_async_9_SUBSCRIPT_visibility_off_7']
            },
            {
                "identifier": 'EVENT_3504_action_queue_async_9_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3504_action_queue_async_9_SUBSCRIPT_reset_properties_16',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_3504_action_queue_async_9_SUBSCRIPT_set_solidity_bits_17',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3504_enable_controls_until_return_10',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3504_enable_trigger_11',
        "command": 'enable_trigger',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3504_set_short_12',
        "command": 'set_short',
        "args": [0x701c, 0x0002],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3504_run_background_event_with_pause_return_on_exit_13',
        "command": 'run_background_event_with_pause_return_on_exit',
        "args": [3505, 0x701c, [12, 13]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3504_ret_14',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3504_reset_coords_15',
        "command": 'reset_coords',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3504_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70A8, 711],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3504_set_short_17',
        "command": 'set_short',
        "args": [0x7028, 0x0030],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3504_jmp_18',
        "command": 'jmp',
        "args": ['EVENT_3501_action_queue_sync_19'],
        "subscript": []
    }
]
