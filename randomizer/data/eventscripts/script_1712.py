from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1712_stop_all_background_events_0',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_1712_set_short_1',
        "command": 'set_short',
        "args": [0x700e, 0x0009]
    },
    {
        "identifier": 'EVENT_1712_start_battle_700E_2',
        "command": 'start_battle_700E'
    },
    {
        "identifier": 'EVENT_1712_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x707c, 5]
    },
    {
        "identifier": 'EVENT_1712_set_bit_4',
        "command": 'set_bit',
        "args": [0x707c, 6]
    },
    {
        "identifier": 'EVENT_1712_set_bit_5',
        "command": 'set_bit',
        "args": [0x707c, 7]
    },
    {
        "identifier": 'EVENT_1712_run_event_as_subroutine_6',
        "command": 'run_event_as_subroutine',
        "args": [24]
    },
    {
        "identifier": 'EVENT_1712_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1712_action_queue_sync_7_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1712_action_queue_sync_7_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_1712_set_8',
        "command": 'set',
        "args": [0x70ab, 20]
    },
    {
        "identifier": 'EVENT_1712_start_loop_n_times_9',
        "command": 'start_loop_n_times',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1712_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_1712_inc_16']
    },
    {
        "identifier": 'EVENT_1712_jmp_if_object_not_in_level_11',
        "command": 'jmp_if_object_not_in_level',
        "args": [AreaObjects.MEM_70AB, Rooms._207_BANDITS_WAY_AREA_02, 'EVENT_1712_action_queue_async_13']
    },
    {
        "identifier": 'EVENT_1712_jmp_12',
        "command": 'jmp',
        "args": ['EVENT_1712_inc_16']
    },
    {
        "identifier": 'EVENT_1712_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70AB],
        "subscript": [
            {
                "identifier": 'EVENT_1712_action_queue_async_13_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1712_action_queue_async_13_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0xfd, 0x12]
            },
            {
                "identifier": 'EVENT_1712_action_queue_async_13_SUBSCRIPT_set_700C_to_object_coord_2',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.MARIO, Coords.X, [7], CoordUnits.PIXEL]
            },
            {
                "identifier": 'EVENT_1712_action_queue_async_13_SUBSCRIPT_mem_compare_val_3',
                "command": 'mem_compare_val',
                "args": [14]
            },
            {
                "identifier": 'EVENT_1712_action_queue_async_13_SUBSCRIPT_jmp_if_comparison_result_is_lesser_4',
                "command": 'jmp_if_comparison_result_is_lesser',
                "args": ['EVENT_1712_action_queue_async_13_SUBSCRIPT_transfer_to_xyzf_9']
            },
            {
                "identifier": 'EVENT_1712_action_queue_async_13_SUBSCRIPT_transfer_to_xyzf_5',
                "command": 'transfer_to_xyzf',
                "args": [8, 74, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1712_action_queue_async_13_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1712_action_queue_async_13_SUBSCRIPT_face_northeast_7',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1712_action_queue_async_13_SUBSCRIPT_jmp_8',
                "command": 'jmp',
                "args": ['EVENT_1712_action_queue_async_13_SUBSCRIPT_set_solidity_bits_12']
            },
            {
                "identifier": 'EVENT_1712_action_queue_async_13_SUBSCRIPT_transfer_to_xyzf_9',
                "command": 'transfer_to_xyzf',
                "args": [18, 73, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1712_action_queue_async_13_SUBSCRIPT_visibility_on_10',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1712_action_queue_async_13_SUBSCRIPT_face_southwest_11',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1712_action_queue_async_13_SUBSCRIPT_set_solidity_bits_12',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_1712_action_queue_async_13_SUBSCRIPT_object_memory_clear_bit_13',
                "command": 'object_memory_clear_bit',
                "args": [0x30, [4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1712_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70AB, 474]
    },
    {
        "identifier": 'EVENT_1712_summon_to_level_15',
        "command": 'summon_to_level',
        "args": [AreaObjects.MEM_70AB, Rooms._207_BANDITS_WAY_AREA_02]
    },
    {
        "identifier": 'EVENT_1712_inc_16',
        "command": 'inc',
        "args": [0x70ab]
    },
    {
        "identifier": 'EVENT_1712_end_loop_17',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_1712_run_background_event_18',
        "command": 'run_background_event',
        "args": [1705, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_1712_ret_19',
        "command": 'ret'
    }
]
