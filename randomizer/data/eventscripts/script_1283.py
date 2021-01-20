from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1283_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR, RadialDirections.NORTHEAST, 4, 19, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1283_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1283_action_queue_sync_1_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_1283_action_queue_sync_1_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [7, 13, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1283_action_queue_sync_1_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1283_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1283_action_queue_sync_2_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1283_action_queue_sync_2_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1283_action_queue_sync_2_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1283_action_queue_sync_2_SUBSCRIPT_shift_west_pixels_3',
                "command": 'shift_west_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1283_action_queue_sync_2_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1283_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1283_action_queue_sync_3_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1283_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1283_action_queue_sync_4_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1283_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1283_action_queue_sync_5_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1283_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1283_action_queue_async_6_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1283_remove_from_current_level_7',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1283_fade_in_from_black_async_8',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1283_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1283_action_queue_async_9_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_1283_pause_10',
        "command": 'pause',
        "args": [80],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1283_enter_area_11',
        "command": 'enter_area',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, RadialDirections.SOUTHWEST, 3, 26, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1283_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1283_action_queue_async_12_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1283_action_queue_async_12_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1283_action_queue_async_12_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_1283_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
