from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2354_jmp_if_object_in_level_0',
        "command": 'jmp_if_object_in_level',
        "args": [AreaObjects.NPC_8, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS, 'EVENT_2354_action_queue_sync_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2354_set_bit_1',
        "command": 'set_bit',
        "args": [0x708b, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2354_set_bit_2',
        "command": 'set_bit',
        "args": [0x708b, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2354_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2354_action_queue_sync_3_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2354_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2354_action_queue_sync_4_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2354_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2354_action_queue_sync_5_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2354_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2354_action_queue_sync_6_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2354_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2354_action_queue_sync_7_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2354_action_queue_sync_7_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2354_action_queue_sync_7_SUBSCRIPT_shift_southeast_pixels_2',
                "command": 'shift_southeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2354_action_queue_sync_7_SUBSCRIPT_face_southeast_3',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2354_action_queue_sync_7_SUBSCRIPT_shadow_off_4',
                "command": 'shadow_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2354_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2354_action_queue_async_8_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2354_action_queue_async_8_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2354_action_queue_async_8_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2354_action_queue_async_8_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2354_action_queue_async_8_SUBSCRIPT_shadow_off_4',
                "command": 'shadow_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2354_fade_in_from_black_async_9',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2354_ret_10',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
