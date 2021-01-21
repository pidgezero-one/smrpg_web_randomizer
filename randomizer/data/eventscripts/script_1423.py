from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1423_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1423_action_queue_sync_0_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1423_action_queue_sync_0_SUBSCRIPT_ret_1',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_1423_action_queue_async_1',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_1423_action_queue_async_1_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1423_action_queue_async_1_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_1423_action_queue_async_1_SUBSCRIPT_ret_2',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_1423_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7052, 4, 'EVENT_1423_remove_from_current_level_7']
    },
    {
        "identifier": 'EVENT_1423_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7052, 5, 'EVENT_1423_remove_from_current_level_7']
    },
    {
        "identifier": 'EVENT_1423_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7052, 6, 'EVENT_1423_remove_from_current_level_7']
    },
    {
        "identifier": 'EVENT_1423_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1423_ret_6',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_1423_remove_from_current_level_7',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_1423_remove_from_current_level_8',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_1423_fade_in_from_black_async_9',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_1423_ret_10',
        "command": 'ret'
    }
]
