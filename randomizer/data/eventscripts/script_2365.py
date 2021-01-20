from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2365_action_queue_sync_0',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2365_action_queue_sync_0_SUBSCRIPT_shift_west_pixels_0',
                "command": 'shift_west_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_0_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_0_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2365_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2365_action_queue_sync_1_SUBSCRIPT_shift_north_steps_0',
                "command": 'shift_north_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_1_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2365_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2365_action_queue_sync_2_SUBSCRIPT_shift_north_steps_0',
                "command": 'shift_north_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_2_SUBSCRIPT_shadow_off_1',
                "command": 'shadow_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2365_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_2365_action_queue_sync_3_SUBSCRIPT_shift_north_steps_0',
                "command": 'shift_north_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_3_SUBSCRIPT_shift_z_up_pixels_1',
                "command": 'shift_z_up_pixels',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_3_SUBSCRIPT_shadow_off_2',
                "command": 'shadow_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2365_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_2365_action_queue_sync_4_SUBSCRIPT_shift_north_steps_0',
                "command": 'shift_north_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_4_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_4_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_4_SUBSCRIPT_shadow_off_3',
                "command": 'shadow_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2365_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_2365_action_queue_sync_5_SUBSCRIPT_shift_north_steps_0',
                "command": 'shift_north_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_5_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_5_SUBSCRIPT_shadow_off_2',
                "command": 'shadow_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2365_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_6],
        "subscript": [
            {
                "identifier": 'EVENT_2365_action_queue_sync_6_SUBSCRIPT_shift_north_steps_0',
                "command": 'shift_north_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_6_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_6_SUBSCRIPT_shadow_off_2',
                "command": 'shadow_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2365_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2365_action_queue_sync_7_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_7_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_7_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2365_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2365_action_queue_sync_8_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [5, 53, 4, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_2365_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2365_action_queue_async_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2365_action_queue_async_9_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [0, 1]
            }
        ]
    },
    {
        "identifier": 'EVENT_2365_freeze_camera_10',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2365_set_action_script_sync_11',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_1, 763],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2365_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 763],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2365_set_action_script_sync_13',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 763],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2365_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 763],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2365_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 763],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2365_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_6, 763],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2365_fade_in_from_black_async_17',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2365_pause_18',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2365_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 764],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2365_pause_20',
        "command": 'pause',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2365_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2365_action_queue_async_21_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x02]
            },
            {
                "identifier": 'EVENT_2365_action_queue_async_21_SUBSCRIPT_embedded_animation_routine_1',
                "command": 'embedded_animation_routine',
                "args": [0x27]
            },
            {
                "identifier": 'EVENT_2365_action_queue_async_21_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [64]
            },
            {
                "identifier": 'EVENT_2365_action_queue_async_21_SUBSCRIPT_bpl_26_27_28_3',
                "command": 'bpl_26_27_28',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2365_pause_22',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2365_jmp_if_bit_set_23',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_2365_set_action_script_sync_25'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2365_jmp_24',
        "command": 'jmp',
        "args": ['EVENT_2365_pause_22'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2365_set_action_script_sync_25',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_7, 765],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2365_action_queue_sync_26',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2365_action_queue_sync_26_SUBSCRIPT_db_0',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_26_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x25, 0xc0, 0x06, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_26_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_26_SUBSCRIPT_bpl_26_27_28_3',
                "command": 'bpl_26_27_28',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2365_pause_27',
        "command": 'pause',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2365_unfreeze_camera_28',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2365_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2365_action_queue_sync_29_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_29_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2365_action_queue_sync_30',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2365_action_queue_sync_30_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_30_SUBSCRIPT_set_priority_1',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_30_SUBSCRIPT_overwrite_solidity_2',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_30_SUBSCRIPT_shadow_off_3',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_30_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_30_SUBSCRIPT_floating_off_5',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_30_SUBSCRIPT_db_6',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_30_SUBSCRIPT_db_7',
                "command": 'db',
                "args": [0x24, 0x50, 0x01, 0xb0, 0xfe]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_30_SUBSCRIPT_db_8',
                "command": 'db',
                "args": [0x25, 0x00, 0x0c, 0xa0, 0xff]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_30_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [255]
            },
            {
                "identifier": 'EVENT_2365_action_queue_sync_30_SUBSCRIPT_bpl_26_27_28_10',
                "command": 'bpl_26_27_28',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2365_pause_31',
        "command": 'pause',
        "args": [18],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2365_fade_out_to_black_async_duration_32',
        "command": 'fade_out_to_black_async_duration',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2365_jmp_to_event_33',
        "command": 'jmp_to_event',
        "args": [142],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2365_ret_34',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
