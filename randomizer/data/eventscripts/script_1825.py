from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1825_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_1825_priority_set_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7095, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_priority_set_2',
        "command": 'priority_set',
        "args": [[_0x81Flags.LAYER_1, _0x81Flags.LAYER_2, _0x81Flags.NPC_SPRITES], [_0x81Flags.LAYER_3], [_0x81Flags.NPC_SPRITES, _0x81Flags.BACKGROUND, _0x81Flags.HALF_INTENSITY]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_remove_from_current_level_3',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_set_short_4',
        "command": 'set_short',
        "args": [0x7038, 0x0c80],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_set_short_5',
        "command": 'set_short',
        "args": [0x703a, 0x1780],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_set_short_6',
        "command": 'set_short',
        "args": [0x703c, 0x0100],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_set_7',
        "command": 'set',
        "args": [0x70a9, 27],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_start_loop_n_times_8',
        "command": 'start_loop_n_times',
        "args": [3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_1825_action_queue_sync_9_SUBSCRIPT_shift_z_up_pixels_0',
                "command": 'shift_z_up_pixels',
                "args": [4]
            },
        ]
    },
    {
        "identifier": 'EVENT_1825_add_10',
        "command": 'add',
        "args": [0x70a9, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_end_loop_11',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_pause_12',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_jmp_if_bit_clear_13',
        "command": 'jmp_if_bit_clear',
        "args": [0x7095, 4, 'EVENT_1825_set_short_46'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_set_short_mem_14',
        "command": 'set_short_mem',
        "args": [0x7000, 0x702e],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_mem_compare_15',
        "command": 'mem_compare',
        "args": [0x7000, 9],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_jmp_if_comparison_result_is_lesser_16',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1825_add_21'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_mem_compare_17',
        "command": 'mem_compare',
        "args": [0x7000, 19],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_jmp_if_comparison_result_is_lesser_18',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1825_set_short_mem_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_dec_19',
        "command": 'dec',
        "args": [0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_1825_set_short_mem_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_add_21',
        "command": 'add',
        "args": [0x7000, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_set_short_mem_22',
        "command": 'set_short_mem',
        "args": [0x7016, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_set_short_mem_23',
        "command": 'set_short_mem',
        "args": [0x7030, 0x7018],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_jmp_24',
        "command": 'jmp',
        "args": ['EVENT_1825_action_queue_sync_35'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_set_short_mem_25',
        "command": 'set_short_mem',
        "args": [0x702e, 0x7016],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_set_short_mem_26',
        "command": 'set_short_mem',
        "args": [0x7000, 0x7030],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_mem_compare_27',
        "command": 'mem_compare',
        "args": [0x7000, 29],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_jmp_if_comparison_result_is_lesser_28',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1825_add_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_mem_compare_29',
        "command": 'mem_compare',
        "args": [0x7000, 38],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_jmp_if_comparison_result_is_lesser_30',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1825_set_short_mem_34'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_add_31',
        "command": 'add',
        "args": [0x7000, 65534],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_jmp_32',
        "command": 'jmp',
        "args": ['EVENT_1825_set_short_mem_34'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_add_33',
        "command": 'add',
        "args": [0x7000, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_set_short_mem_34',
        "command": 'set_short_mem',
        "args": [0x7018, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_action_queue_sync_35',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1825_action_queue_sync_35_SUBSCRIPT_run_away_transfer_0',
                "command": 'run_away_transfer',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1825_action_queue_async_36',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_1825_action_queue_async_36_SUBSCRIPT_run_away_transfer_0',
                "command": 'run_away_transfer',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1825_add_short_37',
        "command": 'add_short',
        "args": [0x7016, 0xffff],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_action_queue_sync_38',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1825_action_queue_sync_38_SUBSCRIPT_run_away_transfer_0',
                "command": 'run_away_transfer',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1825_action_queue_async_39',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_1825_action_queue_async_39_SUBSCRIPT_run_away_transfer_0',
                "command": 'run_away_transfer',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_1825_set_short_40',
        "command": 'set_short',
        "args": [0x703e, 0x001d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_jmp_to_subroutine_41',
        "command": 'jmp_to_subroutine',
        "args": [0x56cb],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_set_bit_42',
        "command": 'set_bit',
        "args": [0x7094, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_set_43',
        "command": 'set',
        "args": [0x70ab, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_run_event_as_subroutine_44',
        "command": 'run_event_as_subroutine',
        "args": [1739],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_clear_bit_45',
        "command": 'clear_bit',
        "args": [0x7094, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_set_short_46',
        "command": 'set_short',
        "args": [0x702c, 0x001b],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_set_47',
        "command": 'set',
        "args": [0x70a9, 27],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_set_48',
        "command": 'set',
        "args": [0x70aa, 28],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_action_queue_async_49',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_1825_action_queue_async_49_SUBSCRIPT_bpl_26_27_28_0',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_1825_action_queue_async_49_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0xfd, 0x24, 0x11, 0x12]
            },
            {
                "identifier": 'EVENT_1825_action_queue_async_49_SUBSCRIPT_set_short_mem_2',
                "command": 'set_short_mem',
                "args": [0x702a, 0x700c]
            },
        ]
    },
    {
        "identifier": 'EVENT_1825_pause_action_script_50',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_set_action_script_sync_51',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MEM_70AA, 479],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_pause_52',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_set_action_script_sync_53',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_10, 653],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_run_background_event_54',
        "command": 'run_background_event',
        "args": [1828, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_run_background_event_55',
        "command": 'run_background_event',
        "args": [1877, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_6]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1825_jmp_to_event_56',
        "command": 'jmp_to_event',
        "args": [1829],
        "subscript": []
    },
]
