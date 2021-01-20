from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2289_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._247_GAME_INTRO_TADPOLE_POND_MARIO_SUMMONS_TADPOLES, RadialDirections.NORTHEAST, 9, 58, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_freeze_camera_1',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2289_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2289_action_queue_sync_2_SUBSCRIPT_bounce_to_xy_with_height_1',
                "command": 'bounce_to_xy_with_height',
                "args": [11, 34, 0]
            },
            {
                "identifier": 'EVENT_2289_action_queue_sync_2_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_2289_action_queue_async_3',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2289_action_queue_async_3_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_3_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [12, 51, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_2289_fade_in_from_black_async_4',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_freeze_camera_5',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2289_action_queue_async_6_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [35]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_6_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_6_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_6_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2289_pause_7',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2289_action_queue_sync_8_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [12, 47]
            },
            {
                "identifier": 'EVENT_2289_action_queue_sync_8_SUBSCRIPT_ret_1',
                "command": 'ret',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2289_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2289_action_queue_sync_9_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [15, 49]
            },
            {
                "identifier": 'EVENT_2289_action_queue_sync_9_SUBSCRIPT_ret_1',
                "command": 'ret',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2289_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2289_action_queue_sync_10_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [14, 43]
            },
            {
                "identifier": 'EVENT_2289_action_queue_sync_10_SUBSCRIPT_ret_1',
                "command": 'ret',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2289_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2289_action_queue_sync_11_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [17, 45]
            },
            {
                "identifier": 'EVENT_2289_action_queue_sync_11_SUBSCRIPT_ret_1',
                "command": 'ret',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2289_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2289_action_queue_sync_12_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [16, 39]
            },
            {
                "identifier": 'EVENT_2289_action_queue_sync_12_SUBSCRIPT_ret_1',
                "command": 'ret',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2289_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2289_action_queue_sync_13_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [19, 41]
            },
            {
                "identifier": 'EVENT_2289_action_queue_sync_13_SUBSCRIPT_ret_1',
                "command": 'ret',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2289_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2289_action_queue_sync_14_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [18, 35]
            },
            {
                "identifier": 'EVENT_2289_action_queue_sync_14_SUBSCRIPT_ret_1',
                "command": 'ret',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2289_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2289_action_queue_async_15_SUBSCRIPT_shirt_to_xy_coords_0',
                "command": 'shirt_to_xy_coords',
                "args": [21, 37]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_15_SUBSCRIPT_ret_1',
                "command": 'ret',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2289_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 91],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_pause_17',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 92],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_pause_19',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_set_action_script_sync_20',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 91],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_pause_21',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_set_action_script_sync_22',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 92],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_pause_23',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_set_action_script_sync_24',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 91],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_pause_25',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_set_action_script_sync_26',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 92],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_pause_27',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 91],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_pause_29',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_set_action_script_sync_30',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 92],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_pause_31',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_shadow_on_2',
                "command": 'shadow_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_clear_solidity_bits_3',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_jump_to_height_6',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_shift_northeast_steps_7',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_shadow_off_9',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_face_northeast_11',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_shadow_on_13',
                "command": 'shadow_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_clear_solidity_bits_14',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_set_animation_speed_16',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_jump_to_height_17',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_shift_northeast_steps_18',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_set_solidity_bits_19',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_shadow_off_20',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_face_northeast_22',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_pause_23',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_shadow_on_24',
                "command": 'shadow_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_clear_solidity_bits_25',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_pause_26',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_set_animation_speed_27',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_jump_to_height_28',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_shift_northeast_steps_29',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_set_solidity_bits_30',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_shadow_off_31',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_pause_32',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_face_northeast_33',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_pause_34',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_shadow_on_35',
                "command": 'shadow_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_clear_solidity_bits_36',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_pause_37',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_set_animation_speed_38',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_jump_to_height_39',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_shift_northeast_steps_40',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_set_solidity_bits_41',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_shadow_off_42',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_pause_43',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_face_northeast_44',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2289_action_queue_async_32_SUBSCRIPT_pause_45',
                "command": 'pause',
                "args": [5]
            }
        ]
    },
    {
        "identifier": 'EVENT_2289_action_queue_sync_33',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2289_action_queue_sync_33_SUBSCRIPT_shadow_on_0',
                "command": 'shadow_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2289_action_queue_sync_33_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2289_action_queue_sync_33_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2289_action_queue_sync_33_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2289_action_queue_sync_33_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_2289_action_queue_sync_33_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2289_action_queue_sync_33_SUBSCRIPT_set_solidity_bits_6',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2289_action_queue_sync_33_SUBSCRIPT_shadow_off_7',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2289_action_queue_sync_33_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2289_action_queue_sync_33_SUBSCRIPT_face_northeast_9',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2289_action_queue_sync_33_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_2289_fade_out_to_black_async_duration_34',
        "command": 'fade_out_to_black_async_duration',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2289_jmp_to_event_35',
        "command": 'jmp_to_event',
        "args": [134],
        "subscript": []
    }
]
