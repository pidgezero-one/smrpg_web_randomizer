from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1555_set_7016_to_object_xyz_0',
        "command": 'set_7016_to_object_xyz',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1555_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x7016, 0x7026]
    },
    {
        "identifier": 'EVENT_1555_set_short_mem_2',
        "command": 'set_short_mem',
        "args": [0x7018, 0x7028]
    },
    {
        "identifier": 'EVENT_1555_pause_3',
        "command": 'pause',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1555_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 5, 'EVENT_1555_pause_3']
    },
    {
        "identifier": 'EVENT_1555_jmp_if_objects_action_script_running_5',
        "command": 'jmp_if_objects_action_script_running',
        "args": [AreaObjects.NPC_3, 'EVENT_1555_pause_3']
    },
    {
        "identifier": 'EVENT_1555_jmp_if_var_not_equals_short_6',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x702e, 20, 'EVENT_1555_clear_bit_8']
    },
    {
        "identifier": 'EVENT_1555_set_7',
        "command": 'set',
        "args": [0x70af, 0]
    },
    {
        "identifier": 'EVENT_1555_clear_bit_8',
        "command": 'clear_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_1555_clear_bit_9',
        "command": 'clear_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'EVENT_1555_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'EVENT_1555_set_random_11',
        "command": 'set_random',
        "args": [0x7000, 4096]
    },
    {
        "identifier": 'EVENT_1555_mem_compare_12',
        "command": 'mem_compare',
        "args": [0x7000, 2048]
    },
    {
        "identifier": 'EVENT_1555_jmp_if_comparison_result_is_lesser_13',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1555_mem_7000_and_const_15']
    },
    {
        "identifier": 'EVENT_1555_set_bit_14',
        "command": 'set_bit',
        "args": [0x7043, 7]
    },
    {
        "identifier": 'EVENT_1555_mem_7000_and_const_15',
        "command": 'mem_7000_and_const',
        "args": [0x07ff]
    },
    {
        "identifier": 'EVENT_1555_mem_compare_16',
        "command": 'mem_compare',
        "args": [0x7000, 1024]
    },
    {
        "identifier": 'EVENT_1555_jmp_if_comparison_result_is_lesser_17',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1555_mem_7000_and_const_19']
    },
    {
        "identifier": 'EVENT_1555_set_bit_18',
        "command": 'set_bit',
        "args": [0x7044, 0]
    },
    {
        "identifier": 'EVENT_1555_mem_7000_and_const_19',
        "command": 'mem_7000_and_const',
        "args": [0x03ff]
    },
    {
        "identifier": 'EVENT_1555_mem_compare_20',
        "command": 'mem_compare',
        "args": [0x7000, 512]
    },
    {
        "identifier": 'EVENT_1555_jmp_if_comparison_result_is_lesser_21',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1555_mem_7000_and_const_23']
    },
    {
        "identifier": 'EVENT_1555_set_bit_22',
        "command": 'set_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'EVENT_1555_mem_7000_and_const_23',
        "command": 'mem_7000_and_const',
        "args": [0x0007]
    },
    {
        "identifier": 'EVENT_1555_add_24',
        "command": 'add',
        "args": [0x7000, 0x01]
    },
    {
        "identifier": 'EVENT_1555_set_object_memory_to_25',
        "command": 'set_object_memory_to',
        "args": [0x7006]
    },
    {
        "identifier": 'EVENT_1555_pause_26',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'EVENT_1555_end_loop_27',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1555_set_short_mem_28',
        "command": 'set_short_mem',
        "args": [0x7026, 0x7010]
    },
    {
        "identifier": 'EVENT_1555_set_short_mem_29',
        "command": 'set_short_mem',
        "args": [0x7028, 0x7012]
    },
    {
        "identifier": 'EVENT_1555_set_short_30',
        "command": 'set_short',
        "args": [0x7014, 0x0100]
    },
    {
        "identifier": 'EVENT_1555_set_31',
        "command": 'set',
        "args": [0x7000, 20]
    },
    {
        "identifier": 'EVENT_1555_set_short_mem_32',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000]
    },
    {
        "identifier": 'EVENT_1555_start_loop_n_times_33',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'EVENT_1555_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_1555_action_queue_async_34_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1555_action_queue_async_34_SUBSCRIPT_move_7010_7012_7014_to_7016_7018_701A_1',
                "command": 'move_7010_7012_7014_to_7016_7018_701A'
            },
            {
                "identifier": 'EVENT_1555_action_queue_async_34_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x99]
            },
            {
                "identifier": 'EVENT_1555_action_queue_async_34_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1555_add_35',
        "command": 'add',
        "args": [0x70a9, 0x01]
    },
    {
        "identifier": 'EVENT_1555_end_loop_36',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1555_jmp_to_subroutine_37',
        "command": 'jmp_to_subroutine',
        "args": [0x11cf]
    },
    {
        "identifier": 'EVENT_1555_jmp_38',
        "command": 'jmp',
        "args": ['EVENT_1555_pause_3']
    },
    {
        "identifier": 'EVENT_1555_jmp_if_bit_set_39',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 1, 'EVENT_1555_set_action_script_sync_45']
    },
    {
        "identifier": 'EVENT_1555_set_action_script_sync_40',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 32]
    },
    {
        "identifier": 'EVENT_1555_set_action_script_sync_41',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 32]
    },
    {
        "identifier": 'EVENT_1555_set_action_script_sync_42',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 32]
    },
    {
        "identifier": 'EVENT_1555_set_action_script_sync_43',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 32]
    },
    {
        "identifier": 'EVENT_1555_jmp_44',
        "command": 'jmp',
        "args": ['EVENT_1555_ret_49']
    },
    {
        "identifier": 'EVENT_1555_set_action_script_sync_45',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 33]
    },
    {
        "identifier": 'EVENT_1555_set_action_script_sync_46',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 33]
    },
    {
        "identifier": 'EVENT_1555_set_action_script_sync_47',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 33]
    },
    {
        "identifier": 'EVENT_1555_set_action_script_sync_48',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 33]
    },
    {
        "identifier": 'EVENT_1555_ret_49',
        "command": 'ret'
    }
]
