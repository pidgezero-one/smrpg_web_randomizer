from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_520_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7085, 2, 'EVENT_520_jmp_if_bit_set_29']
    },
    {
        "identifier": 'EVENT_520_pause_action_script_1',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_520_set_7016_to_object_xyz_2',
        "command": 'set_7016_to_object_xyz',
        "args": [0x96]
    },
    {
        "identifier": 'EVENT_520_set_short_mem_3',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7016]
    },
    {
        "identifier": 'EVENT_520_set_short_mem_4',
        "command": 'set_short_mem',
        "args": [0x70b8, 0x7000]
    },
    {
        "identifier": 'EVENT_520_set_short_mem_5',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7018]
    },
    {
        "identifier": 'EVENT_520_set_short_mem_6',
        "command": 'set_short_mem',
        "args": [0x70b9, 0x7000]
    },
    {
        "identifier": 'EVENT_520_start_embedded_action_script_async_7',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_520_start_embedded_action_script_async_7_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_520_start_embedded_action_script_async_7_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_520_start_embedded_action_script_async_7_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_520_start_embedded_action_script_async_7_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_520_start_embedded_action_script_async_7_SUBSCRIPT_run_away_shift_4',
                "command": 'run_away_shift'
            }
        ]
    },
    {
        "identifier": 'EVENT_520_run_dialog_8',
        "command": 'run_dialog',
        "args": [788, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_520_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_520_action_queue_async_9_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_520_action_queue_async_9_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_520_action_queue_async_9_SUBSCRIPT_face_mario_2',
                "command": 'face_mario'
            }
        ]
    },
    {
        "identifier": 'EVENT_520_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 3, 'EVENT_520_resume_action_script_27']
    },
    {
        "identifier": 'EVENT_520_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_520_action_queue_async_11_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0xfd, 0x24, 0x07, 0x00]
            },
            {
                "identifier": 'EVENT_520_action_queue_async_11_SUBSCRIPT_mem_700C_and_const_1',
                "command": 'mem_700C_and_const',
                "args": [0x00c0]
            },
            {
                "identifier": 'EVENT_520_action_queue_async_11_SUBSCRIPT_set_short_mem_2',
                "command": 'set_short_mem',
                "args": [0x702a, 0x700c]
            },
            {
                "identifier": 'EVENT_520_action_queue_async_11_SUBSCRIPT_jmp_if_var_equals_short_3',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 0, 'EVENT_520_action_queue_async_11_SUBSCRIPT_face_northwest_7']
            },
            {
                "identifier": 'EVENT_520_action_queue_async_11_SUBSCRIPT_jmp_if_var_equals_short_4',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 64, 'EVENT_520_action_queue_async_11_SUBSCRIPT_set_700C_to_object_coord_9']
            },
            {
                "identifier": 'EVENT_520_action_queue_async_11_SUBSCRIPT_jmp_if_var_equals_short_5',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 128, 'EVENT_520_action_queue_async_11_SUBSCRIPT_face_southeast_14']
            },
            {
                "identifier": 'EVENT_520_action_queue_async_11_SUBSCRIPT_jmp_if_var_equals_short_6',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 192, 'EVENT_520_action_queue_async_11_SUBSCRIPT_set_700C_to_object_coord_9']
            },
            {
                "identifier": 'EVENT_520_action_queue_async_11_SUBSCRIPT_face_northwest_7',
                "command": 'face_northwest'
            },
            {
                "identifier": 'EVENT_520_action_queue_async_11_SUBSCRIPT_jmp_8',
                "command": 'jmp',
                "args": ['EVENT_520_action_queue_sync_12']
            },
            {
                "identifier": 'EVENT_520_action_queue_async_11_SUBSCRIPT_set_700C_to_object_coord_9',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.NPC_2, Coords.X, CoordUnits.PIXEL]
            },
            {
                "identifier": 'EVENT_520_action_queue_async_11_SUBSCRIPT_set_short_mem_10',
                "command": 'set_short_mem',
                "args": [0x702c, 0x700c]
            },
            {
                "identifier": 'EVENT_520_action_queue_async_11_SUBSCRIPT_mem_compare_11',
                "command": 'mem_compare',
                "args": [0x7038, 4]
            },
            {
                "identifier": 'EVENT_520_action_queue_async_11_SUBSCRIPT_jmp_if_comparison_result_is_greater_or_equal_12',
                "command": 'jmp_if_comparison_result_is_greater_or_equal',
                "args": ['EVENT_520_action_queue_async_11_SUBSCRIPT_face_northwest_7']
            },
            {
                "identifier": 'EVENT_520_action_queue_async_11_SUBSCRIPT_jmp_13',
                "command": 'jmp',
                "args": ['EVENT_520_action_queue_async_11_SUBSCRIPT_face_southeast_14']
            },
            {
                "identifier": 'EVENT_520_action_queue_async_11_SUBSCRIPT_face_southeast_14',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_520_action_queue_async_11_SUBSCRIPT_set_bit_15',
                "command": 'set_bit',
                "args": [0x7043, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_520_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_520_action_queue_sync_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_520_action_queue_sync_12_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_520_action_queue_sync_12_SUBSCRIPT_walk_1_step_f_direction_2',
                "command": 'walk_1_step_f_direction'
            },
            {
                "identifier": 'EVENT_520_action_queue_sync_12_SUBSCRIPT_set_700C_to_object_coord_3',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.NPC_2, Coords.F]
            },
            {
                "identifier": 'EVENT_520_action_queue_sync_12_SUBSCRIPT_jmp_if_var_equals_short_4',
                "command": 'jmp_if_var_equals_short',
                "args": [0x700c, 5, 'EVENT_520_action_queue_sync_12_SUBSCRIPT_object_memory_clear_bit_6']
            },
            {
                "identifier": 'EVENT_520_action_queue_sync_12_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_520_action_queue_sync_12_SUBSCRIPT_object_memory_clear_bit_6',
                "command": 'object_memory_clear_bit',
                "args": [0x08, [3, 4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_520_set_action_script_async_13',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_7, 639]
    },
    {
        "identifier": 'EVENT_520_remember_last_object_14',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_520_set_7010_to_object_xyz_15',
        "command": 'set_7010_to_object_xyz',
        "args": [0x96]
    },
    {
        "identifier": 'EVENT_520_set_short_mem_16',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7016]
    },
    {
        "identifier": 'EVENT_520_set_short_mem_17',
        "command": 'set_short_mem',
        "args": [0x70b8, 0x7000]
    },
    {
        "identifier": 'EVENT_520_jmp_if_bit_set_18',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_520_add_25']
    },
    {
        "identifier": 'EVENT_520_set_short_mem_19',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7018]
    },
    {
        "identifier": 'EVENT_520_set_short_mem_20',
        "command": 'set_short_mem',
        "args": [0x70b9, 0x7000]
    },
    {
        "identifier": 'EVENT_520_set_action_script_sync_21',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 15]
    },
    {
        "identifier": 'EVENT_520_clear_bit_22',
        "command": 'clear_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_520_set_bit_23',
        "command": 'set_bit',
        "args": [0x7085, 2]
    },
    {
        "identifier": 'EVENT_520_ret_24',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_520_add_25',
        "command": 'add',
        "args": [0x70b8, 128]
    },
    {
        "identifier": 'EVENT_520_jmp_26',
        "command": 'jmp',
        "args": ['EVENT_520_set_short_mem_19']
    },
    {
        "identifier": 'EVENT_520_resume_action_script_27',
        "command": 'resume_action_script',
        "args": [AreaObjects.NPC_2]
    },
    {
        "identifier": 'EVENT_520_ret_28',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_520_jmp_if_bit_set_29',
        "command": 'jmp_if_bit_set',
        "args": [0x7085, 6, 'EVENT_520_jmp_if_bit_clear_33']
    },
    {
        "identifier": 'EVENT_520_set_bit_30',
        "command": 'set_bit',
        "args": [0x7085, 6]
    },
    {
        "identifier": 'EVENT_520_run_dialog_31',
        "command": 'run_dialog',
        "args": [813, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_520_ret_32',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_520_jmp_if_bit_clear_33',
        "command": 'jmp_if_bit_clear',
        "args": [0x7085, 0, 'EVENT_520_run_dialog_31']
    },
    {
        "identifier": 'EVENT_520_set_short_mem_34',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70b8]
    },
    {
        "identifier": 'EVENT_520_jmp_if_7000_any_bits_set_35',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_520_run_dialog_38']
    },
    {
        "identifier": 'EVENT_520_run_dialog_36',
        "command": 'run_dialog',
        "args": [821, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_520_ret_37',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_520_run_dialog_38',
        "command": 'run_dialog',
        "args": [820, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_520_ret_39',
        "command": 'ret'
    }
]
