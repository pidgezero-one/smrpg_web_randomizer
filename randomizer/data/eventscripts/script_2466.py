from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2466_summon_to_level_0',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_0, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_summon_to_level_1',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_1, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_summon_to_level_2',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_summon_to_level_3',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_summon_to_level_4',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_summon_to_level_5',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_6, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_summon_to_level_6',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_7, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_summon_to_level_7',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_9, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_summon_to_level_8',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_10, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_summon_to_level_9',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_11, Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_clear_bit_10',
        "command": 'clear_bit',
        "args": [0x7047, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_set_7000_to_object_coord_11',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.X, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_jmp_if_var_equals_short_12',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 4, 'EVENT_2466_set_7000_to_object_coord_19'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_jmp_if_var_equals_short_13',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 5, 'EVENT_2466_action_queue_sync_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_jmp_if_var_equals_short_14',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 7, 'EVENT_2466_set_7000_to_object_coord_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_jmp_if_var_equals_short_15',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 9, 'EVENT_2466_action_queue_sync_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_jmp_if_var_equals_short_16',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 13, 'EVENT_2466_action_queue_sync_29'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_jmp_if_var_equals_short_17',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 16, 'EVENT_2466_action_queue_sync_29'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_jmp_18',
        "command": 'jmp',
        "args": ['EVENT_2466_fade_in_from_black_async_36'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_set_7000_to_object_coord_19',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Y, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_jmp_if_var_equals_short_20',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 70, 'EVENT_2466_action_queue_sync_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_jmp_21',
        "command": 'jmp',
        "args": ['EVENT_2466_action_queue_sync_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_set_7000_to_object_coord_22',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Y, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_jmp_if_var_equals_short_23',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 75, 'EVENT_2466_action_queue_sync_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_jmp_24',
        "command": 'jmp',
        "args": ['EVENT_2466_action_queue_sync_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2466_action_queue_sync_25_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [8, 112]
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_25_SUBSCRIPT_jmp_if_random_above_128_1',
                "command": 'jmp_if_random_above_128',
                "args": ['EVENT_2466_action_queue_sync_25_SUBSCRIPT_face_southeast_4']
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_25_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_25_SUBSCRIPT_ret_3',
                "command": 'ret',
                "args": []
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_25_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2466_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2466_action_queue_sync_26_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [6, 111]
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_26_SUBSCRIPT_jmp_if_random_above_128_1',
                "command": 'jmp_if_random_above_128',
                "args": ['EVENT_2466_action_queue_sync_26_SUBSCRIPT_face_southeast_4']
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_26_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_26_SUBSCRIPT_ret_3',
                "command": 'ret',
                "args": []
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_26_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2466_remove_from_current_level_27',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_jmp_28',
        "command": 'jmp',
        "args": ['EVENT_2466_fade_in_from_black_async_36'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2466_action_queue_sync_29_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [15, 72]
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_29_SUBSCRIPT_jmp_if_random_above_128_1',
                "command": 'jmp_if_random_above_128',
                "args": ['EVENT_2466_action_queue_sync_29_SUBSCRIPT_face_southeast_4']
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_29_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_29_SUBSCRIPT_ret_3',
                "command": 'ret',
                "args": []
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_29_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2466_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2466_action_queue_sync_30_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [13, 70]
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_30_SUBSCRIPT_jmp_if_random_above_128_1',
                "command": 'jmp_if_random_above_128',
                "args": ['EVENT_2466_action_queue_sync_30_SUBSCRIPT_face_southeast_4']
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_30_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_30_SUBSCRIPT_ret_3',
                "command": 'ret',
                "args": []
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_30_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2466_remove_from_current_level_31',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_jmp_32',
        "command": 'jmp',
        "args": ['EVENT_2466_fade_in_from_black_async_36'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2466_action_queue_sync_33_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [5, 72]
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_33_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2466_action_queue_sync_34',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2466_action_queue_sync_34_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [8, 82]
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_34_SUBSCRIPT_jmp_if_random_above_128_1',
                "command": 'jmp_if_random_above_128',
                "args": ['EVENT_2466_action_queue_sync_34_SUBSCRIPT_face_southeast_4']
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_34_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_34_SUBSCRIPT_ret_3',
                "command": 'ret',
                "args": []
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_34_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2466_action_queue_sync_35',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2466_action_queue_sync_35_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [7, 88]
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_35_SUBSCRIPT_jmp_if_random_above_128_1',
                "command": 'jmp_if_random_above_128',
                "args": ['EVENT_2466_action_queue_sync_35_SUBSCRIPT_face_southeast_4']
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_35_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_35_SUBSCRIPT_ret_3',
                "command": 'ret',
                "args": []
            },
            {
                "identifier": 'EVENT_2466_action_queue_sync_35_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2466_fade_in_from_black_async_36',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2466_ret_37',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
