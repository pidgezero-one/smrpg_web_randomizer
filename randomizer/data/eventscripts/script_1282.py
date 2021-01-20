from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1282_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR, RadialDirections.NORTHEAST, 4, 19, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1282_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1282_action_queue_sync_1_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_1282_action_queue_sync_1_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [7, 13, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1282_action_queue_sync_1_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1282_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1282_action_queue_sync_2_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1282_action_queue_sync_2_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1282_action_queue_sync_2_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1282_action_queue_sync_2_SUBSCRIPT_shift_west_pixels_3',
                "command": 'shift_west_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1282_action_queue_sync_2_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1282_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x705f, 4, 'EVENT_1282_jmp_to_event_17'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1282_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1282_action_queue_sync_4_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1282_action_queue_sync_4_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [5, 16, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1282_action_queue_sync_4_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1282_action_queue_sync_4_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1282_action_queue_sync_4_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1282_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1282_action_queue_sync_5_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1282_action_queue_sync_5_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [6, 18, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1282_action_queue_sync_5_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1282_action_queue_sync_5_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1282_action_queue_sync_5_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1282_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1282_action_queue_sync_6_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1282_action_queue_sync_6_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [7, 20, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1282_action_queue_sync_6_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1282_action_queue_sync_6_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1282_action_queue_sync_6_SUBSCRIPT_sequence_looping_on_4',
                "command": 'sequence_looping_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1282_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1282_action_queue_async_7_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1282_action_queue_async_7_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [4, 21, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1282_action_queue_async_7_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1282_action_queue_async_7_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1282_action_queue_async_7_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1282_remove_from_current_level_8',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1282_fade_in_from_black_async_9',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1282_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1282_action_queue_async_10_SUBSCRIPT_shift_southwest_pixels_0',
                "command": 'shift_southwest_pixels',
                "args": [12]
            }
        ]
    },
    {
        "identifier": 'EVENT_1282_pause_11',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1282_run_dialog_12',
        "command": 'run_dialog',
        "args": [2571, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1282_pause_13',
        "command": 'pause',
        "args": [80],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1282_enter_area_14',
        "command": 'enter_area',
        "args": [Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, RadialDirections.SOUTHWEST, 3, 26, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1282_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1282_action_queue_async_15_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_1282_action_queue_async_15_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1282_action_queue_async_15_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1282_action_queue_async_15_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1282_action_queue_async_15_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1282_action_queue_async_15_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1282_action_queue_async_15_SUBSCRIPT_fixed_f_coord_off_6',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1282_action_queue_async_15_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1282_ret_16',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1282_jmp_to_event_17',
        "command": 'jmp_to_event',
        "args": [2278],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1282_ret_18',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
