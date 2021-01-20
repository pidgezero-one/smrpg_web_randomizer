from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2082_pause_0',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2082_action_queue_sync_1_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [4, 44, 1, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2082_action_queue_sync_1_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2082_action_queue_sync_1_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_2082_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2082_action_queue_sync_2_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 43, 1, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2082_action_queue_sync_2_SUBSCRIPT_shift_southeast_pixels_1',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2082_action_queue_sync_2_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2082_action_queue_sync_2_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_2082_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2082_action_queue_async_3_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 47, 1, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2082_action_queue_async_3_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2082_action_queue_async_3_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_2082_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7089, 4, 'EVENT_2082_set_action_script_sync_44'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7089, 5, 'EVENT_2082_set_action_script_sync_44'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7089, 6, 'EVENT_2082_set_action_script_sync_44'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 568],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_8',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 568],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_9',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 568],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_jmp_if_bit_set_10',
        "command": 'jmp_if_bit_set',
        "args": [0x7089, 7, 'EVENT_2085_pause_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_pause_11',
        "command": 'pause',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_run_dialog_12',
        "command": 'run_dialog',
        "args": [3006, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_pause_13',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 872],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_run_dialog_15',
        "command": 'run_dialog',
        "args": [3007, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 873],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_pause_17',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 874],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_run_dialog_19',
        "command": 'run_dialog',
        "args": [3008, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 875],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_pause_21',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_22',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 870],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_run_dialog_23',
        "command": 'run_dialog',
        "args": [3009, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_24',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 871],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_pause_25',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_run_dialog_26',
        "command": 'run_dialog',
        "args": [3010, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_pause_27',
        "command": 'pause',
        "args": [45],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 872],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_29',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 874],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_30',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 870],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_pause_31',
        "command": 'pause',
        "args": [150],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_32',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 873],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_33',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 875],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_34',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 871],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_pause_35',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_bit_36',
        "command": 'set_bit',
        "args": [0x7089, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_remove_one_from_inventory_37',
        "command": 'remove_one_from_inventory',
        "args": [items.BigBooFlag],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_remove_one_from_inventory_38',
        "command": 'remove_one_from_inventory',
        "args": [items.DryBonesFlag],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_remove_one_from_inventory_39',
        "command": 'remove_one_from_inventory',
        "args": [items.GreaperFlag],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_equip_item_to_character_40',
        "command": 'equip_item_to_character',
        "args": [PlayableCharacters.MARIO, items.GhostMedal],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_play_sound_41',
        "command": 'play_sound',
        "args": [Sounds._085_FLOWER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_jmp_42',
        "command": 'jmp',
        "args": ['EVENT_2081_run_dialog_93'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_ret_43',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_44',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 568],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_45',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 568],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_46',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 568],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_pause_47',
        "command": 'pause',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_48',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 872],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_jmp_if_bit_set_49',
        "command": 'jmp_if_bit_set',
        "args": [0x7089, 6, 'EVENT_2082_run_dialog_52'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_run_dialog_50',
        "command": 'run_dialog',
        "args": [2998, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_jmp_51',
        "command": 'jmp',
        "args": ['EVENT_2082_set_action_script_sync_53'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_run_dialog_52',
        "command": 'run_dialog',
        "args": [2999, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_53',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 873],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_pause_54',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_55',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 874],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_jmp_if_bit_set_56',
        "command": 'jmp_if_bit_set',
        "args": [0x7089, 5, 'EVENT_2082_run_dialog_59'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_run_dialog_57',
        "command": 'run_dialog',
        "args": [3000, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_jmp_58',
        "command": 'jmp',
        "args": ['EVENT_2082_set_action_script_sync_60'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_run_dialog_59',
        "command": 'run_dialog',
        "args": [3001, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_60',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 875],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_pause_61',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_62',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 870],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_jmp_if_bit_set_63',
        "command": 'jmp_if_bit_set',
        "args": [0x7089, 4, 'EVENT_2082_run_dialog_66'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_run_dialog_64',
        "command": 'run_dialog',
        "args": [3002, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_jmp_65',
        "command": 'jmp',
        "args": ['EVENT_2082_set_action_script_sync_67'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_run_dialog_66',
        "command": 'run_dialog',
        "args": [3003, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_set_action_script_sync_67',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 871],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_pause_68',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2082_jmp_69',
        "command": 'jmp',
        "args": ['EVENT_2081_run_dialog_93'],
        "subscript": []
    }
]
