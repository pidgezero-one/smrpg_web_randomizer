from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_697_set_7000_to_current_level_0',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_697_jmp_if_7000_equals_short_1',
        "command": 'jmp_if_7000_equals_short',
        "args": [65, 'EVENT_697_run_dialog_17']
    },
    {
        "identifier": 'EVENT_697_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x704c, 6, 'EVENT_697_run_dialog_8']
    },
    {
        "identifier": 'EVENT_697_run_dialog_3',
        "command": 'run_dialog',
        "args": [2158, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_697_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_697_action_queue_sync_4_SUBSCRIPT_set_700C_to_object_coord_0',
                "command": 'set_700C_to_object_coord',
                "args": [AreaObjects.DUMMY_0X07, Coords.F, []]
            },
            {
                "identifier": 'EVENT_697_action_queue_sync_4_SUBSCRIPT_set_7000_short_mem_to_700C_1',
                "command": 'set_7000_short_mem_to_700C',
                "args": [0x7024]
            },
            {
                "identifier": 'EVENT_697_action_queue_sync_4_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_697_run_dialog_5',
        "command": 'run_dialog',
        "args": [2159, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_697_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_697_action_queue_async_6_SUBSCRIPT_set_700C_to_7000_short_mem_0',
                "command": 'set_700C_to_7000_short_mem',
                "args": [0x7024]
            },
            {
                "identifier": 'EVENT_697_action_queue_async_6_SUBSCRIPT_face_east_7C_1',
                "command": 'face_east_7C'
            }
        ]
    },
    {
        "identifier": 'EVENT_697_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_697_run_dialog_8',
        "command": 'run_dialog',
        "args": [2160, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_697_set_7000_to_object_coord_9',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MEM_70A8, Coords.F, []]
    },
    {
        "identifier": 'EVENT_697_set_7000_short_mem_to_7000_10',
        "command": 'set_7000_short_mem_to_7000',
        "args": [0x7024]
    },
    {
        "identifier": 'EVENT_697_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_697_action_queue_async_11_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_697_run_dialog_12',
        "command": 'run_dialog',
        "args": [2161, AreaObjects.MEM_70A8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_697_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_697_action_queue_async_13_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_697_run_dialog_14',
        "command": 'run_dialog',
        "args": [2162, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_697_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.MEM_70A8],
        "subscript": [
            {
                "identifier": 'EVENT_697_action_queue_async_15_SUBSCRIPT_set_700C_to_7000_short_mem_0',
                "command": 'set_700C_to_7000_short_mem',
                "args": [0x7024]
            },
            {
                "identifier": 'EVENT_697_action_queue_async_15_SUBSCRIPT_face_east_7C_1',
                "command": 'face_east_7C'
            }
        ]
    },
    {
        "identifier": 'EVENT_697_ret_16',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_697_run_dialog_17',
        "command": 'run_dialog',
        "args": [2179, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_697_ret_18',
        "command": 'ret'
    }
]
