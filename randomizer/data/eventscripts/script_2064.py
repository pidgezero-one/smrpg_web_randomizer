from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2064_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2064_action_queue_sync_0_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2064_action_queue_sync_0_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2064_action_queue_sync_0_SUBSCRIPT_shift_north_steps_2',
                "command": 'shift_north_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2064_action_queue_sync_0_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2064_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 5, 'EVENT_2064_action_queue_sync_15']
    },
    {
        "identifier": 'EVENT_2064_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 2, 'EVENT_2064_action_queue_sync_11']
    },
    {
        "identifier": 'EVENT_2064_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 1, 'EVENT_2064_action_queue_async_8']
    },
    {
        "identifier": 'EVENT_2064_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2064_action_queue_async_4_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [6, 13]
            },
            {
                "identifier": 'EVENT_2064_action_queue_async_4_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2064_action_queue_async_4_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2064_fade_in_from_black_async_5',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2064_jmp_6',
        "command": 'jmp',
        "args": ['EVENT_2065_pause_0']
    },
    {
        "identifier": 'EVENT_2064_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2064_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2064_action_queue_async_8_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 15, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2064_action_queue_async_8_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2064_action_queue_async_8_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2064_fade_in_from_black_async_9',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2064_ret_10',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2064_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2064_action_queue_sync_11_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [5, 9]
            },
            {
                "identifier": 'EVENT_2064_action_queue_sync_11_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_2064_action_queue_sync_11_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2064_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2064_action_queue_async_12_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 15, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2064_action_queue_async_12_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2064_action_queue_async_12_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2064_fade_in_from_black_async_13',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2064_ret_14',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2064_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2064_action_queue_sync_15_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [5, 14]
            },
            {
                "identifier": 'EVENT_2064_action_queue_sync_15_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2064_action_queue_sync_15_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2064_action_queue_sync_15_SUBSCRIPT_object_memory_clear_bit_3',
                "command": 'object_memory_clear_bit',
                "args": [0x08, [3, 4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2064_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2064_action_queue_async_16_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 16, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2064_action_queue_async_16_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2064_action_queue_async_16_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_2064_action_queue_async_16_SUBSCRIPT_shadow_on_3',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_2064_action_queue_async_16_SUBSCRIPT_object_memory_clear_bit_4',
                "command": 'object_memory_clear_bit',
                "args": [0x08, [3, 4]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2064_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 1006]
    },
    {
        "identifier": 'EVENT_2064_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 1006]
    },
    {
        "identifier": 'EVENT_2064_fade_in_from_black_async_19',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2064_ret_20',
        "command": 'ret'
    }
]
