from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_466_set_action_script_sync_0',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_10, 794],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 1, 'EVENT_466_set_action_script_sync_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 431],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_jmp_3',
        "command": 'jmp',
        "args": ['EVENT_466_jmp_if_bit_clear_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 797],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x705e, 2, 'EVENT_466_set_action_script_sync_14'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_set_action_script_sync_6',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 795],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_set_action_script_sync_7',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 796],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_pause_action_script_8',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_466_action_queue_sync_9_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_466_start_embedded_action_script_async_10',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_466_start_embedded_action_script_async_10_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [16, 64, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_466_start_embedded_action_script_async_10_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_466_start_embedded_action_script_async_10_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_466_start_embedded_action_script_async_10_SUBSCRIPT_set_object_memory_bits_3',
                "command": 'set_object_memory_bits',
                "args": [0x0b, bits=[0, 1]]
            },
            {
                "identifier": 'EVENT_466_start_embedded_action_script_async_10_SUBSCRIPT_clear_solidity_bits_4',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_466_set_action_script_sync_11',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 677],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 677],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_jmp_13',
        "command": 'jmp',
        "args": ['EVENT_466_jmp_if_bit_set_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 677],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 677],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 677],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 677],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_jmp_if_bit_set_18',
        "command": 'jmp_if_bit_set',
        "args": [0x705e, 1, 'EVENT_256_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 500],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_clear_bit_20',
        "command": 'clear_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_clear_bit_21',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_clear_bit_22',
        "command": 'clear_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_clear_bit_23',
        "command": 'clear_bit',
        "args": [0x7043, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_clear_bit_24',
        "command": 'clear_bit',
        "args": [0x7043, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_pause_25',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_jmp_if_bit_set_26',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_466_add_31'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_jmp_if_bit_set_27',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_466_set_short_35'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_jmp_if_bit_set_28',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_466_set_short_42'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_jmp_if_bit_set_29',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 4, 'EVENT_466_pause_39'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_jmp_30',
        "command": 'jmp',
        "args": ['EVENT_466_pause_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_add_31',
        "command": 'add',
        "args": [0x70ae, 0x01],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_set_action_script_sync_32',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 499],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_set_action_script_sync_33',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 430],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_jmp_34',
        "command": 'jmp',
        "args": ['EVENT_466_clear_bit_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_set_short_35',
        "command": 'set_short',
        "args": [0x7032, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_set_action_script_sync_36',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 502],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_set_action_script_sync_37',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 428],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_jmp_38',
        "command": 'jmp',
        "args": ['EVENT_466_pause_39'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_pause_39',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_jmp_if_bit_set_40',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 2, 'EVENT_466_clear_bit_20'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_jmp_41',
        "command": 'jmp',
        "args": ['EVENT_466_pause_39'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_set_short_42',
        "command": 'set_short',
        "args": [0x7032, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_set_action_script_sync_43',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 501],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_set_action_script_sync_44',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_9, 430],
        "subscript": []
    },
    {
        "identifier": 'EVENT_466_jmp_45',
        "command": 'jmp',
        "args": ['EVENT_466_pause_39'],
        "subscript": []
    }
]
