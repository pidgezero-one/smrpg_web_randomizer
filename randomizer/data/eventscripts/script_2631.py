from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2631_set_0',
        "command": 'set',
        "args": [0x70ae, 22],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_run_dialog_1',
        "command": 'run_dialog',
        "args": [3312, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_jmp_if_dialog_option_b_2',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2631_pause_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_pause_3',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_set_action_script_async_4',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_jmp_if_bit_set_5',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 7, 'EVENT_2631_store_coin_amount_7000_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_set_bit_6',
        "command": 'set_bit',
        "args": [0x7045, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_run_dialog_7',
        "command": 'run_dialog',
        "args": [3314, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_jmp_if_dialog_option_b_8',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2631_pause_16'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_pause_9',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_set_action_script_async_10',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_store_coin_amount_7000_11',
        "command": 'store_coin_amount_7000',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_mem_compare_12',
        "command": 'mem_compare',
        "args": [0x7000, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_jmp_if_comparison_result_is_greater_or_equal_13',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_2631_run_dialog_27'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_run_dialog_14',
        "command": 'run_dialog',
        "args": [3316, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_pause_16',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_set_action_script_async_17',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_run_dialog_18',
        "command": 'run_dialog',
        "args": [3317, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_jmp_if_dialog_option_b_19',
        "command": 'jmp_if_dialog_option_b',
        "args": ['EVENT_2631_pause_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_pause_20',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_set_action_script_async_21',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_jmp_22',
        "command": 'jmp',
        "args": ['EVENT_2631_store_coin_amount_7000_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_pause_23',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_set_action_script_async_24',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 671],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_run_dialog_25',
        "command": 'run_dialog',
        "args": [3313, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_ret_26',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_run_dialog_27',
        "command": 'run_dialog',
        "args": [3315, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_set_28',
        "command": 'set',
        "args": [0x7000, 10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_dec_coins_29',
        "command": 'dec_coins',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_set_bit_30',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2631_action_queue_async_31_SUBSCRIPT_overwrite_solidity_0',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2631_action_queue_async_31_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2631_action_queue_async_31_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [1, 17]
            },
            {
                "identifier": 'EVENT_2631_action_queue_async_31_SUBSCRIPT_face_south_3',
                "command": 'face_south',
                "args": []
            },
            {
                "identifier": 'EVENT_2631_action_queue_async_31_SUBSCRIPT_overwrite_solidity_4',
                "command": 'overwrite_solidity',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_2631_action_queue_async_31_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2631_enable_controls_32',
        "command": 'enable_controls',
        "args": [[ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_set_action_script_sync_33',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 14],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2631_action_queue_sync_34',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2631_action_queue_sync_34_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [10, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2631_ret_35',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
