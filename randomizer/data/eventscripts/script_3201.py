from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3201_set_short_0',
        "command": 'set_short',
        "args": [0x700a, 0x00cd],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_jmp_to_event_1',
        "command": 'jmp_to_event',
        "args": [720],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_ret_2',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 5, 'EVENT_3201_set_short_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_set_bit_4',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_set_short_5',
        "command": 'set_short',
        "args": [0x700e, 0x00a4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_run_event_as_subroutine_6',
        "command": 'run_event_as_subroutine',
        "args": [18],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_3201_set_short_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_set_bit_8',
        "command": 'set_bit',
        "args": [0x7056, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_restore_all_hp_9',
        "command": 'restore_all_hp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_restore_all_fp_10',
        "command": 'restore_all_fp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_3201_action_queue_async_11_SUBSCRIPT_object_memory_set_bit_0',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3201_action_queue_async_11_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3201_action_queue_async_11_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3201_action_queue_async_11_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3201_action_queue_async_11_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [56]
            },
            {
                "identifier": 'EVENT_3201_action_queue_async_11_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3201_action_queue_async_11_SUBSCRIPT_object_memory_set_bit_6',
                "command": 'object_memory_set_bit',
                "args": [0x30, [4]]
            },
            {
                "identifier": 'EVENT_3201_action_queue_async_11_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._011_WHOOSH_AWAY, 4]
            },
            {
                "identifier": 'EVENT_3201_action_queue_async_11_SUBSCRIPT_ret_8',
                "command": 'ret',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3201_resume_action_script_12',
        "command": 'resume_action_script',
        "args": [AreaObjects.MEM_70A8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_set_7000_to_current_level_13',
        "command": 'set_7000_to_current_level',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_jmp_if_var_not_equals_short_14',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 277, 'EVENT_3201_jmp_if_var_not_equals_short_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 6, 'EVENT_3201_set_short_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3201_action_queue_sync_16_SUBSCRIPT_set_bit_0',
                "command": 'set_bit',
                "args": [0x7043, 1]
            },
            {
                "identifier": 'EVENT_3201_action_queue_sync_16_SUBSCRIPT_jmp_1',
                "command": 'jmp',
                "args": ['EVENT_3192_action_queue_sync_4_SUBSCRIPT_object_memory_set_bit_0']
            }
        ]
    },
    {
        "identifier": 'EVENT_3201_jmp_if_var_not_equals_short_17',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 283, 'EVENT_3201_jmp_if_var_not_equals_short_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_jmp_if_bit_set_18',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 7, 'EVENT_3201_set_short_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_3201_action_queue_sync_19_SUBSCRIPT_set_bit_0',
                "command": 'set_bit',
                "args": [0x7043, 1]
            },
            {
                "identifier": 'EVENT_3201_action_queue_sync_19_SUBSCRIPT_jmp_1',
                "command": 'jmp',
                "args": ['EVENT_3193_action_queue_sync_4_SUBSCRIPT_object_memory_set_bit_0']
            }
        ]
    },
    {
        "identifier": 'EVENT_3201_jmp_if_var_not_equals_short_20',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 273, 'EVENT_3201_jmp_to_event_1'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_jmp_if_bit_set_21',
        "command": 'jmp_if_bit_set',
        "args": [0x7057, 0, 'EVENT_3201_set_short_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_3201_action_queue_sync_22_SUBSCRIPT_set_bit_0',
                "command": 'set_bit',
                "args": [0x7043, 1]
            },
            {
                "identifier": 'EVENT_3201_action_queue_sync_22_SUBSCRIPT_jmp_1',
                "command": 'jmp',
                "args": ['EVENT_3194_action_queue_sync_4_SUBSCRIPT_pause_0']
            }
        ]
    },
    {
        "identifier": 'EVENT_3201_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3201_action_queue_async_23_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3201_action_queue_async_23_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3201_action_queue_async_23_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [15]
            },
            {
                "identifier": 'EVENT_3201_action_queue_async_23_SUBSCRIPT_turn_clockwise_45_degrees_n_times_3',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3201_action_queue_async_23_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3201_action_queue_async_23_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            },
            {
                "identifier": 'EVENT_3201_action_queue_async_23_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=2, flags=[_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3201_action_queue_async_23_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3201_action_queue_async_23_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3201_action_queue_async_23_SUBSCRIPT_reset_properties_9',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3201_close_dialog_24',
        "command": 'close_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_clear_bit_25',
        "command": 'clear_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_stop_sound_26',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_stop_sound_27',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_stop_sound_28',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_stop_sound_29',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_stop_sound_30',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_stop_sound_31',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_stop_sound_32',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_stop_sound_33',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_stop_sound_34',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_stop_sound_35',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_stop_sound_36',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_stop_sound_37',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3201_ret_38',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
