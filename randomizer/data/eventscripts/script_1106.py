from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1106_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_1106_ret_56'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_enable_controls_until_return_2',
        "command": 'enable_controls_until_return',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1106_action_queue_async_3_SUBSCRIPT_bounce_to_xy_with_height_0',
                "command": 'bounce_to_xy_with_height',
                "args": [22, 32, 4]
            },
            {
                "identifier": 'EVENT_1106_action_queue_async_3_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1106_action_queue_async_3_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1106_action_queue_async_3_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1106_action_queue_async_3_SUBSCRIPT_ret_4',
                "command": 'ret',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1106_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1106_action_queue_sync_4_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [12, 47]
            },
            {
                "identifier": 'EVENT_1106_action_queue_sync_4_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_1106_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1106_action_queue_sync_5_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [15, 49]
            },
            {
                "identifier": 'EVENT_1106_action_queue_sync_5_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1106_action_queue_sync_5_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_1106_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1106_action_queue_sync_6_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [14, 43]
            },
            {
                "identifier": 'EVENT_1106_action_queue_sync_6_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_1106_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1106_action_queue_sync_7_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [17, 45]
            },
            {
                "identifier": 'EVENT_1106_action_queue_sync_7_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1106_action_queue_sync_7_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_1106_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1106_action_queue_sync_8_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [16, 39]
            },
            {
                "identifier": 'EVENT_1106_action_queue_sync_8_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_1106_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1106_action_queue_sync_9_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [19, 41]
            },
            {
                "identifier": 'EVENT_1106_action_queue_sync_9_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1106_action_queue_sync_9_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_1106_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1106_action_queue_sync_10_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [18, 35]
            },
            {
                "identifier": 'EVENT_1106_action_queue_sync_10_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_1106_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1106_action_queue_async_11_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [21, 37]
            },
            {
                "identifier": 'EVENT_1106_action_queue_async_11_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1106_action_queue_async_11_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_1106_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 92],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_pause_13',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 91],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_pause_15',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 92],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_pause_17',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 91],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_pause_19',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 92],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_pause_21',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_set_action_script_sync_22',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 91],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_pause_23',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_set_action_script_sync_24',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 92],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_pause_25',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 91],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_pause_27',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_set_7000_to_tapped_button_28',
        "command": 'set_7000_to_tapped_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_pause_29',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_jmp_if_7000_any_bits_set_30',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_1106_set_7000_to_pressed_button_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_jmp_if_7000_any_bits_set_31',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0, 3], 'EVENT_1106_action_queue_sync_36'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_jmp_32',
        "command": 'jmp',
        "args": ['EVENT_1106_set_7000_to_tapped_button_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_set_7000_to_pressed_button_33',
        "command": 'set_7000_to_pressed_button',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_jmp_if_7000_any_bits_set_34',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[1, 2], 'EVENT_1106_action_queue_async_57'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_jmp_35',
        "command": 'jmp',
        "args": ['EVENT_1106_set_7000_to_tapped_button_28'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_action_queue_sync_36',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1106_action_queue_sync_36_SUBSCRIPT_shadow_on_0',
                "command": 'shadow_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1106_action_queue_sync_36_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1106_action_queue_sync_36_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_1106_action_queue_sync_36_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [22]
            },
            {
                "identifier": 'EVENT_1106_action_queue_sync_36_SUBSCRIPT_ret_4',
                "command": 'ret',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1106_set_action_script_sync_37',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 157],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_pause_38',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_set_action_script_sync_39',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 157],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_pause_40',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_set_action_script_sync_41',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 157],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_pause_42',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_set_action_script_sync_43',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 157],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_pause_44',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_set_action_script_sync_45',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 157],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_pause_46',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_set_action_script_sync_47',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 157],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_pause_48',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_set_action_script_sync_49',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 157],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_pause_50',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_set_action_script_sync_51',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 157],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_pause_52',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_enable_controls_until_return_53',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_set_action_script_async_54',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_clear_bit_55',
        "command": 'clear_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_ret_56',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1106_action_queue_async_57',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1106_action_queue_async_57_SUBSCRIPT_shadow_on_0',
                "command": 'shadow_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1106_action_queue_async_57_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1106_action_queue_async_57_SUBSCRIPT_object_memory_set_bit_2',
                "command": 'object_memory_set_bit',
                "args": [0x0b, [3]]
            },
            {
                "identifier": 'EVENT_1106_action_queue_async_57_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1106_action_queue_async_57_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [96]
            },
            {
                "identifier": 'EVENT_1106_action_queue_async_57_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1106_action_queue_async_57_SUBSCRIPT_set_solidity_bits_6',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_1106_action_queue_async_57_SUBSCRIPT_shift_southwest_steps_7',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1106_action_queue_async_57_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1106_action_queue_async_57_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1106_action_queue_async_57_SUBSCRIPT_reset_properties_10',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_1106_action_queue_async_57_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1106_jmp_58',
        "command": 'jmp',
        "args": ['EVENT_1107_set_7000_to_tapped_button_2'],
        "subscript": []
    }
]
