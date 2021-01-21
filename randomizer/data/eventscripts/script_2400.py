from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2400_unfreeze_all_npcs_0',
        "command": 'unfreeze_all_npcs'
    },
    {
        "identifier": 'EVENT_2400_clear_bit_1',
        "command": 'clear_bit',
        "args": [0x7045, 0]
    },
    {
        "identifier": 'EVENT_2400_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7045, 1]
    },
    {
        "identifier": 'EVENT_2400_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7045, 2]
    },
    {
        "identifier": 'EVENT_2400_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2400_action_queue_async_4_SUBSCRIPT_overwrite_solidity_0',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2400_action_queue_async_4_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_2400_action_queue_async_4_SUBSCRIPT_transfer_to_xyzf_2',
                "command": 'transfer_to_xyzf',
                "args": [14, 26, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_2400_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 455]
    },
    {
        "identifier": 'EVENT_2400_pause_6',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2400_pause_7',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2400_set_7000_to_tapped_button_8',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_2400_jmp_if_7000_all_bits_clear_9',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[7], 'EVENT_2400_pause_7']
    },
    {
        "identifier": 'EVENT_2400_pause_action_script_10',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_2400_jmp_if_bit_set_11',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 1, 'EVENT_2400_action_queue_async_15']
    },
    {
        "identifier": 'EVENT_2400_jmp_if_bit_set_12',
        "command": 'jmp_if_bit_set',
        "args": [0x7045, 2, 'EVENT_2400_action_queue_async_18']
    },
    {
        "identifier": 'EVENT_2400_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2400_action_queue_async_13_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_2400_action_queue_async_13_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2400_action_queue_async_13_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_2400_action_queue_async_13_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0x80, 0x00, 0x80, 0x00]
            },
            {
                "identifier": 'EVENT_2400_action_queue_async_13_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x25, 0x00, 0x0a, 0xd0, 0xff]
            },
            {
                "identifier": 'EVENT_2400_action_queue_async_13_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [104]
            },
            {
                "identifier": 'EVENT_2400_action_queue_async_13_SUBSCRIPT_bpl_26_27_28_6',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_2400_jmp_14',
        "command": 'jmp',
        "args": ['EVENT_2400_set_action_script_async_19']
    },
    {
        "identifier": 'EVENT_2400_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2400_action_queue_async_15_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2400_action_queue_async_15_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2400_action_queue_async_15_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_2400_action_queue_async_15_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0x00, 0xff, 0x80, 0x00]
            },
            {
                "identifier": 'EVENT_2400_action_queue_async_15_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x25, 0x00, 0x09, 0xd0, 0xff]
            },
            {
                "identifier": 'EVENT_2400_action_queue_async_15_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [104]
            },
            {
                "identifier": 'EVENT_2400_action_queue_async_15_SUBSCRIPT_bpl_26_27_28_6',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_2400_set_action_script_async_16',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 399]
    },
    {
        "identifier": 'EVENT_2400_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_2400_set_action_script_async_19']
    },
    {
        "identifier": 'EVENT_2400_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2400_action_queue_async_18_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2400_action_queue_async_18_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2400_action_queue_async_18_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_2400_action_queue_async_18_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x24, 0x00, 0x01, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2400_action_queue_async_18_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x25, 0x00, 0x09, 0xd0, 0xff]
            },
            {
                "identifier": 'EVENT_2400_action_queue_async_18_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [104]
            },
            {
                "identifier": 'EVENT_2400_action_queue_async_18_SUBSCRIPT_bpl_26_27_28_6',
                "command": 'bpl_26_27_28'
            }
        ]
    },
    {
        "identifier": 'EVENT_2400_set_action_script_async_19',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 399]
    },
    {
        "identifier": 'EVENT_2400_set_action_script_async_20',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2400_set_action_script_sync_21',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 454]
    },
    {
        "identifier": 'EVENT_2400_ret_22',
        "command": 'ret'
    }
]
