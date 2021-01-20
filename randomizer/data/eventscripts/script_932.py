from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_932_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._129_BABY_YOSHI, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'EVENT_932_enable_controls_until_return_36'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_run_event_as_subroutine_2',
        "command": 'run_event_as_subroutine',
        "args": [456],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_932_action_queue_sync_3_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_932_action_queue_sync_3_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_932_action_queue_sync_3_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [14, 62]
            }
        ]
    },
    {
        "identifier": 'EVENT_932_start_embedded_action_script_async_4',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_932_start_embedded_action_script_async_4_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_932_remember_last_object_5',
        "command": 'remember_last_object',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_932_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_932_action_queue_sync_6_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_932_action_queue_sync_6_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_932_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_932_action_queue_async_7_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_932_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 119],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_store_item_amount_7000_9',
        "command": 'store_item_amount_7000',
        "args": [items.YoshiCookie],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_jmp_if_var_equals_short_10',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_932_close_dialog_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_set_short_mem_11',
        "command": 'set_short_mem',
        "args": [0x7026, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_run_dialog_12',
        "command": 'run_dialog',
        "args": [2365, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_jmp_if_dialog_option_b_13',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_932_close_dialog_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_run_dialog_14',
        "command": 'run_dialog',
        "args": [2366, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_set_bit_15',
        "command": 'set_bit',
        "args": [0x7042, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_jmp_to_subroutine_16',
        "command": 'jmp_to_subroutine',
        "args": [0xa958],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_932_action_queue_async_17_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_932_action_queue_async_17_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [14, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_932_action_queue_async_17_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._061_DEEP_UHOH, 4]
            },
            {
                "identifier": 'EVENT_932_action_queue_async_17_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [54]
            },
            {
                "identifier": 'EVENT_932_action_queue_async_17_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_932_action_queue_async_17_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_932_set_object_memory_to_18',
        "command": 'set_object_memory_to',
        "args": [0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_remove_one_from_inventory_19',
        "command": 'remove_one_from_inventory',
        "args": [items.YoshiCookie],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_end_loop_20',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_set_short_mem_21',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70d9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_add_short_mem_22',
        "command": 'add_short_mem',
        "args": [0x7000, 0x7024],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_set_short_mem_23',
        "command": 'set_short_mem',
        "args": [0x70d9, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_mem_compare_24',
        "command": 'mem_compare',
        "args": [0x7000, 21],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_jmp_if_comparison_result_is_greater_or_equal_25',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_932_set_bit_39'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_pause_26',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_play_sound_27',
        "command": 'play_sound',
        "args": [Sounds._129_BABY_YOSHI, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_close_dialog_28',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_run_background_event_29',
        "command": 'run_background_event',
        "args": [469, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_7]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_clear_bit_30',
        "command": 'clear_bit',
        "args": [0x7042, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_clear_bit_31',
        "command": 'clear_bit',
        "args": [0x7043, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_clear_bit_32',
        "command": 'clear_bit',
        "args": [0x7043, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_clear_bit_33',
        "command": 'clear_bit',
        "args": [0x7043, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_clear_bit_34',
        "command": 'clear_bit',
        "args": [0x7043, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_ret_35',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_enable_controls_until_return_36',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_pause_37',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_ret_38',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_set_bit_39',
        "command": 'set_bit',
        "args": [0x7084, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_set_40',
        "command": 'set',
        "args": [0x70d9, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_932_jmp_41',
        "command": 'jmp',
        "args": ['EVENT_932_pause_26'],
        "subscript": []
    }
]
