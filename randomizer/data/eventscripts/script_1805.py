from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1805_set_short_mem_0',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x70ae, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_jmp_fork_mario_on_object_2',
        "command": 'jmp_fork_mario_on_object',
        "args": ['EVENT_1805_set_41', 'EVENT_1805_set_41'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_store_coin_amount_7000_3',
        "command": 'store_coin_amount_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_mem_compare_4',
        "command": 'mem_compare',
        "args": [0x7000, 50],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_jmp_if_comparison_result_is_lesser_5',
        "command": 'jmp_if_comparison_result_is_lesser',
        "args": ['EVENT_1805_run_dialog_39'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_run_dialog_6',
        "command": 'run_dialog',
        "args": [1240, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_jmp_if_dialog_option_b_7',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_1805_pause_44'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_pause_8',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_set_action_script_async_9',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_1805_action_queue_async_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1805_action_queue_async_10_SUBSCRIPT_sequence_looping_on_1',
                "command": 'sequence_looping_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1805_action_queue_async_10_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1805_action_queue_async_10_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.SEQUENCE]]
            },
        ]
    },
    {
        "identifier": 'EVENT_1805_set_11',
        "command": 'set',
        "args": [0x7000, 50],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_dec_coins_12',
        "command": 'dec_coins',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_play_sound_13',
        "command": 'play_sound',
        "args": [Sounds._055_LOSE_COINS_COIN_FOUNTAIN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_run_dialog_14',
        "command": 'run_dialog',
        "args": [1241, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_set_15',
        "command": 'set',
        "args": [0x70aa, 23],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_jmp_to_subroutine_16',
        "command": 'jmp_to_subroutine',
        "args": [0x4e72],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_set_bit_17',
        "command": 'set_bit',
        "args": [0x7050, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_clear_bit_18',
        "command": 'clear_bit',
        "args": [0x7094, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_add_19',
        "command": 'add',
        "args": [0x70ad, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_jmp_if_bit_clear_20',
        "command": 'jmp_if_bit_clear',
        "args": [0x704f, 2, 'EVENT_1805_ret_38'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_pause_21',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_set_22',
        "command": 'set',
        "args": [0x70ab, 24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_run_event_as_subroutine_23',
        "command": 'run_event_as_subroutine',
        "args": [1739],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_play_sound_24',
        "command": 'play_sound',
        "args": [Sounds._084_SMOKED, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1805_action_queue_sync_25_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1805_action_queue_sync_25_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [10, 26, 20, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_1805_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1805_action_queue_sync_26_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1805_action_queue_sync_26_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [10, 26, 23, RadialDirections.EAST]
            },
        ]
    },
    {
        "identifier": 'EVENT_1805_set_short_27',
        "command": 'set_short',
        "args": [0x7034, 0x0001],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_set_7010_to_object_xyz_28',
        "command": 'set_7010_to_object_xyz',
        "args": [AreaObjects.NPC_0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_start_loop_n_times_29',
        "command": 'start_loop_n_times',
        "args": [14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_pause_30',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_create_packet_at_7010_coords_jmp_if_null_31',
        "command": 'create_packet_at_7010_coords_jmp_if_null',
        "args": [NPCPackets._032_BLUE_CLOUD, 'EVENT_1805_pause_30'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_pause_32',
        "command": 'pause',
        "args": [4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_add_short_33',
        "command": 'add_short',
        "args": [0x7034, 0x0003],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_add_short_34',
        "command": 'add_short',
        "args": [0x7014, 0x0050],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_end_loop_35',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_set_36',
        "command": 'set',
        "args": [0x70ab, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_run_event_as_subroutine_37',
        "command": 'run_event_as_subroutine',
        "args": [1739],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_ret_38',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_run_dialog_39',
        "command": 'run_dialog',
        "args": [1239, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_ret_40',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_set_41',
        "command": 'set',
        "args": [0x70aa, 23],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_jmp_to_subroutine_42',
        "command": 'jmp_to_subroutine',
        "args": [0x4e72],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_ret_43',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_pause_44',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_set_action_script_async_45',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1805_ret_46',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
