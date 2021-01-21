from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_592_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7063, 6, 'EVENT_257_fade_in_from_black_async_0']
    },
    {
        "identifier": 'EVENT_592_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_592_action_queue_sync_1_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_592_action_queue_sync_1_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 0, 8, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_592_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_592_action_queue_sync_2_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_592_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_592_action_queue_sync_3_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_592_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_592_action_queue_sync_4_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_592_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_592_action_queue_sync_5_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_592_action_queue_sync_5_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_592_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_592_action_queue_sync_6_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_592_action_queue_sync_6_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_592_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_592_action_queue_async_7_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_592_action_queue_async_7_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_592_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 3, 'EVENT_257_fade_in_from_black_async_0']
    },
    {
        "identifier": 'EVENT_592_run_background_event_9',
        "command": 'run_background_event',
        "args": [596, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_592_fade_in_from_black_async_10',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_592_ret_11',
        "command": 'ret'
    }
]
