from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1105_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7051, 1, 'EVENT_1109_run_dialog_0']
    },
    {
        "identifier": 'EVENT_1105_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'EVENT_1105_ret_69']
    },
    {
        "identifier": 'EVENT_1105_set_bit_2',
        "command": 'set_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1105_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_1105_clear_bit_4',
        "command": 'clear_bit',
        "args": [0x7043, 5]
    },
    {
        "identifier": 'EVENT_1105_clear_bit_5',
        "command": 'clear_bit',
        "args": [0x7043, 6]
    },
    {
        "identifier": 'EVENT_1105_enable_controls_until_return_6',
        "command": 'enable_controls_until_return',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1105_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1105_action_queue_async_7_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_1105_action_queue_async_7_SUBSCRIPT_object_memory_set_bit_1',
                "command": 'object_memory_set_bit',
                "args": [0x0b, [3]]
            },
            {
                "identifier": 'EVENT_1105_action_queue_async_7_SUBSCRIPT_bounce_to_xy_with_height_2',
                "command": 'bounce_to_xy_with_height',
                "args": [12, 51, 0]
            },
            {
                "identifier": 'EVENT_1105_action_queue_async_7_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1105_action_queue_async_7_SUBSCRIPT_face_northeast_4',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_1105_action_queue_async_7_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1105_action_queue_async_7_SUBSCRIPT_ret_6',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_1105_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1105_action_queue_sync_8_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1105_action_queue_sync_8_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_1105_action_queue_sync_8_SUBSCRIPT_shirt_to_xy_coords_2',
                "command": 'shirt_to_xy_coords',
                "args": [12, 47]
            }
        ]
    },
    {
        "identifier": 'EVENT_1105_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1105_action_queue_sync_9_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1105_action_queue_sync_9_SUBSCRIPT_shirt_to_xy_coords_1',
                "command": 'shirt_to_xy_coords',
                "args": [15, 49]
            },
            {
                "identifier": 'EVENT_1105_action_queue_sync_9_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1105_action_queue_sync_9_SUBSCRIPT_set_vram_priority_3',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_1105_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1105_action_queue_sync_10_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            },
            {
                "identifier": 'EVENT_1105_action_queue_sync_10_SUBSCRIPT_shirt_to_xy_coords_1',
                "command": 'shirt_to_xy_coords',
                "args": [14, 43]
            },
            {
                "identifier": 'EVENT_1105_action_queue_sync_10_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_1105_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1105_action_queue_sync_11_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [17, 45]
            },
            {
                "identifier": 'EVENT_1105_action_queue_sync_11_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1105_action_queue_sync_11_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_1105_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1105_action_queue_sync_12_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [16, 39]
            },
            {
                "identifier": 'EVENT_1105_action_queue_sync_12_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_1105_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1105_action_queue_sync_13_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [19, 41]
            },
            {
                "identifier": 'EVENT_1105_action_queue_sync_13_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1105_action_queue_sync_13_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_1105_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_1105_action_queue_sync_14_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [18, 35]
            },
            {
                "identifier": 'EVENT_1105_action_queue_sync_14_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_1105_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1105_action_queue_async_15_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [21, 37]
            },
            {
                "identifier": 'EVENT_1105_action_queue_async_15_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1105_action_queue_async_15_SUBSCRIPT_set_vram_priority_2',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_1105_jmp_if_bit_set_16',
        "command": 'jmp_if_bit_set',
        "args": [0x7051, 7, 'EVENT_1105_action_queue_sync_23']
    },
    {
        "identifier": 'EVENT_1105_stop_music_FDA2_17',
        "command": 'stop_music_FDA2'
    },
    {
        "identifier": 'EVENT_1105_set_bit_18',
        "command": 'set_bit',
        "args": [0x7051, 7]
    },
    {
        "identifier": 'EVENT_1105_set_bit_19',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_1105_deactivate_sound_channels_20',
        "command": 'deactivate_sound_channels',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_1105_pause_21',
        "command": 'pause',
        "args": [45]
    },
    {
        "identifier": 'EVENT_1105_play_music_default_volume_22',
        "command": 'play_music_default_volume',
        "args": [Music._17_TADPOLE_POND]
    },
    {
        "identifier": 'EVENT_1105_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1105_action_queue_sync_23_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1105_action_queue_sync_23_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [10, 33, 0]
            },
            {
                "identifier": 'EVENT_1105_action_queue_sync_23_SUBSCRIPT_ret_2',
                "command": 'ret'
            }
        ]
    },
    {
        "identifier": 'EVENT_1105_set_action_script_sync_24',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 91]
    },
    {
        "identifier": 'EVENT_1105_pause_25',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1105_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 92]
    },
    {
        "identifier": 'EVENT_1105_pause_27',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1105_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 91]
    },
    {
        "identifier": 'EVENT_1105_pause_29',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1105_set_action_script_sync_30',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 92]
    },
    {
        "identifier": 'EVENT_1105_pause_31',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1105_set_action_script_sync_32',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 91]
    },
    {
        "identifier": 'EVENT_1105_pause_33',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1105_set_action_script_sync_34',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 92]
    },
    {
        "identifier": 'EVENT_1105_pause_35',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1105_set_action_script_sync_36',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 91]
    },
    {
        "identifier": 'EVENT_1105_pause_37',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1105_set_action_script_sync_38',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 92]
    },
    {
        "identifier": 'EVENT_1105_pause_39',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1105_clear_bit_40',
        "command": 'clear_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_1105_set_7000_to_tapped_button_41',
        "command": 'set_7000_to_tapped_button'
    },
    {
        "identifier": 'EVENT_1105_pause_42',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1105_jmp_if_7000_any_bits_set_43',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[7], 'EVENT_1105_set_7000_to_pressed_button_46']
    },
    {
        "identifier": 'EVENT_1105_jmp_if_7000_any_bits_set_44',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[1, 2], 'EVENT_1105_action_queue_sync_49']
    },
    {
        "identifier": 'EVENT_1105_jmp_45',
        "command": 'jmp',
        "args": ['EVENT_1105_set_7000_to_tapped_button_41']
    },
    {
        "identifier": 'EVENT_1105_set_7000_to_pressed_button_46',
        "command": 'set_7000_to_pressed_button'
    },
    {
        "identifier": 'EVENT_1105_jmp_if_7000_any_bits_set_47',
        "command": 'jmp_if_7000_any_bits_set',
        "args": [[0, 3], 'EVENT_1107_action_queue_async_0']
    },
    {
        "identifier": 'EVENT_1105_jmp_48',
        "command": 'jmp',
        "args": ['EVENT_1105_set_7000_to_tapped_button_41']
    },
    {
        "identifier": 'EVENT_1105_action_queue_sync_49',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1105_action_queue_sync_49_SUBSCRIPT_shadow_on_0',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_1105_action_queue_sync_49_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1105_action_queue_sync_49_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_1105_action_queue_sync_49_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [22]
            }
        ]
    },
    {
        "identifier": 'EVENT_1105_set_action_script_sync_50',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 157]
    },
    {
        "identifier": 'EVENT_1105_pause_51',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1105_set_action_script_sync_52',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 157]
    },
    {
        "identifier": 'EVENT_1105_pause_53',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1105_set_action_script_sync_54',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 157]
    },
    {
        "identifier": 'EVENT_1105_pause_55',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1105_set_action_script_sync_56',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 157]
    },
    {
        "identifier": 'EVENT_1105_pause_57',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1105_set_action_script_sync_58',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 157]
    },
    {
        "identifier": 'EVENT_1105_pause_59',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1105_set_action_script_sync_60',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 157]
    },
    {
        "identifier": 'EVENT_1105_pause_61',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1105_set_action_script_sync_62',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 157]
    },
    {
        "identifier": 'EVENT_1105_pause_63',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1105_set_action_script_sync_64',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 157]
    },
    {
        "identifier": 'EVENT_1105_pause_65',
        "command": 'pause',
        "args": [5]
    },
    {
        "identifier": 'EVENT_1105_enable_controls_until_return_66',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_1105_set_action_script_async_67',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_1105_clear_bit_68',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'EVENT_1105_ret_69',
        "command": 'ret'
    }
]
